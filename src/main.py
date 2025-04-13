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
    path_image = "data/RET293OD.jpg"
    
    # Llamar a la función para mostrar la imagen
    show_image(path_image)