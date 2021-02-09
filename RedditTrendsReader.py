
import praw, os, time, threading, math
import numpy as np
import graphRedditBot
from datetime import datetime

from secret import ClientID, ClientSecret, Username, Password, User_agent

reddit = praw.Reddit(client_id = ClientID, client_secret = ClientSecret, username = Username, password = Password, user_agent = User_agent) #Login into Reddit with Dev Account

subreddit = reddit.subreddit("wallstreetbets") # Subreddit looking at 


#Ticker and Counter:
commonWords = np.loadtxt("commonWords.txt", dtype=str)
commonWords = np.char.lower(commonWords)
ticker = []
alreadyPrinted = []
counter = []


print("Running: ")
for comment in subreddit.stream.comments(): # Stream from reddit, since processing is slow the stream is fast enough
    currentComment = comment.body.split() # splits comments into arrays each index == word
    for currentWord in currentComment: # goes through the array word by word
        currentWord = currentWord.lower() # lowercase to compare words
        if not(currentWord in commonWords): # checks if word is in commonWords
            if (currentWord.find("’") == -1 and currentWord.find("'") == -1 and currentWord.find(".") == -1 and currentWord.find(",") == -1 and currentWord.find("=") == -1 and currentWord.find("%") == -1 
            and currentWord.find("*") == -1 and currentWord.find("[") == -1 and currentWord.find("]") == -1 and currentWord.find("!") == -1 and currentWord.find("@") == -1 and currentWord.find("?") == -1 
            and currentWord.find("&") == -1 and currentWord.find(":") == -1 and currentWord.find("(") == -1 and currentWord.find(")") == -1 and currentWord.find("/") == -1 and currentWord.find("\"") == -1 
            and currentWord.find("-") == -1 and currentWord.find("0") == -1 and currentWord.find("1") == -1 and currentWord.find("2") == -1 and currentWord.find("3") == -1 and currentWord.find("4") == -1 
            and currentWord.find("5") == -1 and currentWord.find("6") == -1 and currentWord.find("7") == -1 and currentWord.find("8") == -1 and currentWord.find("9") == -1): # Check Special Characters
                        if not(currentWord in ticker): # checks if word is in ticker
                            ticker.append(currentWord) # appends new word to ticker
                            counter.append(1) # adds one to the new counter slot for the new word
                        else: 
                            index = ticker.index(currentWord) # finds index of word inside ticker
                            counter[index] += 1 # adds one to the index of the new word

    for i in range(len(ticker)): # goes through ticker 
        if not(ticker[i] in alreadyPrinted): # checks if word in ticker was already printed
            if counter[i] > 10: # if not printed checks if it was mentioned more than 10 times
                alreadyPrinted.append(ticker[i]) #adds not printed word with 10+ mentions to alreadyPrinted 
                print(ticker[i]) # prints new word with 10+ mentions
