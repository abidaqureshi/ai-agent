import os

from openai import OpenAI


def get_openai_object():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return client
