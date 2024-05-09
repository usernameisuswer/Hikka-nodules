from hikkatl.types import Message
from .. import loader , utils 
import logging
from g4f.client import Client 

# requires: g4f
# meta developer:@DieModules (@ytkanelox)

logging.basicConfig(level=logging.INFO)

@loader.tds
class G4FModule(loader.Module):
    """Модуль для работы с библиотекой g4f"""
    strings = {"name": "G4FModule"}

    async def gptcmd(self, message: Message):
        """Отправляет запрос к GPT-4 и возвращает ответ"""
        request = message.raw_text.split(maxsplit=1)[1] if len(message.raw_text.split(maxsplit=1)) > 1 else "Привет!"
        await utils.answer(message, "<emoji document_id=5334904192622403796>🫥</emoji> Получаю ответ...")
        response = await self.request_event(request)
        formatted_response = f"<emoji document_id=5199682846729449178>🧠</emoji> Ответ: {response}\n <emoji document_id=5328239124933515868>⚙️</emoji> запрос: {request}"
        await message.edit(formatted_response)

    async def request_event(self, request: str) -> str:
        '''Возвращает ответ на запрос пользователя от GPT-4'''
        client = Client()
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{
                    "role": "user", "content": request
                }]
            )
            return response.choices[0].message.content
        except Exception as e:
            logging.error(f"Произошла ошибка: {e}")
            return "Произошла ошибка"