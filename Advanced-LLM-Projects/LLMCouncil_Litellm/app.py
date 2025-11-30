from litellm import completion
import os
from dotenv import load_dotenv
load_dotenv()

def ask_model(model_name, messages):
    resp = completion(model=model_name, messages=messages)
    return resp["choices"][0]["message"]["content"]

def consensus_qa(question: str, model_list: list[str]) -> dict:
    messages = [{"role":"user", "content": question}]
    answers = {}
    for model in model_list:
        try:
            answers[model] = ask_model(model, messages)
        except Exception as e:
            answers[model] = f"Error: {e}"
    return {"question": question, "answers": answers}

if __name__ == "__main__":
    models = [
        "openai/gpt-3.5-turbo",
        "groq/gemma2-9b-it",
        "gemini/gemini-3-pro-preview"
    ]
    q = input("Ask a factual question: ")
    result = consensus_qa(q, models)
    for m, a in result["answers"].items():
        print(f"{m} => {a}")
