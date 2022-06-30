import sys
from jinja2 import Template
from pathlib import Path

def render(**kwargs):
    file = Path(sys.argv[0]).name[:-3]
    template = open('scripts/templates/{}.html'.format(file))
    tpl = Template(template.read())
    print(tpl.render(kwargs))