import os

from groq import Groq
from dotenv import load_dotenv

from prompts import SYSTEM_PROMPT

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_code(requirement, context):

    prompt = f"""
Requirement:
{requirement}

Relevant Examples:
{context}

Generate production-ready code.

Rules:
1. Use the examples only as inspiration.
2. Generate complete code.
3. Add comments.
4. Include error handling.
5. Return only code.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    code = response.choices[0].message.content

    code = (
        code
        .replace("```python", "")
        .replace("```", "")
    )

    return code