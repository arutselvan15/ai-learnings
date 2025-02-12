import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv


def main():
    load_dotenv()

    llm = OpenAI(temperature=0.6)

    name_prompt = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food, suggest a fancy name for it."
    )

    name_chain = LLMChain(llm=llm, prompt=name_prompt, output_key="restaurant_name")

    menu_prompt = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest some menu items for {restaurant_name}.  Return it as a comma separated string."
    )

    menu_chain = LLMChain(llm=llm, prompt=menu_prompt, output_key="menu_items")

    seq_chain = SequentialChain(
        chains=[name_chain, menu_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"],
    )

    response = seq_chain({"cuisine": "Italian"})

    print(response)


if __name__ == '__main__':
    main()
