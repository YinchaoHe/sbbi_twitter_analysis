import threading
import json
import os
import time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

# Enter Twitter API Keys
access_token = '1352703664713052161-Zd0hO2IBh45G081ZAuPDKkxkcf3AOn'#"ENTER ACCESS TOKEN"
access_token_secret = 'OkZ4wMSZ61ieue46Lat5Ve5Ha6skaAqFyj8K9rBFprUJy' #"ENTER ACCESS TOKEN SECRET"
consumer_key = 'S8VooVgIjBeX065l7aM9nrXFh' #"ENTER CONSUMER KEY"
consumer_secret = 'NA2gYfho2CgyF82yGlxifMDarMaAMVwmjxyGrbRBql9kaEBH0X' #"ENTER CONSUMER SECRET"

#evantual tweets array
tweets = []
amount = 0
exitFlag = 1
# Create the class that will handle the tweet stream
class StdOutListener(StreamListener):


    def on_data(self, data):
        global tweets
        global amount
        tweet = {}
        data_json = json.loads(data)
        if not data_json['retweeted'] and 'RT @' not in data_json['text']:
            tweet["created_at"] = data_json["created_at"]
            tweet["id"] = data_json["id"]
            tweet["text"] = data_json["text"]
            tweet["user"] = data_json["user"]
            tweet["geo"] = data_json["geo"]
            tweet["coordinates"] = data_json["coordinates"]
            tweet["place"] = data_json["place"]
            tweet["favorite_count"] = data_json["favorite_count"]
            tweet["entities"] = data_json["entities"]
            with open("TwitterData_Stream/" + food4search + "/result.json", 'a') as file:
                json.dump(tweet, file)
                file.write(",\n")
            file.close()
            tweets.append(tweet)
            print(food4search)
            print(tweet["created_at"])
            amount += 1
            time.sleep(3)
            return True


    def on_error(self, status):
        print(status)

def Twitter_Stream_handler_1(tracklist, category, name):
    # Handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    threadLock = threading.Lock()
    global exitFlag
    while True:
        if exitFlag == 1:
            threadLock.acquire()
            global food4search
            food4search = category
            print("Starting " + name)
            print("category: " + food4search)
            stream.filter(track=tracklist, languages=['en'], is_async=True)
            time.sleep(60)
            stream.disconnect()
            exitFlag = 2
            time.sleep(5)
            threadLock.release()


def Twitter_Stream_handler_2(tracklist, category, name):
    # Handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    threadLock = threading.Lock()
    global exitFlag
    while True:
        if exitFlag == 2:
            threadLock.acquire()
            global food4search
            food4search = category
            print("Starting " + name)
            print("category: " + food4search)
            stream.filter(track=tracklist, languages=['en'], is_async=True)
            time.sleep(60)
            exitFlag = 3
            stream.disconnect()
            time.sleep(5)
            threadLock.release()

def Twitter_Stream_handler_3(tracklist, category, name):
    # Handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    threadLock = threading.Lock()
    global exitFlag
    while True:
        if exitFlag == 3:
            threadLock.acquire()
            global food4search
            food4search = category
            print("Starting " + name)
            print("category: " + food4search)
            stream.filter(track=tracklist, languages=['en'], is_async=True)
            time.sleep(60)
            exitFlag = 4
            stream.disconnect()
            time.sleep(5)
            threadLock.release()

def Twitter_Stream_handler_4(tracklist, category, name):
    # Handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    threadLock = threading.Lock()
    global exitFlag
    while True:
        if exitFlag == 4:
            threadLock.acquire()
            global food4search
            food4search = category
            print("Starting " + name)
            print("category: " + food4search)
            stream.filter(track=tracklist, languages=['en'], is_async=True)
            time.sleep(60)
            exitFlag = 5
            stream.disconnect()
            time.sleep(5)
            threadLock.release()

def Twitter_Stream_handler_5(tracklist, category, name):
    # Handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    threadLock = threading.Lock()
    global exitFlag
    while True:
        if exitFlag == 5:
            threadLock.acquire()
            global food4search
            food4search = category
            print("Starting " + name)
            print("category: " + food4search)
            stream.filter(track=tracklist, languages=['en'], is_async=True)
            time.sleep(60)
            exitFlag = 6
            stream.disconnect()
            time.sleep(5)
            threadLock.release()

def Twitter_Stream_handler_6(tracklist, category, name):
    # Handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    threadLock = threading.Lock()
    global exitFlag
    while True:
        if exitFlag == 6:
            threadLock.acquire()
            global food4search
            food4search = category
            print("Starting " + name)
            print("category: " + food4search)
            stream.filter(track=tracklist, languages=['en'], is_async=True)
            time.sleep(60)
            exitFlag = 7
            stream.disconnect()
            time.sleep(5)
            threadLock.release()

def Twitter_Stream_handler_7(tracklist, category, name):
    # Handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    threadLock = threading.Lock()
    global exitFlag
    while True:
        if exitFlag == 7:
            threadLock.acquire()
            global food4search
            food4search = category
            print("Starting " + name)
            print("category: " + food4search)
            stream.filter(track=tracklist, languages=['en'], is_async=True)
            time.sleep(60)
            exitFlag = 8
            stream.disconnect()
            time.sleep(5)
            threadLock.release()


def Twitter_Stream_handler_8(tracklist, category, name):
    # Handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    threadLock = threading.Lock()
    global exitFlag
    while True:
        if exitFlag == 8:
            threadLock.acquire()
            global food4search
            food4search = category
            print("Starting " + name)
            print("category: " + food4search)
            stream.filter(track=tracklist, languages=['en'], is_async=True)
            time.sleep(60)
            exitFlag = 9
            stream.disconnect()
            time.sleep(5)
            threadLock.release()

def Twitter_Stream_handler_9(tracklist, category, name):
    # Handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    threadLock = threading.Lock()
    global exitFlag
    while True:
        if exitFlag == 9:
            threadLock.acquire()
            global food4search
            food4search = category
            print("Starting " + name)
            print("category: " + food4search)
            stream.filter(track=tracklist, languages=['en'], is_async=True)
            time.sleep(60)
            exitFlag = 1
            stream.disconnect()
            time.sleep(5)
            threadLock.release()

class myThread (threading.Thread):
   def __init__(self, threadID, name, category, my_track_list):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.category = category
      self.list = my_track_list

   def run(self):
        if self.threadID == 1:
            Twitter_Stream_handler_1(self.list, self.category, self.name)
        elif self.threadID == 2:
            Twitter_Stream_handler_2(self.list, self.category, self.name)
        elif self.threadID == 3:
            Twitter_Stream_handler_3(self.list, self.category, self.name)
        elif self.threadID == 4:
            Twitter_Stream_handler_4(self.list, self.category, self.name)
        elif self.threadID == 5:
            Twitter_Stream_handler_5(self.list, self.category, self.name)
        elif self.threadID == 6:
            Twitter_Stream_handler_6(self.list, self.category, self.name)
        elif self.threadID == 7:
            Twitter_Stream_handler_7(self.list, self.category, self.name)
        elif self.threadID == 8:
            Twitter_Stream_handler_8(self.list, self.category, self.name)
        elif self.threadID == 9:
            Twitter_Stream_handler_9(self.list, self.category, self.name)
        else:
            print("no thread")

def main():
    try:
        os.mkdir("TwitterData_Stream")
    except:
        pass
    with open("checked_targets.json", "r") as file:
        food_list = json.load(file)

    category1 = 'Fast_Foods'
    category2 = 'Poultry'
    category3 = 'Meats'
    category4 = 'Cereal_Grains_and_Pasta'
    category5 = 'Soups'
    category6 = 'Vegetables'
    category7 = 'Fruits'
    category8 = 'Seafood'
    category9 = 'Legumes'

    categorys = [category1, category2, category3, category4, category5, category6, category7, category8, category9]
    for category in categorys:
        try:
            path = "TwitterData_Stream/" + category
            os.mkdir(path)
        except:
            pass
    threads = []
    i = 1
    while i <= len(categorys):
        my_track_list = []
        for target in food_list[categorys[i-1]]:
            my_track_list.append(target)
        thread = myThread(i, 'Thread-' + str(i), categorys[i-1], my_track_list)
        i += 1
        threads.append(thread)

    for run_thread in threads:
        run_thread.start()



    # tracklist1 = []
    # for target in list[category1]:
    #     tracklist1.append(target)
    #
    # tracklist2 = []
    # for target in list[category2]:
    #     tracklist2.append(target)
    #
    # thread1 = myThread(1, 'Thread-1', category1, tracklist1)
    # thread2 = myThread(2, 'Thread-2', category2, tracklist2)
    #
    # thread1.start()
    # thread2.start()


if __name__ == '__main__':
    main()
    # with open('TwitterData_Stream/Beverages.json', 'r') as f:
    #     data = json.load(f)
    # print(len(data))
