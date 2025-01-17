from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import re
import os
from aiohttp import web
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)

from pyrogram.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)


# Reemplaza estos valores con tus credenciales
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SESSION_NAME = "my_userbot"

# Palabra clave para filtrar mensajes
KEYWORD1 = None
KEYWORD2 = None
KEYWORD3= '#VENTA'

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Join Telegram Channal @ALV")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

class Bot(Client): 
    def __init__(self):
        super().__init__(
            "Prer",
            api_hash=API_HASH,
            api_id=API_ID,
            bot_token=BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
         #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, 8080).start()
        self.id = me.id
        self.username = me.username
        self.first_name = me.first_name
        await idle()

USERBOT = None
handlers_setup = False

def setup_userbot_handlers():
    global USERBOT, handlers_setup
    if USERBOT is not None and not handlers_setup:
        @USERBOT.on_message(filters.channel & filters.text)
        async def button_click(client, message):
            if message.chat.id == -1002020239933:
                global KEYWORD1, KEYWORD2
                if KEYWORD3 in message.text:
                    contenido = message.text
                    match = re.search(r'por (\d+\.\d+).*?Tasa de cambio:\s*(\d+\.\d+)', contenido, re.DOTALL)
                    if match:
                        numero_por = float(match.group(1))  # Número después de "por"
                        numero_tasa = float(match.group(2))  # Número después de "Tasa de cambio"
                        if numero_por >= KEYWORD1 and numero_tasa <= KEYWORD2:
                            if message.reply_markup:
                                button = message.reply_markup.inline_keyboard[0][0]  # Presiona el primer botón
                                await client.send_callback_query(message.chat.id, button.callback_data)
        @USERBOT.on_message(filters.bot & filters.text)
        async def button_click2(client, message):
            if message.chat.id == 7185958939:
                if message.reply_markup:
                                button = message.reply_markup.inline_keyboard[0][0]  # Presiona el primer botón
                                await client.send_callback_query(message.chat.id, button.callback_data)
        handlers_setup = True
        
@Bot.on_message(filters.command("start"))
async def start(client, message):
    await client.send_message(message.chat.id, "¡Hola! Soy tu bot de Telegram. ¿En que puedo ayudarte?\nUtiliza uno de estos:\n\n/loging para loggearte con el userbot(solo una vez, sino seguro <b>CRASH<\b>)\n/iniciar para que comience la tarea en segundo plano\n/detener para detenerla/modificar para cambiar los terminos 1 y 2")

@Bot.on_message(filters.command("detener"))
async def detener(client, message):
    global USERBOT
    if USERBOT.connect():
        USERBOT.stop()
        await client.send_message(message.chat.id, "Deteniendo la tarea en segundo plano...")
    else:
        await client.send_message(message.chat.id, "El userbot ya esta off.")
        
@Bot.on_message(filters.command("iniciar"))
async def iniciar(client, message):
    global USERBOT
    if not USERBOT:
        await client.send_message(message.chat.id, "No se ha iniciado el userbot.\n\n /login")
    elif USERBOT.connect():
        await client.send_message(message.chat.id, "Ya esta funcionando")
    else:
        USERBOT.start()
        setup_userbot_handlers()
        await client.send_message(message.chat.id, "La tarea en segundo plano ha sido iniciada.")
        
# Comando /login para el bot
@Bot.on_message(filters.command("login"))
async def start(client, message):
    global USERBOT
    userbot = await add_session(client, message)
    USERBOT = await userbot.start()
    

# Comando /modificar para el bot
@Bot.on_message(filters.command("modificar"))
async def modificar(client, message):
    conf1_msg = await client.ask(message.chat.id, "Ingrese el nuevo valor de la configuración 1:")
    conf2_msg = await client.ask(message.chat.id, "Ingrese el nuevo valor de la configuración 2:")
    global KEYWORD1, KEYWORD2
    KEYWORD1 = conf1_msg.text
    KEYWORD2 = conf2_msg.text
    await client.send_message(message.chat.id, "Configuraciones modificadas!")
    
async def add_session(bot, message):
     user_id = int(message.from_user.id)
     api_id = API_ID
     api_hash = API_HASH
     t = "☞︎︎︎ » Por favor, ingresa tu número de teléfono para continuar: Ejemplo: +53 5xxxxxxx"
     phone_number_msg = await bot.ask(chat_id=user_id, text=t)
     if phone_number_msg.text=='/cancel':
        return await phone_number_msg.reply('Process Cancelled !')
     phone_number = phone_number_msg.text
     await phone_number_msg.reply("» Intentando enviar OTP al número dado...")
     client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True, app_version="1.0.1",
            system_version="Windows",
            device_model="PC 64bit")
     await client.connect()
     try:
        code = await client.send_code(phone_number)
     except (PhoneNumberInvalid, PhoneNumberInvalid1):
        await phone_number_msg.reply("» El número de teléfono que has enviado no pertenece a ninguna cuenta de Telegram.")
        return
     try:
        phone_code_msg = None 
        phone_code_msg = await bot.ask(user_id, "» Por favor, envía el OTP que has recibido de Telegram en tu cuenta.\nSi el OTP es 12345, por favor envíalo como P12345.", filters=filters.text, timeout=600)
        if phone_code_msg.text=='/cancel':
           return await phone_code_msg.reply('Process Cancelled !')
     except TimeoutError:
        await phone_number_msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 10 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.")
        return
     phone_code = phone_code_msg.text.replace("P", "")
     try:
        await client.sign_in(phone_number, code.phone_code_hash, phone_code)
     except (PhoneCodeInvalid, PhoneCodeInvalid1):
        await phone_code_msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴡʀᴏɴɢ.**\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.")
        return
     except (PhoneCodeExpired, PhoneCodeExpired1):
        await phone_code_msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴇxᴩɪʀᴇᴅ.**\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.")
        return
     except (SessionPasswordNeeded, SessionPasswordNeeded1):
        try:
           two_step_msg = await bot.ask(user_id, "» ᴩʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ **ᴛᴡᴏ sᴛᴇᴩ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ** ᴩᴀssᴡᴏʀᴅ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.", filters=filters.text, timeout=300)
        except TimeoutError:
           await phone_code_msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.")
           return
        try:
           password = two_step_msg.text
           await client.check_password(password=password)
        except (PasswordHashInvalid, PasswordHashInvalid1):
           await two_step_msg.reply("» ᴛʜᴇ ᴩᴀssᴡᴏʀᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ᴡʀᴏɴɢ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.")
           return
     string_session = await client.export_session_string()
     
     userbot = Client("USERBOT", API_ID, API_HASH, session_string=string_session, app_version="1.0.1",
            system_version="Windows",
            device_model="PC 64bit")

     return userbot
# Ejecuta ambos clientes
if __name__ == "__main__":
    print ("Iniciando el bot...")
    app = Bot()
    app.run()

    

    
