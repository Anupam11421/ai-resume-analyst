import requests

headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}

payload = {
    "model": "openchat:7b",
    "messages": [{"role": "user", "content": "Hello! Can you help me improve my resume?"}]
}

response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.text)
