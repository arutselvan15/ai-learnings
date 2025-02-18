from dotenv import load_dotenv
from langchain_openai import OpenAI


def main():
    load_dotenv()

    llm = OpenAI(temperature=0.6)

    name = llm.invoke("write a two lines of a poem about keyboard and mouse")

    print(name)


if __name__ == '__main__':
    main()
