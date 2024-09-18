from conductor import  Conductor

class Tractorista(Conductor):
    ## constructor
    def __init__(self,nombre,licencia,licencia2):
        ## invoca al constructor de clase Conductor
        super().__init__(nombre,licencia)
        __edad = 21  ## redefine el valor de edad
        ## incluye nuevos atributos
        __experiencia = "novato" 
        
        self.__licencia2 = licencia2
        self.__experiencia = __experiencia
        

    def getExperiencia(self):
        return self.__experiencia
    def getLicencia2(self):
        return self.__licencia2
    def setExperiencia(self,experiencia):
        self.__experiencia = experiencia
    def setLicencia2(self,licencia):
        self.__licencia2 = licencia


ana  = Tractorista('Ana Maria',888888,'Trac8888')

ana.subir_puntos()
ana.getLicencia()
ana.getLicencia2()
ana.setLicencia(777777)
print(ana.getLicencia()) 

        

