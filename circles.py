# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Circles
# Description: Округляет всё
# meta developer: @die_tg
# Commands:
# .round
# ---------------------------------------------------------------------------------


import io
import logging
import os

from moviepy.editor import VideoFileClip
from PIL import Image, ImageDraw, ImageFilter, ImageOps
from telethon.tl.types import DocumentAttributeFilename

from .. import loader, utils  # pylint: disable=relative-beyond-top-level

logger = logging.getLogger(__name__)


def register(cb):
    cb(CirclesMod())


@loader.tds
class CirclesMod(loader.Module):
    """округляет всё"""

    strings = {"name": "Circles"}

    def __init__(self):
        self.name = self.strings["name"]

    async def client_ready(self, client, db):
        self.client = client

    @loader.sudo
    async def roundcmd(self, message):
        """.round <Ответь на стикер/фото видео/гиф>"""
        reply = None
        if message.is_reply:
            reply = await message.get_reply_message()
            data = await check_media(reply)
            if isinstance(data, bool):
                await utils.answer(
                    message, "<b>Ответь на стикер/фото видео/гиф</b>"
                )
                return
        else:
            await utils.answer(message, "<b>ответь на стикер/видео фото/гиф</b>")
            return
        data, type = data
        if type == "img":
            await message.edit("<b>округляю фото</b>📷")
            img = io.BytesIO()
            bytes = await message.client.download_file(data, img)
            im = Image.open(img)
            w, h = im.size
            img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
            img.paste(im, (0, 0))
            m = min(w, h)
            img = img.crop(((w - m) // 2, (h - m) // 2, (w + m) // 2, (h + m) // 2))
            w, h = img.size
            mask = Image.new("L", (w, h), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((10, 10, w - 10, h - 10), fill=255)
            mask = mask.filter(ImageFilter.GaussianBlur(2))
            img = ImageOps.fit(img, (w, h))
            img.putalpha(mask)
            im = io.BytesIO()
            im.name = "img.webp"
            img.save(im)
            im.seek(0)
            await message.client.send_file(message.to_id, im, reply_to=reply)
        else:
            await message.edit("<b>округляю видеo </b>🎥")
            await message.client.download_file(data, "video.mp4")
            video = VideoFileClip("video.mp4")
            video.reader.close()
            w, h = video.size
            m = min(w, h)
            box = [(w - m) // 2, (h - m) // 2, (w + m) // 2, (h + m) // 2]
            video = video.crop(*box)
            await message.edit("<b>Сохраняю видео</b>📼")
            video.write_videofile("result.mp4")
            await message.client.send_file(
                message.to_id, "result.mp4", video_note=True, reply_to=reply
            )
            os.remove("video.mp4")
            os.remove("result.mp4")
        await message.delete()


async def check_media(reply):
    type = "img"
    if reply and reply.media:
        if reply.photo:
            data = reply.photo
        elif reply.document:
            if (
                DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
                in reply.media.document.attributes
            ):
                return False
            if reply.gif or reply.video:
                type = "vid"
            if reply.audio or reply.voice:
                return False
            data = reply.media.document
        else:
            return False
    else:
        return False
    if not data or data is None:
        return False
    else:
        return (data, type)