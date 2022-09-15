import os
import openai
openai.organization = "org-5wXvXlEHbG9wwVDoY36t8hvf"
openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = "curie:ft-personal:kookmodel-2022-09-14-15-46-30"


def get_par(prompt:str, model:str = MODEL, max_tokens:int = 500, temp:float =0.9):

    completion = openai.Completion.create(model=model, prompt = prompt, max_tokens=max_tokens, temperature=temp)
    par = prompt + completion["choices"][0]["text"]
    par = par[0:par.rfind(".") + 1]
    return par

