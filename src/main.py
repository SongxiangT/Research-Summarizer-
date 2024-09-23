from scholarly_search import get_filtered_articles
from gpt_analysis import analyze_with_chatgpt
from data_saver import save2Csv
from data_saver import save2Textt


def main():
    results = []
    # User-defined attributes and language
    user_defined_attributes = ["Year", "Research Field", "Title", "Clinical Application", "Methodology", "Outcomes"]
    summary_language = "English"  # You can change to other languages like "Spanish", "French", "Chinese", etc.

    # The basic paras
    """
    Fetches articles related to a topic from Google Scholar and filters them by year.
    :param max_results: Maximum number of articles to fetch.
    :param topic: The research topic to search for.
    :param start_year: Start year for filtering articles.
    :param end_year: End year for filtering articles.
    """
    max_results = 10  # Adjust based on needs
    topic = "computer assisted rehabilitation environment"
    start_year = 2019
    end_year = 2024

    articles = get_filtered_articles(topic, start_year, end_year, max_results)

    if not articles:
        print("No articles found in the specified date range.")
        return

    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Year: {article['year']}")
        print(f"Abstract: {article['abstract']}")
        parsed = analyze_with_chatgpt(article['abstract'], user_defined_attributes, summary_language)
        print(parsed)
        results.append({
            'summary': parsed,
            'url': article['url']
        })
        print(f"URL: {article['url']}")
        print("\n" + "=" * 80 + "\n")

    save2Csv([result['summary'] for result in results], "research_articles.csv")
    save2Textt(results, "research_articles.txt")

if __name__ == "__main__":
    main()