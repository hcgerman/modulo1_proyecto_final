import Patient
import EyeExamination

class Diagnosis:

    def __init__(self, diagnosis_id: int, diagnosis: int):
        self.diagnosis_id = diagnosis_id
        self.diagnosis = diagnosis
        self.patient = None
        self.eye_examination_od = None
        self.eye_examination_os = None

    def add_patient(self, patient: Patient):
        self.patient = patient    

    def add_eye_examination_od(self, eye_od: EyeExamination):
        self.eye_examination_od = eye_od

    def add_eye_examination_os(self, eye_os: EyeExamination):
        self.eye_examination_os = eye_os

    def update_diagnosis(self, diagnosis: int):
        self.diagnosis = diagnosis
