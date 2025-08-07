from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(query, context_chunks, prompt_path="prompts/interpretation.txt"):
    """
    Uses GPT to answer a query based on retrieved context chunks and system prompt.
    """
    # Load system prompt
    with open(prompt_path, "r") as f:
        system_prompt = f.read()

    context = "\n\n".join(context_chunks)

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
            ],
            temperature=0.2,
            max_tokens=700
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"
