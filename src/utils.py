from models.diagnosis import Diagnosis
from models.patient import Patient
from models.eye_examination import EyeExamination
from models.eye_image import EyeImage
from models.retina import Retina
from models.contours import Contours
import pandas as pd
import os

# Convierte el excel recibido en un DataFrame de pandas
def convert_xls_to_df(path_file: pd.ExcelFile, sheet: str) -> pd.DataFrame:
    df = pd.read_excel(path_file, sheet_name=sheet)
    df_optimazing = optimazing_df(df)
    print(df_optimazing)
    return df_optimazing

# Realiza la limpieza del código ID a formato int y aplica tipo de dato a las columnas del DataFrame
def optimazing_df(df: pd.DataFrame) -> pd.DataFrame:
    df['ID'] = df['ID'].str.replace('#', '').astype('int')
    df['Age'] = df['Age'].astype('Int8')
    df['Gender'] = df['Gender'].astype('category')
    df['Diagnosis'] = df['Diagnosis'].astype('category')
    df['dioptre_1'] = df['dioptre_1'].astype('Float32')
    df['dioptre_2'] = df['dioptre_2'].astype('Float32')
    df['astigmatism'] = df['astigmatism'].astype('Float32')
    df['Phakic/Pseudophakic'] = df['Phakic/Pseudophakic'].astype('category')
    df['Pneumatic'] = df['Pneumatic'].astype('Float32')
    df['Perkins'] = df['Perkins'].astype('Float32')
    df['Pachymetry'] = df['Pachymetry'].astype('Float32')
    df['Axial_Length'] = df['Axial_Length'].astype('Float32')
    df['VF_MD'] = df['VF_MD'].astype('Float32')
    return df

# Carga los datos de patient, diagnosis, EyeExamination (OD), EyeImage (OD), Contours (OD), Retina (OD). De df_entry_od a la lista diagnosises[]
def load_data(df_entry_od: str) -> list:
    try:
        diagnosises = []
        for index, row in df_entry_od.iterrows():
            diagnosis = Diagnosis(
                diagnosis_id=row['ID'],
                diagnosis=row['Diagnosis'],
            )
            patient = Patient(
                age=row['Age'],
                gender=row['Gender']
            )
            diagnosis.add_patient(patient=patient)
            eye_examination = EyeExamination(
                dioptre_1=row['dioptre_1'],
                dioptre_2=row['dioptre_2'],
                astigmatism=row['astigmatism'],
                phakic_pseudophakic=row['Phakic/Pseudophakic'],
                pneumatic=row['Pneumatic'],
                perkins=row['Perkins'],
                pachymetry=row['Pachymetry'],
                axial_length=row['Axial_Length'],
                vf_md=row['VF_MD']
            )
            diagnosis.add_eye_examination_od(eye_examination_od=eye_examination)
            eye_image = EyeImage(
                path_retina_contours_image=os.path.join('..', 'data', 'load_data', 'ExpertsSegmentations', 'ImagesWithContours', f'Opht_cont_RET{row['ID']:03d}OD.jpg'),            
            )
            retina_image = Retina(
                path_retina_image=os.path.join('..', 'data', 'load_data', 'FundusImages', f'RET{row['ID']:03d}OD.jpg')
            )
            contours_layers = Contours(
                path_retina_cup_exp1=os.path.join('..', 'data', 'load_data', 'ExpertsSegmentations', 'Contours', f'RET{row['ID']:03d}OD_cup_exp1.txt'),
                path_retina_cup_exp2=os.path.join('..', 'data', 'load_data', 'ExpertsSegmentations', 'Contours', f'RET{row['ID']:03d}OD_cup_exp2.txt'),
                path_retina_disc_exp1=os.path.join('..', 'data', 'load_data', 'ExpertsSegmentations', 'Contours', f'RET{row['ID']:03d}OD_disc_exp1.txt'),
                path_retina_disc_exp2=os.path.join('..', 'data', 'load_data', 'ExpertsSegmentations', 'Contours', f'RET{row['ID']:03d}OD_disc_exp2.txt')
            )
            eye_examination.add_eye_image(eye_image=eye_image)
            eye_image.add_retina_image(retina_image=retina_image)
            eye_image.add_contours_layer(contours_layer=contours_layers)
            diagnosises.append(diagnosis)
    except Exception as e:
        print(e)
    else: 
        return diagnosises

# Agrega EyeExamination (OS), EyeImage (OS), Contours (OS), Retina (OS). De df_entry_os a la lista diagnosises[]
def add_diagnosises_os(diagnosises: list[Diagnosis], df_entry_os: pd.DataFrame):
    for index, row_os in df_entry_os.iterrows():
        for diagnosis in diagnosises:
            if row_os['ID']==diagnosis.diagnosis_id:
                eye_examination = EyeExamination(
                    dioptre_1=row_os['dioptre_1'],
                    dioptre_2=row_os['dioptre_2'],
                    astigmatism=row_os['astigmatism'],
                    phakic_pseudophakic=row_os['Phakic/Pseudophakic'],
                    pneumatic=row_os['Pneumatic'],
                    perkins=row_os['Perkins'],
                    pachymetry=row_os['Pachymetry'],
                    axial_length=row_os['Axial_Length'],
                    vf_md=row_os['VF_MD']
                )
                diagnosis.add_eye_examination_os(eye_examination_os=eye_examination)
                eye_image = EyeImage(
                    path_retina_contours_image=os.path.join('..', 'data', 'load_data', 'ExpertsSegmentations', 'ImagesWithContours', f'Opht_cont_RET{row_os['ID']:03d}OS.jpg'),            
                )
                retina_image = Retina(
                    path_retina_image=os.path.join('..', 'data', 'load_data', 'FundusImages', f'RET{row_os['ID']:03d}OS.jpg')
                )
                contours_layers = Contours(
                    path_retina_cup_exp1=os.path.join('..', 'data', 'load_data', 'ExpertsSegmentations', 'Contours', f'RET{row_os['ID']:03d}OS_cup_exp1.txt'),
                    path_retina_cup_exp2=os.path.join('..', 'data', 'load_data', 'ExpertsSegmentations', 'Contours', f'RET{row_os['ID']:03d}OS_cup_exp2.txt'),
                    path_retina_disc_exp1=os.path.join('..', 'data', 'load_data', 'ExpertsSegmentations', 'Contours', f'RET{row_os['ID']:03d}OS_disc_exp1.txt'),
                    path_retina_disc_exp2=os.path.join('..', 'data', 'load_data', 'ExpertsSegmentations', 'Contours', f'RET{row_os['ID']:03d}OS_disc_exp2.txt')
                )
                eye_examination.add_eye_image(eye_image=eye_image)
                eye_image.add_retina_image(retina_image=retina_image)
                eye_image.add_contours_layer(contours_layer=contours_layers)

# Carga los datos de los archivos Excel a la Estructura de Clases creada
def load():
    df = convert_xls_to_df(os.path.join('..', 'data', 'load_data', 'ClinicalData', 'diagnosis_data.xlsx'), 'od')
    diagnosises = load_data(df)
    df_os = convert_xls_to_df(os.path.join('..', 'data', 'load_data', 'ClinicalData', 'diagnosis_data.xlsx'), 'os')
    add_diagnosises_os(diagnosises=diagnosises, df_entry_os=df_os)