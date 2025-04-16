import os


class Retina:
    # Funciones para gestionar Retina
    def __init__(self, path_retina_image: str):
        self.path_retina_image = path_retina_image

    def update_path_retina_image(self, path_retina_image: str):
        self.path_retina_image = path_retina_image

    def __str__(self):
        return f"Retina: '{os.path.basename(self.path_retina_image)}'"

    def __repr__(self):
        return self.__str__()
