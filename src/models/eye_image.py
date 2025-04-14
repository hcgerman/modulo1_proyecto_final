from models.retina import Retina
from models.contours import Contours

class EyeImage:

    def __init__(self, path_retina_contours_image: str):
        self.path_retina_contours_image = path_retina_contours_image
        self.retina_image = None
        self.contours_layer = None

    def add_retina_image(self, retina_image: Retina):
        self.retina_image = retina_image

    def add_contours_layer(self, contours_layer: Contours):
        self.contours_layer = contours_layer

    def update_path_retina_contours_image(self, path_retina_contours_image: str):
        self.path_retina_contours_image =  path_retina_contours_image

    def __str__(self):
        return f"EyeImage: (path_retina_contourns_image='{self.path_retina_contours_image}', retina_image={self.retina_image}, contours_layer={self.contours_layer})"
    
    def __repr__(self):
        return self.__str__()