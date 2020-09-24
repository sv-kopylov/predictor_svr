from tensorflow import keras


class ModelKeeper:
    path_to_model = 'model.v0.0.md5'

    def __init__(self):
        self.model = keras.models.load_model(ModelKeeper.path_to_model)

    def predict(self, preprocessed_data):
        return self.model.predict(preprocessed_data)
