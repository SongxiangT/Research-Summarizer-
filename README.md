# Research Abstract Summarizer

This project fetches research articles related to a specific topic from Google Scholar, analyzes their abstracts using OpenAI's GPT model, and summarizes the information in a table format in a chosen language.

## Features

- Fetches research articles from Google Scholar.
- Summarizes research abstracts using OpenAI's GPT model.
- Supports user-defined attributes for summary tables.
- Saves the summarized data and article url to CSV and text files.
- Supports multiple output languages for summaries.

## Prerequisites

- Python 3.7 or later
- OpenAI API key

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

  ```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
###2. Install dependencies:
   ``` bash
    pip install -r requirements.txt
 ```
###3. Set up environment variables:
   The project requires an OpenAI API key to function. Configure your environment variables by creating an env.dotenv file in the parent directory (../) with the following contents:
   ```json 
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_MODEL=gpt-3.5-turbo  # Default model
 ```

## 4. Run the main file

Run the main.py script:

```bash
python src/main.py
```
