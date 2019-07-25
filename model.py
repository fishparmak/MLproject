import numpy as np 
import pandas as pd 


from sklearn.utils import shuffle

# Importing the dataset
dataset = pd.read_csv('../input/heart.csv')
dataset = shuffle(dataset) # shuffling the dataset
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

len(dataset['age'])
# Checking for missing dataset
print('The number of missing values is : %d' %(dataset.isnull().sum().sum()))

# Encoding the dataset
# Not required

# Splitting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.15,random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Part 2 - Building the ANN
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam

def build_clf(opt):
    clf = Sequential()
    clf.add(Dense(units=13,kernel_initializer='uniform',activation='relu',
                  input_dim=13))
    clf.add(Dropout(rate=0.2))
    clf.add(Dense(units=18,kernel_initializer='uniform',activation='relu'))
    clf.add(Dropout(rate=0.2))
    clf.add(Dense(units=6,kernel_initializer='uniform',activation='relu'))
    clf.add(Dropout(rate=0.2))
    clf.add(Dense(units=1, kernel_initializer='uniform',activation='sigmoid'))
    clf.compile(optimizer=opt,loss='binary_crossentropy',metrics=['accuracy'])
    return clf

# Fitting the neural network to dataset
opt = Adam(lr=0.001, decay=0.000001)
clf = build_clf(opt)
Network = clf.fit(X_train, y_train, validation_split=0.15,epochs=100, verbose=1, batch_size=16)

# Predicting the output
y_pred = clf.predict(X_test)
y_pred = (y_pred>0.5)
y_pred = y_pred.astype(int)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
print('Accuracy of Prediction : %.3f' %(np.trace(cm)/np.sum(cm)*100))

# Saving model to disk
pickle.dump(clf, open('model.pkl','wb'))

# Loading model to compare the results
# model = pickle.load(open('model.pkl','rb'))
# print(model.predict([[2, 9, 6]]))