from models.patient import Patient
from models.eye_examination import EyeExamination

class Diagnosis:
    #Funciones para gestionar diagnosis del paciente
    def __init__(self, diagnosis_id: int, diagnosis: int):
        self.diagnosis_id = diagnosis_id
        self.diagnosis = diagnosis
        self.patient = None
        self.eye_examination_od = None
        self.eye_examination_os = None

    def add_patient(self, patient: Patient):
        self.patient = patient    

    def add_eye_examination_od(self, eye_examination_od: EyeExamination):
        self.eye_examination_od = eye_examination_od

    def add_eye_examination_os(self, eye_examination_os: EyeExamination):
        self.eye_examination_os = eye_examination_os

    def update_diagnosis(self, diagnosis: int):
        self.diagnosis = diagnosis

    def __str__(self):
        return f'Diagnosis: (diagnosis_id: {self.diagnosis_id}, diagnosis: {self.diagnosis}, patient: {self.patient}, eye_examination_od: {self.eye_examination_od}, eye_examination_os: {self.eye_examination_os})'

    def __repr__(self):
        return self.__str__()