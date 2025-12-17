import requests
import time

OLLAMA_URL = "http://localhost:11434/api/generate"

def get_token_usage(prompt, model="llama3.2:latest"):
    payload = {
        "model": model,
        "prompt": "Miraj",
        "stream": False
    }

    start = time.time()
    response = requests.post(OLLAMA_URL, json=payload)
    end = time.time()

    data = response.json()

    return {
        "model": model,
        "prompt": prompt,
        "response": data["response"],
        "input_tokens": data["prompt_eval_count"],
        "output_tokens": data["eval_count"],
        "total_tokens": data["prompt_eval_count"] + data["eval_count"],
        "time_taken_sec": round(end - start, 2)
    }


if __name__ == "__main__":
    prompt = "Explain machine learning in simple words"

    result = get_token_usage(prompt)

    print("\n===== OLLAMA TOKEN USAGE =====")
    print("Model:", result["model"])
    print("Prompt:", result["prompt"])
    print("\nResponse:\n", result["response"])
    print("\n📥 Input tokens :", result["input_tokens"])
    print("📤 Output tokens:", result["output_tokens"])
    print("🔢 Total tokens :", result["total_tokens"])
    print("⏱ Time taken   :", result["time_taken_sec"], "seconds")
