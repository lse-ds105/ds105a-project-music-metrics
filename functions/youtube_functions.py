from googleapiclient.discovery import build
from IPython.display import JSON
from pprint import pprint
import pandas as pd
import json

def search_youtube(any_youtube, max_results: int, query: str, searchtype: str, region: str, category: int):
    search_data = []
    video_ids = []

    next_page_token = None

    while True :
        youtube_search_request = any_youtube.search().list(
            part="snippet",
            maxResults=min(50, max_results),  # Maximum allowed value is 50
            q=query,
            type=searchtype,
            regionCode = region,
            videoCategoryId=category,
            order="viewCount",
            fields="items(id/videoId,snippet(channelId,channelTitle,description,title)),nextPageToken,pageInfo,prevPageToken,regionCode",
            pageToken=next_page_token
        )

        # Execute the request and get the response
        youtube_search_response = youtube_search_request.execute()
        print(youtube_search_response['pageInfo']['totalResults'])

        # iterate through each element in the nested dictionary to get the relevant values of each video
        for item in youtube_search_response.get('items', []):
            video_id = item['id']['videoId']
            title = item['snippet']['title']
            channel_id = item['snippet']['channelId']
            channel_title = item['snippet']['channelTitle']

            # append the relevant values to the data dictionary to save as a dataframe
            search_data.append({
                'video_id': video_id,
                'title': title,
                'channel_id': channel_id,
                'channel_title': channel_title,
            })

            video_ids.append(video_id)

        # Check if there are more pages
        next_page_token = youtube_search_response.get('nextPageToken')
        if not next_page_token or len(video_ids) >= max_results:
            break  # No more pages or reached the desired number of results

    # Return the collected data and video IDs
    return search_data, video_ids


def get_stats(any_youtube, videoId:list):

    # video_ids_str = ','.join(videoId) # pre-2024 code, video ID as comma separated strings; but apparently it's ok to just use a list now
    video_data= []


    # create the request object
    # from the above response, we already have the channelId, channelTitle, videoID, categoryID, 
    chunk_size = 50
    for i in range(0, len(videoId), chunk_size):
        current_chunk = videoId[i:i+chunk_size-1]
        video_request = any_youtube.videos().list(
        part="statistics, id, topicDetails, contentDetails",
        id=",".join(current_chunk))

        video_response = video_request.execute()

        print(len(video_response['items']))
        pprint(video_response['items'])

    # iterate through each element in the nested dictionary to get the relevant values
        for item in video_response['items']:
            view_count = item['statistics']['viewCount'] if 'viewCount' in item['statistics'] else None
            like_count = item['statistics']['likeCount'] if 'likeCount' in item['statistics'] else None 
            comment_count = item['statistics']['commentCount'] if 'commentCount' in item['statistics'] else None
            wikipedia_category = item['topicDetails']['topicCategories'] if 'topicCategories' in item['topicDetails'] else None
            duration = item['contentDetails']['duration']


            # append the relevant values to the data dictionary to save as a dataframe
            video_data.append ({
            'video_id': item['id'],
            'view_count': view_count,
            'like_count': like_count,
            'comment_count': comment_count,
            'wikipedia_categories': wikipedia_category,
            'duration': duration
            })
            print(len(video_data))
        
    return video_data

def get_comments_in_videos(youtube, video_ids):
    """
    Get top level comments as text from all videos with given IDs (only the first 10 comments due to quote limit of Youtube API)
    Params:
    
    youtube: the build object from googleapiclient.discovery
    video_ids: list of video IDs
    
    Returns:
    Dataframe with video IDs and associated top level comment in text.
    
    """
    all_comments = []
    
    for i in range (0,len(video_ids),1):
        try:   
            request = youtube.commentThreads().list(
                part="snippet,replies",
                videoId=video_ids[i]
            )
            response = request.execute()
            print(response)
           
            comments_in_video = [comment['snippet']['topLevelComment']['snippet']['textOriginal'] for comment in response['items'][0:10]] 
            comments_in_video_info = {'video_id':video_ids[i], 'comments': comments_in_video}

            all_comments.append(comments_in_video_info)

        except Exception as e:
            print(f'Could not get comments for video {i}. Error: {e}')
        continue # Skip to the next iteration in case of an error
        
    return pd.DataFrame(all_comments)  