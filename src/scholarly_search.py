from scholarly import scholarly

def get_filtered_articles(topic, start_year, end_year, max_results):
    """
    Fetches articles related to a topic from Google Scholar and filters them by year.

    :param topic: The research topic to search for.
    :param start_year: Start year for filtering articles.
    :param end_year: End year for filtering articles.
    :param max_results: Maximum number of articles to fetch.
    :return: List of filtered articles with title, abstract, year, and URL.
    """
    search_query = scholarly.search_pubs(topic)
    articles = []

    for article in search_query:
        # Check the publication year for the article
        pub_year_str = article['bib'].get('pub_year', '0')
        pub_year = int(pub_year_str) if pub_year_str.isdigit() else 0

        # Show progress
        print(f"Progress: {len(articles)}/{max_results}")
        print(f"Found article: {article['bib']['title']} ({pub_year})")

        # Stop if the desired number of articles is reached
        if len(articles) >= max_results:
            break

        # Filter targeted articles
        if start_year <= pub_year <= end_year:
            abstract = article['bib'].get('abstract', 'No abstract available')
            articles.append({
                'title': article['bib']['title'],
                'abstract': abstract,
                'year': pub_year,
                'url': article.get('pub_url', 'No URL available')
            })

    return articles
