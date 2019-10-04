import numpy as np
#import matplotlib as plt
import pandas as pd
# Importing the dataset
data_set = pd.read_csv('rpifinal.csv')

#data_set.groupby(['datetime']).mean().add_suffix('_avg').reset_index()

y=data_set.iloc[:,-1].values #@9-'_rain'
X=data_set.iloc[:,1:4].values#@6-'_hum',@8-'_pressurem',@11-'_tempm'


#Splitting Dataset into X_train, X_test, y_train, y_test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)



# Fitting X_train,y_train in Random Forest Classification model
from sklearn.ensemble import RandomForestClassifier
cf = RandomForestClassifier(n_estimators =70, criterion = 'entropy', random_state = 0)
cf.fit(X_train, y_train)


# Predicting the results of test set
def preg(b,h,u):
    X_test[1834][0]=b
    X_test[1834][1]=h
    X_test[1834][2]=u
    y_pred = cf.predict(X_test)
    return y_pred[1834]

"""#Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

#measuring accuracy of the model
from sklearn.metrics import accuracy_score
a=accuracy_score(y_test, y_pred)

#visualising important features of data
imp = cf.feature_importances_
indices = np.argsort(imp)
plt.figure(1)
plt.title('Feature Importances')
plt.barh(range(len(indices)), imp[indices], color='b', align='center')
plt.xlabel('Relative Importance')
plt.yticks(range(len(indices)), indices)"""