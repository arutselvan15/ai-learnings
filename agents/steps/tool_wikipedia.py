from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


def main():
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

    response = wikipedia.run("HUNTER X HUNTER")

    print(response)


if __name__ == '__main__':
    main()
