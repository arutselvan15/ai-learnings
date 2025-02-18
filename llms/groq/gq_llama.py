import os
from dotenv import load_dotenv
from groq import Groq


def main():
    load_dotenv()
    
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "write a two lines of a poem about keyboard and mouse",
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    print(chat_completion.choices[0].message.content)


if __name__ == '__main__':
    main()
