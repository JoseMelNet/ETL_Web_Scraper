
import yaml

# Variable global
__config = None    # Nos sirve para cachear nuestra configuracion, para no estar leyendo la configracion desde el disco

# La función config() lee el archivo config.yaml y retorna un diccionario con los 
# elementos de configuración.
# El archivo config.yaml contiene los datos de las webs a scrapear
def config():
    global __config
    if not __config:
        with open('config.yaml', mode='r') as f:
            __config = yaml.safe_load(f)
    
    return __config


