import tweepy
import requests

##########################
#Do bitcoin scraping work#
##########################

bitcoin_api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
response = requests.get(bitcoin_api_url)
response_json = response.json()


#First round of raw data cleaning
timeStamp = response_json.get("time")
coindeskDisclaimer = response_json.get("disclaimer")
priceData = response_json.get("bpi")


#Final price related data cleaning
usdData = priceData.get("USD")
gbpData = priceData.get("GBP")
eurData = priceData.get("EUR")

usdBtcPrice = usdData.get("rate")
gbpBtcPrice = gbpData.get("rate")
eurBtcPrice = eurData.get("rate")


#Final time related data cleaning
time1 = timeStamp.get("updated")
time2 = timeStamp.get("updatedISO")
time3 = timeStamp.get("updateduk")


#Organize the tweet with raw data
tweetTime = " Updated: [" + time1 + "], [" + time2 + "], [" + time3 + "] "
tweetData = "1 BTC = $" + usdBtcPrice +" USD," + " 1 BTC = £" + gbpBtcPrice +" GBP," + " 1 BTC = €" + eurBtcPrice +" EUR"
tweetResult = tweetTime + tweetData



#########################
#Do tweepy/ twitter work# 
#########################


# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status(tweetResult)