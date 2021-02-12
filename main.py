import praw, heapq
import numpy as np
from secret import ClientID, ClientSecret, Username, Password, User_agent

reddit = praw.Reddit(client_id = ClientID, client_secret = ClientSecret, username = Username, password = Password, user_agent = User_agent) # login into Reddit with Dev Account

subreddit = reddit.subreddit("wallstreetbets") # subreddit looking at 

# ticker and counter
commonWords = np.loadtxt("commonWords.txt", dtype=str)
commonWords = np.char.lower(commonWords)
ticker = []
counter = []


print("Running: ")
for comment in subreddit.stream.comments(): # stream from reddit, since processing is slow the stream is fast enough
    currentComment = comment.body.split() # splits comments into arrays each index == word
    for currentWord in currentComment: # goes through the array word by word
        currentWord = currentWord.lower() # lowers words
        if not(currentWord in commonWords): # checks if word is in commonWords
            if (currentWord.find("’") == -1 and currentWord.find("'") == -1 and currentWord.find(".") == -1 and currentWord.find(",") == -1 and currentWord.find("=") == -1 and currentWord.find("%") == -1 
            and currentWord.find("*") == -1 and currentWord.find("[") == -1 and currentWord.find("]") == -1 and currentWord.find("!") == -1 and currentWord.find("@") == -1 and currentWord.find("?") == -1 
            and currentWord.find("&") == -1 and currentWord.find(":") == -1 and currentWord.find("(") == -1 and currentWord.find(")") == -1 and currentWord.find("/") == -1 and currentWord.find("\"") == -1 
            and currentWord.find("-") == -1 and currentWord.find("0") == -1 and currentWord.find("1") == -1 and currentWord.find("2") == -1 and currentWord.find("3") == -1 and currentWord.find("4") == -1 
            and currentWord.find("5") == -1 and currentWord.find("6") == -1 and currentWord.find("7") == -1 and currentWord.find("8") == -1 and currentWord.find("9") == -1): # check special characters
                if not(currentWord in ticker): # checks if word is in ticker
                    ticker.append(currentWord) # appends new word to ticker
                    counter.append(1) # adds one to the new counter slot for the new word
                else: 
                    index = ticker.index(currentWord) # finds index of word inside ticker
                    counter[index] += 1 # adds one to the index of the new word


        tickerIndex = heapq.nlargest(10, range(len(counter)), counter.__getitem__) # finds index of 10 biggest values in counter
        with open("result.txt", "w") as file: # writes ticker and counter into result.txt
            for i in tickerIndex:
                line = [(ticker[i]), " - ", str(counter[i]), "\n"]
                file.writelines(line)
            file.close()


