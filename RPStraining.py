import numpy as np

x_train = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
y_train = np.array([0,1,2,2,2,2,2,2,2,2])
y_train = y_train.reshape(len(y_train),1)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train_sc = sc.fit_transform(x_train)

from sklearn.svm import SVC
classifier = SVC(kernel='rbf')
classifier.fit(x_train_sc,y_train.ravel())


round = 11
def myfunction(n):
    global x_train,x_train_sc,y_train,round
    system = classifier.predict(sc.transform([[round]]))
    x_train = list(x_train)
    x_train.append([round])
    x_train = np.array(x_train)
    x_train_sc = sc.fit_transform(x_train)
    y_train = list(y_train)
    y_train.append([(n+1)%3])
    y_train = np.array(y_train)
    classifier.fit(x_train_sc,y_train.ravel())
    round+=1
    return system
