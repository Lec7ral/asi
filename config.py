
import os

class Config:
    API_ID = 25951341#os.environ.get("API_ID", "21714374")
    API_HASH = "f1f620f451989a04994e1d0796466d55"#os.environ.get("API_HASH", "700092e37d7da9a7b781994b7503a488")
    BOT_TOKEN = "6674516595:AAGXTP1vxs5TI4zR-Twhq739rU7U-roDmgQ"#os.environ.get("BOT_TOKEN", "") 
    DB_URL = "mongodb+srv://admin:asd1234@clouster0.b2fgx.mongodb.net/?retryWrites=true&w=majority&appName=Clouster0"#os.environ.get("DB_URL", "")
    DB_NAME = "User_bot"#os.environ.get("DB_NAME", "madflixbotz")
    OWNER_ID = 971580959#[int(id) for id in os.environ.get("OWNER_ID", '6140468904').split()]
    CHANNEL_ID = -1002422039132
    CHANNEL_URL = "https://t.me/asdadsasdasdasdadad/"
    PAY_API = "060853e8e491c5e57cec9f408"
    CARD_CUP = 9224959877252237
    CARD_MLC = 9225959878761003
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
class Plans:
    PLANS = {
        "FREE": {
            "name": "Gratis",
            "price-cup": 0,
            "price-mlc": 0,
            "price-USDT": 0,
            "duration": "Sin límites",
            "default_time": 86400,  # Tiempo mínimo de reenvío en minutos
            "min-time": 86400,
            "benefits": [
                 "║┣⪼✅ Reenvíos limitados a 1 por día.",
                 "║┣⪼✅ Enlace del bot al final del mensaje.",
                 "║┣⪼❌ Sin acceso a botones en los mensajes.",
                 "║┣⪼❌ No se pueden enviar archivos multimedia (fotos y videos).",
                 "║┣⪼❌ Limitado a un solo mensaje de texto."
            ]
        },
        "PREMIUM-1": {
            "name": "Básico 🌱",
            "price-cup": 0,
            "price-mlc": 0,
            "price-USDT": 0,
            "duration": 30,
            "default_time": 28800,  # Tiempo mínimo de reenvío en segundos
            "min-time": 28800,
            "benefits": [
                "║┣⪼✅ Reenvíos limitados a 1 cada 8horas.",
                "║┣⪼❌ Sin acceso a botones en los mensajes.",
                "║┣⪼❌ No se pueden enviar archivos multimedia (fotos y videos).",
                "║┣⪼❌ No puedes mandar varios mensajes."
            ]
        },
        "PREMIUM-2": {
            "name": "Premium Mensual 🌟",
            "price-cup": 0,
            "price-mlc": 0,
            "price-USDT": 0,
            "duration": 30,
            "default_time": 18000,  # Tiempo de reenvío en segundos(5h)
            "min-time": 120,
            "benefits": [
                "║┣⪼🔘 Posibilidad de agregar botones al final de los mensajes.",
                "║┣⪼📸 Envío de archivos multimedia como fotos y videos.",
                "║┣⪼💬 Puedes mandar varios mensajes.",
                "║┣⪼⏱️ Tiempo mínimo de reenvío: 2 minutos."
            ]
        },
        "PREMIUM-3": {
            "name": "Premium Semanal 📅",
            "price-cup": 0,
            "price-mlc": 0,
            "price-USDT": 0,
            "duration": 7,
            "default_time": 18000,
            "min-time": 120,
            "benefits": [
                "║┣⪼🔘 Posibilidad de agregar botones al final de los mensajes.",
                "║┣⪼📸 Envío de archivos multimedia como fotos y videos.",
                "║┣⪼💬 Puedes mandar varios mensajes.",
                "║┣⪼⏱️ Tiempo mínimo de reenvío: 2 minutos."
            ]
        }
    }

    @classmethod
    def get_plan(cls, plan_key):
        return cls.PLANS.get(plan_key, None)
