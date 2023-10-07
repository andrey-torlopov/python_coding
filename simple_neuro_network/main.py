from matplotlib.pylab import rand
import numpy as np
import matplotlib.pyplot as plt
import utils
import random

images, labels = utils.load_dataset()

weights_input_to_hidden = np.random.uniform(-0.5, 0.5, (20, 784))
weights_hidden_to_output = np.random.uniform(-0.5, 0.5, (10, 20))

bias_input_to_hidden = np.zeros((20, 1))
bias_hidden_to_output = np.zeros((10, 1))

epochs = 5
e_loss = 0
e_correct = 0
learning_rate = 0.01

for epoch in range(epochs):
    print(f"Epoch {epoch + 1}/{epochs}")

    for image, label in zip(images, labels):
        image = np.reshape(image, (-1, 1))
        label = np.reshape(label, (-1, 1))

        # Forward propagation to hidden layer

        hidden_raw = bias_input_to_hidden + weights_input_to_hidden @ image
        hidden = 1 / (1 + np.exp(-hidden_raw))  # sigmoid

        # Forward propagation to output layer
        output_raw = bias_hidden_to_output + weights_hidden_to_output @ hidden
        output = 1 / (1 + np.exp(-output_raw))

        # Loss / Error calculation
        e_loss += 1 / len(output) * np.sum((output - label) ** 2, axis=0)
        e_correct += int(np.argmax(output) == np.argmax(label))

        # LEARNING!
        # Backpropagation to output layer
        delta_output = output - label
        weights_hidden_to_output += -learning_rate * delta_output @ np.transpose(hidden)
        bias_hidden_to_output += -learning_rate * delta_output

        # Backpropagation to hidden layer
        delta_hidden = np.transpose(weights_hidden_to_output) @ delta_output * hidden * (1 - hidden)
        weights_input_to_hidden += -learning_rate * delta_hidden @ np.transpose(image)
        bias_input_to_hidden += -learning_rate * delta_hidden

        # LEARN DONE

    # Debug info between epochs
    # print(output)
    print(f"Loss:  {round((e_loss[0] / images.shape[0]) * 100, 3)} %")
    print(f"Accuracy:  {round((e_correct / images.shape[0]) * 100, 3)} %")
    e_loss = 0
    e_correct = 0


# CHECKING

# test_image = random.choice(images)
test_image = plt.imread("five.png", format="png")
# test_image = plt.imread("custom.jpg", format="jpeg")
# Grayscale + Unit RGB + inverse colors
def gray(rgb): return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


test_image = 1 - (gray(test_image).astype("float32") / 255)


image = np.reshape(test_image, (-1, 1))
# Forward propagation (to hidden layer)
hidden_raw = bias_input_to_hidden + weights_input_to_hidden @ image
hidden = 1 / (1 + np.exp(-hidden_raw))  # sigmoid
# Forward propagation (to output layer)
output_raw = bias_hidden_to_output + weights_hidden_to_output @ hidden
output = 1 / (1 + np.exp(-output_raw))

plt.imshow(test_image.reshape(28, 28), cmap="Greys")
plt.title(f"Your number is: {output.argmax()}")
print("Random answer: ", random.choice(range(10)))
plt.show()
