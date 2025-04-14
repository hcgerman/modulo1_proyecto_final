class Contours:

    def __init__(self, path_retina_cup_exp1: str, path_retina_cup_exp2: str, path_retina_disc_exp1: str, path_retina_disc_exp2: str):
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
        return f"Contours: (path_retina_cup_exp1='{self.path_retina_cup_exp1}', path_retina_cup_exp2='{self.path_retina_cup_exp2}', path_retina_disc_exp1='{self.path_retina_disc_exp1}', path_retina_disc_exp2='{self.path_retina_disc_exp2}')"
    
    def __repr__(self):
        return self.__str__()