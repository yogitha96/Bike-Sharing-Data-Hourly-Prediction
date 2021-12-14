import matplotlib.pyplot as plt
import seaborn as sns
import  numpy as np


def visualize_plots(bike_hour_data):
    fig,ax=plt.subplots(figsize=(18,10))
    sns.set_style('white')
    #Bar plot for seasonwise monthly distribution of counts
    sns.barplot(x='month',y='total_count',data=bike_hour_data[['month','total_count','season']],hue='season',ax=ax)
    ax.set_title('Monthly distribution of counts of different seasons')
    plt.show()

    #Bar plot for weekday wise monthly distribution of counts
    fig,ax1=plt.subplots(figsize=(18,10))
    sns.barplot(x='month',y='total_count',data=bike_hour_data[['month','total_count','weekday']],hue='weekday',ax=ax1)
    ax1.set_title('Monthly distribution of counts throughout weekdays')
    plt.show()

    #Bar plot for yearly distribution of counts
    fig,ax2=plt.subplots(figsize=(18,10))
    sns.barplot(x='year',y='total_count',data=bike_hour_data[['year','total_count','month']],hue='month',ax=ax2)
    ax2.set_title('yearly distribution of counts in all months')
    plt.show()

    #Barplot for Holiday distribution of counts
    fig,ax3=plt.subplots(figsize=(18,10))
    sns.barplot(x='holiday',y='total_count',data=bike_hour_data[['holiday','total_count','season']],hue='season',ax=ax3)
    ax3.set_title('Holiday wise distribution of counts in different seasons')
    plt.show()

    #Bar plot for weather_condition distribution of counts
    fig,ax4=plt.subplots(figsize=(18,10))
    sns.barplot(x='weather_condition',y='total_count',data=bike_hour_data[['month','total_count','weather_condition']],hue='month',ax=ax4)
    ax4.set_title('Weather_condition wise monthly distribution of counts')
    plt.show()
    
    #Create the correlation matrix
    correMtr=bike_hour_data[["temp","atemp","humidity","windspeed","casual","registered","total_count"]].corr()
    mask=np.array(correMtr)
    mask[np.tril_indices_from(mask)]=False

    #Heat map for correlation matrix of attributes
    fig,ax5=plt.subplots(figsize=(18,10))
    sns.heatmap(correMtr,mask=mask,vmax=0.8,square=True,annot=True,ax=ax5)
    sns.color_palette("mako")
    ax5.set_title('Correlation matrix of attributes')
    plt.show()
