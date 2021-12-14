import pandas as pd
import numpy as np
import models
import visualize
import EDA

def main():
    bike_hour_data = pd.read_csv("../BikeShare/Bike-Sharing-Dataset/hour.csv")
    print("EXPLORATORY DATA ANALYSIS:\n")
    bike_data = EDA.bike_EDA(bike_hour_data)
    print("Visualization of different features against counts: \n")
    visualize.visualize_plots(bike_data)
    #split the data into train & test sets
    X_train, y_train, X_test, y_test = models.data_split(bike_data)
    #results stored in a table
    table = models.models(X_train, y_train, X_test, y_test)
    print(table)


if __name__ == '__main__':
    main()