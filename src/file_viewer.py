import os

import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class FileViewer:
    @staticmethod
    def mostrar(path, tipo):
        if tipo == "image":
            FileViewer._mostrar_imagen(path)
        elif tipo == "text":
            FileViewer._mostrar_texto(path)

    @staticmethod
    def _mostrar_imagen(path):
        try:
            img = mpimg.imread(path)
            plt.imshow(img)
            plt.axis("off")
            plt.title(os.path.basename(path))
            plt.show()
        except Exception as e:
            print(f"❌ Error al mostrar imagen: {e}")

    @staticmethod
    def _mostrar_texto(path, lines_per_page=40):
        try:
            with open(path, "r", encoding="utf-8") as f:
                lineas = f.readlines()
        except Exception as e:
            print(f"❌ Error al leer archivo de texto: {e}")
            return

        total_lineas = len(lineas)
        paginas = (total_lineas + lines_per_page - 1) // lines_per_page
        for i in range(paginas):
            contenido = "".join(lineas[i * lines_per_page : (i + 1) * lines_per_page])

            fig, ax = plt.subplots(figsize=(10, 6))
            ax.axis("off")
            plt.title(
                f"{os.path.basename(path)} (Página {i + 1}/{paginas})",
                fontsize=10,
                pad=10,
            )
            plt.text(0.01, 0.99, contenido, fontsize=10, family="monospace", va="top")

            plt.tight_layout()
            plt.show()

            if i < paginas - 1:
                continuar = input(
                    "Presione Enter para ver la siguiente página, o 'q' para salir: "
                )
                if continuar.lower() == "q":
                    break
