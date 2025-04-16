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
                self.edit_record()
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

        try:
            diagnosis_id = int(input("ID del diagnóstico: "))
            if any(r.diagnosis_id == diagnosis_id for r in self.records):
                print(
                    f"❌ Ya existe un registro con el ID {diagnosis_id}. No se puede crear duplicado."
                )
                return None

            age = int(input("Edad del paciente: "))
            gender = int(input("Género (0 = masculino, 1 = femenino): "))
            patient = Patient(age, gender)

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

        except ValueError:
            print("❌ Entrada inválida. No se pudo crear el registro.")
            return None

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

    def edit_record(self):
        print("\n" + "=" * 40)
        print("✏️ FUNCIÓN: EDITAR REGISTRO POR ID")
        print("=" * 40)

        if not self.records:
            print("⚠️ No hay registros disponibles.")
            return

        try:
            ids = [r.diagnosis_id for r in self.records]
            print(f"Registros disponibles: {ids}")
            diagnosis_id = int(input("Ingrese el ID del diagnóstico a editar: "))

            for record in self.records:
                if record.diagnosis_id == diagnosis_id:
                    print("\n📌 Registro encontrado:")
                    print(record)

                    confirm = (
                        input("\n¿Desea editar este registro? (s/n): ").strip().lower()
                    )
                    if confirm != "s":
                        print("❎ Edición cancelada.")
                        return

                    # Editar paciente
                    edad = input(f"Edad del paciente [{record.patient.age}]: ").strip()
                    if edad:
                        record.patient.update_age(int(edad))
                    genero = input(
                        f"Género del paciente (0=masculino, 1=femenino) [{record.patient.gender}]: "
                    ).strip()
                    if genero:
                        record.patient.update_gender(int(genero))

                    # Editar tipo de diagnóstico
                    tipo = input(
                        f"Tipo de diagnóstico (0=sano, 1=glaucoma, 2=sospechoso) [{record.diagnosis}]: "
                    ).strip()
                    if tipo:
                        record.update_diagnosis(int(tipo))

                    # Editar examen OD
                    print("\n=== Editar datos de OD (ojo derecho) ===")
                    self.edit_eye_examination(record.eye_examination_od)

                    # Editar examen OS
                    print("\n=== Editar datos de OS (ojo izquierdo) ===")
                    self.edit_eye_examination(record.eye_examination_os)

                    print("\n✅ Registro editado correctamente.")
                    return

            print("❌ No se encontró ningún registro con ese ID.")
        except ValueError:
            print("❌ Entrada inválida. Debe ser un número.")

    def edit_eye_examination(self, exam):
        def is_valid_file(path, ext):
            return os.path.exists(path) and path.lower().endswith(ext)

        campos = [
            ("Dioptría 1", exam.dioptre_1, exam.update_dioptre_1),
            ("Dioptría 2", exam.dioptre_2, exam.update_dioptre_2),
            ("Astigmatismo", exam.astigmatism, exam.update_astigmatism),
            (
                "Phakic/Pseudophakic (0/1)",
                exam.phakic_pseudophakic,
                exam.update_phakic_pseudophakic,
            ),
            ("Presión neumática", exam.pneumatic, exam.update_pneumatic),
            ("Presión Perkins", exam.perkins, exam.update_perkins),
            ("Paquimetría", exam.pachymetry, exam.update_pachymetry),
            ("Longitud axial", exam.axial_length, exam.update_axial_length),
            ("Defecto medio (VF_MD)", exam.vf_md, exam.update_vf_md),
        ]

        for label, actual, update_func in campos:
            nuevo_valor = input(f"{label} [{actual}]: ").strip()
            if nuevo_valor:
                update_func(
                    float(nuevo_valor)
                    if "." in nuevo_valor or "e" in nuevo_valor.lower()
                    else int(nuevo_valor)
                )

        print("\n=== Editar imagen de retina ===")
        retina = exam.eye_image.retina_image
        retina_path = input(
            f"Ruta imagen retina [{retina.path_retina_image}]: "
        ).strip()
        if retina_path:
            if is_valid_file(retina_path, ".jpg"):
                retina.update_path_retina_image(os.path.normpath(retina_path))
            else:
                print(
                    "⚠️ Ruta no válida o formato incorrecto. Se mantiene el archivo actual."
                )

        print("\n=== Editar contornos ===")
        contours = exam.eye_image.contours_layer
        cup1 = input(f"Ruta CUP EXP1 [{contours.path_retina_cup_exp1}]: ").strip()
        if cup1:
            if is_valid_file(cup1, ".txt"):
                contours.update_path_retina_cup_exp1(os.path.normpath(cup1))
            else:
                print(
                    "⚠️ Ruta no válida o formato incorrecto. Se mantiene el archivo actual."
                )
        cup2 = input(f"Ruta CUP EXP2 [{contours.path_retina_cup_exp2}]: ").strip()
        if cup2:
            if is_valid_file(cup2, ".txt"):
                contours.update_path_retina_cup_exp2(os.path.normpath(cup2))
            else:
                print(
                    "⚠️ Ruta no válida o formato incorrecto. Se mantiene el archivo actual."
                )
        disc1 = input(f"Ruta DISC EXP1 [{contours.path_retina_disc_exp1}]: ").strip()
        if disc1:
            if is_valid_file(disc1, ".txt"):
                contours.update_path_retina_disc_exp1(os.path.normpath(disc1))
            else:
                print(
                    "⚠️ Ruta no válida o formato incorrecto. Se mantiene el archivo actual."
                )
        disc2 = input(f"Ruta DISC EXP2 [{contours.path_retina_disc_exp2}]: ").strip()
        if disc2:
            if is_valid_file(disc2, ".txt"):
                contours.update_path_retina_disc_exp2(os.path.normpath(disc2))
            else:
                print(
                    "⚠️ Ruta no válida o formato incorrecto. Se mantiene el archivo actual."
                )

        print("\n=== Editar imagen con contornos superpuestos ===")
        path_contours_img = input(
            f"Ruta imagen contornos [{exam.eye_image.path_retina_contours_image}]: "
        ).strip()
        if path_contours_img:
            if is_valid_file(path_contours_img, ".jpg"):
                exam.eye_image.update_path_retina_contours_image(
                    os.path.normpath(path_contours_img)
                )
            else:
                print(
                    "⚠️ Ruta no válida o formato incorrecto. Se mantiene el archivo actual."
                )
