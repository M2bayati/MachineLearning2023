# -*- coding: utf-8 -*-
"""Project_1_Part_1_Question_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wvzrIP0qkYXzlKLOMPP74QtDGA_DBd5D

# Part 1

## Dataset
"""

import matplotlib.pyplot as plt

from sklearn.datasets import make_classification

# Create the dataset
X, y = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_repeated=0,
    n_clusters_per_class=1,
    class_sep=1,
    n_classes=2,
    random_state=93
    )

# Display the dimensions of the dataset
print(f'Dimensions of the features: {X.shape}')
print(f'Dimensions of the target: {y.shape}')

# Create a scatter plot
plt.figure(figsize=(8, 6))  # Set the figure size
scatter_class_0 = plt.scatter(X[y == 0, 0], X[y == 0, 1], color='blue', label='Class 0', edgecolors='k', marker='o')
scatter_class_1 = plt.scatter(X[y == 1, 0], X[y == 1, 1], color='orange', label='Class 1', edgecolors='k', marker='o')
plt.xlabel("1'st feature")
plt.ylabel("2'nd feature")
plt.title('Scatter Plot of Dataset')  # Title for the plot
plt.legend(handles=[scatter_class_0, scatter_class_1], title='Classes',loc="upper left")
plt.grid(alpha=0.2)  # Display grid lines

"""# Part 2

## Classification
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, SGDClassifier, Perceptron

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=93, stratify=y)

# Display the dimensions of the training and testing sets
print(f'Dimensions of the training features: {X_train.shape}')
print(f'Dimensions of the training target: {y_train.shape}')
print(f'Dimensions of the testing features: {X_test.shape}')
print(f'Dimensions of the testing target: {y_test.shape}')

"""### Logistic Regression"""

LogReg_classifier = LogisticRegression(C=1.0, penalty='l2', solver='sag', max_iter=20000, random_state=93)
LogReg_classifier.fit(X_train, y_train)
y_pred = LogReg_classifier.predict(X_test)
LogReg_train_accuracy = LogReg_classifier.score(X_train, y_train)
LogReg_test_accuracy = LogReg_classifier.score(X_test, y_test)

y_pred, y_test

"""### SGD Classifier"""

SGD_classifier = SGDClassifier(alpha=0.01, loss='log_loss', max_iter=20000, penalty='l2', random_state=93)
SGD_classifier.fit(X_train, y_train)
y_pred1 = SGD_classifier.predict(X_test)
SGD_train_accuracy = SGD_classifier.score(X_train, y_train)
SGD_test_accuracy = SGD_classifier.score(X_test, y_test)

y_pred1, y_test

"""### Perceptron"""

perceptron_classifier = Perceptron(alpha=0.01, penalty='l2', max_iter=20000, random_state=93)
perceptron_classifier.fit(X_train, y_train)
y_pred2 = perceptron_classifier.predict(X_test)
perceptron_train_accuracy = perceptron_classifier.score(X_train, y_train)
perceptron_test_accuracy = perceptron_classifier.score(X_test, y_test)

y_pred2, y_test

"""### Accuracies"""

print(f"Logistic Regression Train Accuracy: {LogReg_train_accuracy:.2f}")
print(f"Logistic Regression Test Accuracy: {LogReg_test_accuracy:.2f}")

print(f"SGD Classifier Train Accuracy: {SGD_train_accuracy:.2f}")
print(f"SGD Classifier Test Accuracy: {SGD_test_accuracy:.2f}")

print(f"Perceptron Train Accuracy: {perceptron_train_accuracy:.2f}")
print(f"Perceptron Test Accuracy: {perceptron_test_accuracy:.2f}")

"""# Part 3

## Decision Boundary
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from mlxtend.plotting import plot_decision_regions

"""### Logistic Regression"""

plt.figure(figsize=(8,6))
plot_decision_regions(X, y, clf=SGD_classifier, legend=2)

# misclassified samples
misclassified = X[y != SGD_classifier.predict(X)]
plt.scatter(misclassified[:, 0], misclassified[:, 1], c='red', marker='*', s=100, label='Misclassified')

# label and title
plt.xlabel("1'st feature")
plt.ylabel("2'nd feature")
plt.title('Decision Regions and misclassified samples for SGD classifier method')
plt.legend(loc="upper left")

"""### SGD Classifier"""

plt.figure(figsize=(8,6))
plot_decision_regions(X, y, clf=SGD_classifier, legend=2)

# misclassified samples
misclassified = X[y != SGD_classifier.predict(X)]
plt.scatter(misclassified[:, 0], misclassified[:, 1], c='red', marker='*', s=100, label='Misclassified')

# label and title
plt.xlabel("1'st feature")
plt.ylabel("2'nd feature")
plt.title('Decision Regions and misclassified samples for SGD classifier method')
plt.legend(loc="upper left")

"""### Perceptron"""

plt.figure(figsize=(8,6))
plot_decision_regions(X, y, clf=perceptron_classifier, legend=2)

# misclassified samples
misclassified = X[y != perceptron_classifier.predict(X)]
plt.scatter(misclassified[:, 0], misclassified[:, 1], c='red', marker='*', s=100, label='Misclassified')

# label and title
plt.xlabel("1'st feature")
plt.ylabel("2'nd feature")
plt.title('Decision Regions and misclassified samples for perceptron method')
plt.legend(loc="upper left")

"""# Part 4

## Dataset
"""

import matplotlib.pyplot as plt

from sklearn.datasets import make_classification

# Create the dataset
X, y = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_repeated=0,
    n_clusters_per_class=2,
    class_sep=0.7,
    n_classes=2,
    random_state=93
    )

# Display the dimensions of the dataset
print(f'Dimensions of the features: {X.shape}')
print(f'Dimensions of the target: {y.shape}')

# Create a scatter plot
plt.figure(figsize=(8, 6))  # Set the figure size
scatter_class_0 = plt.scatter(X[y == 0, 0], X[y == 0, 1], color='blue', label='Class 0', edgecolors='k', marker='o')
scatter_class_1 = plt.scatter(X[y == 1, 0], X[y == 1, 1], color='orange', label='Class 1', edgecolors='k', marker='o')
plt.xlabel("1'st feature")
plt.ylabel("2'nd feature")
plt.title('Scatter Plot of Dataset')  # Title for the plot
plt.legend(handles=[scatter_class_0, scatter_class_1], title='Classes',loc="upper left")
plt.grid(alpha=0.2)  # Display grid lines

"""## Part 4-2

### Classification
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, SGDClassifier, Perceptron

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=93, stratify=y)

# Display the dimensions of the training and testing sets
print(f'Dimensions of the training features: {X_train.shape}')
print(f'Dimensions of the training target: {y_train.shape}')
print(f'Dimensions of the testing features: {X_test.shape}')
print(f'Dimensions of the testing target: {y_test.shape}')

"""**Logistic regression**"""

LogReg_classifier = LogisticRegression(C=1.0, penalty='l2', solver='sag', max_iter=20000, random_state=93)
LogReg_classifier.fit(X_train, y_train)
y_pred = LogReg_classifier.predict(X_test)
LogReg_train_accuracy = LogReg_classifier.score(X_train, y_train)
LogReg_test_accuracy = LogReg_classifier.score(X_test, y_test)

y_pred, y_test

"""**SGD Classifier**"""

SGD_classifier = SGDClassifier(alpha=0.01, loss='log_loss', max_iter=20000, penalty='l2', random_state=93)
SGD_classifier.fit(X_train, y_train)
y_pred1 = SGD_classifier.predict(X_test)
SGD_train_accuracy = SGD_classifier.score(X_train, y_train)
SGD_test_accuracy = SGD_classifier.score(X_test, y_test)

y_pred1, y_test

"""**Perceptron**"""

perceptron_classifier = Perceptron(alpha=0.01, penalty='l2', max_iter=20000, random_state=93)
perceptron_classifier.fit(X_train, y_train)
y_pred2 = perceptron_classifier.predict(X_test)
perceptron_train_accuracy = perceptron_classifier.score(X_train, y_train)
perceptron_test_accuracy = perceptron_classifier.score(X_test, y_test)

y_pred2, y_test

"""**Accuracies**"""

print(f"Logistic Regression Train Accuracy: {LogReg_train_accuracy:.2f}")
print(f"Logistic Regression Test Accuracy: {LogReg_test_accuracy:.2f}")

print(f"SGD Classifier Train Accuracy: {SGD_train_accuracy:.2f}")
print(f"SGD Classifier Test Accuracy: {SGD_test_accuracy:.2f}")

print(f"Perceptron Train Accuracy: {perceptron_train_accuracy:.2f}")
print(f"Perceptron Test Accuracy: {perceptron_test_accuracy:.2f}")

"""## Part 4-3

### Decision Boundary
"""

import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions

"""**Logistic Regression**"""

plt.figure(figsize=(8,6))
plot_decision_regions(X, y, clf=LogReg_classifier, legend=2)

# misclassified samples
misclassified = X[y != LogReg_classifier.predict(X)]
plt.scatter(misclassified[:, 0], misclassified[:, 1], c='red', marker='*', s=100, label='Misclassified')

# label and title
plt.xlabel("1'st feature")
plt.ylabel("2'nd feature")
plt.title('Decision Regions and misclassified samples for Logistic Regression method')
plt.legend(loc="upper left")

"""**SGD Classifier**"""

plt.figure(figsize=(8,6))
plot_decision_regions(X, y, clf=SGD_classifier, legend=2)

# misclassified samples
misclassified = X[y != SGD_classifier.predict(X)]
plt.scatter(misclassified[:, 0], misclassified[:, 1], c='red', marker='*', s=100, label='Misclassified')

# label and title
plt.xlabel("1'st feature")
plt.ylabel("2'nd feature")
plt.title('Decision Regions and misclassified samples for SGD classifier method')
plt.legend(loc="upper left")

"""**Perceptron**"""

plt.figure(figsize=(8,6))
plot_decision_regions(X, y, clf=perceptron_classifier, legend=2)

# misclassified samples
misclassified = X[y != perceptron_classifier.predict(X)]
plt.scatter(misclassified[:, 0], misclassified[:, 1], c='red', marker='*', s=100, label='Misclassified')

# label and title
plt.xlabel("1'st feature")
plt.ylabel("2'nd feature")
plt.title('Decision Regions and misclassified samples for perceptron method')
plt.legend(loc="upper left")

"""# Part 5

## Dataset
"""

import matplotlib.pyplot as plt

from sklearn.datasets import make_classification

# Create the dataset
X, y = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_repeated=0,
    n_clusters_per_class=1,
    class_sep=1,
    n_classes=3,
    random_state=93
    )

# Display the dimensions of the dataset
print(f'Dimensions of the features: {X.shape}')
print(f'Dimensions of the target: {y.shape}')

# Create a scatter plot
plt.figure(figsize=(8, 6))  # Set the figure size
scatter_class_0 = plt.scatter(X[y == 0, 0], X[y == 0, 1], color='blue', label='Class 0', edgecolors='k', marker='o')
scatter_class_1 = plt.scatter(X[y == 1, 0], X[y == 1, 1], color='orange', label='Class 1', edgecolors='k', marker='o')
scatter_class_1 = plt.scatter(X[y == 2, 0], X[y == 2, 1], color='green', label='Class 2', edgecolors='k', marker='o')
plt.xlabel("1'st feature")
plt.ylabel("2'nd feature")
plt.title('Scatter Plot of Dataset')  # Title for the plot
plt.legend(handles=[scatter_class_0, scatter_class_1], title='Classes',loc="upper left")
plt.grid(alpha=0.2)  # Display grid lines

"""## Classification"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, SGDClassifier, Perceptron

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=93)

# Display the dimensions of the training and testing sets
print(f'Dimensions of the training features: {X_train.shape}')
print(f'Dimensions of the training target: {y_train.shape}')
print(f'Dimensions of the testing features: {X_test.shape}')
print(f'Dimensions of the testing target: {y_test.shape}')

"""### Logistic Regression"""

LogReg_classifier = LogisticRegression(C=1.0, penalty='l2', solver='sag', max_iter=20000, random_state=93)
LogReg_classifier.fit(X_train, y_train)
y_pred = LogReg_classifier.predict(X_test)
LogReg_train_accuracy = LogReg_classifier.score(X_train, y_train)
LogReg_test_accuracy = LogReg_classifier.score(X_test, y_test)

y_pred, y_test

"""### SGD Classifier"""

SGD_classifier = SGDClassifier(alpha=0.01, loss='log_loss', max_iter=20000, penalty='l2', random_state=93)
SGD_classifier.fit(X_train, y_train)
y_pred1 = SGD_classifier.predict(X_test)
SGD_train_accuracy = SGD_classifier.score(X_train, y_train)
SGD_test_accuracy = SGD_classifier.score(X_test, y_test)

y_pred1, y_test

"""### Perceptron"""

perceptron_classifier = Perceptron(alpha=0.01, penalty='l2', max_iter=20000, random_state=93)
perceptron_classifier.fit(X_train, y_train)
y_pred2 = perceptron_classifier.predict(X_test)
perceptron_train_accuracy = perceptron_classifier.score(X_train, y_train)
perceptron_test_accuracy = perceptron_classifier.score(X_test, y_test)

y_pred2, y_test

"""### Accuracies"""

print(f"Logistic Regression Train Accuracy: {LogReg_train_accuracy:.2f}")
print(f"Logistic Regression Test Accuracy: {LogReg_test_accuracy:.2f}")

print(f"SGD Classifier Train Accuracy: {SGD_train_accuracy:.2f}")
print(f"SGD Classifier Test Accuracy: {SGD_test_accuracy:.2f}")

print(f"Perceptron Train Accuracy: {perceptron_train_accuracy:.2f}")
print(f"Perceptron Test Accuracy: {perceptron_test_accuracy:.2f}")

"""## Decision Boundary"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from mlxtend.plotting import plot_decision_regions

"""### Logistic Regression"""

plt.figure(figsize=(8,6))
plot_decision_regions(X, y, clf=SGD_classifier, legend=2)

# misclassified samples
misclassified = X[y != SGD_classifier.predict(X)]
plt.scatter(misclassified[:, 0], misclassified[:, 1], c='red', marker='*', s=100, label='Misclassified')

# label and title
plt.xlabel("1'st feature")
plt.ylabel("2'nd feature")
plt.title('Decision Regions and misclassified samples for SGD classifier method')
plt.legend(loc="upper left")

"""### SGD Classifier"""

plt.figure(figsize=(8,6))
plot_decision_regions(X, y, clf=SGD_classifier, legend=2)

# misclassified samples
misclassified = X[y != SGD_classifier.predict(X)]
plt.scatter(misclassified[:, 0], misclassified[:, 1], c='red', marker='*', s=100, label='Misclassified')

# label and title
plt.xlabel("1'st feature")
plt.ylabel("2'nd feature")
plt.title('Decision Regions and misclassified samples for SGD classifier method')
plt.legend(loc="upper left")

"""### Perceptron"""

plt.figure(figsize=(8,6))
plot_decision_regions(X, y, clf=perceptron_classifier, legend=2)

# misclassified samples
misclassified = X[y != perceptron_classifier.predict(X)]
plt.scatter(misclassified[:, 0], misclassified[:, 1], c='red', marker='*', s=100, label='Misclassified')

# label and title
plt.xlabel("1'st feature")
plt.ylabel("2'nd feature")
plt.title('Decision Regions and misclassified samples for perceptron method')
plt.legend(loc="upper left")