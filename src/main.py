from utils import convert_xls_to_df, add_diagnosises_os
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def show_image(path_image):
    """
    Muestra una imagen en una ventana emergente.
    
    :param path_image: Ruta de la imagen a mostrar.
    """
    img = mpimg.imread(path_image)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    # Ruta de la imagen a mostrar
    path_image = 'data/load_data/FundusImages/RET007OS.jpg'
    # path_image = 'data/load_data/ExpertsSegmentations/Contours/RET002OD_disc_exp1.txt'
    
    # Llamar a la función para mostrar la imagen
    show_image(path_image)
    # load_data()