from app.tools import get_weather
from app.core import get_openai_object
from app.memory import memory_store

client = get_openai_object()


def run_agent(user_input: str):
    # Step 1: Load memory
    context = memory_store.get("history", "")

    # Step 2: Decision-making
    if "weather" in user_input.lower():
        city = "Lahore"
        result = get_weather(city)
        response = f"Tools says {result}"
    else:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are helpful AI Agent"},
                {"role": "user", "content": context + "\n" + user_input}
            ]
        )

        response = completion.choices[0].message.content

    memory_store["history"] = context + f"\nUser: {user_input}\nAI: {response}"

    return response
