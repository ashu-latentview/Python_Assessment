

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Q1
df=pd.read_excel('Walmart_Dataset Python_Final_Assessment.xlsx')
df.info()

df.head()

df.shape

df.describe()

df['Category'].value_counts()

# Q2
df.isnull().sum()

# Here we can see that in the given dataset we dont have any null values.

df.fillna(0)

df.duplicated().sum()

# Here we can see thet we dont have any duplicate values in our dataset



# 3
print("Mean= \n", df.mean())

# this will give the mean, median and standard deviation of all the columns present in the dataset

print("Median= \n",df.median())

print("Sales range Is = ",(df['Sales'].max()-df['Sales'].min()))

print("Quantity range Is = ",(df['Quantity'].max()-df['Quantity'].min()))

print("Profit range Is = ",(df['Profit'].max()-df['Profit'].min()))

print("Standard Deviation= \n",df.std())

print("Variance= \n",df.var())

# Here in above cells we have found the mean,median,standard diviation and variuance of all the numeric column

# Q4 PLotting the charts
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Plotting the chart
plt.figure(figsize=(10, 6))
plt.plot(df['Order Date'], df['Sales'])
plt.title('Sales vs Date')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

df['Order Date'] = pd.to_datetime(df['Order Date'])
plt.figure(figsize=(10, 6))
df.resample('M', on='Order Date')['Sales'].sum().plot(kind='line')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

df['Order Date'] = pd.to_datetime(df['Order Date'])
plt.figure(figsize=(10, 6))
df.resample('M', on='Order Date')['Profit'].sum().plot(kind='line')
plt.title('Monthly Profit Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

plt.figure(figsize=(10, 6))
df['Category'].value_counts().plot(kind='pie')
plt.title('Product Category Distribution')
plt.xlabel('Product Category')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
df['Category'].value_counts().plot(kind='bar')
plt.title('Product Category Distribution')
plt.xlabel('Product Category')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
df.groupby('Geography')['Sales'].sum().plot(kind='bar')
plt.title('Sales Performance by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.show()

df['Order Date'] = pd.to_datetime(df['Order Date'])
plt.figure(figsize=(10, 6))
df.groupby('Category')['Sales'].sum().plot(kind='line', marker='o')
plt.title('Sales Growth Over the Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.grid(True)
plt.show()



x=df['Geography'].unique()
print("There are ",len(x)," Different locations")

x = df['Geography'].value_counts().index
y = df['Geography'].value_counts().values

plt.figure(figsize=(10, 6))
plt.bar(x, y)
plt.xlabel('Geography')
plt.ylabel('Frequency')
plt.title('Unique Locations Distribution')
plt.xticks(rotation=45, ha='right')
plt.show()

# Q5
correlation_matrix = df.corr()
print("Correlation Matrix:")
print(correlation_matrix)

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# Q6
plt.boxplot(df['Sales'])
plt.title('Boxplot of Sales')
plt.show()

Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['Sales'] < lower_bound) | (df['Sales'] > upper_bound)]
print("Outliers:")

plt.boxplot(df['Profit'])
plt.title('Boxplot of Profit with Outliers')
plt.show()

print("Total Number Of Outliers In the dataset are ",len(outliers))

# Q7
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year
sf = df.groupby('Year').agg({'Sales': 'sum', 'Profit': 'sum'})
sf.plot(kind='line', subplots=True)

sc = df.groupby(['Year', 'Category']).agg({'Sales': 'sum'}).unstack()
sc.plot(kind='line', marker='o', figsize=(10, 6))

top_orders = df.groupby('EmailID')['Order ID'].nunique().nlargest(5)
top_sales = df.groupby('EmailID')['Sales'].sum().nlargest(5)
print('top_customers_orders',top_orders)
print('top_customers_sales',top_sales)

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Order Date Previous'] = df.groupby('EmailID')['Order Date'].shift(1)
df['Time Between Orders'] = df['Order Date'] - df['Order Date Previous']
average_time_between_orders = df.groupby('EmailID')['Time Between Orders'].mean()

average_time_between_orders = df.groupby('EmailID')['Time Between Orders'].mean()
print(average_time_between_orders)

"""Question 7
Trend Analysis:-
1. While comparing the trend of profits and sales throuout the month and year. We can conclude that Sales have increased significantly but has faced some downfalls also but the overall trend of sales is in upward direction

But when we see the chart of profit trend then the profit has gone up but not to the extenct as that of the sales. Also profit of the company declined during the period of May 2024. This is maybe because of expansion of the company. But that was for a short period of time and then the comapany recovered from the Loss.

2. By seeing the charts We can conclude that Copiers and blinders has shown the highest growth in terms of sales Over the year.

Question 7 Customer Analysis
1.  Ater grouping the data on the basis of customers email id and aggregating the data we found the top 5 customers who have made most orders and customers wo has made the highest sales
and those customers are

on the basis of order quantity

ArianneIrving@gmail.com    7

BillDonatelli@gmail.com    7

SallyHughsby@gmail.com     7

SanjitEngle@gmail.com      7

ArthurPrichep@gmail.com    6


On the basis of sales

RaymondBuch@gmail.com      14345.276

KenLonsdale@gmail.com       8472.394

EdwardHooks@gmail.com       7447.770

JaneWaco@gmail.com          7391.530

KarenFerguson@gmail.com     7182.766

2. We can find the average repetion time for repeating order by a customer by using
average_time_between_orders = df.groupby('EmailID')['Time Between Orders'].mean()
print(average_time_between_orders)
"""



"""Comprehensive Analysis
1. Sales of the product is fluctuating between different month but if we see for whole year it is increasing stedily so with every passing year we must focus on the expansion of supply chains
2. We can see on the basis of the chart that some locations have extremely hight order rate but on the other hand some locations are also there which have low order rate. So our target should be to keep on the strategy that we are following in the high order rate locations but we also need to focus more heavily on increasing the orders quantity in low order rate location. In order to do that we have to do some promotional campaigning and we have to give discounts.

3. By seeing the top 5 high value customers we can say that person wo is placing more quantity of order is having high sales also. So by taking this info into consideration we can apply some strategies to make customer place more quantity of orders and hence the revenue will be increased. we can use several dicounts coupons above a certain quantity of order
"""