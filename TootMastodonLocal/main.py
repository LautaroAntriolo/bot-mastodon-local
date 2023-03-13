def funcionViernes(mje, *args):
    Toot.video(f'''{mje}''','TootMastodonLocal/video/viernes/graciasADiosEsViernes.mp4',*args)  

def funcionDiaria(mje,dia,nombreImagen, *args):
    Toot.imagen(f'{mje}', f'TootMastodonLocal/img/{dia}/{nombreImagen}.jpg',*args)


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
        return f'faltan 5 días para el Viernes.'
    elif posicionDeHoy == 2: # martes
        return f'faltan 4 días para el Viernes.'
    elif posicionDeHoy == 3: #Miercoles
        return f'A cortar la semanaa! Solo faltan 3 días para el Viernes.'
    elif posicionDeHoy == 4: # Jueves
        return f'Ya casi estamoss. Solo faltan 2 días para el Viernes.'
    elif posicionDeHoy == 6: # Sabado
        return f'Paso {abs(5-posicionDeHoy)} día viernes, ya volvera...'
    elif posicionDeHoy == 7: # Domingo
        return f'Pasaron {abs(5-posicionDeHoy)} días del viernes, hoy es Domingo de recuperación.'

if __name__=="__main__":
    from datetime import datetime
    import Toot
    import random
    mensajedeldia = mensajeSegunElDia()
    quediaes = diaDeHoy()
    print(quediaes)
    if quediaes == 'viernes':
        funcionViernes(mensajedeldia, 'viernes','Friday','shrek')
    elif quediaes == 'lunes':
        funcionDiaria(mensajedeldia,quediaes.capitalize(),f'{quediaes}{random.randint(1,4)}',quediaes, quediaes.capitalize())