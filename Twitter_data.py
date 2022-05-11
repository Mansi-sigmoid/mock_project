# from datetime import datetime
# from kafka import KafkaConsumer, KafkaProducer
# from country import get_country_name
# from Credentials import keys
# import json
# from tweepy import Stream
# #
# producer = KafkaProducer(bootstrap_servers='localhost:9092')
# topic_name = 'SigProject10'
#
# def sig_pro():
#     class Listener(Stream):
#         def on_data(self, raw_data):
#             try:
#                 data = json.loads(raw_data)
#                 info = dict()
#                 info['id'] = data['id']
#                 if "extended_tweet" in data:
#                     info['text'] = data['extended_tweet']['full_text']
#                     # print(info['extended_tweet'])
#                 else:
#                     info['text'] = data['text']
#                     # print(info['text'])
#                 # info['text'] = data['text']
#                 info['user_name'] = data['user']['screen_name']
#                 dtime = data['created_at']
#                 new_datetime = datetime.strftime(datetime.strptime(dtime, '%a %b %d %H:%M:%S +0000 %Y'), '%d-%m-%Y ')
#                 info['created_at'] = new_datetime
#                 info['language']=data['lang']
#                 info['location'] = get_country_name(data['user']['location'])
#                 info['followers_count'] = data['user']['followers_count']
#                 info['retweet_count'] = data['retweet_count']
#                 # producer.send(topic_name, json.dumps(info).encode('utf-8'))
#                 print(info)
#             except Exception as e:
#                 print("Error",e)
#
#
#     api_key = keys()
#     api = api_key.elevated_key_3()
#
#     myStream = Listener(api[0], api[1], api[2], api[3])
#     myStream.filter(track=['#covid, #corona', '#virus', 'covid', 'corona', 'virus'])
#
# sig_pro()

from datetime import datetime
# from kafka import KafkaProducer
import json
from tweepy import Stream
#
from Credentials import keys
from country import get_country_name

# producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic_name = 'SigProject11'


class Listener(Stream):
    def on_data(self, raw_data):
        try:
            data = json.loads(raw_data)
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
            info['location'] = get_country_name(data['user']['location'])
            info['followers_count'] = data['user']['followers_count']
            info['retweet_count'] = data['retweet_count']
            # producer.send(topic_name, json.dumps(info).encode('utf-8'))
            print(info)
        except Exception as e:
            print("Error",e)



# project()

def run_airflow():
    api_key = keys()
    api = api_key.elevated_key_3()

    myStream = Listener(api[0], api[1], api[2], api[3])
    myStream.filter(track=['#covid, #corona', '#virus', 'covid', 'corona', 'virus'])
    print(api[0])


