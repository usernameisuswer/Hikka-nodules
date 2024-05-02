#meta developer:@ytkanelox
import io
import logging
from io import BytesIO

import requests
from PIL import Image
from requests import post
from telethon import events
from telethon.tl.types import DocumentAttributeFilename

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class UploaderMod(loader.Module):
    """Uploader"""

    strings = {"name": "Uploader"}

    async def client_ready(self, client, db):
        self.client = client

    @loader.sudo
    async def uplcmd(self, message):
        """Upload"""
      
        await message.edit("<b>загружаю🤫🤯...</b>")
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("<b> реплай проебался</b>")
            return
        media = reply.media
        if not media:
            file = io.BytesIO(bytes(reply.raw_text, "utf-8"))
            file.name = "txt.txt"
        else:
            file = io.BytesIO(await self.client.download_file(media))
            file.name = reply.file.name or reply.file.id + reply.file.ext
        try:
            gayporn = post("https://hikkabot.serv00.net/script.php", files={"file": file})
        except ConnectionError:
            await message.edit("<b>Ошибка</b>")
            return
        url = gayporn.text
        output = f' ссылка на файл:  </a><code>{url}</code>'
        await message.edit(output)
        
        
        