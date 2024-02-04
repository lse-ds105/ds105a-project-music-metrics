# DS105 Final Project

![Despacito](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTEwejk2cXFuZ28wZjA3Z29tODhpanIxMXFna2k1dzBlcmljM3lxZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l1Etct30M1D6VQUjm/giphy.gif)





# What makes good music? 🎶

What makes good music? One's taste of music is a rather subjective matter: one's favourite music could very well be another's most hated song. It seems that music could be one of the worst topics for newbie data scientists to choose. But... we want to challenge ourselves, and see that if even something as abstract as music can be quantified using the prowess of knowledge in DS105. While music is an art, it can also be a science. While it will be naive for us to assume that music taste can be "solved", we believe that we can at least find some insights into the world of music, by simply applying basic data science principles. Let's dive in!

# Our Findings 

[1 graph summarising the most insightful findings]
explanation
summary


# Breakdown of our tools 🔩

Before we present our methodology, we will first present the tools (a surgeon needs to lay down the tools before commencing the operation). Our repository will consist of several parts, namely:
* Data folder: this include raw data for testing, and saved data
* Notebook folder: this will be mainly for pure coding work
* "DeeS tools" folder: this folder is where we store all our functions! We found a way to import them directly :smirk:
  ```python
  from dees_package.genius_functions import *
  ```
* Images folder: where we keep our images used for this website\

[insert screenshots of functions]
explain how we used package folders to streamline our code

# Our sources of data :open_file_folder:

There were a few options for us to source for data, the most popular ones being YouTube API, Spotify API and Genius. After some trial and error, we have concluded:

| Scope        | YouTube           | Spotify  | Genius |
| -------------|:-------------| :-----| :-----|
| **Type** | Mostly video contents, numbers of views or likes are good popularity indicators | A lot of content available, such as artist, song duration, genre etc. | Very useful platform for lyrics of songs |
| **Relevance** | Most data are not be relevant, except for popularity indicators such as likes or views | A wide range of data available, but API provides limited access | Highly relevant for lyrics scraping |
| **Technicality** | Most data are available, with high upper bound limit (10,000) | Hard to obtain specific data due to privacy reasons, only content such as genre can be determined | Difficult to use API, but easy to obtain lyrics via web scraping instead |

Hence, considering the strengths and weaknesses as a whole, we decided to use a combination of all 3

## YouTube API 📺
For the Youtube API, we used three methods, namely the .search(), .videos(), and .commentThreads() methods. 

The .search() method is contained in the search_youtube() function and it acts just as its name suggests, we are basically inputting "official music video" into the YouTube search engine and getting the video IDs as our output. 

The methods are closely linked in our code, as the output of the search_youtube() function is used as the input for the get_stats() function and get_comments_in_videos() function which contains the .videos() and .commentThreads() methods. 

The .videos() method is used to obtain the statistics of the video, such as the number of views, likes, dislikes, comments etc. The .commentThreads() method is used to obtain the top few comments of the video.




## Genius 🟢

We used the Genius API and webscraping to scrape data on the Title, Artist and Lyrics of each song.

Beginning with the Video Title of the most popular music videos on YouTube, we first cleaned the video title to be standardised, such as removing "(Official Music Video)" from each title. We then used the Genius API to query Genius with the video title as the parameter. This allowed us to get the respective Title, Artist and URL of the Genius page for each song.

Since the API does not give us the lyrics of each song directly, we had to fall back on webscraping to get the lyrics. Using the URL of each Genius page, we ran a custom webscraping function to get the lyrics of each song as a single string, while also cleaning it to remove line breaks and section headers (such as [Bridge] or [Verse]). 

This enabled us to end up with cleaned data on the Title, Artist and Lyrics of each song, which we then merged together with the raw data collected from YouTube to form a final dataframe consisting of all the scraped data.

# Breakdown of approach

| Problem        | Solution           | Tool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

# Used functions extensively, codes for illustration :warning:

## Data Cleaning

overall breakdown
show examples

## Data Wrangling

overall breakdown
show examples


# Data Expansion 🟣

Our current dataframe is cleaned and there are several factors that we can analyse already. However, we want to dive in deeper into our analysis and potentially create even more data for even better visualisation later on. Hence, we want to expand our dataframe further by looking at the following aspects.

## 1. Lyrics 🟣

## 1.1 Song length 🟣

Most directly, given the lyrics, we are able to find the length of a song and it can be useful data.

## 1.2 Lexical richness 🟣

We want to have a sense of 


# Visualisation 🔵

Show all graphs and explain each graph



# Acknowledgement of AI use 🤖

We have relied on ChatGPT on an occasional basis throughout our project. We used ChatGPT extensively on:
* Finding the right functions, and then reading official documentation afterwards
* Debugging
* Generating ideas

These are some of the examples where we used ChatGPT:
* 


