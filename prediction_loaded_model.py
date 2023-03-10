import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
import cv2
import tensorflow as tf
import warnings
warnings.filterwarnings('ignore')
from keras.models import load_model
#from keras.preprocessing import image
from keras.utils import load_img, img_to_array
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from keras.optimizers import Adam
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import time


image_gen = ImageDataGenerator(rotation_range=25,
                              width_shift_range=0.1,
                              height_shift_range=0.1,rescale=1/255,shear_range=0.2,
                              zoom_range=0.2,horizontal_flip=True,fill_mode='nearest')

image_gen.flow_from_directory("street_view/train_data/train_data")

training_image =image_gen.flow_from_directory("street_view/train_data/train_data", target_size=(224, 224), batch_size=25)

testing_image =image_gen.flow_from_directory("street_view/test_data/test_data", target_size=(224, 224), batch_size=25)

model = load_model('saved_models/vgg19_transfer_learning.h5')


def processing(path):
    img = cv2.imread(path)
    image_dim = np.array(img)
    print(image_dim.shape)
    test1_proc = load_img(path, target_size=(224, 224))
    test1_proc_1 = img_to_array(test1_proc)
    t1 = np.expand_dims(test1_proc, axis=0)
    t1 = t1 / 255
    pred_classes = model.predict(t1)
    pred = np.argmax(pred_classes, axis=1)

    plt.subplot(121)
    pic = Image.open(path)
    plt.xlabel("Original Image")
    plt.imshow(pic)

    plt.subplot(122)

    s1 = pd.Series(pred_classes.ravel(), index=training_image.class_indices.keys())
    s1.plot(kind='bar', figsize=(10, 5))
    plt.xlabel("prediction")

    plt.show()

    pred_classes = pred_classes.tolist()
    pred_classes = str(pred_classes[0])
    pred_classes = pred_classes.replace('[', '').replace(']', '').replace(',', '')
    # percentage = [words for segments in pred_classes for words in segments.split()]
    print(pred_classes)
    x = pred_classes.split()
    print(x)
    class_percentage = {
        'city': 0,
        'coast': 0,
        'field': 0,
        'forest': 0,
        'inconclusive': 0,
        'mountain': 0
    }
    perc_class = 0
    for perc in x:
        if perc_class == 0:
            class_percentage['city'] = float(perc)*100
            perc_class += 1
        elif perc_class == 1:
            class_percentage['coast'] = float(perc)*100
            perc_class += 1
        elif perc_class == 2:
            class_percentage['field'] = float(perc)*100
            perc_class += 1
        elif perc_class == 3:
            class_percentage['forest'] = float(perc)*100
            perc_class += 1
        elif perc_class == 4:
            class_percentage['inconclusive'] = float(perc)*100
            perc_class += 1
        elif perc_class == 5:
            class_percentage['mountain'] = float(perc)*100

    for i in training_image.class_indices:
        if pred == training_image.class_indices[i]:
            print("prediction made by model is :", i, pred)
            return i, class_percentage


image_path = "street_view/predict_data/predict_data/27.9290769,-15.7234258_pano.jpg"
result, percent = processing(image_path)
print(f'Model prediction: {result}, percentage: {percent["city"]}')


def display_image_result(result, image_path):
    image = Image.open(image_path)

    # Create a blank image to draw the headline on
    headline_image = Image.new('RGBA', (image.width, image.height), (255, 255, 255, 0))

    # Get a drawing context
    headline_draw = ImageDraw.Draw(headline_image)

    # Set the font and font size for the headline
    font = ImageFont.truetype("arial.ttf", 36)

    # Set the headline text
    headline_text = result

    # Calculate the x-coordinate for the headline text to be centered
    x_pos = (headline_image.width - headline_draw.textsize(headline_text, font=font)[0]) / 2

    # Draw the headline text onto the headline image
    headline_draw.text((x_pos, 20), headline_text, font=font, fill=(0, 0, 0, 255))

    # Combine the original image and the headline image
    combined_image = Image.alpha_composite(image, headline_image)

    # Show the combined image
    combined_image.show()


# display_image_result(result, image_path)
