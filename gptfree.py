from hikkatl.types import Message
from .. import loader, utils
import logging
from bingart import BingArt 

# requires: bingart
# meta developer:@DieModules (@ytkanelox)

logging.basicConfig(level=logging.INFO)

@loader.tds
class BingImgCreate(loader.Module):
    """Модуль для работы с библиотекой bingart"""
    strings = {
        "name": "BingCreateImage",
        "cfg_doc_U": "Настройка cookie '_U' для bingart."
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "COOKIE_U", 
            "", 
            lambda m: self.strings("cfg_doc_U", m)
        )

    async def client_ready(self, client, db):
        self._db = db
        cookie_u_value = db.get(self.strings("name"), "COOKIE_U", "")
        if cookie_u_value:
            self.config["COOKIE_U"] = cookie_u_value

    async def imgcmd(self, message: Message):
        """Генерирует изображение с помощью bingart"""
        prompt = message.raw_text.split(maxsplit=1)[1] if len(message.raw_text.split(maxsplit=1)) > 1 else "изображение"
        await utils.answer(message, "<emoji document_id=5307675706283533118>🫥</emoji> <b>Генерирую...</b>")
        image_response = await self.generate_image(prompt)
        if image_response.startswith('http'):
            await message.client.send_file(message.chat_id, f'{image_response}.jpg', caption=f"prompt: {prompt}")
        else:
            await utils.answer(message, image_response)

    async def generate_image(self, prompt: str):
        '''Генерирует изображение по запросу пользователя'''
        bing_art = BingArt(auth_cookie_U=self.config["COOKIE_U"])
        try:
            results = bing_art.generate_images(prompt)
            if results['images']:
                return results['images'][0]['url']
            else:
                return "Не удалось сгенерировать изображение."
        except Exception as e:
            logging.error(f"Произошла ошибка при генерации изображения: {e}")
            return "Произошла ошибка при генерации изображения(ошибка находится в логах)"
        finally:
            bing_art.close_session()
            

    