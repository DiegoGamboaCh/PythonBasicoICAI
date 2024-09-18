import conductor as drv

if __name__ == '__main__':
        
    ana  = drv.Conductor('Ana Maria',888888)
    luis = drv.Conductor('Luis Eduardo',7777777)
    juan = drv.Conductor("Juan Felipe",9999999)
    
    juan.subir_puntos()
    juan.disponible = False
    
    juan.__nombre = 10
    juan.__cambiar_categoria = 'experto' 

    print(ana.get_info())
     

     

