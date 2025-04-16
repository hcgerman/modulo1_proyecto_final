import os

from app_diagnosis import (
    get_diadnosis_records,
)
from file_viewer import FileViewer
from models.contours import Contours
from models.diagnosis import Diagnosis
from models.eye_examination import EyeExamination
from models.eye_image import EyeImage
from models.patient import Patient
from models.retina import Retina


class DiagnosisCLI:
    def __init__(self):
        self.records = get_diadnosis_records()

    def mostrar_menu(self):
        print("\n=== Menú de Gestión de Registros ===")
        print("1. Crear registro")
        print("2. Editar registro")
        print("3. Buscar registro")
        print("4. Eliminar registro")
        print("5. Salir")

    def run(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción (1-5): ")

            if opcion == "1":
                record = self.create_record()
                self.records.append(record)
                print("=" * 40)
                print("✅ Registro creado exitosamente")
                print("=" * 40)
                print(record)
            elif opcion == "2":
                print("Función: Editar registro")
            elif opcion == "3":
                record = self.search_record()
                if record:
                    print(record)
                    self.menu_visualizar_archivos(record)
            elif opcion == "4":
                self.delete_record()
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, intente nuevamente.")

        print("\n" + "=" * 50)
        print(f"📋 RESUMEN FINAL - TOTAL DE REGISTROS: {len(self.records)}")
        print("=" * 50)

        if self.records:
            for record in self.records:
                print(f"\n🧾 ID de diagnóstico: {record.diagnosis_id}")
        else:
            print("⚠️ No se han creado registros en esta sesión.")

        print("=" * 50)

    def create_record(self):
        print("\n" + "=" * 40)
        print("🆕 FUNCIÓN: CREAR NUEVO REGISTRO")
        print("=" * 40)
        age = int(input("Edad del paciente: "))
        gender = int(input("Género (0 = masculino, 1 = femenino): "))
        patient = Patient(age, gender)

        diagnosis_id = int(input("ID del diagnóstico: "))
        diagnosis_type = int(
            input("Tipo de diagnóstico (0 = sano, 1 = glaucoma, 2 = sospechoso): ")
        )
        diagnosis = Diagnosis(diagnosis_id, diagnosis_type)
        diagnosis.add_patient(patient)

        print("\n=== Datos para OD (ojo derecho) ===")
        diagnosis.add_eye_examination_od(self.create_eye_examination())

        print("\n=== Datos para OS (ojo izquierdo) ===")
        diagnosis.add_eye_examination_os(self.create_eye_examination())

        return diagnosis

    def create_eye_examination(self):
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
        path_retina_image = os.path.normpath(
            input("Ruta de la imagen de retina (.jpg): ").strip()
        )
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

    def search_record(self):
        print("\n" + "=" * 40)
        print("🔍 FUNCIÓN: BUSCAR REGISTRO POR ID")
        print("=" * 40)
        try:
            ids = [r.diagnosis_id for r in self.records]
            print(f"Registros disponibles: {ids}")
            diagnosis_id = int(input("Ingrese el ID del diagnóstico: "))
            for record in self.records:
                if record.diagnosis_id == diagnosis_id:
                    print("\n✅ Registro encontrado:")
                    return record
        except ValueError:
            print("⚠️ Entrada inválida.")

        print("❌ No se encontró ningún registro.")
        return None

    def menu_visualizar_archivos(self, diagnosis):
        archivos = self.listar_archivos_para_visualizar(diagnosis)
        if not archivos:
            print("⚠️ No hay archivos disponibles.")
            return

        while True:
            print("\n📂 Archivos disponibles para visualizar:")
            for idx, (nombre, path, tipo) in enumerate(archivos, start=1):
                print(f"{idx}. {nombre:<25} -> {os.path.basename(path)}")
            print("0. Cancelar")

            try:
                opcion = int(input("Seleccione un archivo para visualizar (número): "))
                if opcion == 0:
                    print("🔙 Visualización finalizada.")
                    break
                elif 1 <= opcion <= len(archivos):
                    _, path, tipo = archivos[opcion - 1]
                    FileViewer.mostrar(path, tipo)
                else:
                    print("❌ Opción fuera de rango.")
            except ValueError:
                print("❌ Entrada inválida. Debe ser un número.")

    def listar_archivos_para_visualizar(self, diagnosis):
        archivos = []
        for lado in ["eye_examination_od", "eye_examination_os"]:
            exam = getattr(diagnosis, lado, None)
            if not exam or not exam.eye_image:
                continue
            eye_img = exam.eye_image
            if eye_img.retina_image:
                archivos.append(
                    (
                        f"Imagen retina {lado[-2:].upper()}",
                        eye_img.retina_image.path_retina_image,
                        "image",
                    )
                )
            if eye_img.contours_layer:
                cont = eye_img.contours_layer
                archivos += [
                    (
                        f"Cup Exp1 {lado[-2:].upper()}",
                        cont.path_retina_cup_exp1,
                        "text",
                    ),
                    (
                        f"Cup Exp2 {lado[-2:].upper()}",
                        cont.path_retina_cup_exp2,
                        "text",
                    ),
                    (
                        f"Disc Exp1 {lado[-2:].upper()}",
                        cont.path_retina_disc_exp1,
                        "text",
                    ),
                    (
                        f"Disc Exp2 {lado[-2:].upper()}",
                        cont.path_retina_disc_exp2,
                        "text",
                    ),
                ]
        return archivos

    def delete_record(self):
        print("\n" + "=" * 40)
        print("🗑️ FUNCIÓN: ELIMINAR REGISTRO POR ID")
        print("=" * 40)

        if not self.records:
            print("⚠️ No hay registros cargados.")
            return

        try:
            ids = [r.diagnosis_id for r in self.records]
            print(f"Registros disponibles: {ids}")
            diagnosis_id = int(input("Ingrese el ID del diagnóstico a eliminar: "))

            for i, record in enumerate(self.records):
                if record.diagnosis_id == diagnosis_id:
                    print("\n📌 Registro encontrado:")
                    print(record)

                    confirm = (
                        input("\n¿Desea eliminar este registro? (s/n): ")
                        .strip()
                        .lower()
                    )
                    if confirm.lower() == "s":
                        del self.records[i]
                        print("✅ Registro eliminado exitosamente.")
                    else:
                        print("❎ Eliminación cancelada.")
                    return

            print("❌ No se encontró ningún registro con ese ID.")
        except ValueError:
            print("❌ Entrada inválida. Debe ser un número.")
