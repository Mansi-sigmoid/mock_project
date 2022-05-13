from datetime import datetime
from kafka import KafkaConsumer, KafkaProducer
from country import get_country_name
from encrypt import keys
import json
from tweepy import Stream
producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic_name = 'Topic_1' #user defined

count = 0
class Listener(Stream):
    def on_data(self, raw_data):
        global count
        count += 1
        data = json.loads(raw_data)
        info = dict()
        info['id'] = data['id']
        info['text'] = data['text']
        info['created_at'] = data['created_at']
        info['location'] = data['user']['location']
        info['name'] = data['user']['name']
        info['followers_count'] = data['user']['followers_count']
        info['retweet_count'] = data['retweet_count']
        # print(info)
        print(count)
        # producer.send(topic_name, json.dumps(info).encode('utf-8'))
        if count == 20:
            self.disconnect()

    def disconnect(self):
        if self.running is False:
            return
        self.running = False

    def on_closed(self, response):
        print("Stream closed")




api_key = keys()
# api = api_key.elevated_key_3()
api=api_key.keys()

myStream = Listener(api[0], api[1], api[2], api[3])
myStream.filter(track=['#covid, #corona', '#virus', 'covid', 'corona', 'virus']) #Filter for covid tweets

