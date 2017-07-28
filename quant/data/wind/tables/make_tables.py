import re
import warnings
import jinja2
import pandas as pd
from pyquery import PyQuery

FILEPATH = "WindQuantDBV4.43.html"
COLUMNS = ["字段", "字段类型", "字段名称", "备注"]
PATTERN = re.compile(r"\d{1,2}\.\d{1,3}")
TEMPLATE = """from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class {{tablename}}(BaseModel):
    \"""
    {{chname}}

    Attributes
    ----------
{% for _, row in table.iterrows() %}    {{row['name'].lower()}}: {{row.type}}
        {{row.cname}}   {{row.comment}}
{% endfor %}
    \"""
    __tablename__ = "{{tablename}}"
    {% for _, row in table.iterrows() %}{{row['name'].lower()}} = {%if row['name'].lower() == 'object_id' %}Column(VARCHAR2(100), primary_key=True){%else%}Column({{row.type.upper()}}){%endif%}
    {% endfor %}

"""


def read_html(filepath):
    with open(filepath, encoding="utf-8") as f:
        html = f.read()
    return PyQuery(html)


def handle_table(pq, divs, start):
    offset = 0
    table = [[] for _ in range(4)]
    heads = [divs[i+start] for i in range(4)]
    head_classes = [[c for c in h.classes if c.startswith("x")][0] for h in heads]
    # print([pq(head).text() for head in heads], head_classes)
    i = 4
    while 1:
        cell = divs[start+i]
        try:
            this_class = [c for c in cell.classes if c.startswith("x")][0]
        except IndexError:
            break
        assert "t" not in cell.classes or "fs0" in cell.classes
        if this_class in head_classes:
            value = pq(cell).text().replace(" ", "").replace("（", "(").replace("）", ")").replace("，", ", ")    # replace chinese symbols to english
            if (i+offset) % 4 == 1 and not value.endswith(")") and value not in ("CLOB", "DATE"):
                value += ")"                                            # Sometimes the docs misses the `)`
            this_col_num = head_classes.index(this_class)
            if this_col_num != (offset + i) % 4:
                table[(i + offset + this_col_num) % 4][-1] += value
                offset = -(i + 1) % 4
            else:
                table[(i + offset) % 4].append(value)
        else:
            break
        i += 1
    if (i + offset) % 4 != 0 or i == 4:
        warnings.warn(UserWarning("Unexpected End of Table"))
        # raise ValueError("Unexpected end of table, {d}".format(d=(i+offset)%4))
    table = pd.DataFrame(table, index=["name", "type", "cname", "comment"]).T
    columns = [col.lower() for col in table["name"]]
    if "opdate" not in columns:
        table = table.append(pd.Series(dict(name="opdate", type="DATETIME", cname="opdate", comment="")), ignore_index=True)
    if "mode" not in columns:
        table = table.append(pd.Series(dict(name="opmode", type="VARCHAR(1)", cname="opmode", comment="")), ignore_index=True)
    return start + i, table

def resolve_tables():
    pq = read_html(FILEPATH)
    divs = pq("div.pf>div.pc>div.c,div.pf>div.pc>div.t.fs0").not_(".hd, .x5e")
    tables = {}
    i = 0
    while i < len(divs) - 4:
        if [pq(divs[i+j]).text() for j in range(4)] == COLUMNS:
            for j in range(10):
                if divs[i - j].text and PATTERN.match(divs[i - j].text):
                    title = pq(divs[i-j]).text()
                    break
            section_no = title.split(" ")[0]
            try:
                tmp = "".join(title.split(" ")[1:]).split("-")
                table_ch_name, table_name = "-".join(tmp[:-1]), tmp[-1]
            except ValueError:
                table_ch_name = title.split(" ")[1:]
                table_name = pq(divs[i-j+1]).text().strip("-")
            table_ch_name = " ".join([section_no, table_ch_name])
            table_name = table_name.replace("&", "")
            try:
                i, table = handle_table(pq, divs, i)
            except ValueError:
                print(title, table)
                raise ValueError
            tables[table_name] = (table_ch_name, table)
            # print(table_name, table_ch_name, i)
        i += 1
    return tables


def generate_pyfiles():
    tables = resolve_tables()
    init_file = open("__init__.py", "w")
    for tablename, (chname, table) in tables.items():
        generate_file(tablename, chname, table)
        init_file.write("from .{} import {}\n".format(tablename.lower(), tablename))
        # print(tablename, chname)
    init_file.close()


def generate_file(tablename, chname, table):
    template = jinja2.Template(TEMPLATE)
    py = template.render(tablename=tablename, chname=chname, table=table)
    with open("{fname}.py".format(fname=tablename.lower()), "w", encoding="utf-8") as f:
        f.write(py)


if __name__ == '__main__':
    generate_pyfiles()
    
