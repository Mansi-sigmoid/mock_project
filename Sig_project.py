from datetime import datetime
from kafka import KafkaConsumer, KafkaProducer
from country import get_country_name
from encrypt import keys
import json
from tweepy import Stream
producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic_name = 'Topic_1' #user defined

class Listener(Stream):
    def on_data(self, raw_data):
        try:
            data = json.loads(raw_data) #to json format
            info = dict()
            info['id'] = data['id']
            if "extended_tweet" in data:
                info['text'] = data['extended_tweet']['full_text']
                # print(info['extended_tweet'])
            else:
                info['text'] = data['text']
                # print(info['text'])
            # info['text'] = data['text']
            info['user_name'] = data['user']['screen_name']
            dtime = data['created_at']
            new_datetime = datetime.strftime(datetime.strptime(dtime, '%a %b %d %H:%M:%S +0000 %Y'), '%d-%m-%Y ')
            info['created_at'] = new_datetime
            info['language']=data['lang']
            info['location'] = get_country_name(data['user']['location']) #to get the valid country name.
            info['followers_count'] = data['user']['followers_count']
            info['retweet_count'] = data['retweet_count']
            producer.send(topic_name, json.dumps(info).encode('utf-8'))  #send the data from twitter to Kafka topic
            print(info)
        except Exception as e:
            print("Error",e)




api_key = keys()
# api = api_key.elevated_key_3()
api=api_key.keys()

myStream = Listener(api[0], api[1], api[2], api[3])
myStream.filter(track=['#covid, #corona', '#virus', 'covid', 'corona', 'virus']) #Filter for covid tweets

