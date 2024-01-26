from googleapiclient.discovery import build
import pandas as pd
import numpy as np

# def youtube_search(any_youtube, max_results:int, query:str, region:str, searchtype:str, category:int):
#     search_data = []
#     video_ids = []
    
#     youtube_search_request = any_youtube.search().list(
#         part="snippet",
#         maxResults= max_results,
#         q= query,
#         regionCode= region,
#         type=searchtype,
#         videoCategoryId=category,
#         order = "viewCount",
#         fields="items(id/videoId,snippet(channelId,channelTitle,description,title)),nextPageToken,pageInfo,prevPageToken,regionCode"
#     )
    
#     # Execute the request and get the response
#     youtube_search_response = youtube_search_request.execute()
    
#     # iterate through each element in the nested dictionary to get the relevant values of each video
#     for item in youtube_search_response['items']:
#         video_id = item['id']['videoId']
#         title = item['snippet']['title']
#         channel_id = item['snippet']['channelId']
#         channel_title = item['snippet']['channelTitle']
#         description = item['snippet']['description']
        
#         # append the relevant values to the data dictionary to save as a dataframe
#         search_data.append({
#         'video_id': video_id,
#         'title': title,
#         'channel_id': channel_id,
#         'channel_title': channel_title,
#         'description': description
#         })
    
#         video_ids.append (video_id)
#         #return two dictionaries because video_id will be used in the second part of the code
#     return search_data, video_ids

def youtube_search(any_youtube, max_results: int, query: str, region: str, searchtype: str, category: int):
    search_data = []
    video_ids = []

    next_page_token = None

    while True :
        youtube_search_request = any_youtube.search().list(
            part="snippet",
            maxResults=min(50, max_results),  # Maximum allowed value is 50
            q=query,
            regionCode=region,
            type=searchtype,
            videoCategoryId=category,
            order="viewCount",
            fields="items(id/videoId,snippet(channelId,channelTitle,description,title)),nextPageToken,pageInfo,prevPageToken,regionCode",
            pageToken=next_page_token
        )

        # Execute the request and get the response
        youtube_search_response = youtube_search_request.execute()

        # iterate through each element in the nested dictionary to get the relevant values of each video
        for item in youtube_search_response.get('items', []):
            video_id = item['id']['videoId']
            title = item['snippet']['title']
            channel_id = item['snippet']['channelId']
            channel_title = item['snippet']['channelTitle']
            description = item['snippet']['description']

            # append the relevant values to the data dictionary to save as a dataframe
            search_data.append({
                'video_id': video_id,
                'title': title,
                'channel_id': channel_id,
                'channel_title': channel_title,
                'description': description
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
    
        #id = video_ids_str
    chunk_size = 50
    for i in range(0, 600, chunk_size):
        current_chunk = videoId[i:i+chunk_size-1]
        video_request = any_youtube.videos().list(
        part="statistics, id, topicDetails",
        id=current_chunk)
        print(i,i+chunk_size-1)
        video_response = video_request.execute()

    # iterate through each element in the nested dictionary to get the relevant values
    for item in video_response['items']:
        like_count = item['statistics']['likeCount']
        view_count = item['statistics']['viewCount']
        comment_count = item['statistics']['commentCount']
        wikipedia_category = item['topicDetails']['topicCategories']

        # append the relevant values to the data dictionary to save as a dataframe
        video_data.append ({
        'video_id': item['id'],
        'like_count': like_count,
        'view_count': view_count,
        'comment_count': comment_count,
        'wikipedia_categories': wikipedia_category
        })
        
    return video_data


def get_channel_stats(youtube, channel_ids):
    """
    Get channel statistics: title, subscriber count, view count, video count, upload playlist
    Params:
    
    youtube: the build object from googleapiclient.discovery
    channels_ids: list of channel IDs
    
    Returns:
    Dataframe containing the channel statistics for all channels in the provided list: title, subscriber count, view count, video count, upload playlist
    
    """
    all_data = []
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=','.join(channel_ids))
    response = request.execute() 
    
    for i in range(len(response['items'])):
        data = dict(channelName = response['items'][i]['snippet']['title'],
                    subscribers = response['items'][i]['statistics']['subscriberCount'],
                    views = response['items'][i]['statistics']['viewCount'],
                    totalVideos = response['items'][i]['statistics']['videoCount'],
                    playlistId = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
        all_data.append(data)
    
    return pd.DataFrame(all_data)

def get_video_ids(youtube, playlist_id):
    """
    Get list of video IDs of all videos in the given playlist
    Params:
    
    youtube: the build object from googleapiclient.discovery
    playlist_id: playlist ID of the channel
    
    Returns:
    List of video IDs of all videos in the playlist
    
    """
    
    request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId = playlist_id,
                maxResults = 50)
    response = request.execute()
    
    video_ids = []
    
    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])
        
    next_page_token = response.get('nextPageToken')
    more_pages = True
    
    while more_pages:
        if next_page_token is None:
            more_pages = False
        else:
            request = youtube.playlistItems().list(
                        part='contentDetails',
                        playlistId = playlist_id,
                        maxResults = 50,
                        pageToken = next_page_token)
            response = request.execute()
    
            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])
            
            next_page_token = response.get('nextPageToken')
        
    return video_ids

def get_video_details(youtube, video_ids):
    """
    Get video statistics of all videos with given IDs
    Params:
    
    youtube: the build object from googleapiclient.discovery
    video_ids: list of video IDs
    
    Returns:
    Dataframe with statistics of videos, i.e.:
        'channelTitle', 'title', 'description', 'tags', 'publishedAt'
        'viewCount', 'likeCount', 'favoriteCount', 'commentCount'
        'duration', 'definition', 'caption'
    """
        
    all_video_info = []
    
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=','.join(video_ids[i:i+50])
        )
        response = request.execute() 

        for video in response['items']:
            stats_to_keep = {'snippet': ['channelTitle', 'title', 'description', 'tags', 'publishedAt'],
                             'statistics': ['viewCount', 'likeCount', 'favouriteCount', 'commentCount'],
                             'contentDetails': ['duration', 'definition', 'caption']
                            }
            video_info = {}
            video_info['video_id'] = video['id']

            for k in stats_to_keep.keys():
                for v in stats_to_keep[k]:
                    try:
                        video_info[v] = video[k][v]
                    except:
                        video_info[v] = None

            all_video_info.append(video_info)
            
    return pd.DataFrame(all_video_info)

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
    
    for video_id in video_ids:
        try:   
            request = youtube.commentThreads().list(
                part="snippet,replies",
                videoId=video_id
            )
            response = request.execute()
        
            comments_in_video = [comment['snippet']['topLevelComment']['snippet']['textOriginal'] for comment in response['items'][0:10]]
            comments_in_video_info = {'video_id': video_id, 'comments': comments_in_video}

            all_comments.append(comments_in_video_info)
            
        except: 
            # When error occurs - most likely because comments are disabled on a video
            print('Could not get comments for video ' + video_id)
        
    return pd.DataFrame(all_comments)  
