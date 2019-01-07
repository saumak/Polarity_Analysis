import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


data1 = pd.read_csv('RC_2016-06.csv', index_col = 0, parse_dates=True)
data2 = pd.read_csv('RC_2016-07.csv', index_col = 0, parse_dates=True)
data = data1.append(data2)
data['datetime'] = pd.to_datetime(data['created_utc'], unit='s')
data['datetime'] = data['datetime'].astype(str)

#data['dates'] = data['datetime'][:10].replace('-','')
dates_col = []
for i in range(data.shape[0]):
    dates_col.append(data.iloc[i]['datetime'][:10].replace('-',''))
se = pd.Series(dates_col)
data['dates'] = se.values
data['dates'] = data['dates'].astype(int)

#####Weekly Details
beforedatelist = [20160602, 20160609, 20160616, 20160623]
afterdatelist = [20160623, 20160630, 20160707, 20160714]

countbefore = []
for j in range(1, len(beforedatelist)):
    df = data.loc[(data['dates'] < beforedatelist[j]) & (data['dates'] >= beforedatelist[j-1])]
    countbefore.append(df.shape[0])
    
countafter = []
for j in range(1, len(afterdatelist)):
    df = data.loc[(data['dates'] < afterdatelist[j]) & (data['dates'] >= afterdatelist[j-1])]
    countafter.append(df.shape[0])
    
###Graph for before brexit
objects = ('2nd-9thJune', '10-16thJune', '18-23rdJune')
y_pos = np.arange(len(objects))
plt.bar(y_pos, countbefore, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of Reddit Comments')
plt.title('Week Usage before Brexit')
plt.show()

###Graph for after brexit
objects = ('23rd-30thJune', '01-7thJuly', '08-14July')
y_pos = np.arange(len(objects))
plt.bar(y_pos, countafter, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of Reddit Comments')
plt.title('Week Usage after Brexit')    
plt.show()

#####Daily Details for 2 weeks
df1 = data.loc[(data['dates'] <= 20160630) & (data['dates'] >= 20160616)]
a = df1['dates'].value_counts()
a = a.to_frame()
a.reset_index(level=0, inplace=True)
a.columns = ['date', 'counts']
a = a.sort_values(by = ['date'])

######Daily trend graph
objects = a['date']
y_pos = np.arange(len(objects))
plt.bar(y_pos, a['counts'], align='center', alpha=0.5, )
plt.xticks(y_pos, objects)
plt.xticks(rotation = 'vertical')
plt.ylabel('Number of Reddit Comments')
plt.title('Daily usage')    
plt.show()

#####data only from 20160602 to 20160714
df2 = data.loc[(data['dates'] <= 20160714) & (data['dates'] >= 20160602)]
subreddit = df2['subreddit'].value_counts()
subreddit = subreddit.to_frame()
subreddit.reset_index(level=0, inplace=True)
subreddit.columns = ['subreddit', 'counts']
top10 = subreddit.head(10)
top10.to_csv('top10subreddit.csv')

######Two of the major subreddits are UnitedKingdom and Europe in these periods
top2_dataL = df2.loc[(df2['subreddit'] == 'unitedkingdom')]
top2_dataE = df2.loc[(df2['subreddit'] == 'europe')]
top2_data = top2_dataL.append(top2_dataE)
top2_data.to_csv('UnitedKingdomvsEurope.csv')


######UNitedKingdom related subreddits and Europe related subreddits in top50
top50 = subreddit.head(50)
