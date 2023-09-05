# Comics Generator

This program use Generative AI to create an entire comic strip from a short scenario.

The scenario must mention the characters with a physical description.

## How it works

First, a LLM (OpenAI API) is used to split the scenario into 6 panels with their description and associated text.

Then for each panel:
 - an image is generated with Stable Diffusion (Stability API).
 - the panel text is added to the image

The 6 generated images with their texts are then merged into a final strip !


![strip.png](output/strip.png)

Generated with the following scenario as input:
```
Characters: Adrien is a guy with blond hair and glasses. Vincent is a guy with black hair and wearing a hat.
Adrien and Vincent work at the office and want to start a new product, and they create it in one night before presenting it to the board.
```

## Usage

Export `OPENAI_API_KEY` and `STABILITY_KEY`.

Install dependencies: `pip install langchain openai stability-sdk pillow`

Then edit the `SCENARIO` variable in [kartoon.py](kartoon.py).

Run the script: `python kartoon.py`
