import tweepy
import sys
import imp
import time

twitter = imp.load_source('twit', '/Users/ipekecesener/PhD/Summer 2019/Python Class/start_twitter.py')
api = twitter.client

wustl = api.get_user('WUSTL')

### QUESTIONS 1 & 2 ###

itsfollowers = []
## All the followers' IDs
for item in tweepy.Cursor(api.followers_ids, 'WUSTL').items():
	itsfollowers.append(item)

## Extract all information about WUSTL followers using their IDs
## This is the step that took about 10 hours
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

## Among the followers of @WUSTL, how many tweets does the account with the greatest number of tweets have?
print(max(followers_tweet_no))
## 582447

## Among the followers of @WUSTL, who has the greatest number of total tweets?
user[followers_tweet_no.index(max(followers_tweet_no))].name
## "Michael F Ozaki MD"

## Find the follower with greatest number of followers
followers_follower_no = []
for i in range(0,len(user)):
	followers_follower_no.append(user[i].followers_count)

## Among the followers of @WUSTL, how many followers does the account with the greatest number of followers have?
print(max(followers_follower_no))
## 7858471

## Among the followers of @WUSTL, who has the greatest number of followers?
user[followers_follower_no.index(max(followers_follower_no))].name
## "Hootsuite"



### QUESTIONS 3 & 4 ###


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

## This function will help me find the user with the greatest number of tweets by group

def maxtweet(usertype, accountinfo):
	tweetcount = {}
	for j in range(0,len(usertype)):
		tweetcount.update([(accountinfo[usertype[j]].name, accountinfo[usertype[j]].statuses_count)])
	highest = max(tweetcount.values())
	return [k for k, v in tweetcount.items() if v == highest]

maxtweet(layman,friends)
## ['WUSTL Weather']
maxtweet(expert,friends)
## ['Just ⚖️ Terry']
maxtweet(celebrity,friends)
## ['The New York Times']



##############		WUSTLPoliSci	 ###########

### QUESTION 1 ###

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
		polisci_fol.append(api.get_user(polisci_followers[i]))
	except tweepy.error.TweepError:
		pass

## Among the followers of @WUSTLPoliSci, who has the greatest number of tweets? (for groups layman and expert)

layman = []
expert = []

for i in range(0,len(polisci_fol)):
	if polisci_fol[i].followers_count < 100:
		layman.append(i)
	if 100 <= polisci_fol[i].followers_count <= 1000:
		expert.append(i)

maxtweet(layman,polisci_fol)
## ['Beirut Mugharid']
maxtweet(expert,polisci_fol)
## ['dailysquirrel™']



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
		polisci_fol_fol.append(api.get_user(polisci_fol_fol_id[i]))
	except tweepy.error.TweepError:
		pass

## Among the followers of the @WUSTLPoliSci followers, who has the greatest number of tweets?

layman = []
expert = []

for i in range(0,len(polisci_fol_fol)):
	if polisci_fol_fol[i].followers_count < 100:
		layman.append(i)
	if 100 <= polisci_fol_fol[i].followers_count <= 1000:
		expert.append(i)

maxtweet(layman,polisci_fol_fol)
## ['Capsizing']
maxtweet(expert,polisci_fol_fol)
## ['Ze Djebar HAMMOUCHE 🙏']

### QUESTION 2 ###

polisci_friends = []

## All the account IDs who WUSTLPoliSci follows:
for item in tweepy.Cursor(api.friends_ids, 'WUSTLPoliSci').items():
	polisci_friends.append(item)

## Extract all information about accounts WUSTLPoliSci follows
polisci_fri = []
for i in range(0,len(polisci_friends)):
	try:
		polisci_fri.append(api.get_user(polisci_friends[i]))
	except tweepy.error.RateLimitError:
		time.sleep(15 * 60)
		polisci_fri.append(api.get_user(polisci_friends[i]))
	except tweepy.error.TweepError:
		pass

## Among those who @WUSTLPoliSci follows, who has the greatest number of tweets? (for groups layman and expert)

layman = []
expert = []

for i in range(0,len(polisci_fri)):
	if polisci_fri[i].followers_count < 100:
		layman.append(i)
	if 100 <= polisci_fri[i].followers_count <= 1000:
		expert.append(i)

maxtweet(layman,polisci_fri)
## ['usman falalu']
maxtweet(expert,polisci_fri)
## ['Tim...the enchanter']


## Extract all information about WustlPoliSci friends' friends

polisci_fri_fri_id = []
polisci_fri_fri = []

for i in range(0, len(polisci_fri)):
	try:
		for item in tweepy.Cursor(api.friends_ids, polisci_fri[i].screen_name).items():
			polisci_fri_fri_id.append(item)	
	except tweepy.error.TweepError:
		pass

for i in range(0, len(polisci_fri_fri_id)):
	try:
		polisci_fri_fri.append(api.get_user(polisci_fri_fri_id[i]))
	except tweepy.error.RateLimitError:
		time.sleep(15 * 60) 
		polisci_fri_fri.append(api.get_user(polisci_fri_fri_id[i]))
	except tweepy.error.TweepError:
		pass

## Among the friends of those who @WUSTLPoliSci follows, who has the greatest number of tweets?

layman = []
expert = []

for i in range(0,len(polisci_fri_fri)):
	if polisci_fri_fri[i].followers_count < 100:
		layman.append(i)
	if 100 <= polisci_fri_fri[i].followers_count <= 1000:
		expert.append(i)

maxtweet(layman,polisci_fri_fri)
## ['Mark Peter Detwiler']
maxtweet(expert,polisci_fri_fri)
## ['Julián 💚']

