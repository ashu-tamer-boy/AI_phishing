from sklearn.model_selection import train_test_split
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from FeatureExtraction import *
import os
# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

data = pd.read_csv('./phishing.csv')
data.head()
import modelll 

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
from sklearn import metrics
import warnings
from sklearn.ensemble import GradientBoostingClassifier
warnings.filterwarnings('ignore')

data = pd.read_csv('./phishing.csv')
data.head()
data.columns
data.isnull().sum()

X = data.drop(["class","Index"],axis =1)
y = data["class"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
X_train.shape, y_train.shape, X_test.shape, y_test.shape

gbc = GradientBoostingClassifier(max_depth=4,learning_rate=0.7)
gbc.fit(X_train,y_train)
y_train_gbc = gbc.predict(X_train)
y_test_gbc = gbc.predict(X_test)
# acc_train_gbc = metrics.accuracy_score(y_train,y_train_gbc)
# acc_test_gbc = metrics.accuracy_score(y_test,y_test_gbc)
# print("Gradient Boosting Classifier : Accuracy on training Data: {:.3f}".format(acc_train_gbc))
# print("Gradient Boosting Classifier : Accuracy on test Data: {:.3f}".format(acc_test_gbc))
# print()

# f1_score_train_gbc = metrics.f1_score(y_train,y_train_gbc)
# f1_score_test_gbc = metrics.f1_score(y_test,y_test_gbc)

# precision_score_train_gbc = metrics.precision_score(y_train,y_train_gbc)
# precision_score_test_gbc = metrics.precision_score(y_test,y_test_gbc)

# storeResults('Gradient Boosting Classifier',acc_test_gbc,f1_score_test_gbc,precision_score_train_gbc)




gbc = GradientBoostingClassifier(max_depth=4,learning_rate=0.7)
gbc.fit(X_train,y_train)


# url="htds://naksjd@/.nakul"
#can provide any URL. this URL was taken from PhishTank
# obj = FeatureExtraction(url)
# x = np.array(obj.getFeaturesList()).reshape(1,30) 
# y_pred =gbc.predict(x)[0]
# if y_pred==1:
#   print("We guess it is a safe website")
# else:
#   print("Caution! Suspicious website detected")


# modelll.mode()

# objectofmodel = mode()
# print()
# o = objectofmodel.just(x)
# print(o)
# if(o[0] == 1):
#        print('This url is safe to view' )
# else:
#         print('this URL  can be phishing url')