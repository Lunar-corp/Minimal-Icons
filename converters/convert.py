from jinja2 import Template
from jinja2 import Environment, FileSystemLoader, select_autoescape

import glob, os, re

for file in glob.glob("./illustrator-raw/*.svg"):
  print(file)
  with open(file) as f:
    svg = f.readlines()

  env = Environment(
      loader=FileSystemLoader("."),
      autoescape=select_autoescape()
  )

  svgTemplate = env.get_template("template-svg")

  regex_pattern = r'<\?xml.*?>|<svg.*?>|</svg>|fill="none"\s*|stroke="#000"\s*|stroke-linecap="round"\s*|stroke-linejoin="round"\s*|stroke-width="2"\s*|stroke-width="0"\s*'
  svgFormatted = re.sub(regex_pattern, '', ''.join(svg))
  svgFormatted = re.sub(r'\n\s*', '', svgFormatted)

  svgRender = svgTemplate.render(svg=svgFormatted)

  with open(file.replace('illustrator-raw', 'export-svg').replace("_", ""),"w") as f:
    f.write(svgRender)


  vueTemplate = env.get_template("template-vue")
  vueRender = vueTemplate.render(svg=''.join(svgFormatted).strip().replace('\n', '\n  ').replace('width=\"24\"', ':width="size"').replace('height="24"', ':height="size"').replace('stroke-width="2"', ':stroke-width="stroke"'))

  with open('./export-vue/' + file.replace('./illustrator-raw/', '').replace("_", "").replace('.svg', '').replace("-", " ").title().replace(" ", "")+".vue","w") as f:
    f.write(vueRender)
