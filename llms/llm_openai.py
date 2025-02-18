import os
from dotenv import load_dotenv
from openai import OpenAI


def main():
    load_dotenv()

    from openai import OpenAI
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "write a two lines of a poem about keyboard and mouse."
            }
        ]
    )

    print(completion.choices[0].message)


if __name__ == '__main__':
    main()
