from duckduckgo_search import DDGS

def prompt_search(query):
    websites = ["site:al-islam.org"]
    if query:
        site_query = " OR ".join(websites)
        full_query = f"{query} {site_query}"

        ddgs = DDGS()
        results = ddgs.text(full_query, max_results=1)

        if results:
            for result in results:
                info = [
                    result['title'],
                    result['href'],
                    result['body']
                ]
                return info
    return ['', '', '']
