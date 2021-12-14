#load the required libraries
from sklearn.tree import DecisionTreeRegressor
from sklearn import preprocessing,metrics,linear_model
from sklearn.model_selection import cross_val_score,cross_val_predict,train_test_split
import math
import pandas as pd
import numpy as np
from  prettytable import PrettyTable
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

def data_split(bike_df):

    X_train,X_test,y_train,y_test=train_test_split(bike_df.iloc[:,0:-3],bike_df.iloc[:,-1],test_size=0.3, random_state=42)

    #Reset train index values
    X_train.reset_index(inplace=True)
    y_train=y_train.reset_index()

    # Reset train index values
    X_test.reset_index(inplace=True)
    y_test=y_test.reset_index()

    #print("X train & test shapes, Y train & test shapes:\n",X_train.shape,X_test.shape,y_train.shape,y_test.shape)
    #print(y_train.head())
    
    #categorical attributes
    category_features = ['season', 'hour', 'month', 'year', 'weekday', 'workingday', 'weather_condition']
    #numerical attributes
    numerical_features = ['temp', 'humidity', 'windspeed']

    features= category_features + numerical_features
    target = ['total_count']
    
    #Train dataset for modeling
    X_train = X_train[features].values
    y_train = y_train[target].values.ravel()

    #Test dataset for prediction
    X_test=X_test[features].values
    y_test=y_test[target].values.ravel()
    

    return X_train, y_train, X_test, y_test



def models(X_train, y_train, X_test, y_test):

    #print("X train & test shapes, Y train & test shapes:\n",X_train.shape,X_test.shape,y_train.shape,y_test.shape)
    linear_reg = linear_model.LinearRegression()
    dtr=DecisionTreeRegressor(min_samples_split=2,max_leaf_nodes=10)
    rf = RandomForestRegressor(n_estimators=200)
    SVR_lr = SVR(gamma='auto', kernel='linear')
    SVR_rbf = SVR(gamma='auto', kernel='rbf')
    table = PrettyTable()
    table.field_names = ["Model", "MSE", 'RMSE', 'MAE', 'ACC', 'MAD']
    diff_models = [linear_reg, dtr, SVR_rbf, rf]
    
    for model in diff_models:
        #fit the model
        model.fit(X_train,y_train)
        #Accuracy of the model
        acc=model.score(X_train,y_train)
        
        cross_predict=cross_val_predict(model,X_train,y_train,cv=3)

        #R-squared scores
        r2_scores = cross_val_score(model, X_train, y_train, cv=3)
        #predict the model
        y_pred=model.predict(X_test)

        #test accuracy
        acc_test=model.score(X_test,y_test)
        #Root mean square error 
        rmse=math.sqrt(metrics.mean_squared_error(y_test,y_pred))
        #Mean absolute error
        mae=metrics.mean_absolute_error(y_test,y_pred)
        #mean square error
        mse=metrics.mean_squared_error(y_test,y_pred)

        mad=mean_abs_deviation(y_test-y_pred)
        mad_pd = pd.Series(y_test,y_pred).mad()
        
        print("MAE & MAD & MAD PD:", mae, mad, mad_pd)
        
        table.add_row([type(model).__name__,format(mse, '.2f'), format(rmse, '.2f'), format(mae, '.2f'), format(acc_test, '.2f'),format(mad_pd, '.2f')])
        if model==rf:
                Bike_predictions=pd.DataFrame({'test': y_test, 'pred': y_pred}, columns=['test', 'pred'])
                Bike_predictions.to_csv('../BikeShare/Bike_Renting_Python.csv',sep=',')
    return table
           

def mean_abs_deviation(data):
    M = np.mean(data)
    sum = 0
    # Calculate mean absolute deviation
    for i in range(len(data)):
        dev = np.absolute(data[i] - M)
        sum = sum + round(dev,2)
    print ("Mean Absolute Deviation: ", sum/len(data))
    res = sum/len(data)
    return res




