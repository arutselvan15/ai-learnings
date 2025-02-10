import os
from langchain_openai import OpenAI
from dotenv import load_dotenv


def main():
    load_dotenv()

    llm = OpenAI(temperature=0.6)

    name = llm.invoke("i want to open a restaurant for Italian food.  Suggest a fancy name for this.")

    print(name)


if __name__ == '__main__':
    main()
