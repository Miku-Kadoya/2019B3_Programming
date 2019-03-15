import numpy as np
from a41 import NeuralNetwork
from dataset.mnist import load_mnist

def main():
    mnist = load_mnist()
    model = NeuralNetwork()

    batch_size = 100
    train_images = 60000
    train_epochs = 100
    train_iters = train_epochs * (train_images // batch_size)

    for i in range(train_iters):
        indices = np.random.choice(train_images, batch_size)
        minibatch_image = mnist["train_img"][indices]
        minibatch_label = mnist["train_label"][indices]
        model.sgd(minibatch_image, minibatch_label, 0.0001)
        if i % 100 == 0:
            print("Loss {0}: {1}".format(
                i, model.loss(minibatch_image, minibatch_label)))
            accuracy = np.average(
                (np.argmax(minibatch_label, axis=1) == \
                 np.argmax(model.forward(minibatch_image), axis=1)).astype(int))
            print("Acc: {0} %".format(accuracy * 100))

    print("Test Loss: {0}".format(model.loss(
        mnist["test_img"], mnist["test_label"])))
    test_acc = np.average(
        (np.argmax(mnist["test_label"], axis=1) == \
         np.argmax(model.forward(mnist["test_img"]), axis=1)).astype(int))
    print("Test Acc: {0} %".format(test_acc * 100))

if __name__ == "__main__":
    main()
