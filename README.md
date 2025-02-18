# LLM Learning

LLM learning experience and hands-on

# Settings

Each project have .env file with secret values.  load_dotenv library is used to load the env during run time.

# Types of LLMs

## Open Source

- llama by Meta
- mistral
- gemma by Google

## Paid

- gtp by OpenAI

# Using LLMs

You can use these llm by going to provider website in browser or use the python library to call the LLM programmatically.

## Using UI

https://chat.openai.com/

https://www.meta.ai/

## Using Code

    from openai import OpenAI
    client = OpenAI(api_key="*****")

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "write a two lines of a poem about keyboard and mouse."
            }
        ]
    )

    print(completion.choices[0].message)


Sample: [openai.py](llms/llm_openai.py)


Not all providers have python libraries to call the LLMs.  

We can use Hugging Face, Groq, Langchain libraries to run LLMs using the code.

### Hugging Face

Hugging Face is a free, open-source platform for machine learning (ML) and data science

https://huggingface.co/

Transformers

Not all providers have langchain library to access the LLM.  Hugging Face transformers and pipelines provides options
to run opensource LLM in generic way.

    huggingface-cli login

CLI login is must

    from transformers import pipeline

    pipe = pipeline("text-generation", model="model-name-here")
    llm = HuggingFacePipeline(pipeline=llama_pipeline)
    name = llm.invoke("write a two lines of a poem about keyboard and mouse")

    print(name)


https://huggingface.co/models

https://huggingface.co/meta-llama/Llama-2-7b

Code samples:

- [llama](./llms/huggingface/hf_llama.py)

### Groq

Groq, Inc. is an American artificial intelligence company that builds an AI accelerator application-specific integrated circuit that they call the Language Processing Unit and related hardware to accelerate the inference performance of AI workloads


    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "write a two lines of a poem about keyboard and mouse",
            }
        ],
        model="MODEL-NAME-HERE",
    )

    print(chat_completion.choices[0].message.content)

https://groq.com/

https://console.groq.com/docs/models

Code samples:

- [llama](./llms/groq/gq_llama.py)
- [mistral](./llms/groq/gq_mistral.py)
- [gemma](./llms/groq/gq_gemma.py)
- [openai](./llms/groq/gq_openai.py)

### LangChain

LangChain is a framework for developing applications powered by large language models (LLMs)

Code samples:

- [openai](./llms/langchain/lc_openai.py)

# LLM in Local

## Ollama

Get up and running with large language models locally.


Install the ollama on your system and follow in steps to run the llm.

https://ollama.com/

https://ollama.com/search

https://github.com/ollama/ollama


### Using CLI

    $] ollama run llama3.2
    $] hello    # question
        <answer>
    $] /bye # exit
    

    $] ollama list      # view all models

### Using API

ollama provides http server to access the LLMs.

http://localhost:11434/api/chat

If you want to start it manually use the below command.

    $] ollama serve

Sample:
- using [http](llms/ollama/llm_ollama_http.py)
- using [lib](llms/ollama/llm_ollama_lib.py)

### Using custom Model

You can create a custom LLM model using base model and your custom parameters.

Sample [Modelfile](llms/ollama/Modelfile)

    $] ollama create mario -f Modelfile
    $] ollama run mario
    $] hello    # question
        <answer>
    $] /bye # exit

# Jupyter

## Jupyter lab

JupyterLab is the latest web-based interactive development environment for notebooks, code, and data. Its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning. A modular design invites extensions to expand and enrich functionality.

launch JupyterLab with:

`jupyter lab`

## Notebook

The Jupyter Notebook is the original web application for creating and sharing computational documents. It offers a simple, streamlined, document-centric experience.

To run the notebook:

`jupyter notebook`

## Voila

Voilà helps communicate insights by transforming notebooks into secure, stand-alone web applications that you can customize and share.

launch Voilà with:

`voila`

# Projects