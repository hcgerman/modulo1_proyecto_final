from models.patient import Patient
from models.eye_examination import EyeExamination


class Diagnosis:
    # Funciones para gestionar diagnosis
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
        header = f" DIAGNOSIS REPORT - ID: {self.diagnosis_id} "
        line = "=" * len(header)
        return (
            f"{line}\n"
            f"{header}\n"
            f"{line}\n\n"
            f"  Diagnosis: {self.diagnosis}\n"
            f"  Patient:\n    {self.patient}\n"
            f"  Eye Examination OD:\n    {str(self.eye_examination_od).replace(chr(10), chr(10) + '    ')}\n"
            f"  Eye Examination OS:\n    {str(self.eye_examination_os).replace(chr(10), chr(10) + '    ')}"
        )

    def __repr__(self):
        return self.__str__()
