# features: past ratings, time of ratings, current time, num devices
# output: predicted rating

import pandas
from sklearn import linear_model

df = pandas.read_csv("studyspace/views/data.csv")

locationOnlyDf = df.loc[df['Location'] == "IM"]
X = locationOnlyDf[['Devices', 'Time']]
y = locationOnlyDf['Rating']
regr = linear_model.Ridge()
regr.fit(X.values, y.values)

predictedRating = regr.predict([[100, 12]])

print(predictedRating)
