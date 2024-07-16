import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
os.environ['TF_KERAS'] = '1'

import tensorflow as tf
import keras
import numpy as np

print(keras.__version__)

model_weights_dir = 'models\model_nn_weights.h5'

print(model_weights_dir)

# Create the model
model_nn = keras.models.Sequential([
    keras.layers.InputLayer((1200,)),
    keras.layers.Dense(8, activation="relu"),
    keras.layers.Dense(8, activation="relu"),
    keras.layers.Dense(5, activation="softmax"),
])

# 2. Compile the model
model_nn.compile(loss=keras.losses.SparseCategoricalCrossentropy(),
                 optimizer=keras.optimizers.Adam(),
                 metrics=["accuracy"])

model_nn.load_weights(model_weights_dir)

input = tf.expand_dims(tf.zeros(1200), axis=0)
print(input)

pred = model_nn.predict(input)

print(pred[0])