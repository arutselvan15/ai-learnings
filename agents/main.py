from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool, load_tools, AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain.tools import SerpAPIWrapper
from langchain.llms import OpenAI


def main():
    load_dotenv()

    llm = OpenAI(temperature=0.6)

    serp_tool = SerpAPIWrapper()

    tools = [
        Tool(name="Search", func=serp_tool.run),
        # Tool(name="Match", func=)
    ]
    # tools = load_tools(["serpapi", "llm-math"], llm=llm)
    #
    # agent = initialize_agent(
    #     tools,
    #     llm,
    #     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    #     verbose=True
    # )

    agent = AgentExecutor.from_agent_and_tools(
        llm,
        tools=[serp_tool],
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    response = agent.run("What was the GDP of US in 2024 plus 5?")
    print(response)



if __name__ == '__main__':
    main()
