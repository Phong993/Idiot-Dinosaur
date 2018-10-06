import numpy as np
import Idiot_Dinosaur

def relu(array):
    return np.maximum(array, 0.)

def sigmoid(z):
    s = 1 / (1 + np.exp(-z))
    return s

def initialize_parameters(n_x, n_h,n_y):
    """
    Argument:
    n_x -- size of the input layer
    n_h -- size of the hidden layer
    n_y -- size of the output layer

    Returns:
    params -- python dictionary containing your parameters:
                    W1 -- weight matrix of shape (n_h, n_x)
                    b1 -- bias vector of shape (n_h, 1)
                    W2 -- weight matrix of shape (n_y, n_h)
                    b2 -- bias vector of shape (n_y, 1)
    """

    #W1 = np.random.randn(n_h,n_x) * 0.01
    #b1 = np.random.randn(n_h,1) * 0.5
    #W2 = np.random.randn(n_y,n_h) * 1.5
    #b2 = np.random.randn(n_y, 1) * 0.15

    W1 = np.array([[-0.02062025,  0.00016742,  0.00381535],
       [ 0.00226537,  0.01325698,  0.02389935],
       [ 0.02300561,  0.01351209,  0.00588823]])
    b1 = np.array([[-0.73119972],
       [-0.05157346],
       [-0.00290758]])
    W2 = np.array([[ 0.91572382, -0.29862268,  0.30955728]])
    b2 = np.array([[ 0.27304736]])

    parameters = {"W1": W1, "b1": b1, "W2": W2, "b2": b2}

    return parameters

def re_shape_X(X, n_x):
    return np.reshape(X,(n_x, 1))

def tRex_model(X, parameters):
    """
    Argument:
    X -- input data of size (n_x, m)
    parameters -- python dictionary containing your parameters (output of initialization function)

    Returns:
    A2 -- The sigmoid output of the second activation
    """
    if len(parameters) == 4:
        W1 = parameters['W1']
        b1 = parameters['b1']
        W2 = parameters['W2']
        b2 = parameters['b2']

        Z1 = np.dot(W1, X) + b1
        A1 = sigmoid(Z1)
        Z2 = np.dot(W2, A1) + b2
        A2 = sigmoid(Z2)

        return A2
    else:
        parameters = initialize_parameters(3, 3, 1)
        W1 = parameters['W1']
        b1 = parameters['b1']
        W2 = parameters['W2']
        b2 = parameters['b2']

        Z1 = np.dot(W1, X) + b1
        A1 = sigmoid(Z1)
        Z2 = np.dot(W2, A1) + b2
        A2 = sigmoid(Z2)

        return A2

def from_model_to_action(value, threshold = 0.6):
    if value > threshold:
        Idiot_Dinosaur.press_up()

def wrap_model(X, parameters, n_x):
    X_adj = re_shape_X(X, n_x)
    action_value = tRex_model(X_adj, parameters).item()
    from_model_to_action(action_value, threshold = 0.6)
