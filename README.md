# BikeSharing

The hourly data of bike-share consists of data with records of 17379 and 17 features. I have explored the data and looked into various features like hourly,  monthly, and yearly count of bikes and changed the column names into readable names for ease of use. Also, a graph is plotted to show the correlation between features to understand their linear relation for building better models and to consider a few variables that contain information to predict the labels and help in dimensionality reduction.

The first two plots show that the number of bike rentals increases in the spring(1) and summer(2) and decreases in the fall(3) and winter(4), with weekends having the lowest number because people may use bikes as a mode of transportation during working days. Figure 3 shows that the count grew from 2011 to 2012, with a relatively fair growth in monthly distribution, whereas Figure 4 shows that the count is highest in clear or partly cloudy and misty or partly overcast weather, with the least amount of rain. Holidays (with or without) have a comparable distribution, therefore there isn't much of a difference. The count variable's probability plot reveals that certain points deviate from the normal distribution, i.e., normality.

![Figure_1](https://user-images.githubusercontent.com/30980154/146015599-f5b6c373-4102-45d2-acc7-8843fc155330.png)
![Figure_2](https://user-images.githubusercontent.com/30980154/146015604-385af2c2-bc5d-400f-9107-6f3c6d77a137.png)
![Figure_3](https://user-images.githubusercontent.com/30980154/146015606-108cb980-94b0-498a-b7b9-18499069de4c.png)
![Figure_4](https://user-images.githubusercontent.com/30980154/146015609-8d7644e6-83f2-4dfb-9efd-9b16d7c3ffe8.png)
![Figure_9](https://user-images.githubusercontent.com/30980154/146015619-78761f10-eea7-4451-bff4-4a08dc5ba54d.png)
![Figure_6](https://user-images.githubusercontent.com/30980154/146015614-439a94c9-b2e9-4aae-9c96-098ac0e14939.png)
![Figure_7](https://user-images.githubusercontent.com/30980154/146015615-3834a7ba-828e-447e-87d4-a5e99756be80.png)

For better results, the data is divided into random splits of train and test with ratios of 70 and 30 respectively. Few models have been trained and tested to see which one performs better based on metrics. The metrics considered are Mean Squared Error(MSE), Root Mean Squared Error(RMSE), Mean Absolute Error(MAE), Mean Absolute Deviation(MAD) and Test Accuracy(acc_test). Random Forest, the model with the least MSE and RMSE error and highest accuracy, is selected as a prediction model for daily analysis of bike rentals. The following table consists of results for only the selected model along with Mean Absolute Deviation(MAD).

![bike_rf](https://user-images.githubusercontent.com/30980154/146020965-7a93812d-1fa4-4609-aa2a-06b064b9c8c7.jpg)

