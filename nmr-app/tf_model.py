import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
os.environ['TF_KERAS'] = '1'

import tensorflow as tf
import keras

def load_pattern_search():

    model_weights_dir = 'models\model_nn_weights.h5'

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

    return model_nn

def predict(model, input):

    input = tf.expand_dims(tf.convert_to_tensor(input), axis=0)

    pred = model.predict(input)
    pred = pred[0]

    return pred