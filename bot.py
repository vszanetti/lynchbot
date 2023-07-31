import tweepy
import random
import time

client = tweepy.Client(consumer_key='2tCHECuZnByqUCK3lPIuSfzWR',
                       consumer_secret='tak1VFhuDBiPDWlyLBrSUhDE6o5cHFoyp8TU1zV7TbtkATQe3x',
                       access_token='983374461222211584-n6IxqXDcM5gyyzxypH87Eb53bq5iy6e',
                       access_token_secret='QWI1cUOycGwE5e9IVUszOAh8OdGJi5ilBybtLvVRGYh73')

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

