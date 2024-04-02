# meta developer: @mm_mods
# requires: toml
import os
from hikka import loader, utils
import pickle
from telethon.tl.types import Channel
import toml


# noinspection PyCallingNonCallable
@loader.tds
class RPMod(loader.Module):
    """A little upgraded mod of module of @trololo_1."""

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "action_decoration",
                'normal | без стилей',
                lambda: self.strings("cfg_action_decoration"),
                validator=loader.validators.Choice(
                    [
                        "normal | без стилей",
                        "bold | полужирный",
                        "italic | курсив",
                        "underlined | подчёркнутый",
                        "strikethrough | зачёркнутый",
                        "spoiler | скрытый",
                    ]
                ),
            ),

            loader.ConfigValue(
                "replica_decoration",
                'normal | без стилей',
                lambda: self.strings("cfg_replica_decoration"),
                validator=loader.validators.Choice(
                    [
                        "normal | без стилей",
                        "bold | полужирный",
                        "italic | курсив",
                        "underlined | подчёркнутый",
                        "strikethrough | зачёркнутый",
                        "spoiler | скрытый",
                    ]
                ),
            ),

            loader.ConfigValue(
                "speech_bubble",
                '💬',
                lambda: self.strings("cfg_speech_bubble"),
                validator=loader.validators.String()
            )
        )

    strings = {
        'name': 'LiMERPMod',
        'separator…': '🤐 <b>Here\'s an emoji separator, but no emoji. eh</b>',
        'name?': '🧐 <b>Where\'s the name of the RP command?</b>',
        'action?': '🧐 <b>Where\'s the action of the RP command?</b>',
        'aarf': '🤢 <b>RP commands can\'t be named "all"</b>',
        'space': '🤐 <b>RP commands consisting of multiple words aren\'t supported.</b>',
        'added1': "🤩 <b>Command '<code>{}</code>' succesfully added with emoji '{}'!</b>",
        'added2': "☺️ <b>Command '<code>{}</code>' succesfully added!</b>",
        'weresall': '🤐 <b>You\'ve not entered separator or have\'nt entered anything at all.</b>',
        'cleared': '🍃 <b>RP commands succesfully cleared!</b>',
        'arg?': '🧐 <b>Where\'s the argument?</b>',
        'deleted': '🗑️ <b>RP command <code>{}</code> succesfully deleted!</b>',
        'notfound': '🧐 <b>Command <code>{}</code> not found!</b>',
        'on': '😀 <b>RP commands are now on!</b>',
        'off': '😴 <b>RP commands are now off!</b>',
        's-t-wrong': '😟 <b>Something went wrong!</b>',
        'nick-changed': '🏷️ <b>RP nickname of {} succesfully changed to <code>{}</code>!</b>',
        'count': '📋 <b>You have <code>{}</code> commands</b>',
        'error-with-type': '❌ <b>Error: <code>{}</code></b>',
        'actualised': '👍🏻 <b>RP commands succesfully actualised!</b>',
        'chat-excluded': '➖ <b>Chat {} succesfully excluded!</b>',
        'chat-included': '➕ <b>Chat {} succesfully included!</b>',
        'id-wrong': '🔢 <b>Wrong ID!</b>',
        'empty-exclude': '🪁 <b>Excluded chats list is empty!</b>',
        'excluded-chats': '📃 <b>Excluded chats:</b>',
        'on-in-chat': '📗💬 <b>RP commands are now on for members of this chat!</b>',
        'off-in-chat': '📕💬 <b>RP commands are now off for members of this chat!</b>',
        'who-have': '📄 <b>Who have RP commands access:</b>',
        'chats-s': '💬 <b>Chats:</b>',
        'users-s': '👤 <b>Users:</b>',
        'on-for-usr': '📗 <b>RP commands are now on for <code>{}</code>!</b>',
        'off-for-usr': '📕 <b>RP commands are now off for <code>{}</code>!</b>',
        'whatschanged': '''🍋 <b>LIME</b> (1.2) — mod of RPMod (@trololo_1) by @mm_mods
What\'s changed?
    • No limits now!
    • No check for emoji validity now — add custom emojies…
    • No buggy import now, everyone can use the module.
    • Additions and replicas now save there\'s case.
    • New commands backup format.
    • Config optoins moved to config.
Enjoy!''',
        'with-replica': 'Saying:',
        'arg-unknown': '🤌🏻 <b>Unknown argument!</b>',
        'num-unknown': 'Ⓜ️ <b>Unknown number!</b>',
        'done': '✅ <b>Done!</b>',
        'less-then-2': '▫️ <b>Less then 2 arguments!</b>',
        'toml-minparse-failure': '😦 <b>Failed to parse toml!</b>\nAre you sure it\'s a backup?',
        'toml-parse-failure': '💀 <b>Failed to parse toml!</b>\nThe backup is corrupted.',
        'cfg_action_decoration': 'Decoration for RP action',
        'cfg_replica_decoration': 'Decoration for RP replica',
        'cfg_speech_bubble': 'Speech bubble emoji for «with replica»',
    }

    strings_ru = {
        'name': 'LiMERPMod',
        'separator…': '🤐 <b>Вот разделитель, но нет эмодзи. епт</b>',
        'name?': '🧐 <b>Где имя РП-команды?</b>',
        'action?': '🧐 <b>Где действие РП-команды?</b>',
        'aarf': '🤢 <b>РП-команды не могут называться "all"</b>',
        'space': '🤐 <b>Многословные команды не поддерживаются.</b>',
        'added1': "🤩 <b>Команда '<code>{}</code>' успешно добавлена с эмодзи '{}'!</b>",
        'added2': "☺️ <b>Команда '<code>{}</code>' успешно добавлена!</b>",
        'weresall': '🤐 <b>Вы не ввели разделитель или ничего не ввели вообще.</b>',
        'cleared': '🍃 <b>РП-команды успешно очищены!</b>',
        'arg?': '🧐 <b>Где аргумент?</b>',
        'deleted': '🗑️ <b>РП-команда <code>{}</code> успешно удалена!</b>',
        'notfound': '🧐 <b>Команда <code>{}</code> не найдена!</b>',
        'on': '😀 <b>РП-команды теперь включены!</b>',
        'off': '😴 <b>РП-команды теперь выключены!</b>',
        's-t-wrong': '😟 <b>Что-то пошло не так!</b>',
        'nick-changed': '🏷️ <b>Ник {} успешно изменен на <code>{}</code>!</b>',
        'count': '📋 <b>У вас <code>{}</code> команд</b>',
        'error-with-type': '❌ <b>Ошибка: <code>{}</code></b>',
        'actualised': '👍🏻 <b>РП-команды успешно обновлены!</b>',
        'chat-excluded': '➖ <b>Чат {} успешно исключен!</b>',
        'chat-included': '➕ <b>Чат {} успешно включен!</b>',
        'id-wrong': '🔢 <b>Неверный ID!</b>',
        'empty-exclude': '🪁 <b>Список исключённых чатов пуст!</b>',
        'excluded-chats': '📃 <b>Исключённые чаты:</b>',
        'on-in-chat': '📗💬 <b>РП-команды теперь включены для участников этого чата!</b>',
        'off-in-chat': '📕💬 <b>РП-команды теперь выключены для участников этого чата!</b>',
        'who-have': '📄 <b>Кто имеет доступ к РП-командам:</b>',
        'chats-s': '💬 <b>Чаты:</b>',
        'users-s': '👤 <b>Пользователи:</b>',
        'on-for-usr': '📗 <b>РП-команды теперь включены для <code>{}</code>!</b>',
        'off-for-usr': '📕 <b>РП-команды теперь выключены для <code>{}</code>!</b>',
        'whatschanged': '''🍋 <b>LIME</b> (1.2) — модуль RPMod (@trololo_1) от @mm_mods
Что изменилось?
    • Больше нет ограничений!
    • Больше нет проверки на валидность эмодзи — добавляйте кастомные эмодзи…
    • Больше нет багов с импортом — теперь модуль может использовать каждый.
    • Дополнения и реплики теперь сохраняют свой регистр.
    • Новый формат сохранения команд.
    • Опции конфига переехали в конфиг.
Наслаждайтесь!''',
        'with-replica': 'С репликой:',
        'arg-unknown': '🤌🏻 <b>Неизвестный аргумент!</b>',
        'num-unknown': 'Ⓜ️ <b>Неизвестная цифра!</b>',
        'done': '✅ <b>Готово!</b>',
        'less-then-2': '▫️ <b>Меньше 2 аргументов!</b>',
        'toml-minparse-failure': '😦 <b>Ошибка парсинга toml!</b>\nЭто точно бэкап?',
        'toml-parse-failure': '💀 <b>Ошибка парсинга toml!</b>\nБэкап повреждён.',
        'cfg_action_decoration': 'Декорация для действия РП-команды',
        'cfg_replica_decoration': 'Декорация для реплики РП-команды',
        'cfg_speech_bubble': 'Эмодзи речевого пузыря для «с репликой»',
        '_cls_doc': 'Слегка улучшенный мод на модуль от @trololo_1.',
        '_cmd_doc_dobrp': 'Создать РП-команду. Аргументы: <команда>/<действие>[/<эмодзи>]',
        '_cmd_doc_addrp': 'Псевдоним для .dobrp.',
        '_cmd_doc_delrp': 'Удалить РП-команду. Аргументы: <команда>',
        '_cmd_doc_rplist': 'Показать список РП-команд.',
        '_cmd_doc_rpconf': 'Настроить шаблон для РП-команд. Аргументы: <параметр> <значение>',
        '_cmd_doc_orpback': 'Сохранить/загрузить РП-команды (старый метод). Используйте без аргументов, чтобы '
                            'сохранить, или в ответ на файл, чтобы загрузить.',
        '_cmd_doc_rpback': 'Новый метод, чтобы сохранить/загрузить РП-команды. Используйте без аргументов, чтобы '
                            'сохранить, или в ответ на файл, чтобы загрузить.',
        '_cmd_doc_rpnick': 'Изменить ник для РП-команд. Аргументы: <ник> или без ника, чтобы его сбросить. '
                           'В ответ на сообщение нужного пользователя.',
        '_cmd_doc_rpnicks': 'Используйте .rpnicks, чтобы просмотреть список ников для РП-команд.',
        '_cmd_doc_rpblock': 'Заблокировать/разблокировать РП-команды в чате. Аргументы: <айди чата>. '
                            'Можно и без него, чтобы сменить настройки в этом чате.',
        '_cmd_doc_rptoggle': 'Используйте .rptoggle, чтобы включить/выключить РП-мод.',
        '_cmd_doc_useraccept': 'Допустить или нет пользователя/чат к РП-командам. Аргументы: <айди пользователя/чата>. '
                               'Можно без ответа и аргумента, тогда действие будет выполнена над текущим чатом. '
                               'Можно просто без аргумента, тогда действие будет выполнено над пользователем из '
                               'ответа. Еси использовано с -l (л), то будет показан список допущенных пользователей/чатов.',
        '_cmd_doc_mmminfo': 'Показать информацию о моде.',
    }

    async def client_ready(self, client, db):
        self.db = db

        if not self.db.get("RPMod", "exlist", False):
            self.db.set("RPMod", "exlist", [])

        if not self.db.get("RPMod", "status", False):
            self.db.get("RPMod", "status", 1)

        if not self.db.get("RPMod", "rpnicks", False):
            self.db.set("RPMod", "rpnicks", {})

        if not self.db.get("RPMod", "rpcomands", False):
            self.db.set("RPMod", "rpcomands", {})

        if not self.db.get("RPMod", "rpemoji", False):
            self.db.set("RPMod", "rpemoji", {})

        if not self.db.get("RPMod", "nrpcommands", False):
            # Check if the old version of the module is installed
            if self.db.get("RPMod", "rpcomands", False):
                # Copy the dict
                commands_old = self.db.get("RPMod", "rpcomands")
                emoji_old = self.db.get("RPMod", "rpemoji")
                # Create a new dict
                commands_new = {}
                # For each key in the old dict try to find the emoji in the old dict and add as second element of list
                for key in commands_old:
                    try:
                        commands_new[key] = [commands_old[key], emoji_old[key]]
                    except KeyError:
                        commands_new[key] = [commands_old[key], '']

                # Save the new dict
                self.db.set("RPMod", "nrpcommands", commands_new)

            else:
                # If the old version of the module is not installed, create an empty dict
                self.db.set("RPMod", "nrpcommands", {})

        if not self.db.get("RPMod", "useraccept", False):
            self.db.set("RPMod", "useraccept", {"chats": [], "users": []})

        elif isinstance(type(self.db.get("RPMod", "useraccept")), list):
            self.db.set(
                "RPMod",
                "useraccept",
                {"chats": [], "users": self.db.get("RPMod", "useraccept")},
            )

    async def dobrpcmd(self, message):
        """Use: .dobrp (command) / (action) / (emoji) to add command. You can do it without emoji."""
        args = utils.get_args_raw(message)
        dict_rp = self.db.get("RPMod", "nrpcommands")

        try:
            key_rp = str(args.split("/")[0]).strip().casefold()
            value_rp = str(args.split("/", maxsplit=2)[1]).strip()
            lenght_args = args.split("/")
            count_emoji = 0

            if ' ' in key_rp:
                await utils.answer(message, self.strings("space"))
                return

            if len(lenght_args) >= 3:
                emoji_rp = str(message.text.split("/", maxsplit=2)[2]).strip()
                count_emoji = 1

                if not emoji_rp or not emoji_rp.strip():
                    await utils.answer(
                        message, self.strings("separator…")
                    )
                    return

            if not key_rp or not key_rp.strip():
                return await utils.answer(message, self.strings("name?"))

            elif not value_rp or not value_rp.strip():
                return await utils.answer(
                    message, self.strings("action")
                )

            elif key_rp == "all":
                return await utils.answer(
                    message, self.strings("aarf"),
                )

            elif count_emoji == 1:
                dict_rp[key_rp] = [value_rp, emoji_rp]
                self.db.set("RPMod", "nrpcommands", dict_rp)
                await utils.answer(
                    message,
                    self.strings("added1").format(key_rp, emoji_rp),
                )

            else:
                dict_rp[key_rp] = [value_rp, '']
                self.db.set("RPMod", "nrpcommands", dict_rp)
                await utils.answer(
                    message,
                    self.strings("added2").format(key_rp),
                )

        except Exception:
            await utils.answer(
                message, self.strings("weresall"),
            )

    async def addrpcmd(self, message):
        """dobrp alias."""
        await self.dobrpcmd(message)

    async def delrpcmd(self, message):
        """Use: .delrp (command) to delete command.
Use: .delrp all to delete all commands."""
        dict_rp = self.db.get("RPMod", "nrpcommands")

        args = utils.get_args_raw(message)
        key_rp = str(args)

        if key_rp == "all":
            dict_rp.clear()
            self.db.set("RPMod", "nrpcommands", dict_rp)
            await utils.answer(message, self.strings("cleared"))
            return

        elif not key_rp or not key_rp.strip():
            await utils.answer(message, self.strings("name?"))

        else:
            try:
                dict_rp.pop(key_rp)
                self.db.set("RPMod", "nrpcommands", dict_rp)

                await utils.answer(
                    message, self.strings("deleted").format(key_rp),
                )

            except KeyError:
                await utils.answer(message, self.strings("notfound"))

    async def rptogglecmd(self, message):
        """Use: .rptoggle to turn on/off RP mode."""
        status = self.db.get("RPMod", "status")

        if status == 1:
            self.db.set("RPMod", "status", 2)
            await utils.answer(message, self.strings("off"))

        else:
            self.db.set("RPMod", "status", 1)
            await utils.answer(message, self.strings("on"))

    async def rplistcmd(self, message):
        """Use: .rplist to see list of RP commands."""
        com = self.db.get("RPMod", "nrpcommands")

        coms_amount = len(com)
        com_list = self.strings("count").format(coms_amount)

        if len(com) == 0:
            await utils.answer(message, self.strings("count").format(coms_amount))
            return

        for i in com:
            if com[i][1] != '':
                com_list += f"\n• <b><code>{i}</code> - {com[i][0]} |</b> {com[i][1]}"
            else:
                com_list += f"\n• <b><code>{i}</code> - {com[i][0]}</b>"

        await utils.answer(message, com_list)

    async def rpnickcmd(self, message):
        """Use: .rpnick (nick) to change nick to user or yourself."""
        args = utils.get_args_raw(message).strip()
        reply = await message.get_reply_message()
        nicks = self.db.get("RPMod", "rpnicks")

        if not reply:
            user = await message.client.get_entity(message.sender_id)
        else:
            user = await message.client.get_entity(reply.sender_id)

        if not args:
            if str(user.id) in nicks:
                nicks.pop(str(user.id))

            self.db.set("RPMod", "rpnicks", nicks)
            return await utils.answer(
                message,
                self.strings("nick-changed").format(user.id, user.first_name),
            )

        nicks[str(user.id)] = args
        self.db.set("RPMod", "rpnicks", nicks)
        await utils.answer(
            message,
            self.strings("nick-changed").format(user.id, args),
        )

    async def rpnickscmd(self, message):
        """Use: .rpnicks to see list of nicknames."""
        nicks = self.db.get("RPMod", "rpnicks")

        if len(nicks) == 0:
            return await utils.answer(message, self.strings("no-nicks"))

        str_nicks = "• " + "\n •".join(
            " --- ".join([f"<code>{user_id}</code>", f"<b>{nick}</b>"])
            for user_id, nick in nicks.items()
        )
        await utils.answer(message, str_nicks)

    async def orpbackcmd(self, message):
        """Backup RP commands (old fashioned method).
Use as reply to file with commands to load them or use without
arguments to back up them."""
        commands = self.db.get("RPMod", "nrpcommands")
        file_name = "LiMERPModBackUp (on compat).pickle"
        mes_id = message.to_id

        reply = await message.get_reply_message()

        if not reply:
            # Split them into 2 dicts
            emojies = {}
            for key, value in commands.items():
                if commands[key][1] != "":
                    emojies[key] = commands[key][1]
                commands[key] = commands[key][0]

            try:
                await message.delete()
                dict_all = {"rp": commands, "emj": emojies}

                with open(file_name, "wb") as f:
                    pickle.dump(dict_all, f)

                await message.client.send_file(mes_id, file_name)
                os.remove(file_name)

            except Exception as e:
                await utils.answer(message, f"<b>Ошибка:\n</b>{e}")

        else:
            try:
                if not reply.document:
                    await utils.answer(message, self.strings("itsnotafile"))
                await reply.download_media(file_name)

                with open(file_name, "rb") as f:
                    data = pickle.load(f)

                rp = data["rp"]
                emj = data["emj"]

                # Iterating through keys
                for key in rp.keys():
                    if key in emj.keys():
                        rp[key] = [rp[key], emj[key]]

                self.db.set("RPMod", "nrpcommands", rp)

                await utils.answer(message, self.strings("actualised"))

            except Exception as e:
                await utils.answer(message, self.strings("error-with-type").format(e))

    async def rpbackcmd(self, message):
        """New way to backup RP commands. Use as reply to file with commands to load them or use without arguments to back up them."""
        commands = self.db.get("RPMod", "nrpcommands")
        file_name = "LiMERPModBackUp.toml"
        mes_id = message.to_id

        reply = await message.get_reply_message()

        if not reply:
            # Dump it into toml
            try:
                await message.delete()
                with open(file_name, "w") as f:
                 