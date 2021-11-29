# Car Price Prediction

Determining whether the listed price of a used car is a challenging task, due to the many factors that drive a used vehicle’s price on the market. The focus of this project is developing machine learning models that can accurately predict the price of a used car based on its features, in order to make informed purchases.

# Problem Statement

Based on the factors given in the dataset need to predict the prices of car. It is a Regression problem.

# Source of Dataset:

The dataset is taken from Kaggle.Below is the link for the dataset:

https://www.kaggle.com/avikasliwal/used-cars-price-prediction

# Perfomance Metric

1)R2_ score

2)MSE

In this MSE is reduced as much as possible as it is Regression problem And Ideal MSE is 0.

# Machine Learning algorithms 

1). Linear Regression

2). RandomForest Regression

3). DecisionTree Regression

4). ExtraTree Regression

5). KNeighborsRegressor

# Car Price Prediction with Machine Learning

One of the main areas of research in machine learning is the prediction of the price of used cars. This dataset consists information about used car listed on cardekho.com. It has 9 columns each columns consists information about specific features like Car_Name: Car names gives information about car company.

Year: In which year the brand new car has been purchased.

selling_price: Its about the price at which car is being sold and this will be *target label *for further prediction of price.

km_driven : It is the number of kilometre car has been driven.

Fuel_Type: This feature the fuel type of car (CNG , petrol,diesel etc).

seller_type: This tells whether the seller is individual or a dealer.

transmission: This feature gives information about the whether the car is automatic and manual.

owner: It is number of previous owner of the car.

Present_price :This will be about current showroom price of the car.

# Data Analysis

![image](https://user-images.githubusercontent.com/74994512/134683295-f6f5ab25-4934-4a83-9364-0fa2f4e149b0.png)





![image](https://user-images.githubusercontent.com/74994512/134684418-06f0c5d2-dc0c-4e50-bb56-ea1d0c980e4e.png)

# Observation:

*   city appears to be most favoured car amongst all other car names.
  
*   Number of petrol fueled type cars are more compared to diesel and CNG.
  
*   Number of cars selled by Dealers are more than Indiviuals.

*   Manually Transmitted cars are heigher.

![image](https://user-images.githubusercontent.com/74994512/134684781-b6f37f85-28a9-45e3-a22e-da74927dcd60.png)





  Most of the cars have owned by 0 owners.
  
  # After training all the models we have got good results with RandomForest Regressor.
  
  # Feature Importance
  
  ![image](https://user-images.githubusercontent.com/74994512/134687914-e04272b6-189e-4bdf-a806-923a904948c0.png).
  
  
  
  
  
  Reference: 
  
  https://www.kaggle.com/cagkanbay/car-price-prediction
  
  https://www.appliedaicourse.com/

Deployed:

The model is deployed in AWS Platform.


Link: http://ec2-18-118-103-34.us-east-2.compute.amazonaws.com:5050/



