# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data=pd.read_csv(path)
data.rename(columns={'Total': 'Total_Medals'}, inplace=True)
data.head(10)
#Code starts here



# --------------
#Code starts here
import pandas as pd 
import numpy as np 


data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')

data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event']) 

better_event=data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here

top_countries=data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index,inplace=True)

def top_ten(df,colname):
    country_list=[]
    x=df.nlargest(10, colname)
    country_list=x['Country_Name']
    return country_list

top_10_summer=list(top_ten(top_countries,'Total_Summer'))
top_10_winter=list(top_ten(top_countries,'Total_Winter'))
top_10=list(top_ten(top_countries,'Total_Medals'))
s_top_10_summer=set(top_10_summer)
s_top_10_winter=set(top_10_winter)
s_top_10=set(top_10)

s_tmp=s_top_10_summer.intersection(s_top_10_winter)
common=list(s_tmp.intersection(s_top_10))
print(common)




# --------------
#Code starts here

print(top_10_summer)
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]


summer_countries=list(summer_df['Country_Name'])
y_pos = np.arange(len(summer_countries))
summer_golds=list(summer_df['Total_Summer'])
print(summer_golds)

plt.bar(y_pos, summer_golds, align='center', alpha=1)
plt.xticks(y_pos, summer_countries)
plt.ylabel('Medals')
plt.title('Summer Gold Countries')
plt.show()

winter_countries=list(winter_df['Country_Name'])
y_pos = np.arange(len(winter_countries))
winter_golds=list(summer_df['Total_Winter'])
print(winter_golds)

plt.bar(y_pos, winter_golds, align='center', alpha=1)
plt.xticks(y_pos, winter_countries)
plt.ylabel('Medals')
plt.title('Winter Gold Countries')

plt.show()

all_countries=list(top_df['Country_Name'])
y_pos = np.arange(len(all_countries))
total_golds=list(top_df['Total_Medals'])
print(total_golds)

plt.bar(y_pos, total_golds, align='center', alpha=1)
plt.xticks(y_pos, all_countries)
plt.ylabel('Total_Medals')
plt.title('Total Medal Countries')

plt.show()


# --------------
#Code starts here


summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold_idx=summer_df['Golden_Ratio'].idxmax()
summer_country_gold=summer_df.loc[summer_country_gold_idx,'Country_Name']

print("------")
print(summer_country_gold)
print(summer_country_gold_idx)
print(summer_max_ratio)

print("++++++")

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold_idx=winter_df['Golden_Ratio'].idxmax()
winter_country_gold=winter_df.loc[winter_country_gold_idx,'Country_Name']

print("------")
print(winter_country_gold)
print(winter_country_gold_idx)
print(winter_max_ratio)

print("++++++")

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold_idx=top_df['Golden_Ratio'].idxmax()
top_country_gold=top_df.loc[top_country_gold_idx,'Country_Name']

print("------")
print(top_country_gold)
print(top_country_gold_idx)
print(top_max_ratio)



# --------------
#Code starts here

data_1=data.drop(data.tail(1).index)
print(data_1.count())
data_1['Total_Points']=data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']*1
print(data_1['Total_Points'])

most_points=data_1['Total_Points'].max()
most_points_idx=data_1['Total_Points'].idxmax()
best_country=data_1.loc[most_points_idx,'Country_Name']

print(most_points)
print(most_points_idx)
print(best_country)



# --------------
#Code starts here

print(best_country)
best=data[data['Country_Name'] == best_country]

best=best[['Gold_Total', 'Silver_Total', 'Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


print(best)


