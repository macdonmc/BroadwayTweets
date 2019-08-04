# BroadwayTweets
I wrote this program to help me figure out which current Off-Broadway shows are well liked. Many shows find fame/a path to Broadway through social media (such as Be More Chill), so I thought that Twitter would be a good way to collect this information.
Additionally, this program may tell us more about which shows are more likely to make it to Broadway (those which come out with a higher popularity score).

# How it works
Using Tweepy and Beautiful Soup, I was able to create this project. First, I compiled a list of all of the current Off-Broadway shows from the Playbill website in addition to lists of both positive and negative words. Using the word lists, each tweet is deemed either positive or negative (or it is ignored if none of these words are found). Each show then recieves a total popularity score and the final outcome is a reccomendation of which show(s) to go to.

# Usage
To use this, you must have a Twitter Developer's account and set up a Dev Environment to get keys and tokens.
