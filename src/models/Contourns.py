class Contourns:

    def __init__(self, retina_cup_exp1: str, retina_cup_exp2: str, retina_disc_exp1: str, retina_disc_exp2: str):
        self.path_retina_cup_exp1 = retina_cup_exp1
        self.path_retina_cup_exp2 = retina_cup_exp2
        self.path_retina_disc_exp1 = retina_disc_exp1
        self.path_retina_disc_exp2 = retina_disc_exp2

    def update_path_retina_cup_exp1(self, retina_cup_exp1: str):
        self.path_retina_cup_exp1 = retina_cup_exp1

    def update_path_retina_cup_exp2(self, retina_cup_exp2: str):
        self.path_retina_cup_exp2 = retina_cup_exp2

    def update_path_retina_disc_exp1(self, retina_disc_exp1: str):
        self.path_retina_disc_exp1 = retina_disc_exp1

    def update_path_retina_disc_exp2(self, retina_disc_exp2: str):
        self.path_retina_disc_exp2 = retina_disc_exp2