# https://owlfroggy.github.io/terracotta-docs/ << actual website
---
# terracotta documentation site

how to build locally:
- clone repo
- create (and activate) a venv for the project
- `pip install mkdocs`
- `pip install mkdocs-material`
- `pip install mkdocs-table-reader-plugin`
- `python setup.py install`
- `mkdocs serve`
if the above steps somehow fail to work on your machine but you still want to contribute just contact me and ill try to figure it out

if you update the lexer, in order to see the changes you have to kill the `mkdocs serve` process, rerun `python3 setup.py install`, then restart `mkdocs serve`
