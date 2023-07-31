import tweepy
import random
import time

client = tweepy.Client(consumer_key='YOUR_CONSUMER_KEY_HERE',
                       consumer_secret='YOUR_CONSUMER_SECRETE_HERE',
                       access_token='YOUR_ACCESS_TOKEN_HERE',
                       access_token_secret='YOUR_ACCESS_TOKEN_SECRET_HERE')

# Create a list of files to read from -- these must be in the same folder as this script or be correctly linked
files = ["mulholland_drive.txt", "blue_velvet.txt", "the_elephant_man.txt","firewalkwithme.txt","eraserhead.txt"]

# Iterate through the files and read a random line from each file
for file in files:
    with open(file) as f:
        lines = f.readlines()
        line = random.choice(lines)

        # Check if the line contains any words
        if len(line.split()) > 0:
            try:
                response = client.create_tweet(text=line)
                print(response)
                # waits two minutes to tweet again
                time.sleep(120)
            except tweepy.errors.BadRequest:
                print("Error. There must be something wrong...")
        else:
            print("Skipping blank line.")

