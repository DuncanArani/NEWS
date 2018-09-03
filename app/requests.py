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
    # highlights_url = app.config['HIGHLIGHTS_API_BASE_URL']
    # catg_url = app.config['CATG_API_BASE_URL']


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
        title = source.get('name')
        sammary = source.get('descriptrion')
        link = source.get('url')
        type = source.get('category')
        place = source.get('country')

    

        sources_object = Source(id,title,sammary,link, type,place)
        sources_results.append(sources_object)
            
    return sources_results



# def get_category(highlights, apikey):
#     get_category_url = 'https://newsapi.org/v2/top-headlines?country={}&category={}&apiKey={}'.format(category,headlines,api_key)
#     with urllib.request.urlopen(get_category_url) as url:
#         get_category_data = url.read()
#         get_category_response = json.loads(get_category_data)

#         search_highlights_results = None

#         if get_category_response['results']:
#             get_category_list = get_category_response['results']
#             get_category_results = process_results(get_category_list)


#     return category_results

# def get_highlights(category,highlights,api_key):
#     get_highlights_articles_url = base_url.format(category,highlights,api_key)

#     with urllib.request.urlopen(get_highlights_articles_url) as url:
#         highlights_articles_data = url.read()
#         highlights_articles_response = json.loads(highlights_articles_data)

#         highlights_object = None
#         if highlights_articles_response:
#             id = highlights_articles_response.get('id')
#             title = highlights_articles_response.get('original_title')
#             sammary = highlights_articles_response.get('sammary')
#             image = highlights_articles_response.get('image_path')
#             vote_average = highlights_articles_response.get('vote_average')
#             vote_count = highlights_articles_response.get('vote_count')

#             highlights_object =highlights(id,title,sammary,image,vote_average,vote_count)

#     return highlights_object



# def search_highlights(highlights_name):
#     search_highlights_url = 'https://newsapi.org/v2/top-headlines?country={}&category={}&apiKey={}'.format(category,highlights_name,api_key)
#     with urllib.request.urlopen(search_highlights_url) as url:
#         search_highlights_data = url.read()
#         search_highlights_response = json.loads(search_highlights_data)

#         search_highlights_results = None

#         if search_highlights_response['results']:
#             search_highlights_list = search_highlights_response['results']
#             search_highlights_results = process_results(search_highlights_list)


#     return search_highlights_results




# def process_sources(highlights_list):
    '''
    Function  that processes the highlights result and transform them to a list of Objects
    Args:
        highlights_list: A list of dictionaries that contain highlights details
    Returns :
        highlights_results: A list of highlights objects
    '''
    highlights_results = []
    for highlights_item in highlights_list:
        id = highlights_item.get('id')
        title = highlights_item.get('name')
        sammary = highlights_item.get('discriptrion')
        link = highlights_item.get('url')
        type = highlights_item.get('category')
        place = highlights_item.get('country')

        

        highlights_object = Source(id,title,sammary,link, type,place)
        highlights_results.append(highlights_object)

    return highlights_results
