#導入X API
import tweepy
import pandas as pd
import json

# 設定 X API 認證金鑰
consumer_key = 'gaoKR98kPArWOXv14ipFDbWgg'
consumer_secret = 'hxN6R2etCgkCy2Alz6hVDkBeJdyXr8EhuJ9rKPQQb1Hf9SbY4Q'
access_token = '1816761176195485696-5NIsSQRanD0GMsI2DK2zgQcIUOVrVP'
access_token_secret = 'ezvMxtGHlktmYKxeXhO7TDah18OnUWAH5lSG2qYCnugCh'

# X API認證
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#爬取的帳號
user_handle = 'elonmusk'

'''
user_timeline 方法獲取指定用戶的推文
screen_name 指定用戶名
count 設定獲取推文數量
tweet_mode='extended' 獲取完整的推文內容避免被截斷
'''
tweets = api.user_timeline(screen_name=user_handle, count=100, tweet_mode='extended')

# 收集推文數據
tweet_data = {
    '推文內容': [tweet.full_text for tweet in tweets],
    '讚數': [tweet.favorite_count for tweet in tweets],
    '留言數': [tweet.reply_count if hasattr(tweet, 'reply_count') else None for tweet in tweets],
    '分享數': [tweet.retweet_count for tweet in tweets],
    '時間戳': [tweet.created_at.isoformat() for tweet in tweets]
}

# 將數據轉換為DataFrame
df = pd.DataFrame(tweet_data)

# 指定為JSON格式名稱
json_file = 'tweets_data.json'

# 將DataFrame轉換為JSON格式儲存
df.to_json(json_file, orient='records', lines=True, force_ascii=False)

print(f"數據已儲存到 {json_file}")
