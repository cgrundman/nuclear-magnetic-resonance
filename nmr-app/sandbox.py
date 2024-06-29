import tensorflow as tf

from tensorflow import keras

model_dir = "models\model_nn.keras"
model = keras.models.load_model(model_dir)
