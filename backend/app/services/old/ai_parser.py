import json
import re
import requests

OLLAMA_URL = "http://ollama:11434/api/generate"


def ai_cleanup(raw_text: str):

    prompt = f"""
Return ONLY valid JSON.

Schema:
{{
  "store": null,
  "date": null,
  "items": [
    {{
      "name": "",
      "price": null
    }}
  ],
  "total": null
}}

Extract receipt data.

OCR:
{raw_text}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "qwen2.5:7b",
            "prompt": prompt,
            "format": "json",
            "stream": False,
            "options": {
                "temperature": 0
            }
        },
        timeout=120
    )

    response.raise_for_status()

    content = response.json()["response"]

    try:
        return json.loads(content)

    except Exception:

        match = re.search(r"\{.*\}", content, re.S)

        if match:
            return json.loads(match.group(0))

        raise