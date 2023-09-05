import json

from generate_panels import generate_panels
from stability_ai import text_to_image
from add_text import add_text_to_panel
from create_strip import create_strip

scenario = """
Adrien is a guy with blond hair. Vincent is a guy with black hair.
Adrien and vincent want to start a new product, and they create it in one night before presenting it to the board.
"""

print(f"Generate panels for this scenario: \n {scenario}")

panels = generate_panels(scenario)

with open('output/panels.json', 'w') as outfile:
  json.dump(panels, outfile)

# load panels from json file
# with open('output/panels.json') as json_file:
#   panels = json.load(json_file)

panel_images = []

for panel in panels:
  panel_prompt = "cartoon box of " + panel["description"] + " in manga style black and white"
  print(f"Generate panel {panel['number']} with prompt: {panel_prompt}")
  panel_image = text_to_image(panel_prompt)
  panel_image_with_text = add_text_to_panel(panel["text"], panel_image)
  panel_image_with_text.save(f"output/panel-{panel['number']}.png")
  panel_images.append(panel_image_with_text)

create_strip(panel_images).save("output/strip.png")
