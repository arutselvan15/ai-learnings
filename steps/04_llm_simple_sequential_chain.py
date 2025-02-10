import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

os.environ[
    'OPENAI_API_KEY'] = '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'


def main():
    llm = OpenAI(temperature=0.6)

    name_prompt = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food, suggest a fancy name for it."
    )

    name_chain = LLMChain(llm=llm, prompt=name_prompt)

    menu_prompt = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}.  Return it as a comma separated string."
    )

    menu_chain = LLMChain(llm=llm, prompt=menu_prompt)

    simple_seq_chain = SimpleSequentialChain(
        chains=[name_chain, menu_chain],
    )

    response = simple_seq_chain.run("Italian")

    print(response)


if __name__ == '__main__':
    main()
