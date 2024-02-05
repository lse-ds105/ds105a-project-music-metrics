import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_category_number(x):
    string = str(x)
    count = string.count(',')
    if count == 1:
        return "Low"
    elif count == 2:
        return "Medium"
    else:
        return "High"
    
sid = SentimentIntensityAnalyzer()
def get_sentiment_score(lyric):
    lyric_string = str(lyric)
    scores = sid.polarity_scores(lyric_string)
    list = [scores['neg'], scores['neu'], scores['pos'], scores['compound']]
    return list

def get_lexical_richness(lyric):
    lyric_string = str(lyric)
    total_words = len(lyric_string.split())
    unique_words = len(set(lyric_string.split()))
    lexical_richness = unique_words/total_words*100
    return round(lexical_richness)
    
def market_availability_category(x):
    number = float(x)
    if number == 184:
        return 'High'
    elif 50 < number < 184:
        return 'Medium'
    else:
        return 'Low'