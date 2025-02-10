from langchain.prompts import PromptTemplate


def main():
    name_prompt = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food, suggest a fancy name for it."
    )

    prompt = name_prompt.format(cuisine='Italian')

    print(prompt)


if __name__ == '__main__':
    main()
