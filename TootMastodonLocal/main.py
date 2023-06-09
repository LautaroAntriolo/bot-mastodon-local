async def post_video(mje,media,Sensitive=False, formato='mp4',visibilidad='public'):
    with open(f'{media}', 'rb') as video_file:
        video_bytes = video_file.read()
    media_dict = masto.media_post(media_file=video_bytes, mime_type=f'video/{formato}')
    media_id = media_dict['id']
    await asyncio.sleep(5) # espera 10 segundos antes de publicar
    masto.status_post(status=f'{mje}', media_ids=[media_id], sensitive=Sensitive, visibility=f'{visibilidad}')

def tendencias(n):
    tendencias = []
    cadena = ''
    for i in range(n):
        tendencias.append(masto.trending_tags(limit=n)[i]['name'])
    cadena += ' #'.join(tendencias)
    return cadena

def registroImagenes(semanaNumero,nombreImagen):
    # nombreImagen = str(nombreImagen)
    if os.path.exists('C:/Lautaro/Python-personal/Mastodon/TootMastodonLocal/registro.json'):
        with open('C:/Lautaro/Python-personal/Mastodon/TootMastodonLocal/registro.json','r') as f:
                data = json.load(f)
                if f'semana {semanaNumero}' in data:
                    # La clave está en el archivo JSON
                    data[f'semana {semanaNumero}'].append(nombreImagen)
                else:
                    # La clave NO está en el archivo JSON
                    print("Entramos acá ehhhh ")
                    data[f'semana {semanaNumero}'] = []
                    data[f'semana {semanaNumero}'].append(nombreImagen)
        with open('C:/Lautaro/Python-personal/Mastodon/TootMastodonLocal/registro.json', 'w') as f:
            json.dump(data, f)
    else:
        data = {}
        with open('C:/Lautaro/Python-personal/Mastodon/TootMastodonLocal/registro.json', 'w') as f: 
            data[f'semana {semanaNumero}'] = [nombreImagen]
            json.dump(data, f)
    

def post_imagen(mje,media,Sensitive=False,formato='jpg',visibilidad='public'):
   
    media_dict = masto.media_post(media_file={media}, mime_type=f'image/{formato}')
    media_id = media_dict['id']
    masto.status_post(status=f'{mje}', media_ids=[media_id], sensitive=Sensitive, visibility=visibilidad)

def video(mje,media,*args):
    numerales = ''
    for arg in args:
        numerales += f'#{arg} '
    asyncio.run(post_video(f'''{mje}
{numerales}''', f'{media}'))

def imagen(mje,media,*args):
    numerales = ''
    for arg in args:
        numerales += f'#{arg} '
    print(media, type(media))
    post_imagen(f'''{mje} {numerales}''', media)


def funcionDiaria(mje,dia,nombreImagen, *args):
    imagen(f'{mje}', f'TootMastodonLocal/img/{dia}/{nombreImagen}',*args)

def cantImagenes(dia):
    carpeta = f'C:/Lautaro/Python-personal/Mastodon/TootMastodonLocal/img/{dia.capitalize()}'
    extensiones_permitidas = ('.jpg', '.jpeg', '.png', '.gif')

    cantidad_imagenes = len([nombre_archivo for nombre_archivo in os.listdir(carpeta)
                        if nombre_archivo.endswith(extensiones_permitidas)])
    return cantidad_imagenes

def nombreImagenes(dia):
    import os
    carpeta =f'C:/Lautaro/Python-personal/Mastodon/TootMastodonLocal/img/{dia.capitalize()}/'
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
    dia = datetime.datetime.now().weekday()
    return list(nameDias.keys())[dia]


def mensajeSegunElDia():
    posicionDeHoy = nameDias[diaDeHoy()]
    if posicionDeHoy == 5:
        return "Gracias a Dios es Vierness"
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
    import datetime
    import random
    from mastodon import Mastodon
    from dotenv import load_dotenv
    import asyncio
    import tracemalloc
    import json

    date_string = str(datetime.date.today())
    fecha = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    semanaNumero = fecha.isocalendar()[1]
    load_dotenv()
    tracemalloc.start()
    masto = Mastodon(
        access_token = os.getenv("TOKEN"),
        api_base_url = "https://masto.es"
    )
    hashtags = tendencias(5)
    mensajedeldia = mensajeSegunElDia()
    quediaes = diaDeHoy()
    nombreArchivos = nombreImagenes(quediaes)
    hora = datetime.datetime.now().hour
    queImagenSubo = str(random.choice(nombreArchivos))
    if hora < 11:
        if quediaes == 'viernes':
            video(f'''{mensajedeldia}''','C:/Lautaro/Python-personal/Mastodon/TootMastodonLocal/video/viernes/graciasADiosEsViernes.mp4','viernes','Friday','shrek', hashtags)
        else:
            funcionDiaria(mensajedeldia,quediaes.capitalize(),f'{queImagenSubo}',quediaes, quediaes.capitalize(), hashtags)
            registroImagenes(semanaNumero,queImagenSubo)
    else:
        if quediaes == 'viernes':
            archivo = str(random.choice(nombreImagenes("imgrandom")))
            funcionDiaria(mensajedeldia,'imgrandom',f'{archivo}', hashtags)
            registroImagenes(semanaNumero,archivo)
        else:
            archivo = str(random.choice(nombreImagenes("imgrandom")))
            funcionDiaria(str(mensajedeldia),'imgrandom',f'{archivo}', hashtags)
            registroImagenes(semanaNumero,archivo)
    tracemalloc.stop()