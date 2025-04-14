import EyeImage

class EyeExamination:

    def __init__(self, dioptre_1: float, dioptre_2: float, astigmatism: int, phakic_pseudophakic: int, pneumatic: int, perkins: int, pachymetry: int, axial_length: float, vf_md: float):
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
        self.eye_image_os = eye_image

    def update_dioptre_1(self, dioptre_1: float):
        self.dioptre_1 = dioptre_1
    
    def update_dioptre_2(self, dioptre_2: float):
        self.dioptre_2 = dioptre_2
    
    def update_astigmatism(self, astigmatism: int):
        self.astigmatism = astigmatism
    
    def update_phakic_pseudophakic(self, phakic_pseudophakic: int):
        self.phakic_pseudophakic = phakic_pseudophakic
    
    def update_pneumatic(self, pneumatic: int):
        self.pneumatic = pneumatic
    
    def update_perkins(self, perkins: int):
        self.perkins = perkins
    
    def update_pachymetry(self, pachymetry: int):
        self.pachymetry = pachymetry
    
    def update_axial_length(self, axial_length: float):
        self.axial_length = axial_length
    
    def update_vf_md(self, vf_md: float):
        self.vf_md = vf_md