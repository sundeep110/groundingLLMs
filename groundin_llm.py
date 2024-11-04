import os
from openai import OpenAI
from dotenv import load_dotenv
import faiss
import numpy as np

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Grounding data
grounding_data = {
    "Python": "Python is dynamically typed, which can be a double-edged sword. While it makes coding faster and more flexible, it can lead to runtime errors that might have been caught at compile-time in statically-typed languages.",
    "LLMs": "Large Language Models (LLMs) are neural networks trained on large text datasets.",
    "Data Science": "Data Science involves using algorithms, data analysis, and machine learning to understand and interpret data.",
    "Java": "Java is great, it power most of Machine learning code, it has a rich set of libraries available."
}

# Function to generate embedding for a text
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return np.array(response.data[0].embedding)

# Create FAISS index and populate it with grounding data embeddings
dimension = len(get_embedding("test"))  # Dimension of embeddings
index = faiss.IndexFlatL2(dimension)  # L2 distance index for similarity search
grounding_embeddings = []
grounding_keys = list(grounding_data.keys())

for key, text in grounding_data.items():
    embedding = get_embedding(text)
    grounding_embeddings.append(embedding)
    index.add(np.array([embedding]).astype("float32"))

# Function to perform vector search on FAISS
def vector_search(query_text, threshold=0.8):
    query_embedding = get_embedding(query_text).astype("float32").reshape(1, -1)
    D, I = index.search(query_embedding, 1)  # Search for the closest vector
    if I[0][0] != -1 and D[0][0] <= threshold:
        return grounding_data[grounding_keys[I[0][0]]]
    else:
        return None  # No similar grounding information available

def enhance_response(topic, llm_response):
    grounding_info = vector_search(llm_response)
    
    if grounding_info:
        # Check if the LLM's response aligns well with grounding information
        return f"{llm_response}\n\n(Verified Information: {grounding_info})"
    else:
        # Add a disclaimer when no grounding data is available
        return f"{llm_response}\n\n(Disclaimer: This information could not be verified against known data and may contain inaccuracies.)"

# Query the LLM
def query_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Main function to execute the grounding check
def main():
    topic = input("Enter a topic: ")
    llm_response = query_llm(f"What can you tell me about {topic}?")
    
    print("LLM Response:", llm_response)
    enhanced_response = enhance_response(topic, llm_response)
    print("\nEnhanced Response:")
    print(enhanced_response)

if __name__ == "__main__":
    main()
