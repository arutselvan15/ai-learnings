import json
import os

import requests
from dotenv import load_dotenv


def main():
    load_dotenv()

    url = "http://localhost:11434/api/chat"

    payload = {
        "model": "mistral",
        "messages": [{
            "role": "user",
            "content": "write a two lines of a poem about keyboard and mouse."
        }]
    }

    response = requests.post(url, json=payload, stream=True)

    if response.status_code == 200:
        print("Streaming response from Ollama:")

        for line in response.iter_lines(decode_unicode=True):
            if line:
                try:
                    json_data = json.loads(line)

                    if "message" in json_data and "content" in json_data["message"]:
                        print(json_data["message"]["content"], end="")
                except json.JSONDecodeError:
                    print(f"failed to parse line: {line}")

    # last line should be newline
    print()


if __name__ == '__main__':
    main()
