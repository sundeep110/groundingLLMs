# groundingLLMs

This repository provides an example of how to ground responses from Large Language Models (LLMs) using a knowledge base. By grounding responses, we can reduce the likelihood of generating hallucinated or incorrect information by comparing responses to factual data.

## Features

- Uses OpenAI’s GPT models for generating responses.
- Utilizes FAISS for efficient similarity search with embeddings.
- Checks generated responses against a knowledge base for reliability.

## Prerequisites

- **Python 3.7+**
- **OpenAI API Key**

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sundeep110/groundingLLMs.git
   cd groundingLLMs
   ```

2. **Install dependencies**:
   Make sure you have Python and `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key to the `.env` file:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key_here
     ```

   Replace `your_openai_api_key_here` with your actual API key from OpenAI.

## Usage

Once everything is set up, you can run the main script `groundin_llm.py` to query a topic and check if the response from the LLM is grounded based on the knowledge base.

### Example Run

1. In your terminal, navigate to the project directory:
   ```bash
   cd groundingLLMs
   ```

2. Run the script:
   ```bash
   python groundin_llm.py
   ```

3. **Input Prompt**: When prompted, enter a topic. For example:
   ```
   Enter a topic: a great programming language for machine learning
   ```

4. **Expected Output**: The script will provide the LLM's response, grounding information, and whether the response is reliable. Here’s a sample output based on this query:

   ```
   LLM Response: One of the most recommended programming languages for machine learning is Python. Python is a high-level, interpreted language that is known for its simplicity and readability, which makes it great for beginners and experts alike.

   Python has a vast selection of libraries and frameworks that are useful for machine learning, such as TensorFlow, PyTorch, Scikit-Learn, and more, allowing you to implement machine learning models quickly.

   It also has strong support for integration with other languages and tools, and it's frequently updated with new features and optimizations. One reason why Python is popular in the machine learning field is due to the large and active community, offering plenty of resources, tutorials, and code samples.

   However, Python is not the only language suitable for machine learning. Other programming languages like R, Java, and C++ are also utilized in machine learning, each with their own set of advantages and trade-offs. The best language to use will often depend on the specific requirements of the project and the preferences of the development team.

   Grounding Information: Java is great, it powers most of the machine learning code, it has a rich set of libraries available.
   
   Response is grounded and reliable.
   ```

In this example:
- **LLM Response**: The LLM provides a comprehensive response, mentioning Python’s advantages and comparing it to other languages like R, Java, and C++.
- **Grounding Information**: The grounding information for "Java" is retrieved and confirmed as reliable based on FAISS similarity.
- **Output Conclusion**: The response is determined to be grounded and reliable.

## Troubleshooting

- **Missing OpenAI API Key**: If you see an error about missing API credentials, ensure your `.env` file is in the project directory and correctly formatted.
- **FAISS installation issues**: Make sure you installed `faiss-cpu` with `pip install faiss-cpu`, as GPU versions may require additional setup.
- **Rate Limits**: OpenAI's API may limit the number of requests. Monitor your usage if you encounter rate limit errors.

## Contributing

Feel free to fork this repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the Apache-2.0 License.