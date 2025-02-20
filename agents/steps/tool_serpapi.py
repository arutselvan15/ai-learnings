from dotenv import load_dotenv
from langchain_community.utilities import SerpAPIWrapper


def main():
    load_dotenv()

    search = SerpAPIWrapper()

    response = search.run("What is the USA GDP in 2024?")

    print(response)


if __name__ == '__main__':
    main()
