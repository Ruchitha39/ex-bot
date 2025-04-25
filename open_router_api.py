# import request module to make a request
import requests

import json


response = requests.post(url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer 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",
    "Content-Type": "application/json",
  },
  data=json.dumps({
    "model": "nvidia/llama-3.1-nemotron-nano-8b-v1:free",
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of ex bf?"
      }
    ],
    
  })
)

print(response.text)