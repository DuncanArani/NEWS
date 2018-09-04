import urllib.request,json
from .models import Source
# Highlights = Highlights


# Getting api key
api_key = None
# Getting the highlights base url
base_url = None
highlights_url = None
catg_url = None


def configure_request(app):
    global api_key, base_url,  catg_url
    api_key = app.config['HIGHLIGHTS_API_KEY']
    base_url = app.config['SOURCES_API_BASE_URL']
    highlights_url = app.config['HIGHLIGHTS_API_BASE_URL']
    catg_url = app.config['CATG_API_BASE_URL']


def get_source(source_name):
    get_source_url = base_url.format(source_name,api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        get_source_results = None

        if get_source_response['sources']:
            get_source_list = get_source_response['sources']
            get_source_results = process_sources(get_source_list)


    return get_source_results

def process_sources(sources):
    '''
    Function  that processes the highlights result and transform them to a list of Objects
    Args:
        highlights_list: A list of dictionaries that contain highlights details
    Returns :
        highlights_results: A list of highlights objects
    '''
    sources_results = []
    for source in sources:
        id = source.get('id')
        title = source.get('title')
        description = source.get('descriptrion')
        link = source.get('url')
        type = source.get('category')
        place = source.get('country')

    

        sources_object = Source(id,title,description,link, type,place)
        sources_results.append(sources_object)
            
    return sources_results

def get_articles(id):
    get_articles_url = base_url.format(id,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        get_articles_results = None

        if get_articles_response['article']:
            get_articles_list = get_articles_response['article']
            get_articles_results = process_articles(get_articles_list)


    return get_articles_results

def process_articles(articles):
    '''
    Function  that processes the highlights result and transform them to a list of Objects
    Args:
        highlights_list: A list of dictionaries that contain highlights details
    Returns :
        highlights_results: A list of highlights objects
    '''
    articles_results = []
    for article in artyicles:
        id = articles.get('id')
        title = articles.get('title')
        sammary = articles.get('descriptrion')
        link = articles.get('url')
        place = articles.get('title')
        urlToImage = urlToImage
        publishedAt = publishedAt
    

        articles_object = Article(id,title,link, description, urlToImage,  publishedAt)
        articles_results.append(artcle_object)
            
    return articles_results


def get_highlights(highlight_sammary):
    get_highlights_url = base_url.format(highlight_sammary,api_key)
    with urllib.request.urlopen(get_highlights_url) as url:
        get_highlights_data = url.read()
        get_highlights_response = json.loads(get_highlights_data)

        get_highlights_results = None

        if get_highlights_response['highlight']:
            get_highlights_list = get_highlights_response['highlight']
            get_highlights_results = process_highlights(get_highlights_list)


    return get_highlights_results

def process_highlights(highlights):
    '''
    Function  that processes the highlights result and transform them to a list of Objects
    Args:
        highlights_list: A list of dictionaries that contain highlights details
    Returns :
        highlights_results: A list of highlights objects
    '''
    highlights_results = []
    for highlights in highlights:
        id = highlights.get('id')
        title = highlights.get('name')
        sammary = highlights.get('descriptrion')
        link = highlights.get('url')
        place = highlights.get('title')
        urlToImage = urlToImage
        publishedAt = publishedAt
    

        
        highlights_object = highlights(id,title, link, url, description, urlToImage,  publishedAt)
        highlightss_results.append(artcle_object)
            
    return highlightss_results




       
