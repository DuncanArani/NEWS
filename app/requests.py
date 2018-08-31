import urllib.request,json
from .models import Highlights

Highlights = Highlights


# Getting api key
api_key = None
# Getting the highlights base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['HIGHLIGHTS_API_KEY']
    base_url = app.config['HIGHLIGHTS_API_BASE_URL']


def get_highlights(category):
    '''
    Function that gets the json responce to our url request
    '''
    get_highlights_url = base_url.format(category,headlines,api_key)

    with urllib.request.urlopen(get_highlights_url) as url:
        get_highlights_data = url.read()
        get_highlights_response = json.loads(get_highlights_data)

        highlights_results = None

        if get_highlights_response['results']:
            highlights_results_list = get_highlights_response['results']
            highlights_results = process_results(highlights_results_list)


    return highlights_results


def get_highlights(id):
    get_highlights_details_url = base_url.format(category,headlines,api_key)

    with urllib.request.urlopen(get_highlights_details_url) as url:
        highlights_details_data = url.read()
        highlights_details_response = json.loads(highlights_details_data)

        highlights_object = None
        if highlights_details_response:
            id = highlights_details_response.get('id')
            title = highlights_details_response.get('original_title')
            sammary = highlights_details_response.get('sammary')
            image = highlights_details_response.get('image_path')
            vote_average = highlights_details_response.get('vote_average')
            vote_count = highlights_details_response.get('vote_count')

            highlights_object =highlights(id,title,sammary,image,vote_average,vote_count)

    return highlights_object



def search_highlights(highlights_name):
    search_highlights_url = 'https://newsapi.org/v2/top-headlines?country={}&category={}&apiKey={}'.format(category,headlines,api_key)
    with urllib.request.urlopen(search_highlights_url) as url:
        search_highlights_data = url.read()
        search_highlights_response = json.loads(search_highlights_data)

        search_highlights_results = None

        if search_highlights_response['results']:
            search_highlights_list = search_highlights_response['results']
            search_highlights_results = process_results(search_highlights_list)


    return search_highlights_results




def process_results(highlights_list):
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
        title = highlights_item.get('original_title')
        sammary = highlights_item.get('sammary')
        image = highlights_item.get('image_path')
        vote_average = highlights_item.get('vote_average')
        vote_count = highlights_item.get('vote_count')

        if image:

            highlights_object = Highlights(id,title,sammary,image,vote_average,vote_count)
            highlights_results.append(highlights_object)

    return highlights_results
