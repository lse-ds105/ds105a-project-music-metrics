import requests
from scrapy import Selector
import re

def search_genius(query, access_token):
    '''
    Returns a dictionary of song title, artist and URL

        Parameters:
            query (str): The video title scraped from YouTube
            access_token (str): The Genius API access token

        Returns:
            data_as_dict (dict): A dictionary containing song title, artist and URL
    '''

    base_url = 'https://api.genius.com'
    search_endpoint = '/search'

    # prepare headers with authorization
    headers = {'Authorization': f'Bearer {access_token}'}

    # prepare the query parameter
    params = {'q': query}

    # make a request to the Genius API
    response = requests.get(base_url + search_endpoint, headers=headers, params=params)
    
    # parse the JSON response
    data = response.json()

    # find the first result with a URL ending in 'lyrics'
    for hit in data['response']['hits']:
        result = hit['result']
        title = result['title']
        artist = result['primary_artist']['name']
        url = result['url']

        # append the information to the list
        data_as_dict = {'Title': title or '', 'Artist': artist or '', 'URL': url or ''}
        # stop the loop after finding the first matching result
        return data_as_dict
    
    # return empty strings if no information is found
    return {'Title': '', 'Artist': '', 'URL': ''}

def scrape_lyrics(session, song_url):
    '''
    Returns a string of song lyrics, with each line separated by a new line

        Parameters:
            session (variable): The session that has been initialised for requesting from the Genius website
            song_url (str): The URL of the Genius page for the song

        Returns:
            lyrics (str): The lyrics of the song
    '''
    
    # use initialised session to enhance performance
    response = session.get(song_url)
    sel = Selector(text=response.text)
    
    # scrape lyrics into one large string
    raw_lyrics = ' '.join(sel.css('div.Lyrics__Container-sc-1ynbvzw-1.kUgSbL ::text').getall())

    # clean lyrics using regular expression to remove words in square brackets
    pattern = r'\[.*?\]'
    result_string = re.sub(pattern, '', raw_lyrics)
    lyrics = ' '.join(result_string.split())

    return lyrics