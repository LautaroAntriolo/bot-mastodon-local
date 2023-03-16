def funcionViernes(mje, *args):
    Toot.video(f'''{mje}''','TootMastodonLocal/video/viernes/graciasADiosEsViernes.mp4',*args)  

def funcionDiaria(mje,dia,nombreImagen, *args):
    Toot.imagen(f'{mje}', f'TootMastodonLocal/img/{dia}/{nombreImagen}',*args)

def cantImagenes(dia):
    carpeta = f'C:/Lautaro/Python-personal/Mastodon/TootMastodonLocal/img/{dia.capitalize()}'
    extensiones_permitidas = ('.jpg', '.jpeg', '.png', '.gif')

    cantidad_imagenes = len([nombre_archivo for nombre_archivo in os.listdir(carpeta)
                        if nombre_archivo.endswith(extensiones_permitidas)])
    return cantidad_imagenes

def nombreImagenes(dia):
    import os
    carpeta =f'C:/Lautaro/Python-personal/Mastodon/TootMastodonLocal/img/{dia.capitalize()}'
    nombres_archivos = os.listdir(carpeta)
    return nombres_archivos

nameDias ={
        'lunes':1,
        'martes':2,
        'miercoles':3,
        'jueves':4,
        'viernes':5,
        'sabado':6,
        'domingo':7
    }
def diaDeHoy():
    dia = datetime.now().weekday()
    return list(nameDias.keys())[dia]


def mensajeSegunElDia():
    posicionDeHoy = nameDias[diaDeHoy()]
    if posicionDeHoy == 5:
        return "¡Es hoy! Gracias a Dios es Vierness"
    elif posicionDeHoy == 1: # Lunes
        return f'faltan 4 días para el Viernes.'
    elif posicionDeHoy == 2: # martes
        return f'faltan 3 días para el Viernes.'
    elif posicionDeHoy == 3: #Miercoles
        return f'A cortar la semanaa! Solo faltan 2 días para el Viernes.'
    elif posicionDeHoy == 4: # Jueves
        return f'Ya casi estamoss. Solo faltan 1 días para el Viernes.'
    elif posicionDeHoy == 6: # Sabado
        return f'Ya paso el viernes,¿Cuándo vuelvee...?'
    elif posicionDeHoy == 7: # Domingo
        return f'Hoy es Domingo de recuperación...'

if __name__=="__main__":
    import os
    from datetime import datetime
    import Toot
    import random
    mensajedeldia = mensajeSegunElDia()
    quediaes = diaDeHoy()
    nombreArchivos = nombreImagenes(quediaes)
    print(quediaes)
    if quediaes == 'viernes':
        funcionViernes(mensajedeldia, 'viernes','Friday','shrek')
    else:
        funcionDiaria(mensajedeldia,quediaes.capitalize(),f'{random.choice(nombreArchivos)}',quediaes, quediaes.capitalize())