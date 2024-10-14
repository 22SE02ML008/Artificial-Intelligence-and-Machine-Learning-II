# importing packages
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# getting the data from iris file
iris = load_iris()
x = iris.data
y = iris.target

# dividing the data for training and tesing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# initializing the KNN classifier with k=3
knn = KNeighborsClassifier(n_neighbors=3)

# training the classifier
knn.fit(x_train, y_train)

# making the prediction
y_pred = knn.predict(x_test)

# getting the accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Predicted labels:", y_pred)
print("True labels: ", y_test)
print("Accuracy:", accuracy)
