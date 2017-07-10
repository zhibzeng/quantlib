import re
import warnings
import jinja2
import pandas as pd
from pyquery import PyQuery

FILEPATH = "WindQuantDBV4.43.html"
COLUMNS = ["字段", "字段类型", "字段名称", "备注"]
PATTERN = re.compile(r"\d{1,2}\.\d{1,2}")
TEMPLATE = """from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class {{tablename}}(BaseModel):
    \"""
    {{chname}}

    Attributes
    ----------
{% for _, row in table.iterrows() %}    {{row['name'].lower()}}: {{row.type}}
        {{row.cname}}   {{row.comment}}
{% endfor %}
    \"""
    {% for _, row in table.iterrows() %}{{row['name'].lower()}} = Column({{row.type}})
    {% endfor %}

"""


def read_html(filepath):
    with open(filepath) as f:
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
        if head_classes[i % 4] in cell.classes:
            table[i % 4].append(pq(cell).text().replace(" ", "").replace("（", "(").replace("）", ")"))
        else:
            break
        i += 1
    if i % 4 != 0:
        warnings.warn(UserWarning("Unexpected End of Table"))
    table = pd.DataFrame(table, index=["name", "type", "cname", "comment"]).T
    return start + i, table

def resolve_tables():
    pq = read_html(FILEPATH)
    divs = pq("div.pf>div.pc>div")
    tables = {}
    i = 0
    while i < len(divs) - 4:
        if [pq(divs[i+j]).text() for j in range(4)] == COLUMNS:
            for j in range(10):
                if divs[i - j].text and PATTERN.match(divs[i - j].text):
                    title = pq(divs[i-j]).text()
                    break
            try:
                table_ch_name, table_name = "".join(title.split(" ")[1:]).split("-")
            except:
                print(title)
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
    with open("{fname}.py".format(fname=tablename.lower()), "w") as f:
        f.write(py)


if __name__ == '__main__':
    generate_pyfiles()
    
