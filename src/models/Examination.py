import EyeImage

class Examination:

    def __init__(self, examination_id: int, age: int, gender: int, diagnosis: int, dioptre_1: float, dioptre_2: float, astigmatism: int, phakic_pseudophakic: int, pneumatic: int, perkins: int, pachymetry: int, axial_length: float, vf_md: float):
        self.examination_id = examination_id = examination_id
        self.age = age
        self.gender = gender
        self. diagnosis = diagnosis
        self.dioptre_1 = dioptre_1
        self.dioptre_2 = dioptre_2
        self.astigmatism = astigmatism
        self.phakic_pseudophakic = phakic_pseudophakic
        self.pneumatic = pneumatic
        self.perkins = perkins
        self.pachymetry = pachymetry
        self.axial_length = axial_length
        self.vf_md = vf_md
        self.eye_image_od = None
        self.eye_image_os = None

    def add_eye_image_contourns_od(self, image_od: EyeImage):
        self.eye_image_od = image_od

    def add_eye_image_contourns_os(self, image_os: EyeImage):
        self.eye_image_os = image_os

    def update_age(self, age: int):
        self.age = age

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