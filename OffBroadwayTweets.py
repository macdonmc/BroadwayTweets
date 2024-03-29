#!/usr/bin/env python
# coding: utf-8

# In[26]:


import tweepy
import requests
from bs4 import BeautifulSoup

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#simple class to print tweets
class TweetPrinter():
    def __init__(self, consumer_key, consumer_secret, access_token, 
                 access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.auth = tweepy.OAuthHandler(self.consumer_key, 
                                        self.consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)

    def tweet_print(self):
        api = tweepy.API(self.auth)
        
        #define variables
        bestShow = ""
        bestCount = 0
        
        #create needed lists
        positiveList = createWordList("https://www.enchantedlearning.com/wordlist/positivewords.shtml")
        negativeList = createWordList("https://www.enchantedlearning.com/wordlist/negativewords.shtml")
        offBroadwayShows = createBroadwayList()
        
        for show in offBroadwayShows:
            positiveCount = 0
            negativeCount = 0
            totalScore = 0
            
            #reminder -- count automatically set to 15
            broadway_tweets = api.search(q=show, count = 2)
        
            #search thru each tweet
            for tweet in broadway_tweets:
                #find positive words in tweet
                for word in positiveList:
                    if word in tweet.text:
                        positiveCount += 1
        
                #find negative words in tweet
                for word in negativeList:
                    if word in tweet.text:
                        negativeCount += 1
                
                #decide if tweet is overall positive or negative
                if positiveCount > negativeCount:
                    totalScore += 1
                if negativeCount > positiveCount:
                    totalScore -= 1
            
            #check if it is the best score so far
            if totalScore > bestCount:
                bestCount = totalScore
                bestShow = show
            
            #check if it is the same as the best score
            if totalScore == bestCount:
                bestShow += (' & ' + show)
        
            printResults(show, totalScore)
            
        print('It looks like the most liked show is ' + bestShow + '. Go see it before it goes on Broadway!')
            
def createWordList(link):
    #create a list of positive words
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, 'html')
    myList = []
    
    for div_tag in soup.find_all('div', attrs={'class': 'wordlist-item'}):
        word = div_tag.text
        myList.append(word)
    
    return myList

def createBroadwayList():
    #create list of off broadway shows
    offBroadwayShows = []
    result = requests.get("http://www.playbill.com/productions?q=&venue-type=offbroadway&zip=")
    src = result.content
    soup = BeautifulSoup(src, 'html')

    for div_tag in soup.find_all('div', attrs={'class': 'pb-pl-tile-title'}):
        title = div_tag.text
        title = title[37:]
        title = title[:-33]
        offBroadwayShows.append(title)
    
    return offBroadwayShows

def printResults(show, totalScore):
    print('Show: '+ show)
    print('Popularity score: ' + str(totalScore))                         
                                  
def main():
    tweet_printer = TweetPrinter(consumer_key, consumer_secret, access_token, access_token_secret)
    
    tweet_printer.tweet_print()

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




