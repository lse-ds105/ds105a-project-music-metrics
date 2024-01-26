[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/WKKzpWVj)

# DS105 Final Project

*insert snippet of most popular music video

# What makes good music? :notes:

What makes good music? One's taste of music is a rather subjective matter: one's favourite music could very well be another's most hated song. It seems that music could be one of the worst topics for newbie data scientists to choose. But... we want to challenge ourselves, and see that if even something as abstract as music can be quantified using the prowess of knowledge in DS105. While music is an art, it can also be a science. While it will be naive for us to assume that music taste can be "solved", we believe that we can at least find some insights into the world of music, by simply applying basic data science principles. Let's dive in!

# Our Findings 

[1 graph summarising the most insightful findings]
explanation
summary


# Breakdown of our tools :nut_and_bolt:

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

Hence, considering the strengths and weaknesses as a whole, we decided to

## YouTube API 



## Genius

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

# Visualisation

Show all graphs and explain each graph




# Acknowledgement of AI use

We used ChatGPT to help with creating some of our code:
for eg: 


