import os
from mastodon import Mastodon
from dotenv import load_dotenv
import asyncio

load_dotenv()

masto = Mastodon(
    access_token = os.getenv("TOKEN"),
    api_base_url = "https://masto.es"
)

async def post_video(mje,media,Sensitive=False, formato='mp4',visibilidad='public'):
    with open(f'{media}', 'rb') as video_file:
        video_bytes = video_file.read()
    media_dict = masto.media_post(media_file=video_bytes, mime_type=f'video/{formato}')
    media_id = media_dict['id']
    await asyncio.sleep(5) # espera 10 segundos antes de publicar
    await masto.status_post(status=f'{mje}', media_ids=[media_id], sensitive=Sensitive, visibility=f'{visibilidad}')


def post_imagen(mje,media,Sensitive=False, formato='jpg',visibilidad='public'):
    media_dict = masto.media_post(media_file=media, mime_type=f'imagen/{formato}')
    media_id = media_dict['id']
    # await asyncio.sleep(5) # espera 10 segundos antes de publicar
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
