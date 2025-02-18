from dotenv import load_dotenv
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline


def main():
    load_dotenv()

    llama_pipeline = pipeline(
        "text-generation",
        model="meta-llama/Llama-2-7b",  # Replace with your specific model path
        device=-1  # Set to -1 for CPU or a GPU device ID (e.g., 0 for the first GPU)
    )

    # Wrap the pipeline in a LangChain LLM interface
    llm = HuggingFacePipeline(pipeline=llama_pipeline)

    name = llm.invoke("write a two lines of a poem about keyboard and mouse")

    print(name)


if __name__ == '__main__':
    main()
