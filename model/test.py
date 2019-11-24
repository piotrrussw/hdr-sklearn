from model import *
import numpy
from sklearn.model_selection import train_test_split

model = init()
mnist = datasets.load_digits()
(trainData, testData, trainLabels, testLabels) = train_test_split(numpy.array(mnist.data), mnist.target, test_size=0.2, random_state=42)
wrongly_predicted = [0] * 10
tested = [0] * 10

for i in numpy.random.randint(0, high=len(testLabels), size=(10000,)):
    image = testData[i]
    prediction = model.predict([image])[0]
    tested[testLabels[i]] += 1
    
    if prediction != testLabels[i]:
        wrongly_predicted[testLabels[i]] += 1

print("Wrongly predicted: ", str(wrongly_predicted))
print("Tested: ", str(tested))