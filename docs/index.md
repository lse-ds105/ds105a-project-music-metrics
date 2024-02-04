# DS105 Final Project – Music Metrics

_What type of music do AI models prefer? Algo-rhythms._

![Despacito](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTEwejk2cXFuZ28wZjA3Z29tODhpanIxMXFna2k1dzBlcmljM3lxZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l1Etct30M1D6VQUjm/giphy.gif)





# What makes good music? 🎶

What makes good music? One's taste of music is a rather subjective matter: one's favourite music could very well be another's most hated song. It seems that music could be one of the worst topics for newbie data scientists to choose. But... we want to challenge ourselves, and see that if even something as abstract as music can be quantified using the prowess of knowledge in DS105. While music is an art, it can also be a science. While it will be naive for us to assume that music taste can be "solved", we believe that we can at least find some insights into the world of music, by simply applying basic data science principles. Let's dive in!

# ⚠️Spoiler alert: a snippet of a final result 😲

[1 graph summarising the most insightful findings]
explanation
summary

# Procurement Map 🔴🟡🟢🟣🔵

This is the breakdown of our overall approach. We have categorised our approach into different categories and colour-coded them. We have 🔴 for YouTube, 🟡 for Genius, 🟢 for Spotify, 🟣 for data expansion, and 🔵 for visualisation.

'screenshot'

# Breakdown of our tools 🔴🟡🟢🟣🔵

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

# Our sources of data 🔴🟡🟢

There were a few options for us to source for data, the most popular ones being YouTube API, Spotify API and Genius. After some trial and error, we have concluded:

| Scope        | YouTube 🔴          | Spotify 🟢  | Genius 🟡 |
| :-------------|:-------------| :-----| :-----|
| **Type** | Mostly video contents, numbers of views or likes are good popularity indicators | A lot of content available, such as artist, song duration, genre etc. | Very useful platform for lyrics of songs |
| **Relevance** | Most data are not be relevant, except for popularity indicators such as likes or views | A wide range of data available, but API provides limited access | Highly relevant for lyrics scraping |
| **Technicality** | Most data are available, with high upper bound limit (10,000) | Hard to obtain specific data due to privacy reasons, only content such as genre can be determined | Difficult to use API, but easy to obtain lyrics via web scraping instead |

Hence, considering the strengths and weaknesses as a whole, we decided to use a combination of all 3

# YouTube API 🔴
For the Youtube API, we used three methods, namely the .search(), .videos(), and .commentThreads() methods. 

The .search() method is contained in the search_youtube() function and it acts just as its name suggests, we are basically inputting "official music video" into the YouTube search engine and getting the video IDs as our output. 

The methods are closely linked in our code, as the output of the search_youtube() function is used as the input for the get_stats() function and get_comments_in_videos() function which contains the .videos() and .commentThreads() methods. 

The .videos() method is used to obtain the statistics of the video, such as the number of views, likes, dislikes, comments etc. The .commentThreads() method is used to obtain the top few comments of the video.




# Genius 🟡

We used the Genius API and webscraping to scrape data on the Title, Artist and Lyrics of each song.

Beginning with the Video Title of the most popular music videos on YouTube, we first cleaned the video title to be standardised, such as removing "(Official Music Video)" from each title. We then used the Genius API to query Genius with the video title as the parameter. This allowed us to get the respective Title, Artist and URL of the Genius page for each song.

Since the API does not give us the lyrics of each song directly, we had to fall back on webscraping to get the lyrics. Using the URL of each Genius page, we ran a custom webscraping function to get the lyrics of each song as a single string, while also cleaning it to remove line breaks and section headers (such as [Bridge] or [Verse]). 

This enabled us to end up with cleaned data on the Title, Artist and Lyrics of each song, which we then merged together with the raw data collected from YouTube to form a final dataframe consisting of all the scraped data.

# Spotify API 🟢

We leverage on the Spotify API to obtain an access token.

We then found a very useful `spotipy` package that is available. Using our access token and the package, we are able to use the `search()` tool to obtain a huge `json` format regarding a particular song. We then used [JSON Crack]([url](https://jsoncrack.com/)) to navigate the output and we are able to find insights such as a song's release date, popularity, explicitness and available markets.

# Data Expansion 🟣

Our current dataframe is cleaned and there are several factors that we can analyse already. However, we want to dive in deeper into our analysis and potentially create even more data for even better visualisation later on. Hence, we want to expand our dataframe further by looking at the following aspects.

#### Song length 🟣

Most directly, given the lyrics, we are able to find the length of a song and it can be useful data.

#### Lexical richness 🟣

We want to have a sense of the range of vocabulary being used. To measure this quantitatively, we have identified a popular matrix called "lexical richness". In our definition, it is the proportion of unique words used of total words.

#### Sentiment analysis 🟣

We found the package `nltk` particularly useful for sentiment analysis. Given a particular lyric, we are able to determine the level of sadness, happiness, as well as an overall score for the sentiment called "sentiment compound".

#### Market category 🟣


#### Genre category 🟣



# Visualisation 🔵

Once we have expanded our dataframe, we are able to have a wider range of data for visualisation purposes. Here is our final dataframe:

Dataframe

We used three different methodologies for data visualisation and analysis, namely:
* Statistical inference
* Univariate visualisation
* Multivariate visualisation

#### Statistical inference 🔵


#### Univariate visualisation 🔵


#### Multivariate visualisation 🔵

# Before we conclude... Just some highlights of our skills 🌟

We have conducted extensive data cleaning, data manipulation and data wrangling throughout all our notebooks. However, to highlight a few skillsets that we have used:

#### 'description' 🔴
```python
code = code
```

# Conclusion 🔥
* Bullet 1
* Bullet 2

# Acknowledgement of AI use 🤖

We have relied on ChatGPT on an occasional basis throughout our project. We used ChatGPT extensively on:
* Finding the right functions, and then reading official documentation afterwards
* Debugging
* Generating ideas

These are some of the examples where we used ChatGPT:

|         | Example Prompt           | Rationale  |
| :------------- |:-------------| :-----|
| 🔴 |  |  |
| 🔴 |  |   |
| 🟡 |  |  |
| 🟡 |  |   |
| 🟢 |  |  |
| 🟢 |  |  |
| 🟣 | "Brainstorm some ideas of how to analyse lyrics" | We used ChatGPT to brainstorm ideas, and then we crafted our own functions based on some of the ideas |
| 🟣 | "What are the ways to conduct sentiment analysis?" | ChatGPT will recommend nltk as one of the packages, then we will Google the actual package and read its documentation |
| 🔵 | "How to plot contour lines using ggplot2?" | ChatGPT will give an overall guidance, and we will read the actual documentation afterwards |
| 🔵 | "What are the effective ways to find correlations in a dataframe?"  | One of the answers is "correlation matrix". Then we will proceed to find a YouTube step-by-step tutorial of how to plot this nicely, with explanations |

# Finally... Some reflections
* First of all, this project may have come to an end for DS105, but it is not the end for us. 
* We have found success in multiple areas – APIs, web-scraping, data manipulation. 😄
* But we have failed in others – building effective models, machine learning, or providing an *exhaustive* list of insights. 😢
* Therefore, we have decided that when we upgrade our coding skills, in particular: ❗
* Learning new languages
* Learning machine learning
* Taking higher-level statistics courses (beyond ST109)
* We are able to come back to this project and build a highly-advanced model that can truly understand music at the next level... 👀
* Till next time! 👋
