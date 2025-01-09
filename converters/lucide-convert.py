from jinja2 import Template
from jinja2 import Environment, FileSystemLoader, select_autoescape

import glob, os
for file in glob.glob("lucide-raw/*.svg"):
  print(file)
  with open(file) as f:
    svg = f.readlines()

  env = Environment(
      loader=FileSystemLoader("."),
      autoescape=select_autoescape()
  )

  t = env.get_template("lucide-template.vue")

  render = t.render(svg=''.join(svg).strip().replace('\n', '\n  ').replace('width=\"24\"', ':width="size"').replace('height="24"', ':height="size"').replace('stroke-width="2"', ':stroke-width="stroke"'))

  with open("export-lucide-vue"+file.replace('lucide-raw', '').replace('.svg', '').replace("-", " ").title().replace(" ", "")+".vue","w") as f:
    f.write(render)
