# IRIS Dataset
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# Loading Dataset
iris = datasets.load_iris()

# Printing Description and Featutes
print(iris.DESCR)
features = iris.data
labels = iris.target

# Training the classifier
clf = KNeighborsClassifier()
clf.fit(features, labels)
preds = clf.predict([[1.1, 2.3, 6.5, 1.3]])
print(preds)
