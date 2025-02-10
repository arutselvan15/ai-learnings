import os

import config
import config as cfg
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain


def openai():
    return OpenAI(api_key=cfg.openai_api_key, temperature=cfg.temperature)


def get_llm(model):
    if model == "openai":
        return openai()


def generate_restaurant_name_and_items(cuisine):
    llm = get_llm(config.model)

    name_prompt = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food, suggest a fancy name for it"
    )

    name_chain = LLMChain(llm=llm, prompt=name_prompt, output_key="restaurant_name")

    menu_prompt = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest some menu items for {restaurant_name}.  Return it as a comma separated string"
    )

    menu_chain = LLMChain(llm=llm, prompt=menu_prompt, output_key="menu_items")

    seq_chain = SequentialChain(
        chains=[name_chain, menu_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"],
    )

    response = seq_chain({"cuisine": cuisine})

    return response


# if __name__ == '__main__':
#     output = generate_restaurant_name_and_items("Italian")
#     print(output)
