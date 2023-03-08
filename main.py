from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

import json
import openai

class Input(BaseModel):
    product_description: str
    vibe_words: str

app = FastAPI()

# put in env. variable
api_key = "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"
openai.api_key = api_key

@app.post("/marketbot/")
async def generate_values(input: Input):

    response1 = openai.Completion.create(
        model="text-davinci-003",
        # prompt=f"Product description: A pair of shoes that can fit any foot size.\nSeed words: adaptable, fit, omni-fit.",
        prompt=f"Product description: {input.product_description}\nSeed words: {input.vibe_words}",
        temperature=0.8,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # product names
    response1_text = response1.choices[0].text

    return input


