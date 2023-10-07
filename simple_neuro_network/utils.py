import numpy as np


def load_dataset():
    with np.load('mnist.npz') as f:
        # Convert from RGB to unit RGB
        x_train = f['x_train'].astype("float32") / 255
        # reshape from (60_000, 28, 28) into (60_000, 784)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1] * x_train.shape[2]))

        # labels
        y_train = f['y_train']
        y_train = np.eye(10)[y_train]

    return x_train, y_train
