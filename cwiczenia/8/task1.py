import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
headers = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df = pd.read_csv(url, names=headers)

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2023)

svm = SVC()

svm.fit(X_train, y_train)

kfold = KFold(n_splits=5, random_state=2023, shuffle=True)
scores = cross_val_score(svm, X_train, y_train, cv=kfold, scoring="accuracy")

print("Cross-validation scores:")
print(scores)
print(f"Mean val: {scores.mean()}")

param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf', 'sigmoid'],
    'gamma': [0.1, 1, 10]
}


grid_search = GridSearchCV(svm, param_grid, cv=KFold(n_splits=5, random_state=2023, shuffle=True))
grid_search.fit(X_train, y_train)

results = pd.DataFrame(grid_search.cv_results_)
print(results)
results.to_csv("results.csv")
print(results["mean_test_score"])
print("Best parameters: ", grid_search.best_params_)
print("Best score: ", grid_search.best_score_)
best_model = grid_search.best_estimator_

best_predict = best_model.predict(X_test)
print("Accuracy on the testing set: ", accuracy_score(y_test, best_predict))

best_predict_train = best_model.predict(X_train)
print("Accuracy on the training set: ", accuracy_score(y_train, best_predict_train))

cm_train = confusion_matrix(y_train, best_predict_train)
print("Confusion matrix for the training set:")
print(cm_train)

report = classification_report(y_train, best_predict_train)
print(report)

with PdfPages('report.pdf') as pdf:
    plt.figure()
    plt.plot(range(1, 6), scores, marker='o')
    plt.xlabel('Fold')
    plt.ylabel('Accuracy')
    plt.title('Cross-Validation Accuracy')
    plt.grid(True)
    pdf.savefig()
    plt.close()

    plt.figure()
    cm = confusion_matrix(y_train, best_predict_train)
    classes = np.unique(y_train)
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix - Training Set')
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.tight_layout()
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, cm[i, j],
                     horizontalalignment="center",
                     color="white" if cm[i, j] > cm.max() / 2. else "black")
    pdf.savefig()
    plt.close()

    plt.figure()
    cm = confusion_matrix(y_test, best_predict)
    classes = np.unique(y_train)
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix - Test Set')
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.tight_layout()
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, cm[i, j],
                     horizontalalignment="center",
                     color="white" if cm[i, j] > cm.max() / 2. else "black")
    pdf.savefig()
    plt.close()

    plt.figure()
    plt.text(0.1, 0.5, report, fontsize=12, verticalalignment='center')
    plt.axis('off')
    plt.title('Classification Report - Training Set')
    pdf.savefig()
    plt.close()

