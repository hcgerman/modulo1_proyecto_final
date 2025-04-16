import os


class Contours:
    # Funciones para gestionar Contourns
    def __init__(
        self,
        path_retina_cup_exp1: str,
        path_retina_cup_exp2: str,
        path_retina_disc_exp1: str,
        path_retina_disc_exp2: str,
    ):
        self.path_retina_cup_exp1 = path_retina_cup_exp1
        self.path_retina_cup_exp2 = path_retina_cup_exp2
        self.path_retina_disc_exp1 = path_retina_disc_exp1
        self.path_retina_disc_exp2 = path_retina_disc_exp2

    def update_path_retina_cup_exp1(self, path_retina_cup_exp1: str):
        self.path_retina_cup_exp1 = path_retina_cup_exp1

    def update_path_retina_cup_exp2(self, path_retina_cup_exp2: str):
        self.path_retina_cup_exp2 = path_retina_cup_exp2

    def update_path_retina_disc_exp1(self, path_retina_disc_exp1: str):
        self.path_retina_disc_exp1 = path_retina_disc_exp1

    def update_path_retina_disc_exp2(self, path_retina_disc_exp2: str):
        self.path_retina_disc_exp2 = path_retina_disc_exp2

    def __str__(self):
        return (
            f"Contours:\n"
            f"    Cup Exp1: {os.path.basename(self.path_retina_cup_exp1)}\n"
            f"    Cup Exp2: {os.path.basename(self.path_retina_cup_exp2)}\n"
            f"    Disc Exp1: {os.path.basename(self.path_retina_disc_exp1)}\n"
            f"    Disc Exp2: {os.path.basename(self.path_retina_disc_exp2)}"
        )

    def __repr__(self):
        return self.__str__()
