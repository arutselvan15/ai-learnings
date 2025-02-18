import ollama


def main():
    client = ollama.Client()

    response = client.generate(model="llama3.2:1b", prompt="write a two lines of a poem about keyboard and mouse.")

    print("Response:", response.response)


if __name__ == '__main__':
    main()
