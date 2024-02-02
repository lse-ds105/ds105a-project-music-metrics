import nltk
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