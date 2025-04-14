import Retina
import Contourns

class EyeImage:

    def __init__(self, path_retina_image: str):
        self.path_retina_image = path_retina_image
        self.retina_image = None
        self.contourns_layer = None

    def add_retina_image(self, retina_image: Retina):
        self.retina_image = retina_image

    def add_contourns_layer(self, contourns_layer: Contourns):
        self.contourns_layer = contourns_layer

    def update_path_retina_contourns_image(self, path_retina_contourns_image: str):
        self.path_retina_contourns_image =  path_retina_contourns_image