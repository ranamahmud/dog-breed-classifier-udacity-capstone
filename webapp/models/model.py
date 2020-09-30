
import pickle
from tensorflow.keras.models import load_model
from keras import backend
from models.utils import face_detector, dog_detector, Resnet50_predict_breed

from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D, Dense
from keras.models import Sequential


def predict_human_dog(img_path):
    # detect human face or dog
    #     face_detector and dog_detector
    # if dog return dog breed
    backend.clear_session()
    # have to try with model trained
    model = Sequential()
    model.add(GlobalAveragePooling2D(input_shape=(1, 1, 2048)))
    model.add(Dense(133, activation='softmax'))
    model.load_weights('models/saved_models/weights.best.Resnet50.hdf5')

    if dog_detector(img_path) == True:
        dog_breed = Resnet50_predict_breed(img_path, model)
        return ("dog", dog_breed)
    # if human return resembling dog breed
    elif face_detector(img_path) == True:
        dog_breed = Resnet50_predict_breed(img_path, model)
        return ("human", dog_breed)
    else:
        return False
