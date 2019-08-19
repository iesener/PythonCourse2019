import tweepy
import sys
import imp
import time

twitter = imp.load_source('twit', '/Users/ipekecesener/PhD/Summer 2019/Python Class/start_twitter.py')
api = twitter.client

wustl = api.get_user('WUSTL')

itsfollowers = []
## All the followers' IDs
for item in tweepy.Cursor(api.followers_ids, 'WUSTL').items():
	itsfollowers.append(item)

## Extract all information about WUSTL followers using their IDs
user = []
for i in range(0,len(itsfollowers)):
	try:
		user.append(api.get_user(itsfollowers[i]))
	except tweepy.error.RateLimitError:
		time.sleep(15 * 60)
		print("hey")
		user.append(api.get_user(itsfollowers[i]))
	except tweepy.error.TweepError:
		pass


## Find the follower with greatest number of tweets
followers_tweet_no = []
for i in range(0,len(user)):
	followers_tweet_no.append(user[i].statuses_count)

## Among the followers of @WUSTL, how many tweets does the accout with the greatest number of tweets have?
print(max(followers_tweet_no))
## 582447

## Among the followers of @WUSTL, who has the greatest number of total tweets?
user[followers_tweet_no.index(max(followers_tweet_no))].name
## "Michael F Ozaki MD"

## Find the follower with greatest number of followers
followers_follower_no = []
for i in range(0,len(user)):
	followers_follower_no.append(user[i].followers_count)

## Among the followers of @WUSTL, how many followers does the accout with the greatest number of followers have?
print(max(followers_follower_no))
## 7858471

## Among the followers of @WUSTL, who has the greatest number of followers?
user[followers_follower_no.index(max(followers_follower_no))].name
## "Hootsuite"



itsfriends = []
## All account IDs who WUSTL follows
for item in tweepy.Cursor(api.friends_ids, 'WUSTL').items():
	itsfriends.append(item)

## Extract all information about accounts WUSTL follows using their IDs
friends = []
for i in range(0,len(itsfriends)):
	try:
		friends.append(api.get_user(itsfriends[i]))
	except tweepy.error.RateLimitError:
		time.sleep(15 * 60)
		print("hey")
		friends.append(api.get_user(itsfriends[i]))
	except tweepy.error.TweepError:
		pass


## Find the friend with greatest number of followers
friends_follower_no = []
for i in range(0,len(friends)):
	friends_follower_no.append(friends[i].followers_count)

## Among those who @WUSTL follows, how many followers does the accout with the greatest number of followers have?
print(max(friends_follower_no))
## 56518736

## Among those who @WUSTL follows, who has the greatest number of followers?
friends[friends_follower_no.index(max(friends_follower_no))].name
## "Twitter"


## Find the friend with greatest number of tweets by group

layman = []
expert = []
celebrity = []

for i in range(0,len(friends)):
	if friends_follower_no[i] < 100:
		layman.append(i)
	if 100 <= friends_follower_no[i] <= 1000:
		expert.append(i)
	if 1000 < friends_follower_no[i]:
		celebrity.append(i)

## The sequence number for the friends who have the greatest number of tweets by group:
layman_tweetcount = {}
expert_tweetcount = {}
celebrity_tweetcount = {}

for j in range(0,len(layman)):
	layman_tweetcount.update({friends[layman[j]].name: friends[layman[j]].statuses_count})

for j in range(0,len(expert)):
	expert_tweetcount.update({friends[expert[j]].name: friends[expert[j]].statuses_count})

for j in range(0,len(celebrity)):
	celebrity_tweetcount.update({friends[celebrity[j]].name: friends[celebrity[j]].statuses_count})

for i in layman_tweetcount, expert_tweetcount,celebrity_tweetcount:
	highest = max(i.values())
	print([k for k, v in i.items() if v == highest])
## layman: 'WUSTL Weather'
## expert: 'Just ⚖️ Terry'
## celebrity: 'The New York Times'




##############		WUSTLPoliSci	 ###########

polisci = api.get_user('WUSTLPoliSci')

polisci_followers = []
## All the polisci followers' IDs
for item in tweepy.Cursor(api.followers_ids, 'WUSTLPoliSci').items():
	polisci_followers.append(item)

## Extract all information about WUSTLPoliSci followers using their IDs
polisci_fol = []
for i in range(0,len(polisci_followers)):
	try:
		polisci_fol.append(api.get_user(polisci_followers[i]))
	except tweepy.error.RateLimitError:
		time.sleep(15 * 60)
		print("hey")
		polisci_fol.append(api.get_user(polisci_followers[i]))
	except tweepy.error.TweepError:
		pass




## Extract all information about WustlPoliSci followers' followers

polisci_fol_fol_id = []
polisci_fol_fol = []

for i in range(0, len(polisci_fol)):
	try:
		for item in tweepy.Cursor(api.followers_ids, polisci_fol[i].screen_name).items():
			polisci_fol_fol_id.append(item)	
	except tweepy.error.TweepError:
		pass

for i in range(0, len(polisci_fol_fol_id)):
	try:
		polisci_fol_fol.append(api.get_user(polisci_fol_fol_id[i]))
	except tweepy.error.RateLimitError:
		time.sleep(15 * 60)
		print("hey")
		polisci_fol_fol.append(api.get_user(polisci_fol_fol_id[i]))
	except tweepy.error.TweepError:
		pass




