import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

os.environ['OPENAI_API_KEY'] = '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'


def main():
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
