import os
import time
import subprocess
from threading import Thread
import tensorflow as tf
from tensorflow.keras import optimizers, layers, models
import numpy as np


BATCH_SIZE = 4
HIDDEN_LAYERS = 2
HIDDEN_LAYER_KERNELS = 4
DATASET_SIZE = 2048
DATA_SHAPE = (256, 256, 3)

model = models.Sequential()
model.add(layers.Conv2D(HIDDEN_LAYER_KERNELS, (3, 3), activation='relu', input_shape=DATA_SHAPE, strides=(1, 1), padding="same"))
model.add(layers.MaxPooling2D((2, 2), strides=(1, 1), padding="same"))
for _ in range(HIDDEN_LAYERS):
    model.add(layers.Conv2D(HIDDEN_LAYER_KERNELS, (5, 5), activation='relu', strides=(1, 1), padding="same"))
    model.add(layers.MaxPooling2D((5, 5), strides=(1, 1), padding="same"))

model.add(layers.Conv2D(2, (DATA_SHAPE[0] // 8, DATA_SHAPE[1] // 8), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))

model.summary()

X = np.ones((DATASET_SIZE, *DATA_SHAPE))
y = np.ones((DATASET_SIZE, 10))
data = tf.data.Dataset.from_tensor_slices((X, y))
data = data.batch(BATCH_SIZE)

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
loss=tf.keras.losses.BinaryCrossentropy())

model.fit(data, epochs=1000)
