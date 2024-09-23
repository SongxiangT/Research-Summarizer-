# Research Abstract Summarizer

This project allows users to fetch research articles from Google Scholar, summarize their abstracts using OpenAI's GPT model, and generate tabulated summaries in a user-defined language. The main aims are:

1. **Break down language barriers** in research papers.
2. **Improve the efficiency** of research.

## Authors

- **Songxiang Tang**  
  Master of Information Systems, University of Melbourne  
  [songxiangt@student.unimelb.edu.au](mailto:songxiangt@student.unimelb.edu.au)

- **Xin Shen**  
  Master of Information Technology, University of Melbourne  
  [xsshen2@student.unimelb.edu.au](mailto:xsshen2@student.unimelb.edu.au)

- **Chun-Hao Chen**  
  Master of Information Systems, University of Melbourne  
  [chunhaoc1@student.unimelb.edu.au](mailto:chunhaoc1@student.unimelb.edu.au)

## Features

- Fetches research articles from Google Scholar.
- Summarizes research abstracts using OpenAI's GPT model.
- Supports user-defined attributes for summary tables.
- Saves the summarized data and article URLs to CSV and text files.
- Supports multiple output languages for summaries.

## Prerequisites

- **Python 3.7 or later**
- **OpenAI API key**

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

  ```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
### 2. Install dependencies:
   ``` bash
    pip install -r requirements.txt
 ```
### 3. Set up environment variables:
   The project requires an OpenAI API key to function. Configure your environment variables by creating an '.env' file in the parent directory ('../') with the following contents:
   ```json 
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_MODEL=gpt-3.5-turbo  # Default model
 ```

### 4. Run the main file

Run the main.py script:

```bash
python src/main.py
```

### 5. Customizing Attributes and Language
You can easily modify the attributes that the GPT model should summarize and the language in which the summary will be returned. This is done in the **'main()'** function within **'main.py'**.

#### Customizing Attributes <br>
To change the attributes being summarized, modify the **"user_defined_attributes'** list.
```python
user_defined_attributes = ["Year", "Research Field", "Title", "Methodology", "Results"]
```
#### Changing the Output Language
To change the language of the summary, simply modify the **'summary_language'** variable.
```python
summary_language = "Spanish"
```
Supported languages include English, Spanish, French, Chinese, etc.

### 6.  Output Formats
The program generates two output files:<br>
Table File: The research summaries are saved in table in a CSV file format named **'research_articles.csv'**.<br>
Text File: The research summaries and their corresponding URLs are saved in a text file named **'research_articles.txt'**.<br>

### 7.  Troubleshooting
#### Error: [WinError 5] Access is Denied<br>
If you receive a permission error when installing dependencies, try running the command with the **'--user'** option or check your administrative privileges.<br>
#### API Key Not Found<br>
Ensure your **'.env'** file is correctly placed in the parent directory and contains the **'OPENAI_API_KEY'** value.<br>
#### Google Scholar MaxTryExceeded Error<br>
If you encounter the MaxTryExceeded error from the Google Scholar API, it typically occurs when the number of requests exceeds the allowed limit in a short time frame.<br>

### 8.  Contributing
We welcome contributions! If you would like to contribute to the project:<br>
Fork the repository.<br>
Create a new branch for your feature or bug fix.<br>
Submit a pull request with a clear description of the changes.<br>


