import numpy as np
import PIL.Image as Image
from flask import current_app
from app import app  

with app.app_context():  # Crea el contexto de aplicación
    app_dir = current_app.root_path
    image_path = app_dir + '/img/cilantro.jpg'
    image = Image.open(image_path)
    image_variable = image

    def img_to_vector(img):
        image_vector = np.array(img)
        print(image_vector)
