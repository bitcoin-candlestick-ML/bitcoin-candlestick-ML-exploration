# Exploring Chart Pattern Analysis

>"If you ever wondered if it was possible to find chart patterns and automatically trade the best, well now you can!"


## What did we do?
***We found a way to analize time series OHLC data to get important points that would create commonly used chart patterns.
We narrowed our project focus to one specific pattern due to constraints. We also focus on bitcoin as our main asset. Still, this code can be modified easily to find other patterns, and it can currently be applied to any asset with OHLC data.***

## What is a Double Bottom?
![Double Bottom](bitcoin-candlestick-ML-exploration/BTCUSD_2021-10-06_19-35-05.png)
***Above is an image of a double bottom with the most important points marked as A-E
A - Lead Up
B - First Bottom
C - Middle High
D - Second Bottom
E - Entry ***

## ETL
***We used Bitcoin daily price data from October 2017 to October 2021. 
During this span of time we were able to succesfully identify 21 trading signals!
Our dataframe has some of the following columns
Columns A-F represent the presence of event points in binary format - 0 (No event point) 1 (Event present).
DB - 0 (No double bottom) 1 (Double bottom finished at point, a.k.a entry)***
[DataFrame - Model 1](Resources/features_2017-2021.csv)

***In here are the images of the events the algo found***
[Events Found From Algorithm](Resources/event_figures)

***We also include a variety of metrics to aid our linear regression model in finding the most succesful signals.
This is the DataFrame used to train our linear regression model***
[DataFrame - Model 2](Resources/21_features.csv)

## Models
***Here are our models and our results.***
[Models](bitcoin-candlestick-ML-exploration/Neural_Net.ipynb)
[Models](bitcoin-candlestick-ML-exploration/Dbottom_net.ipynb)
