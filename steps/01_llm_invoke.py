import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

os.environ['OPENAI_API_KEY'] = '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'


def main():
    llm = OpenAI(temperature=0.6)

    name = llm.invoke("i want to open a restaurant for Italian food.  Suggest a fancy name for this.")

    print(name)


if __name__ == '__main__':
    main()
