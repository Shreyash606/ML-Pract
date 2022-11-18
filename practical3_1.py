# -*- coding: utf-8 -*-
"""practical3_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZM3XKVSA-UHY-TU7QjFXp0FGg8nVZngA
"""

from random import randint
x=[2,34,52,5,4,8,3,73,5,4]
y=[21,19,24,17,16,25,24,21,21,22]
c=[]
for i in range(10):
  c.append(randint(0,1))
print(c)

import matplotlib.pyplot as plt
plt.scatter(x,y,c=c)
plt.show

from sklearn.neighbors import KNeighborsClassifier

data=list(zip(x,y))
knn =KNeighborsClassifier(n_neighbors=3)

knn.fit(data,c)

x_test=[2,3,5,23,4,1]
y_test=[21,5,3,23,6,3]
test_data=list(zip(x_test,y_test))


prediction =knn.predict(test_data)
print(prediction)

plt.scatter(x_test,y_test,c=prediction)

from sklearn.naive_bayes import GaussianNB

#navie bayes
nb_model=GaussianNB()
nb_mod=nb_model.fit(data,c)
predictions= nb_mod.predict(test_data)

plt.scatter(x_test,y_test,c=predictions)
plt.show()

from sklearn.svm import SVC
sv_model=SVC()
sv_mod=sv_model.fit(data,c)
prediction=sv_mod.predict(test_data)
plt.scatter(x_test,y_test,c=prediction)

prediction