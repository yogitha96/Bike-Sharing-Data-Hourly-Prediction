import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.model_selection import train_test_split
warnings.filterwarnings('ignore')
#import os
from scipy import  stats

#print(os.listdir("../BikeShare/Bike-Sharing-Dataset"))


#Exploratory Data Analysis
def bike_EDA(bike_hour_data):

    print("Shape of the bike data hourly: ",bike_hour_data.shape)

    bike_hour_data.rename(columns={'dteday':'datetime','yr':'year','mnth':'month','hr':'hour','weathersit':'weather_condition',
                        'hum':'humidity','cnt':'total_count'},inplace=True)

    print("Data Types of the bike data hourly: ",bike_hour_data.dtypes)

    print("\nFirst 5 rows\n",bike_hour_data.head(5))

    category_features = ['season', 'holiday', 'hour', 'month', 'year', 'weekday', 'workingday', 'weather_condition']
    numerical_features = ['temp', 'atemp', 'humidity', 'windspeed']

    features= category_features + numerical_features
    target = ['total_count']
    #print("\nSummary of the categorical features:\n",bike_hour_data[category_features].describe())

    print("\nSummary of the categorical features:\n",bike_hour_data[category_features].astype('category').describe())

    print("\nChecking for the null values:\n",bike_hour_data.isnull().sum()) #no null values were present
       
    #create dataframe for outliers
    outlier_data=pd.DataFrame(bike_hour_data,columns=['windspeed','humidity'])
    #Cnames for outliers                     
    col_names=['windspeed','humidity']       
                        
    for i in col_names:
        q75,q25=np.percentile(outlier_data.loc[:,i],[75,25]) # Divide data into 75%quantile and 25%quantile.
        iqr=q75-q25 #Inter quantile range
        min=q25-(iqr*1.5) #inner fence
        max=q75+(iqr*1.5) #outer fence
        outlier_data.loc[outlier_data.loc[:,i]<min,:i]=np.nan  #Replace with NA
        outlier_data.loc[outlier_data.loc[:,i]>max,:i]=np.nan  #Replace with NA
    #Imputating the outliers by mean Imputation
    outlier_data['windspeed']=outlier_data['windspeed'].fillna(outlier_data['windspeed'].mean())
    outlier_data['humidity']=outlier_data['humidity'].fillna(outlier_data['humidity'].mean())

    #Replacing the imputated windspeed
    bike_hour_data['windspeed']=bike_hour_data['windspeed'].replace(outlier_data['windspeed'])
    #Replacing the imputated humidity
    bike_hour_data['humidity']=bike_hour_data['humidity'].replace(outlier_data['humidity'])
    print(bike_hour_data.head(5))


    #Normal plot
    fig=plt.figure(figsize=(18,10))
    stats.probplot(bike_hour_data.total_count.tolist(),dist='norm',plot=plt)
    plt.show()

    return bike_hour_data
    



