# from utils import convert_xls_to_df, add_diagnosises_os
# import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import pandas as pd
from pathlib import Path

from models.Diagnosis import Diagnosis
from models.Patient import Patient
from models.Retina import Retina
from models.contours import Contours
from models.eye_examination import EyeExamination
from models.eye_image import EyeImage


def show_image(path_image):
    """
    Muestra una imagen en una ventana emergente.

    :param path_image: Ruta de la imagen a mostrar.
    """
    img = mpimg.imread(path_image)
    plt.imshow(img)
    plt.axis("off")
    plt.show()


def create_eye_examination() -> EyeExamination:
    dioptre_1 = float(input("Dioptría 1: "))
    dioptre_2 = float(input("Dioptría 2: "))
    astigmatism = float(input("Astigmatismo: "))
    phakic_pseudophakic = int(input("¿Fáquico (0) o Pseudo-fáquico (1)?: "))
    pneumatic = float(input("Presión neumática: "))
    perkins = float(input("Presión Perkins: "))
    pachymetry = float(input("Paquimetría: "))
    axial_length = float(input("Longitud axial: "))
    vf_md = float(input("Defecto medio (VF_MD): "))

    exam = EyeExamination(
        dioptre_1,
        dioptre_2,
        astigmatism,
        phakic_pseudophakic,
        pneumatic,
        perkins,
        pachymetry,
        axial_length,
        vf_md,
    )

    print("\n=== Imágenes del ojo ===")
    path_retina_image = input("Ruta de la imagen de retina (.jpg): ").strip()
    path_retina_image = os.path.normpath(path_retina_image)
    retina = Retina(path_retina_image)

    print("Archivos de contornos (formato .txt):")
    cup_exp1 = os.path.normpath(input("Ruta CUP EXP1: ").strip())
    cup_exp2 = os.path.normpath(input("Ruta CUP EXP2: ").strip())
    disc_exp1 = os.path.normpath(input("Ruta DISC EXP1: ").strip())
    disc_exp2 = os.path.normpath(input("Ruta DISC EXP2: ").strip())
    contours = Contours(cup_exp1, cup_exp2, disc_exp1, disc_exp2)

    path_retina_contours_image = os.path.normpath(
        input("Ruta de la imagen con contornos superpuestos (.jpg): ").strip()
    )
    eye_image = EyeImage(path_retina_contours_image)
    eye_image.add_retina_image(retina)
    eye_image.add_contours_layer(contours)

    exam.add_eye_image(eye_image)

    return exam


def create_record():
    print("\n--- Crear nuevo registro ---")

    # Paciente
    age = int(input("Edad del paciente: "))
    gender = int(input("Género (0 = masculino, 1 = femenino): "))
    patient = Patient(age, gender)

    # Diagnóstico
    diagnosis_id = int(input("ID del diagnóstico: "))
    diagnosis_type = int(
        input("Tipo de diagnóstico (0 = sano, 1 = glaucoma, 2 = sospechoso): ")
    )
    diagnosis = Diagnosis(diagnosis_id, diagnosis_type)
    diagnosis.add_patient(patient)

    # Examen OD y OS
    print("\n=== Datos para OD (ojo derecho) ===")
    exam_od = create_eye_examination()
    diagnosis.add_eye_examination_od(exam_od)

    print("\n=== Datos para OS (ojo izquierdo) ===")
    exam_os = create_eye_examination()
    diagnosis.add_eye_examination_os(exam_os)

    return diagnosis


def mostrar_menu():
    print("\n=== Menú de Gestión de Registros ===")
    print("1. Crear registro")
    print("2. Editar registro")
    print("3. Buscar registro")
    print("4. Visualizar registros")
    print("5. Eliminar registro")
    print("6. Salir")


def main():
    records = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            record = create_record()
            records.append(record)
            print("\nRegistro creado exitosamente.")
        elif opcion == "2":
            print("Función: Editar registro")
            # Aquí irá tu lógica para editar un registro
        elif opcion == "3":
            print("Función: Buscar registro")
            # Aquí irá tu lógica para buscar un registro
        elif opcion == "4":
            print("Función: Visualizar registros")
            # Aquí irá tu lógica para mostrar todos los registros
        elif opcion == "5":
            print("Función: Eliminar registro")
            # Aquí irá tu lógica para eliminar un registro
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

    print("\n=== Registros creados ===")
    for record in records:
        print(record)


if __name__ == "__main__":
    main()
