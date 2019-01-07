
import pandas as pd
import numpy as np
import nltk
words = set(nltk.corpus.words.words())
from textblob import TextBlob
import plotly
import plotly.plotly as py
import plotly.graph_objs as go


data1 = pd.read_csv('RC_2016-06.csv', index_col = 0, parse_dates=True)
data2 = pd.read_csv('RC_2016-07.csv', index_col = 0, parse_dates=True)
data3 = pd.read_csv('UnitedKingdomvsEurope.csv', index_col = 0, parse_dates=True)


#for data1(prebrexit)
booleans = []
for i in data1.controversiality:
    if len(data1.controversiality) > 5:
        booleans.append(True)
    else:
        booleans.append(False)
is_longs = pd.Series(booleans)
#print(is_longs.head())

#for data2(postbrexit)
bool1 = []
for i in data2.controversiality:
    if len(data2.controversiality) > 5:
        bool1.append(True)
    else:
        bool1.append(False)
is_log = pd.Series(bool1)
#print(is_log.head())

#for data3(EUvsUK)
bool2 = []
for i in data3.body:
    if len(data3.body) > 5:
        bool2.append(True)
    else:
        bool2.append(False)
is_log1 = pd.Series(bool2)
#print(is_log1.head())


#cleaning data1
data1.controversiality = data1.controversiality.str.lower()
data1.controversiality = data1.controversiality.str.replace('[^\w\s]','')
data1.controversiality = data1.controversiality.str.replace('\d+', '')
#print("BEFORE: ",data1.controversiality.head())
data1.controversiality = data1.controversiality.str.replace('\n', ' ')
#print("AFTER: ",data1.controversiality.head())

#cleaning data2
data2.controversiality = data2.controversiality.str.lower()
data2.controversiality = data2.controversiality.str.replace('[^\w\s]','')
data2.controversiality = data2.controversiality.str.replace('\d+', '')
#print("BEFORE: ",data2.controversiality.head())
data1.controversiality = data1.controversiality.str.replace('\n', ' ')
#print("AFTER: ",data2.controversiality.head())

#cleaning data3
data3.body = data3.body.str.lower()
data3.body = data3.body.str.replace('[^\w\s]','')
data3.body = data3.body.str.replace('\d+', '')
#print("BEFORE: ",data3.body.head())
data3.body = data3.body.str.replace('\n', ' ')
#print("AFTER: ",data3.body.head())


#removing non-english words for data1
for i in data1.controversiality.head():
    entry.append(" ".join(w for w in nltk.wordpunct_tokenize(i) \
		if w.lower() in words or not w.isalpha()))

#removing non-english words for data2
entry2 = []
for i in data2.controversiality.head():
    entry2.append(" ".join(w for w in nltk.wordpunct_tokenize(i)\
		if w.lower() in words or not w.isalpha()))
    
#removing non-english words for data3
entry3 = []
for i in data3.body.head():
    entry3.append(" ".join(w for w in nltk.wordpunct_tokenize(i) \
		if w.lower() in words or not w.isalpha()))

#finding sentiment polarity
pol, pos, neg, nut = ([] for i in range(4))
for i in data1.controversiality:
    val = TextBlob(str(i)).sentiment.polarity
    if val > 0:
        pos.append(val)
    elif val < 0:
        neg.append(val)
    else:
        nut.append(val)
        
#print("###############Before \n {0}:pos /  {1}:neg  / {2}:nut ".format(len(pos), len(neg), len(nut)))

pos1, neg1, nut1 = ([] for i in range(3))
for i in data2.controversiality:
    val = TextBlob(str(i)).sentiment.polarity
    if val > 0:
        pos1.append(val)
    elif val < 0:
        neg1.append(val)
    else:
        nut1.append(val)
        
#print("###############After \n {0}:pos /  {1}:neg  / {2}:nut ".format(len(pos1), len(neg1), len(nut1)))

pos2, neg2, nut2 = ([] for i in range(3))
for i in data3.body:
    val = TextBlob(str(i)).sentiment.polarity
    if val > 0:
        pos2.append(val)
    elif val < 0:
        neg2.append(val)
    else:
        nut2.append(val)
        
#print("###############topreddit \n {0}:pos /  {1}:neg  / {2}:nut ".format(len(pos2), len(neg2), len(nut2)))

#Vizualization of polarity in comments

labels = ['Positive Comment','Negative Comment','Neutral Comment']
value1 = [25430,10922,7807]
value2 = [16959,6985,4575]
value3 = [7145,2942,1251 ]

#tracing 'before' data
trace = go.Pie(labels=labels, values=value1)
py.iplot([trace], filename='basic_pie_chart')

#tracing 'after' data
trace1 = go.Pie(labels=labels, values=value2)
py.iplot([trace1], filename='basic_pie_chart')

#tracing 'EU vs UK' data
trace2 = go.Pie(labels=labels, values=value3)
py.iplot([trace2], filename='basic_pie_chart')


#mean and frequency distribution in all three dataset
dig1 = go.Bar(
    x=['Positive Comment','Negative Comment','Neutral Comment'],
    y=[0.57,0.24,0.17], # mean of each tags(positive, negative, neutral)
    name='Pre Brexit'
)
dig2 = go.Bar(
    x=['Positive Comment','Negative Comment','Neutral Comment'],
    y=[0.59,0.24,0.16],#mean
    name='Post Brexit'
)

dig3 = go.Bar(
    x=['Positive Comment','Negative Comment','Neutral Comment'],
    y=[0.63,0.25,0.11],#mean
    name='EU vs UK'
)

data = [dig1, dig2, dig3]
layout = go.Layout(
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='grouped-bar')

