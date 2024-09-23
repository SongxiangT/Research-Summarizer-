import openai
import os
from dotenv import load_dotenv  # Import dotenv to load environment variables

# Load environment variables from .env file
load_dotenv(dotenv_path='../env.dotenv')

# Load OpenAI API Key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

def analyze_with_chatgpt(abstract, attributes=None, language='English'):
    """
    Analyzes an abstract with OpenAI's GPT model and returns a summarized table format.

    :param abstract: The abstract of the research paper.
    :param attributes: List of attributes for the table format. Default is ["Year", "Research Field", "Title", "Clinical Application", "Methodology", "Outcomes"].
    :param language: Language for the summarized table. Default is 'English'.
    :return: Summarized table format as a string.
    """
    # Set default attributes if none are provided
    if attributes is None:
        attributes = ["Year", "Research Field", "Title", "Clinical Application", "Methodology", "Outcomes"]

    # Create a string from attributes for prompt customization
    attributes_str = ", ".join(attributes)

    # Prepare the prompt for ChatGPT
    prompt = (
        f"Please summarize the following research abstract in table format with attributes "
        f"[{attributes_str}]. Keep the answer brief and in the same format every time. "
        f"Respond in {language}:\n{abstract}"
    )

    # Make the API call
    response = openai.ChatCompletion.create(
        model=os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo'),
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message['content']