
# News Mood

## Analysis

<ul>
<li>It is noticeable that significant part of all tweets has a neutral sentiment score, i.e. compound score=0 .</li>
<li>During the period of data analysis, neither completely positive tweets (compound score=1), nor completely negative tweets (compound score=-1) were observed.</li>
<li>Based on analysis of average compound scores (file "Sentiment.txt" contains screenshots of bar charts), we may notice that FOX and New York times have more positive tweets, than  BBC, CBS and CNN.</li>
</ul>


```python
import tweepy
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Twitter API Keys
from config import (consumer_key, 
                    consumer_secret, 
                    access_token, 
                    access_token_secret)

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```


```python
# create a tuple of twitters of the following news organizations: BBC, CBS, CNN, Fox, and New York times.
target_news=("@BBCWorld", "@CBCNews", "@CNN", "@FoxNews", "@nytimes")
```


```python
#create an empty DataFrame to store  tweets data
tweets_data=pd.DataFrame(columns=["News Source","Tweet Text","Tweet Date","Compound Score","Pos.score","Neg.score",
                                   "Neu.score","Tweets ago"])
index=0

# Loop through each news organization:
for target in target_news: 
    counter = 1   
    public_tweets = api.user_timeline(target, count=100, result_type="recent")    
    for tweet in public_tweets:           
        # Run Vader Analysis on each tweet
        results = analyzer.polarity_scores(tweet["text"])        
        #Add sentiments and tweet data einto a DataFrame
        tweets_data.loc[index,"News Source"]=tweet["user"]["name"]
        tweets_data.loc[index,"Tweet Text"]=tweet["text"]
        tweets_data.loc[index,"Tweet Date"]=tweet["created_at"]
        tweets_data.loc[index,"Compound Score"]=results["compound"]
        tweets_data.loc[index,"Pos.score"]=results["pos"]
        tweets_data.loc[index,"Neg.score"]=results["neg"]
        tweets_data.loc[index,"Neu.score"]=results["neu"]
        tweets_data.loc[index,"Tweets ago"]=counter
        counter += 1
        index+=1
       
```


```python
tweets_data.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>News Source</th>
      <th>Tweet Text</th>
      <th>Tweet Date</th>
      <th>Compound Score</th>
      <th>Pos.score</th>
      <th>Neg.score</th>
      <th>Neu.score</th>
      <th>Tweets ago</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BBC News (World)</td>
      <td>Trump calls for deportations without judicial ...</td>
      <td>Sun Jun 24 19:17:37 +0000 2018</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BBC News (World)</td>
      <td>Europe migrants: Italy warns Schengen is 'at r...</td>
      <td>Sun Jun 24 18:55:57 +0000 2018</td>
      <td>-0.3612</td>
      <td>0</td>
      <td>0.333</td>
      <td>0.667</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BBC News (World)</td>
      <td>Mali Fula villagers were killed 'in cold blood...</td>
      <td>Sun Jun 24 17:44:07 +0000 2018</td>
      <td>-0.6705</td>
      <td>0</td>
      <td>0.36</td>
      <td>0.64</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BBC News (World)</td>
      <td>Event in Dublin for 60 years of UN peacekeepin...</td>
      <td>Sun Jun 24 17:02:54 +0000 2018</td>
      <td>0.4588</td>
      <td>0.231</td>
      <td>0</td>
      <td>0.769</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BBC News (World)</td>
      <td>A juvenile male has been arrested over Tallagh...</td>
      <td>Sun Jun 24 16:48:00 +0000 2018</td>
      <td>-0.7906</td>
      <td>0</td>
      <td>0.467</td>
      <td>0.533</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>BBC News (World)</td>
      <td>RT @bbctennis: He’s done it!\n\nCilic defeats ...</td>
      <td>Sun Jun 24 16:43:57 +0000 2018</td>
      <td>-0.3802</td>
      <td>0</td>
      <td>0.126</td>
      <td>0.874</td>
      <td>6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>BBC News (World)</td>
      <td>Erdogan leads after early results in Turkey ht...</td>
      <td>Sun Jun 24 15:54:59 +0000 2018</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>BBC News (World)</td>
      <td>Lava from Hawaii's Kilauea volcano creeps clos...</td>
      <td>Sun Jun 24 15:22:40 +0000 2018</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>BBC News (World)</td>
      <td>RT @BBCSport: FT #ENG 6-1 #PAN \n\nKane ⚽⚽⚽\nS...</td>
      <td>Sun Jun 24 13:53:17 +0000 2018</td>
      <td>0.4574</td>
      <td>0.166</td>
      <td>0</td>
      <td>0.834</td>
      <td>9</td>
    </tr>
    <tr>
      <th>9</th>
      <td>BBC News (World)</td>
      <td>RT @BBCSport: GOAL! #ENG 6-1 #PAN \n\nComeback...</td>
      <td>Sun Jun 24 13:38:10 +0000 2018</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
tweets_data.count()
```




    News Source       500
    Tweet Text        500
    Tweet Date        500
    Compound Score    500
    Pos.score         500
    Neg.score         500
    Neu.score         500
    Tweets ago        500
    dtype: int64




```python
print("Tweets data is stored in 'tweets_data.csv'")
tweets_data.to_csv("tweets_data.csv")
```

    Tweets data is stored in 'tweets_data.csv'



```python
bbc=tweets_data.loc[tweets_data["News Source"]=="BBC News (World)"]
cbc=tweets_data.loc[tweets_data["News Source"]=="CBC News"]
cnn=tweets_data.loc[tweets_data["News Source"]=="CNN"]
fox=tweets_data.loc[tweets_data["News Source"]=="Fox News"]
ny_times=tweets_data.loc[tweets_data["News Source"]=="The New York Times"]
```


```python
#create scatter plot for each news source
plt.figure(figsize=(10, 7))
plt.scatter(bbc["Tweets ago"], bbc["Compound Score"], color="lightblue", edgecolor="black",
             label="BBC News (World)", alpha=0.5, s=70, linewidths=1)    
plt.scatter(cbc["Tweets ago"], cbc["Compound Score"], color="green", edgecolor="black",
             label="CBC News", alpha=0.5,s=70, linewidths=1) 
plt.scatter(cnn["Tweets ago"], cnn["Compound Score"], color="red", edgecolor="black",
             label="CNN", alpha=0.5, s=70, linewidths=1) 
plt.scatter(fox["Tweets ago"], fox["Compound Score"], color="blue", edgecolor="black",
             label="Fox News", alpha=0.5, s=70, linewidths=1)
plt.scatter(ny_times["Tweets ago"], ny_times["Compound Score"], color="yellow", edgecolor="black",
             label="The New York Times", alpha=0.5, s=70, linewidths=1)

plt.grid()
#manually specify the bounding box into which the legend should be placed, using the bbox_to_anchor argument
plt.legend(bbox_to_anchor=(1.25,1), borderaxespad=0, title="Media Sources",frameon=False)

plt.yticks(np.arange(-1, 1.1, step=0.5))

#display data in the reverse order (100->0)
plt.xlim([bbc["Tweets ago"].max()+5,bbc["Tweets ago"].min()-5])
plt.title(f"Sentiment Analysis of Media Tweets {time.strftime('%x')}")
plt.savefig("compound_scatter.png", bbox_inches='tight', dpi=100)
plt.xlabel("Tweets ago")
plt.ylabel("Tweet Polarity")

plt.show()
```


![png](output_10_0.png)



```python
#aggregate the compound sentiments for each News Source
bbc_avg=bbc["Compound Score"].mean()
cbc_avg=cbc["Compound Score"].mean()
cnn_avg=cnn["Compound Score"].mean()
fox_avg=fox["Compound Score"].mean()
ny_times_avg=ny_times["Compound Score"].mean()
news_list=[bbc_avg, cbc_avg, cnn_avg, fox_avg, ny_times_avg]

#built a bar chart for average compound sentiments
news_names=["BBC", "CBC", "CNN", "Fox", "NYT"]
colors=["lightblue", "green","red", "blue", "yellow"]
x_axis=np.arange(len(news_list))
plt.figure(figsize=(10, 7))
plt.bar(x_axis, news_list, tick_label=news_names, color=colors, edgecolor="grey",width=1.0)
plt.ylabel("Tweet Polarity")
plt.ylim(min(news_list)-0.005,max(news_list)+0.005,)
plt.title(f"Overal Media Sentiment based on Twitter {time.strftime('%x')}")
plt.savefig("compound_bar.png")
plt.show()
```


![png](output_11_0.png)

