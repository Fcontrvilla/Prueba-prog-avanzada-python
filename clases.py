
from abc import abstractmethod, ABC
class Anuncio:
    def __init__(self, ancho, alto, url_archivo, url_click, sub_tipo)
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_click = url_click
        self.__sub_tipo = sub_tipo

    #----------geter
    @property
    def ancho(self):
        return self.__ancho
    #setter
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho

    #----------geter
    @property
    def alto(self):
        return self.__alto
    #setter
    @alto.setter
    def alto(self, alto):
        self.__alto = alto

    #----------geter
    @property
    def url_archivo(self):
        return self.__url_archivo
    #setter
    @url_archivo.setter
    def alto(self, url_archivo):
        self.__url_archivo = url_archivo

    #----------geter
    @property
    def url_click(self):
        return self.__url_click
    #setter
    @url_click.setter
    def url_click(self, url_click):
        self.__url_click = url_click

    #----------geter
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    #setter
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        self.__sub_tipo = sub_tipo

    @staticmethod
    def mostrar_formatos():
        pass

    @abstractmethod
    def comprimir_anuncio():
        pass

    @abstractmethod
    def redimensionar_anuncio():   
        pass





class Campana:
    pass



class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    
    def __init__(self, duracion):
        self.ancho = 1
        self.alto = 1
        self.__duracion = duracion if duracion > 0 else 5

    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion


    def comprimir_anuncio():
        print("Compresion devideo...")

    def redimensionar_anuncio():
        print("Recorte de video no implemetado")



class Display:
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

class Social:
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")