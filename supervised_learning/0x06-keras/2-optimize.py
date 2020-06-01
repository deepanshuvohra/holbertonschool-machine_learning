#!/usr/bin/env python3
"""
Sets up Adam optimization for a keras model with categorical crossentropy
loss and accuracy metrics
"""
import tensorflow.keras as K


def optimize_model(network, alpha, beta1, beta2):
    """
    a function that set ups Adam optimization with Keras
    :param network: the model to optimize
    :param alpha: the learning rate
    :param beta1: the first Adam optimizer parameter
    :param beta2: the second Adam optimizer parameter
    :return: None
    """
    opt = K.optimizers.Adam(lr=alpha, beta_1=beta1, beta_2=beta2)
    network.compile(optimizer=opt, loss='categorical_crossentropy',
                    metrics=['accuracy'])
    return None
