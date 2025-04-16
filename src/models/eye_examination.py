from models.eye_image import EyeImage


class EyeExamination:
    # Funciones para gestionar EyeExamination
    def __init__(
        self,
        dioptre_1: float,
        dioptre_2: float,
        astigmatism: float,
        phakic_pseudophakic: int,
        pneumatic: float,
        perkins: float,
        pachymetry: float,
        axial_length: float,
        vf_md: float,
    ):
        self.dioptre_1 = dioptre_1
        self.dioptre_2 = dioptre_2
        self.astigmatism = astigmatism
        self.phakic_pseudophakic = phakic_pseudophakic
        self.pneumatic = pneumatic
        self.perkins = perkins
        self.pachymetry = pachymetry
        self.axial_length = axial_length
        self.vf_md = vf_md
        self.eye_image = None

    def add_eye_image(self, eye_image: EyeImage):
        self.eye_image = eye_image

    def update_dioptre_1(self, dioptre_1: float):
        self.dioptre_1 = dioptre_1

    def update_dioptre_2(self, dioptre_2: float):
        self.dioptre_2 = dioptre_2

    def update_astigmatism(self, astigmatism: float):
        self.astigmatism = astigmatism

    def update_phakic_pseudophakic(self, phakic_pseudophakic: int):
        self.phakic_pseudophakic = phakic_pseudophakic

    def update_pneumatic(self, pneumatic: float):
        self.pneumatic = pneumatic

    def update_perkins(self, perkins: float):
        self.perkins = perkins

    def update_pachymetry(self, pachymetry: float):
        self.pachymetry = pachymetry

    def update_axial_length(self, axial_length: float):
        self.axial_length = axial_length

    def update_vf_md(self, vf_md: float):
        self.vf_md = vf_md

    def __str__(self):
        return (
            f"EyeExamination:\n"
            f"  Dioptre 1: {self.dioptre_1}\n"
            f"  Dioptre 2: {self.dioptre_2}\n"
            f"  Astigmatism: {self.astigmatism}\n"
            f"  Phakic/Pseudophakic: {self.phakic_pseudophakic}\n"
            f"  Pneumatic: {self.pneumatic}\n"
            f"  Perkins: {self.perkins}\n"
            f"  Pachymetry: {self.pachymetry}\n"
            f"  Axial Length: {self.axial_length}\n"
            f"  VF MD: {self.vf_md}\n"
            f"  Eye Image:\n    {str(self.eye_image).replace(chr(10), chr(10) + '    ')}"
        )

    def __repr__(self):
        return self.__str__()
