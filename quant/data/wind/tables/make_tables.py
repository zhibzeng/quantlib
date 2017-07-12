import re
import warnings
import jinja2
import pandas as pd
from pyquery import PyQuery

FILEPATH = "WindQuantDBV4.43.html"
COLUMNS = ["字段", "字段类型", "字段名称", "备注"]
PATTERN = re.compile(r"\d{1,2}\.\d{1,2}")
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
    table = [[] for _ in range(4)]
    heads = [divs[i+start] for i in range(4)]
    head_classes = [[c for c in h.classes if c.startswith("x")][0] for h in heads]
    # print([pq(head).text() for head in heads], head_classes)
    i = 4
    while 1:
        cell = divs[start+i]
        assert "t" not in cell.classes or "fs0" in cell.classes
        if head_classes[i % 4] in cell.classes:
            value = pq(cell).text().replace(" ", "").replace("（", "(").replace("）", ")").replace("，", ", ")    # replace chinese symbols to english
            if i % 4 == 1 and not value.endswith(")") and value not in ("CLOB", "DATE"):
                value += ")"                                            # Sometimes the docs misses the `)`
            table[i % 4].append(value)
        else:
            break
        i += 1
    if i % 4 != 0 or i == 4:
        warnings.warn(UserWarning("Unexpected End of Table"))
    table = pd.DataFrame(table, index=["name", "type", "cname", "comment"]).T
    return start + i, table

def resolve_tables():
    pq = read_html(FILEPATH)
    divs = pq("div.pf>div.pc>div.c,div.pf>div.pc>div.t.fs0").not_(".hd")
    tables = {}
    i = 0
    while i < len(divs) - 4:
        if [pq(divs[i+j]).text() for j in range(4)] == COLUMNS:
            for j in range(10):
                if divs[i - j].text and PATTERN.match(divs[i - j].text):
                    title = pq(divs[i-j]).text()
                    break
            table_ch_name, table_name = "".join(title.split(" ")[1:]).split("-")
            table_name = table_name.replace("&", "")
            i, table = handle_table(pq, divs, i)
            tables[table_name] = (table_ch_name, table)
            print(table_name, table_ch_name, i)
        i += 1
    return tables


def generate_pyfiles():
    tables = resolve_tables()
    init_file = open("__init__.py", "w")
    for tablename, (chname, table) in tables.items():
        generate_file(tablename, chname, table)
        init_file.write("from .{} import {}\n".format(tablename.lower(), tablename))
        print(tablename, chname)
    init_file.close()


def generate_file(tablename, chname, table):
    template = jinja2.Template(TEMPLATE)
    py = template.render(tablename=tablename, chname=chname, table=table)
    with open("{fname}.py".format(fname=tablename.lower()), "w", encoding="utf-8") as f:
        f.write(py)


if __name__ == '__main__':
    generate_pyfiles()
    
