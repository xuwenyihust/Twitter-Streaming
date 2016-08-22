from tweepy.streaming import StreamListener
import json

class listener(StreamListener):
	
	def on_data(self, data):
		#all_data = json.loads(data)
		#tweet = all_data['text']
		#username = all_data['user']['screen_name']
		print(data)
		return True

	def on_error(self, status):
		print(status)

