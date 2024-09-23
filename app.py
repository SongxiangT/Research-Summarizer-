from flask import Flask, request, render_template, redirect, url_for, send_file
import openai
from scholarly import scholarly
import csv
import os

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = 'you-real-api-key-here'

# Function to filter articles based on topic and date range
def get_filtered_articles(topic, start_year, end_year, max_results):
    search_query = scholarly.search_pubs(topic)
    articles = []

    for article in search_query:
        pub_year_str = article['bib'].get('pub_year', '0')
        pub_year = int(pub_year_str) if pub_year_str.isdigit() else 0

        if len(articles) >= max_results:
            break

        if start_year <= pub_year <= end_year:
            abstract = article['bib'].get('abstract', 'No abstract available')
            articles.append({
                'title': article['bib']['title'],
                'abstract': abstract,
                'year': pub_year,
                'url': article.get('pub_url', 'No URL available')
            })

    return articles

# Function to analyze research abstracts with GPT
def analyze_with_chatgpt(abstract, language, attributes):
    prompt = (
        f"Please summarize the following research abstract in a table format with attributes "
        f"[{', '.join(attributes)}] in {language}. "
        f"Keep the answer brief and in the same format every time:\n{abstract}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

# Function to save results in CSV format
def save_to_csv(table_data_list, csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        for table_data in table_data_list:
            lines = table_data.strip().split("\n")

            headers = [header.strip() for header in lines[0].strip("|").split("|")]
            rows = []
            for line in lines[2:]:
                row = [cell.strip() for cell in line.strip("|").split("|")]
                rows.append(row)

            if file.tell() == 0:
                writer.writerow(headers)

            writer.writerows(rows)

    print(f"Data successfully saved to {csv_file}")

# Home route to render the form and handle POST requests
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        topic = request.form['topic']
        start_year = int(request.form['start_year'])
        end_year = int(request.form['end_year'])
        max_results = int(request.form['max_results'])
        language = request.form.get('language', 'English')

        # Get the customizable attributes or set defaults
        attributes = request.form.get('attributes', 'Year, Research Field, Title, Clinical Application, Methodology, Outcomes')
        attributes_list = [attr.strip() for attr in attributes.split(',')]

        articles = get_filtered_articles(topic, start_year, end_year, max_results)
        results = []

        for article in articles:
            parsed = analyze_with_chatgpt(article['abstract'], language, attributes_list)
            results.append({
                'summary': parsed,
                'url': article['url']
            })

        # Save results to CSV
        csv_file = 'research_articles.csv'
        save_to_csv([res['summary'] for res in results], csv_file)

        # Save results to text file
        text_file = 'research_articles.txt'
        with open(text_file, mode='w', encoding='utf-8') as file:
            for result in results:
                file.write(result['summary'].strip() + "\n")
                file.write(f"URL: {result['url']}\n")
                file.write("\n")

        return redirect(url_for('download_files'))

    return render_template('index.html')

# Route for downloading the files
@app.route('/download')
def download_files():
    csv_file_path = 'research_articles.csv'
    text_file_path = 'research_articles.txt'
    return render_template('download.html', csv_file=csv_file_path, text_file=text_file_path)

# Route for file download links
@app.route('/download_file/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)