

# from google.colab import drive
# drive.mount('/content/drive')

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# from sklearn.metrics import roc_curve , auc
from sklearn.ensemble import RandomForestClassifier

class mode:
  def just(__self__,l):
    trainn = pd.read_csv("./phishing.csv")
    # 11054 rows and 32 columns
    print(trainn.shape)
    missing  = pd.concat([trainn.isnull().sum()],axis = 1 , keys=['Train'])
    # print(trainn.head())
    alldata = trainn.drop(["class","Index"],axis =1)
    # trainn.columns
    # alldata.columns
    trainn.head
    for col in trainn.dtypes[trainn.dtypes == "object"].index:
      for_dummy = trainn.pop(col)
      trainn = pd.concat([trainn, pd.get_dummies(for_dummy,prefix=col)],axis=1)
      # trainn.head()
    labels = trainn.pop("class")
    # labels.head
    # labels.shape
<<<<<<< Updated upstream
    x_train,x_test,y_train,y_test = train_test_split(trainn, labels,test_size = 0.30)
    print(x_test.shape)
    rf = RandomForestClassifier()
    rf.fit(x_train,y_train)
    example =np.array([l]) 
    outputt= rf.predict(example)
    print(outputt)
=======
    x_train,x_test,y_train,y_test = train_test_split(alldata, labels,test_size = 0.10)
    # print(x_test.shape)
    rf = RandomForestClassifier()
    rf.fit(x_train,y_train)
    # example =np.array([l]) 
    outputt= rf.predict(l)
    # print(outputt)
>>>>>>> Stashed changes
    #y_pred = rf.predict(x_test)
    return outputt




# y_pred = ob.rf.predict(x_test)


