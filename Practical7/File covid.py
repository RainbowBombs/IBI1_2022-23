import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("D:/download")
covid_data = pd.read_csv("full_data.csv")
"""print(covid_data.head(5))
my_columns = [True, True, False, True, False,True]"""
print(covid_data.iloc[0:1000:100,1])

#I involve the line of "world" in the following lines.

def search_location(name):
    haze=[False]*len(covid_data)
    for i in range(0,len(covid_data)):
        if name==covid_data.iloc[i,1]:
          haze[i]=True 
    return haze
print(covid_data.loc[search_location("Afghanistan"),"total_cases"]) # also can change "search_location()" into covid_data.loc[："date"]=="Alf"
#↑ It can be replaced by covid_data.loc[covid_data.loc[:,"location"]=="Afghanistan","new_cases"]
#use "print(covid_data.loc[0:81,"total_cases"])" ,after checking I found it is the same

def search_date(name):
    haze=[False]*len(covid_data)
    for i in range(0,len(covid_data)):
        if name==covid_data.iloc[i,0]:
          haze[i]=True 
    return haze
print(np.mean(covid_data.loc[search_date("2020-03-31"),"new_cases"],axis=0),np.mean(covid_data.loc[search_date("2020-03-31"),"new_deaths"],axis=0))
#↑ It can be replaced by covid_data.loc[covid_data.loc[:,"date"]=="2020-03-31","new_cases"]

cases=list(covid_data.loc[search_date("2020-03-31"),"new_cases"])
death=list(covid_data.loc[search_date("2020-03-31"),"new_deaths"])
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,5))
plt.subplots_adjust(wspace=0.5,hspace=2)
ax1.boxplot(cases)
ax1.set_title("box plots of new caseson 31 March")
ax1.set_ylabel("mean of patients")
ax1.set_xlabel("world_new_cases")
ax2.boxplot(death)
ax2.set_title("box plots of new deaths on 31 March")
ax2.set_ylabel("mean of patients")
ax2.set_xlabel("world_new_deaths")
plt.show()
#-----------------------------------------------------------#

'''world_dates=[]
for i in range(len(covid_data)):
   if not covid_data.loc[i,"date"] in world_dates:
      world_dates.append(covid_data.loc[i,"date"])
world_dates.sort()
world_new_cases=[]
world_new_deaths=[]
for i in world_dates: 
    world_new_cases.append(np.sum(covid_data.loc[search_date(i),"new_cases"],axis=0))
for i in world_dates:
    world_new_deaths.append(np.sum(covid_data.loc[search_date(i),"new_deaths"],axis=0))
plt.figure(figsize=(20,6))
plt.plot(world_dates, world_new_cases, 'o',color="b")
plt.plot(world_dates, world_new_deaths, 'o',color="r")
plt.xticks(rotation=-75)
plt.title("new cases and new deaths of COVID worldwide over time")
plt.xlabel("date")
plt.ylabel("number of patients")
plt.legend(["world_new_cases","world_new_deaths"],loc=2)
plt.show()'''
#↑ is a complex way to get the answer

#↓ is less complex solution
#I didn't know there is a line in "location" called world when coding so I used the data in all the country (inculding the "world" line) sum it up a get the world data.
#if the world line could be used, it could be much more easier.
world_dates=[]
for i in range(len(covid_data)):
   if not covid_data.loc[i,"date"] in world_dates:
      world_dates.append(covid_data.loc[i,"date"])
world_dates.sort()
value=0
dct_new_cases={i:value for i in world_dates}
for i in range(len(covid_data)):
    dct_new_cases[covid_data.loc[i,"date"]]+=covid_data.loc[i,"new_cases"]
    world_new_cases=dct_new_cases.values()  
dct_new_deaths={i:value for i in world_dates}
for i in range(len(covid_data)):
    dct_new_deaths[covid_data.loc[i,"date"]]+=covid_data.loc[i,"new_deaths"]
    world_new_deaths=dct_new_deaths.values()
plt.figure(figsize=(20,6))
plt.plot(world_dates, world_new_cases, 'bo')
plt.plot(world_dates, world_new_deaths, 'ro')
plt.subplots_adjust(bottom=0.2)
plt.xticks(world_dates[::3],rotation=-75)
plt.title("new cases and new deaths of COVID worldwide over time")
plt.xlabel("date")
plt.ylabel("number of patients")
plt.legend(["world_new_cases","world_new_deaths"],loc=2)
plt.show()
#--------------------------------------------------------#
#my qestion: What proportion of cases have died in the Germany?
Germany_cases=list(covid_data.loc[covid_data.loc[:,"location"] == "Germany","total_cases"])
Germany_deaths=list(covid_data.loc[covid_data.loc[:,"location"]=="Germany","total_deaths"])
array_total_cases= np.array(Germany_cases)
array_deaths = np.array(Germany_deaths)
deaths_proportion = array_deaths/array_total_cases
plt.figure(figsize=(22,6))
plt.plot(world_dates, deaths_proportion, 'r+')
plt.xticks(world_dates[28::3],rotation=-75)
plt.subplots_adjust(bottom=0.2)
plt.title("proportion of cases have died in the Germany",fontsize=18)
plt.suptitle("there is no case in Germany before 2020-1-27,so there won't be a proportion of death from 2019-12-31 to 2020-1-27",fontsize=10)
plt.xlabel("date")
plt.ylabel("number of patients")

plt.show()