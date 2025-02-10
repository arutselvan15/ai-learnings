import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv


def main():
    load_dotenv()

    llm = OpenAI(temperature=0.6)

    name_prompt = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food, suggest a fancy name for it."
    )

    name_chain = name_prompt | llm
    response = name_chain.invoke({"cuisine": "Italian"})

    print(response)


if __name__ == '__main__':
    main()
