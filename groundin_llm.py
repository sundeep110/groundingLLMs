import openai
import os
from dotenv import load_dotenv
from numpy import dot
from numpy.linalg import norm

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def query_llm(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response['choices'][0]['text'].strip()


def get_grounding_data(topic):
    # Simple dictionary as an example
    grounding_data = {
        "Python": "Python is a programming language known for its readability.",
        "LLMs": "Large Language Models (LLMs) are neural networks trained on large text datasets."
    }
    return grounding_data.get(topic, "No grounding information available.")


def get_embedding(text):
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response['data'][0]['embedding']



def cosine_similarity(vec1, vec2):
    return dot(vec1, vec2) / (norm(vec1) * norm(vec2))

def is_similar_to_grounding(llm_response, grounding_info, threshold=0.8):
    response_embedding = get_embedding(llm_response)
    grounding_embedding = get_embedding(grounding_info)
    similarity_score = cosine_similarity(response_embedding, grounding_embedding)
    
    return similarity_score >= threshold


def main():
    topic = input("Enter a topic: ")
    llm_response = query_llm(f"What can you tell me about {topic}?")
    grounding_info = get_grounding_data(topic)
    
    print(f"LLM Response: {llm_response}")
    print(f"Grounding Information: {grounding_info}")
    
    if is_similar_to_grounding(llm_response, grounding_info):
        print("Response is grounded and reliable.")
    else:
        print("Potential hallucination detected. Using grounded information instead.")
        print(f"Grounded Answer: {grounding_info}")

if __name__ == "__main__":
    main()



