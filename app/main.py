from fastapi import FastAPI
from app.core import get_openai_object


from schema.query import Query




app = FastAPI()

client = get_openai_object()

@app.post("/ask")
def ask(q: Query):
    completion = client.chat.completions.create(model='gpt-4o-mini',
                                                messages=[
                                                    {"role":"system", "content":"You are a helpful assistant"},
                                                    {"role":"user","content":q.question}
                                                ])

    print(completion)
    return {
        "question": completion.choices[0].message.content
    }