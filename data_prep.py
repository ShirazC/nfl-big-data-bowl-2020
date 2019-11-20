#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# In[2]:


pd.set_option('display.max_columns', None)
data = pd.read_csv("./train.csv")
data.head()


# In[3]:


data.columns


# In[4]:


data.dtypes


# In[53]:


homeArray = []
awayArray = []
yardsGained = 0
playDirection = ''
count = 0
for index, row in data.iterrows():
    if row['PlayId'] == 20170907000118:
        if row['Team'] == 'away':
            awayArray.append([row['X'], row['Y'], row['PlayerWeight'], row['Orientation'], row['NflId'], row['NflIdRusher']])
        else:
            homeArray.append([row['X'], row['Y'], row['PlayerWeight'], row['Orientation'], row['NflId'], row['NflIdRusher']])
        yardsGained = row['Yards']
        playDirection = row['PlayDirection']
    else:
        break
print(homeArray)
print(awayArray)
homeX, homeY, homeWeight, homeOrientation, homeId, homeRusherId = zip(*homeArray)
awayX, awayY, awayWeight, awayOrientation, awayId, awayRusherId = zip(*awayArray)


fig = plt.figure(figsize=(60,30))
fig.suptitle('test title', fontsize=20)

field = patches.Rectangle((0, 0), 120, 53.3, linewidth=5.5,
                             edgecolor='black', facecolor='lightgrey', zorder=0)
    
fig, ax = plt.subplots(1, figsize=(60,30))
ax.add_patch(field)

plt.plot([10, 10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80,
          80, 90, 90, 100, 100, 110, 110, 120, 0, 0, 120, 120],
         [0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3,
          53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 53.3, 0, 0, 53.3],
         color='black')
plt.plot([60, 60], [0, 53.3], color='yellow')

plt.xlim(-10, 120); plt.ylim(0, 53.3)
plt.axis('off')
    
        

for i in range(len(homeX)):
    if homeId[i] == homeRusherId[i]:
        if playDirection == 'left':
            plt.plot([homeX[i] - yardsGained, homeX[i] - yardsGained], [0, 58.3],linewidth=5, color='aqua')
        if playDirection == 'right':
            plt.plot([homeX[i] + yardsGained, homeX[i] + yardsGained], [0, 58.3],linewidth=5, color='aqua')
        
        plt.plot(homeX[i],homeY[i], color='red', markersize=homeWeight[i]/5, marker=(3,0,homeOrientation[i]),linestyle='solid',markeredgecolor="red")
        plt.plot(homeX[i],homeY[i], color='red', markersize=homeWeight[i]/5, marker=(2,0,homeOrientation[i]),linestyle='solid',markeredgecolor="red")
    elif awayId[i] == awayRusherId[i]:
        if playDirection == 'left':
            plt.plot([awayX[i] - yardsGained, awayX[i] - yardsGained], [0, 58.3],linewidth=5, color='aqua')
        if playDirection == 'right':
            plt.plot([awayX[i] + yardsGained, awayX[i] + yardsGained], [0, 58.3],linewidth=5, color='aqua')
        
        plt.plot(awayX[i], awayY[i], color="blue", markersize=awayWeight[i]/5, marker=(2,0,awayOrientation[i]), linestyle='solid',markeredgecolor="blue")
        plt.plot(awayX[i], awayY[i], color="blue", markersize=awayWeight[i]/5, marker=(3,0,awayOrientation[i]), linestyle='solid',markeredgecolor="blue")
#     else:
    plt.plot(homeX[i],homeY[i], color='none', markersize=homeWeight[i]/5, marker=(3,0,homeOrientation[i]),linestyle='solid',markeredgecolor="red")
    plt.plot(homeX[i],homeY[i], color='none', markersize=homeWeight[i]/5, marker=(2,0,homeOrientation[i]),linestyle='solid',markeredgecolor="red")
    plt.plot(awayX[i], awayY[i], color="none", markersize=awayWeight[i]/5, marker=(2,0,awayOrientation[i]), linestyle='solid',markeredgecolor="blue")
    plt.plot(awayX[i], awayY[i], color="none", markersize=awayWeight[i]/5, marker=(3,0,awayOrientation[i]), linestyle='solid',markeredgecolor="blue")
plt.show()
    
    
#     if row[index]['PlayId'] == 20170907000118:
#         print(row[index]['PlayId'])
#         print(row[index]['X'])
#         array.append((row[3], row[4]))

# print(array)

# x, y = zip(*array)
# plt.scatter(x, y)
# plt.show()


# In[55]:


modDataFrame = data.drop(
    ["Orientation", "DisplayName", "JerseyNumber", "VisitorScoreBeforePlay", "HomeScoreBeforePlay", "PlayerBirthDate", "VisitorTeamAbbr", "HomeTeamAbbr","Stadium"], axis=1)
print(modDataFrame.columns)
matrix = modDataFrame.values


# In[56]:


print(matrix)


# In[60]:


#Using Pearson Correlation
plt.figure(figsize=(30,25))
cor = modDataFrame.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()


# In[ ]:




