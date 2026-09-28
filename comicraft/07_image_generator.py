import torch
from diffusers import StableDiffusionPipeline
import os

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to("cuda")

def generate_image(prompt: str):
    image = pipe(prompt).images[0]
    filename = f"static/panels/{prompt.replace(' ', '_')}.png"
    image.save(filename)
    return filename
