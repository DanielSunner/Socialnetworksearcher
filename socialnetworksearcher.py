from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from Tkinter import *

access_token = "121151191-5ZjT7JKG3xHzTvCx8UwGc6uoRC7lSnx8b0szlYMK"
access_token_secret = "xOJm8RsUFJ5kQHCZ0o6Fkro7gOAOfORyk8dPjuXGDF5dV"
consumer_key = "2Ys2KkW3fjFc4Yjo6ep1FNwzV"
consumer_secret = "Zi1bCBAVpfiaghQOU0XEqkBiSY7ObHq1XplyKSYzJuZto0OLRs"

root = Tk()

class listener(StreamListener):
	def on_data(self, data):
		tweet = data.split(',"text":"')[1].split('","source')[0]
		print tweet
		saveFile =open('twitDB.csv','a')
		saveFile.write(data)
		saveFile.write('\n')
		saveFile.close()
		return True
	def on_error(self, status):
		print status

button_1 = Button(root, text="search for tweets", command=listener)
button_1.pack()

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["gun"])




