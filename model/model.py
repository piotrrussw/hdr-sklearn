from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn import datasets
from skimage import exposure
import numpy

def init():
    # load the MNIST digits dataset
    mnist = datasets.load_digits()

    # Training and testing split,
    # 75% for training and 25% for testing
    (trainData, testData, trainLabels, testLabels) = train_test_split(numpy.array(mnist.data), mnist.target, test_size=0.01, random_state=42)

    # take 10% of the training data and use that for validation
    (trainData, valData, trainLabels, valLabels) = train_test_split(trainData, trainLabels, test_size=0.25, random_state=84)

    # initialize the values of k for our k-Nearest Neighbor classifier along with the
    # list of accuracies for each value of k
    kVals = range(1, 30, 2)
    accuracies = []

    # loop over kVals
    for k in range(1, 30, 2):
        # train the classifier with the current value of `k`
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(trainData, trainLabels)

        # evaluate the model and print the accuracies list
        score = model.score(valData, valLabels)
        # print("k=%d, accuracy=%.2f%%" % (k, score * 100))
        accuracies.append(score)

    # largest accuracy
    # numpy.argmax returns the indices of the maximum values along an axis
    i = numpy.argmax(accuracies)

    # Now that I know the best value of k, re-train the classifier
    model = KNeighborsClassifier(n_neighbors=kVals[i])
    model.fit(trainData, trainLabels)

    # Predict labels for the test set
    predictions = model.predict(testData)

    # Evaluate performance of model for each of the digits
    print(classification_report(testLabels, predictions))

    return model