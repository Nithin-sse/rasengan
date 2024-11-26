import random
import math

class FeedForwardNN:
    def __init__(self, layers):
        self.layers = layers
        self.weights = [self.random_matrix(layers[i], layers[i+1]) for i in range(len(layers) - 1)]
        self.biases = [self.random_matrix(1, layers[i+1]) for i in range(len(layers) - 1)]

    def random_matrix(self, rows, cols):
        return [[random.random() for _ in range(cols)] for _ in range(rows)]

    def sigmoid(self, x): return [1 / (1 + math.exp(-xi)) for xi in x]

    def sigmoid_derivative(self, x): return [xi * (1 - xi) for xi in x]

    def dot(self, a, b):
        return [sum(x * y for x, y in zip(a_row, b_col)) for a_row in a for b_col in zip(*b)]

    def matrix_add(self, a, b):
        return [[ai + bi for ai, bi in zip(a_row, b_row)] for a_row, b_row in zip(a, b)]

    def matrix_transpose(self, matrix):
        return [list(i) for i in zip(*matrix)]

    def train(self, X, y, epochs, lr):
        for _ in range(epochs):
            # Forward Pass
            activations = [X]
            for w, b in zip(self.weights, self.biases):
                activations.append(self.sigmoid(self.add_bias(self.dot(activations[-1], w), b)))

            # Backward Pass
            error = self.subtract(y, activations[-1])
            deltas = [self.multiply(error, self.sigmoid_derivative(activations[-1]))]

            for i in range(len(self.weights)-1, 0, -1):
                error = self.dot(deltas[0], self.matrix_transpose(self.weights[i]))
                deltas.insert(0, self.multiply(error, self.sigmoid_derivative(activations[i])))

            # Update weights and biases
            for i in range(len(self.weights)):
                weight_gradient = self.dot(self.matrix_transpose(activations[i]), deltas[i])
                self.weights[i] = self.matrix_add(self.weights[i], self.multiply(weight_gradient, lr))
                self.biases[i] = self.matrix_add(self.biases[i], self.multiply(deltas[i], lr))

    def add_bias(self, x, b):
        return [xi + bi[0] for xi, bi in zip(x, b)]

    def subtract(self, a, b):
        return [ai - bi for ai, bi in zip(a, b)]

    def multiply(self, a, b):
        return [ai * bi for ai, bi in zip(a, b)]

    def predict(self, X):
        for w, b in zip(self.weights, self.biases):
            X = self.sigmoid(self.add_bias(self.dot(X, w), b))
        return X

# User Input
try:
    layers = eval(input("Enter layer sizes (e.g., [2, 3, 1]): "))
    X = eval(input("Enter training data (e.g., [[0, 0], [0, 1], [1, 0], [1, 1]]): "))
    y = eval(input("Enter labels (e.g., [[0], [1], [1], [0]]): "))
    epochs = int(input("Enter number of epochs (e.g., 10000): "))
    lr = float(input("Enter learning rate (e.g., 0.1): "))
    
    nn = FeedForwardNN(layers)
    nn.train(X, y, epochs, lr)

    test = eval(input("Enter test data (e.g., [[0, 1], [1, 1]]): "))
    predictions = [nn.predict(row) for row in test]
    print("Predictions:", predictions)

except Exception as e:
    print("Error:", e)

