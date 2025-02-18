import os
from dotenv import load_dotenv
from openai import OpenAI


def main():
    load_dotenv()

    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.environ.get("GROQ_API_KEY")
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "write a two lines of a poem about keyboard and mouse",
            }
        ],
        model="gpt-4o-mini",
    )

    print(chat_completion.choices[0].message.content)


if __name__ == '__main__':
    main()
