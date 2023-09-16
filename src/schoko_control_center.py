# File:        schoko_control_center.py
# Description: Basic streamlit app for using a pre-trained computer vision model
# Author:      Thomas Bulka <thomas.bulka@capgemini.com>
# Last Change: 2023/09/16

# === Import external packages ===

# Streamlit can be used to build tiny web apps in an easy manner
import streamlit as st

# TensorFlow is the deep learning framework we use for image prediction
import tensorflow as tf

# NumPy is used for efficient array operations
import numpy as np

# Pandas allows tabular data representation
import pandas as pd

# PIL provides functions for image manipulation
from PIL import Image, ImageOps

# Regular expressions are needed to clean class names
import re


# === Code block: Loading the TensorFlow model ===
def load_tensorflow_model():
    # Load the model and the labels of the classes
    # Note: In the current implementation the model is expected to be located
    # in the folder ../model/ relative to the folder we start the web app from
    #
    # The files keras_model.h5 and labels.txt are part of the exported model
    # and can easily be copied to the /model/ folder
    model = tf.keras.models.load_model('../model/keras_model.h5', compile=False)
    class_names = open('../model/labels.txt', 'r').readlines()

    return model, class_names


# === Code block: Make a prediction ===
def predict_image_class(input_image, model, class_names):
    # Create the array which is supposed to hold the image data -
    # note, that the first dimension indicates, that we only feed one
    # image at a time to the prediction process
    input_array = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Reformat the input image
    proc_image = input_image.convert('RGB')
    size = (224, 224)
    proc_image = ImageOps.fit(proc_image, size, Image.Resampling.LANCZOS)

    # The image is converted to a regular NumPy array, since we work with
    # numerical representations only
    image_array = np.asarray(proc_image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array which will be fed to TensorFlow
    input_array[0] = normalized_image_array

    # Execute the prediction
    prediction = model.predict(input_array)

    # Prepare the results
    # We want the probabilities of all classes the model can distinguish
    probability_dict = {'Class': class_names,
                        'Probability': prediction[0]}
    probability_df = pd.DataFrame.from_dict(data=probability_dict)

    # We want to find out the most likely class
    index = np.argmax(prediction)
    class_name = re.findall('[a-zA-Z]+', class_names[index])[0]

    # The confidence score of the most likely prediction
    confidence_score = prediction[0][index]

    return probability_df, class_name, confidence_score


# === Code block: Implementation of the Streamlit app ===
# We set a title for our app
st.set_page_config(layout="wide")
st.title('Schokoladenfabrik Control Center')

# Load the trained model upon startup
model_load_state = st.text('Loading model...')
model, class_names = load_tensorflow_model()
model_load_state.text('Loading model...done!')

# We organize our app in two columns
col1, col2 = st.columns(2)

# Define a file uploader which loads and shows image files in column 1
with col1:
    st.header('Load Suspicious Product')
    image_file = st.file_uploader('Upload image file...', type=['png', 'jpg', 'jpeg'])

    st.header('Suspicious Product')
    if image_file is not None:
        image = Image.open(image_file)
        image_width = st.slider('Image Width', 100, 600, 350)
        st.image(image, width=image_width)

# Implement a button which executes the prediction and shows the prediction
# results
with col2:
    st.header('Prediction Control')

    # We can control, when we consider the model's confidence as "confident enough"
    threshold = st.slider('Necessary confidence', 0, 100, 60)
    button_state =  st.button('Execute prediction')

    # Below, we show the prediction results
    st.header('Prediction Results')
    if button_state:
        probability_df, prediction, confidence_score = predict_image_class(image, model, class_names)
        
        st.subheader('Class Probabilities')
        st.dataframe(probability_df)
    
        st.subheader('Identified Result')
        if (confidence_score * 100) >= threshold:
            st.write('Input data has been classified as: ' + prediction)
        else:
            st.write('Input data could not been automatically classified')
