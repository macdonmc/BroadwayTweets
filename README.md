# BroadwayTweets
I wrote this program to help me figure out which current Off-Broadway shows are well liked. Many shows find fame/a path to Broadway through social media (such as Be More Chill), so I though that Twitter would be a good way to collect this information.
Additionally, this program may tell us more about which shows are more likely to make it to Broadway (those which come out with a higher popularity score).

# How it works
Using Tweepy and Beautiful Soup, I was able to create this project. First, I compiled a list of all of the current Off-Broadway shows from the Playbill website in addition to lists of both positive and negative words. If either positive or negative words were found in a tweet, a count was updated that signaled this. In the end, the calculated negative count subtracted from the positive count decided which show is the most well-liked amoing Twitter users. 

# Usage
To use this, you must have a Twitter Developer's account and set up a Dev Environment to get keys and tokens.
