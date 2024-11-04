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

3. **Input Prompt**: The script will prompt you to enter a topic. For example:
   ```
   Enter a topic: Python
   ```

4. **Expected Output**: The script will provide the LLM's response, grounding information, and whether the response is reliable. Here’s a sample output:

   ```
   LLM Response: Python is dynamically typed, allowing flexibility, but it can lead to runtime errors.
   Grounding Information: Python is dynamically typed, which can be a double-edged sword. While it makes coding faster and more flexible, it can lead to runtime errors that might have been caught at compile-time in statically-typed languages.
   Response is grounded and reliable.
   ```

   If the response is not similar to the grounding information, it will detect a potential hallucination:
   
   ```
   LLM Response: Python is used primarily for front-end development.
   Grounding Information: No grounding information available.
   Potential hallucination detected. Using grounded information instead.
   Grounded Answer: Python is dynamically typed, which can be a double-edged sword...
   ```

## Troubleshooting

- **Missing OpenAI API Key**: If you see an error about missing API credentials, ensure your `.env` file is in the project directory and correctly formatted.
- **FAISS installation issues**: Make sure you installed `faiss-cpu` with `pip install faiss-cpu`, as GPU versions may require additional setup.
- **Rate Limits**: OpenAI's API may limit the number of requests. Monitor your usage if you encounter rate limit errors.

## Contributing

Feel free to fork this repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the Apache-2.0 License.