class Conductor:
    def __init__(self,nombre,licencia):
        __edad = 18
        __categoria = "novato"
        __puntos = 10
        
        self.__nombre = nombre
        self.__licencia = licencia
        self.__edad = __edad
        self.disponible = True
        self.__categoria = __categoria
        self.__puntos = __puntos

    def getNombre(self):
        return self.__nombre
    def getLicencia(self):
        return self.__licencia
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setLicencia(self,licencia):
        self.__licencia = licencia

    def toString(self):
        return "Nombre: " + self.__nombre + "Licencia: " + self.__licencia
    def __cambiar_categoria(self, categoria):
        self.__categoria = categoria
    def subir_puntos(self):
        self.__puntos = self.__puntos - 1 
    def bajar_puntos(self):
        self.__puntos = self.__puntos + 1
    def get_info(self):
        return "datos del conductor: " + self.getNombre() + " " +  str(self.getLicencia()) + " Puntos: " + str(self.__puntos)
        
    





