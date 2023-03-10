# ÂŠī¸ Dan Gazizullin, 2021-2022
# This file is a part of Hikka Userbot
# đ https://github.com/hikariatama/Hikka
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# đ https://www.gnu.org/licenses/agpl-3.0.html

import git
from telethon.tl.types import Message
from telethon.utils import get_display_name

from .. import loader, utils, version
from ..inline.types import InlineQuery


@loader.tds
class HikkaInfoMod(loader.Module):
    """Show userbot info"""

    strings = {
        "name": "HikkaInfo",
        "owner": "Owner",
        "version": "Version",
        "build": "Build",
        "prefix": "Prefix",
        "uptime": "Uptime",
        "branch": "Branch",
        "cpu_usage": "CPU usage",
        "ram_usage": "RAM usage",
        "send_info": "Send userbot info",
        "description": "âš This will not compromise any sensitive info",
        "up-to-date": (
            "<emoji document_id=5370699111492229743>đ</emoji> <b>Up-to-date</b>"
        ),
        "update_required": (
            "<emoji document_id=5424728541650494040>đ</emoji> <b>Update required"
            "</b> <code>.update</code>"
        ),
        "setinfo_no_args": (
            "<emoji document_id=5370881342659631698>đĸ</emoji> <b>You need to specify"
            " text to change info to</b>"
        ),
        "setinfo_success": (
            "<emoji document_id=5436040291507247633>đ</emoji> <b>Info changed"
            " successfully</b>"
        ),
        "_cfg_cst_msg": (
            "Custom message for info. May contain {me}, {version}, {build}, {prefix},"
            " {platform}, {upd}, {uptime}, {cpu_usage}, {ram_usage}, {branch} keywords"
        ),
        "_cfg_cst_btn": "Custom button for info. Leave empty to remove button",
        "_cfg_banner": "URL to image banner",
        "desc": (
            "<emoji document_id=6318565919471699564>đ</emoji>"
            " <b>Hikka</b>\n\nTelegram userbot with a lot of features, like inline"
            " galleries, forms, lists and animated emojis support. Userbot - software,"
            " running on your Telegram account. If you write a command to any chat, it"
            " will get executed right there. Check out live examples at <a"
            ' href="https://github.com/hikariatama/Hikka">GitHub</a>'
        ),
    }

    strings_ru = {
        "owner": "ĐĐģĐ°Đ´ĐĩĐģĐĩŅ",
        "version": "ĐĐĩŅŅĐ¸Ņ",
        "build": "ĐĄĐąĐžŅĐēĐ°",
        "prefix": "ĐŅĐĩŅĐ¸ĐēŅ",
        "uptime": "ĐĐŋŅĐ°ĐšĐŧ",
        "branch": "ĐĐĩŅĐēĐ°",
        "cpu_usage": "ĐŅĐŋĐžĐģŅĐˇĐžĐ˛Đ°ĐŊĐ¸Đĩ CPU",
        "ram_usage": "ĐŅĐŋĐžĐģŅĐˇĐžĐ˛Đ°ĐŊĐ¸Đĩ RAM",
        "send_info": "ĐŅĐŋŅĐ°Đ˛Đ¸ŅŅ Đ¸ĐŊŅĐžŅĐŧĐ°ŅĐ¸Ņ Đž ŅĐˇĐĩŅĐąĐžŅĐĩ",
        "description": "âš Đ­ŅĐž ĐŊĐĩ ŅĐ°ŅĐēŅĐžĐĩŅ ĐŊĐ¸ĐēĐ°ĐēĐžĐš ĐģĐ¸ŅĐŊĐžĐš Đ¸ĐŊŅĐžŅĐŧĐ°ŅĐ¸Đ¸",
        "_ihandle_doc_info": "ĐŅĐŋŅĐ°Đ˛Đ¸ŅŅ Đ¸ĐŊŅĐžŅĐŧĐ°ŅĐ¸Ņ Đž ŅĐˇĐĩŅĐąĐžŅĐĩ",
        "up-to-date": (
            "<emoji document_id=5370699111492229743>đ</emoji> <b>ĐĐēŅŅĐ°ĐģŅĐŊĐ°Ņ Đ˛ĐĩŅŅĐ¸Ņ</b>"
        ),
        "update_required": (
            "<emoji document_id=5424728541650494040>đ</emoji> <b>ĐĸŅĐĩĐąŅĐĩŅŅŅ ĐžĐąĐŊĐžĐ˛ĐģĐĩĐŊĐ¸Đĩ"
            "</b> <code>.update</code>"
        ),
        "_cfg_cst_msg": (
            "ĐĐ°ŅŅĐžĐŧĐŊŅĐš ŅĐĩĐēŅŅ ŅĐžĐžĐąŅĐĩĐŊĐ¸Ņ Đ˛ info. ĐĐžĐļĐĩŅ ŅĐžĐ´ĐĩŅĐļĐ°ŅŅ ĐēĐģŅŅĐĩĐ˛ŅĐĩ ŅĐģĐžĐ˛Đ° {me},"
            " {version}, {build}, {prefix}, {platform}, {upd}, {uptime}, {cpu_usage},"
            " {ram_usage}, {branch}"
        ),
        "_cfg_cst_btn": (
            "ĐĐ°ŅŅĐžĐŧĐŊĐ°Ņ ĐēĐŊĐžĐŋĐēĐ° Đ˛ ŅĐžĐžĐąŅĐĩĐŊĐ¸Đ¸ Đ˛ info. ĐŅŅĐ°Đ˛Ņ ĐŋŅŅŅŅĐŧ, ŅŅĐžĐąŅ ŅĐąŅĐ°ŅŅ ĐēĐŊĐžĐŋĐēŅ"
        ),
        "_cfg_banner": "ĐĄŅŅĐģĐēĐ° ĐŊĐ° ĐąĐ°ĐŊĐŊĐĩŅ-ĐēĐ°ŅŅĐ¸ĐŊĐēŅ",
        "setinfo_no_args": (
            "<emoji document_id=5370881342659631698>đĸ</emoji> <b>ĐĸĐĩĐąĐĩ ĐŊŅĐļĐŊĐž ŅĐēĐ°ĐˇĐ°ŅŅ"
            " ŅĐĩĐēŅŅ Đ´ĐģŅ ĐēĐ°ŅŅĐžĐŧĐŊĐžĐŗĐž Đ¸ĐŊŅĐž</b>"
        ),
        "setinfo_success": (
            "<emoji document_id=5436040291507247633>đ</emoji> <b>ĐĸĐĩĐēŅŅ Đ¸ĐŊŅĐž ŅŅĐŋĐĩŅĐŊĐž"
            " Đ¸ĐˇĐŧĐĩĐŊĐĩĐŊ</b>"
        ),
        "desc": (
            "<emoji document_id=6318565919471699564>đ</emoji>"
            " <b>Hikka</b>\n\nTelegram ŅĐˇĐĩŅĐąĐžŅ Ņ ĐžĐŗŅĐžĐŧĐŊŅĐŧ ĐēĐžĐģĐ¸ŅĐĩŅŅĐ˛ĐžĐŧ ŅŅĐŊĐēŅĐ¸Đš, Đ¸Đˇ"
            " ĐēĐžŅĐžŅŅŅ: Đ¸ĐŊĐģĐ°ĐšĐŊ ĐŗĐ°ĐģĐĩŅĐĩĐ¸, ŅĐžŅĐŧŅ, ŅĐŋĐ¸ŅĐēĐ¸, Đ° ŅĐ°ĐēĐļĐĩ ĐŋĐžĐ´Đ´ĐĩŅĐļĐēĐ°"
            " Đ°ĐŊĐ¸ĐŧĐ¸ŅĐžĐ˛Đ°ĐŊĐŊŅŅ ŅĐŧĐžĐ´ĐˇĐ¸. ĐŽĐˇĐĩŅĐąĐžŅ - ĐŋŅĐžĐŗŅĐ°ĐŧĐŧĐ°, ĐēĐžŅĐžŅĐ°Ņ ĐˇĐ°ĐŋŅŅĐēĐ°ĐĩŅŅŅ ĐŊĐ°"
            " ŅĐ˛ĐžĐĩĐŧ Telegram-Đ°ĐēĐēĐ°ŅĐŊŅĐĩ. ĐĐžĐŗĐ´Đ° ŅŅ ĐŋĐ¸ŅĐĩŅŅ ĐēĐžĐŧĐ°ĐŊĐ´Ņ Đ˛ ĐģŅĐąĐžĐŧ ŅĐ°ŅĐĩ, ĐžĐŊĐ°"
            " ŅŅĐ°ĐˇŅ ĐļĐĩ Đ˛ŅĐŋĐžĐģĐŊŅĐĩŅŅŅ. ĐĐąŅĐ°ŅĐ¸ Đ˛ĐŊĐ¸ĐŧĐ°ĐŊĐ¸Đĩ ĐŊĐ° ĐļĐ¸Đ˛ŅĐĩ ĐŋŅĐ¸ĐŧĐĩŅŅ ĐŊĐ° <a"
            ' href="https://github.com/hikariatama/Hikka">GitHub</a>'
        ),
    }

    strings_it = {
        "owner": "Proprietario",
        "version": "Versione",
        "build": "Build",
        "prefix": "Prefisso",
        "uptime": "Uptime",
        "branch": "Branch",
        "cpu_usage": "Uso CPU",
        "ram_usage": "Uso RAM",
        "send_info": "Invia info del bot",
        "description": "âš Questo non rivelera' alcuna informazione personale",
        "_ihandle_doc_info": "Invia info del bot",
        "up-to-date": (
            "<emoji document_id=5370699111492229743>đ</emoji> <b>Versione"
            " aggiornata</b>"
        ),
        "update_required": (
            "<emoji document_id=5424728541650494040>đ</emoji> <b>Aggiornamento"
            " richiesto</b> <code>.update</code>"
        ),
        "_cfg_cst_msg": (
            "Messaggio personalizzato per info. Puo' contenere {me}, {version},"
            " {build}, {prefix}, {platform}, {upd}, {uptime}, {cpu_usage}, {ram_usage},"
            " {branch} keywords"
        ),
        "_cfg_cst_btn": "Bottone personalizzato per info. Lascia vuoto per rimuovere",
        "_cfg_banner": "URL dell'immagine banner",
        "desc": (
            "<emoji document_id=6318565919471699564>đ</emoji>"
            " <b>Hikka</b>\n\nUserbot di Telegram con molte funzioni, come gallerie"
            " inline, form, liste e supporto ad emoji animate. Userbot - software"
            " che gira sul tuo account Telegram. Se scrivi un comando in qualsiasi"
            " chat, viene eseguito lÃŦ. Controlla gli esempi in <a"
            ' href="https://github.com/hikariatama/Hikka">GitHub</a>'
        ),
    }

    strings_de = {
        "owner": "Besitzer",
        "version": "Version",
        "build": "Build",
        "prefix": "Prefix",
        "uptime": "Uptime",
        "branch": "Branch",
        "cpu_usage": "CPU Nutzung",
        "ram_usage": "RAM Nutzung",
        "send_info": "Botinfo senden",
        "description": "âš Dies enthÃŧllt keine persÃļnlichen Informationen",
        "_ihandle_doc_info": "Sende Botinfo",
        "up-to-date": "<emoji document_id=5370699111492229743>đ</emoji> <b>Aktuell</b>",
        "update_required": (
            "<emoji document_id=5424728541650494040>đ</emoji> <b>Update benÃļtigt"
            "</b> <code>.update</code>"
        ),
        "_cfg_cst_msg": (
            "Custom message for info. May contain {me}, {version}, {build}, {prefix},"
            " {platform}, {upd}, {uptime}, {cpu_usage}, {ram_usage}, {branch} keywords"
        ),
        "_cfg_cst_btn": "Custom button for info. Leave empty to remove button",
        "_cfg_banner": "URL to image banner",
        "setinfo_no_args": (
            "<emoji document_id=5370881342659631698>đĸ</emoji> <b>Bitte gib einen"
            " Text an, um die Info zu Ã¤ndern</b>"
        ),
        "setinfo_success": (
            "<emoji document_id=5436040291507247633>đ</emoji> <b>Info geÃ¤ndert</b>"
        ),
        "desc": (
            "<emoji document_id=6318565919471699564>đ</emoji>"
            " <b>Hikka</b>\n\nTelegram userbot mit vielen Funktionen, wie z.B. Inline"
            " Galerien, Formulare, Listen und UnterstÃŧtzung fÃŧr animierte Emojis."
            " Userbot - Software, die auf deinem Telegram-Account lÃ¤uft. Wenn du"
            " einen Befehl in irgendeinem Chat schreibst, wird er dort ausgefÃŧhrt."
            " Sieh dir Live-Beispiele auf <a"
            ' href="https://github.com/hikariatama/Hikka">GitHub</a>'
        ),
    }

    strings_uz = {
        "owner": "Egasi",
        "version": "Versiya",
        "build": "Build",
        "prefix": "Prefix",
        "uptime": "Ishlash vaqti",
        "branch": "Vetkasi",
        "cpu_usage": "CPU foydalanish",
        "ram_usage": "RAM foydalanish",
        "send_info": "Bot haqida ma'lumot",
        "description": "âš Bu shaxsiy ma'lumot emas",
        "_ihandle_doc_info": "Bot haqida ma'lumot",
        "up-to-date": (
            "<emoji document_id=5370699111492229743>đ</emoji> <b>So'ngi versia</b>"
        ),
        "update_required": (
            "<emoji document_id=5424728541650494040>đ</emoji> <b>Yangilash"
            " kerak</b> <code>.update</code>"
        ),
        "_cfg_cst_msg": (
            "Xabar uchun shaxsiy xabar. {me}, {version}, {build}, {prefix}, {platform},"
            " {upd}, {uptime}, {cpu_usage}, {ram_usage}, {branch} kalit so'zlarni"
            " ishlatishingiz mumkin"
        ),
        "_cfg_cst_btn": (
            "Xabar uchun shaxsiy tugma. Tugmani o'chirish uchun bo'sh qoldiring"
        ),
        "_cfg_banner": "URL uchun rasmi",
        "setinfo_no_args": (
            "<emoji document_id=5370881342659631698>đĸ</emoji> <b>Ma'lumotni"
            " o'zgartirish uchun matn kiriting</b>"
        ),
        "setinfo_success": (
            "<emoji document_id=5436040291507247633>đ</emoji> <b>Ma'lumotlar"
            " o'zgartirildi</b>"
        ),
        "desc": (
            "<emoji document_id=6318565919471699564>đ</emoji> <b>Hikka</b>\n\nKo'p"
            " funksiyali userbot, buning ichida: ichki-gallereya, formalar, ro'yhatlar,"
            " hamda animatsiyalangan emojilar. Userbot - bu sening"
            " telegram-akkauntingni ichida ishlaydigan ilova. Hohlagan chatga komanda"
            " yozsangiz, tez orada bu komanda ishlaydi. <a"
            ' href="https://github.com/hikariatama/Hikka">GitHub</a> da misollarni'
            " ko'rishingiz mumkin"
        ),
    }

    strings_tr = {
        "owner": "Sahip",
        "version": "SÃŧrÃŧm",
        "build": "Derleme",
        "prefix": "Ãnek",
        "uptime": "Aktif SÃŧre",
        "branch": "Dal",
        "cpu_usage": "CPU KullanÄąmÄą",
        "ram_usage": "RAM KullanÄąmÄą",
        "send_info": "Bot hakkÄąnda bilgi",
        "description": "âšī¸ KiÅisel bilgileri tehlikeye atmaz",
        "_ihandle_doc_info": "Bot hakkÄąnda bilgi",
        "up-to-date": "<emoji document_id=5370699111492229743>đ</emoji> <b>GÃŧncel</b>",
        "update_required": (
            "<emoji document_id=5424728541650494040>đ</emoji> <b>GÃŧncelleme"
            " gerekli</b> <code>.update</code>"
        ),
        "_cfg_cst_msg": (
            "KiÅisel mesaj iÃ§in bilgi. {me}, {version}, {build}, {prefix}, {platform},"
            " {upd}, {uptime}, {cpu_usage}, {ram_usage}, {branch} anahtar kelimeleri"
            " kullanÄąlabilir"
        ),
        "_cfg_cst_btn": "KiÅisel tuÅ iÃ§in bilgi. TuÅu kaldÄąrmak iÃ§in boÅ bÄąrakÄąn",
        "_cfg_banner": "Resim iÃ§in URL",
        "setinfo_no_args": (
            "<emoji document_id=5370881342659631698>đĸ</emoji> <b>Bilgiyi deÄiÅtirmek"
            " iÃ§in herhangi bir metin girin</b>"
        ),
        "setinfo_success": (
            "<emoji document_id=5436040291507247633>đ</emoji> <b>Bilgiler"
            " deÄiÅtirildi</b>"
        ),
        "desc": (
            "<emoji document_id=6318565919471699564>đ</emoji> <b>Hikka</b>\n\\Ãok fazla"
            " Ãļzellik barÄąndÄąran Telegram kullanÄącÄą botu, ÃļrneÄin ÃevrimiÃ§i galeri,"
            " formlar, listeler ve animasyonlu emoji desteÄi gibi. KullanÄącÄą botu -"
            " Telegram hesabÄąnÄązda Ã§alÄąÅan bir yazÄąlÄąmdÄąr. Bir sohbete bir komut"
            " yazarsanÄąz, hemen orada Ã§alÄąÅacaktÄąr. Ãrnekleri gÃļrmek iÃ§in <a"
            ' href="https://github.com/hikariatama/Hikka">GitHub\'Äą ziyaret'
            " edebilirsin</a>"
        ),
    }

    strings_es = {
        "owner": "Propietario",
        "version": "VersiÃŗn",
        "build": "Construir",
        "prefix": "Prefijo",
        "uptime": "Tiempo de actividad",
        "branch": "Rama",
        "cpu_usage": "Uso de CPU",
        "ram_usage": "Uso de RAM",
        "send_info": "Enviar informaciÃŗn del bot",
        "description": "âšī¸ No exponga su informaciÃŗn personal",
        "_ihandle_doc_info": "InformaciÃŗn del bot",
        "up-to-date": (
            "<emoji document_id=5370699111492229743>đ</emoji> <b>Actualizado</b>"
        ),
        "update_required": (
            "<emoji document_id=5424728541650494040>đ</emoji> <b>ActualizaciÃŗn"
            " necesaria</b> <code>.update</code>"
        ),
        "_cfg_cst_msg": (
            "InformaciÃŗn del mensaje personalizado. Puede usar las palabras clave {me},"
            " {version}, {build}, {prefix}, {platform}, {upd}, {uptime}, {cpu_usage},"
            " {ram_usage}, {branch}"
        ),
        "_cfg_cst_btn": (
            "InformaciÃŗn del botÃŗn personalizado. Eliminar el botÃŗn deje en blanco"
        ),
        "_cfg_banner": "URL de la imagen",
        "setinfo_no_args": (
            "<emoji document_id=5370881342659631698>đĸ</emoji> <b>Para cambiar la"
            " informaciÃŗn, ingrese algÃēn texto</b>"
        ),
        "setinfo_success": (
            "<emoji document_id=5436040291507247633>đ</emoji> <b>InformaciÃŗn cambiada"
            " con ÃŠxito</b>"
        ),
        "desc": (
            "<emoji document_id=6318565919471699564>đ</emoji> <b>Hikka</b>\n\nEl bot de"
            " usuario proporciona varias funciones. Por ejemplo: GalerÃ­a en lÃ­nea,"
            " formulario, lista, Emoji animado y mÃĄs. El bot de usuario es una"
            " aplicaciÃŗn que funciona dentro de una cuenta de Telegram. Las Ãŗrdenes de"
            " chat se ejecutan de inmediato. Para obtener mÃĄs informaciÃŗn, consulte <a"
            ' href="https://github.com/hikariatama/Hikka">GitHub</a>'
        ),
    }

    strings_kk = {
        "owner": "ĶĐēŅĐŧŅŅ",
        "version": "ĐŌąŅŌĐ°ŅŅ",
        "build": "ŌŌąŅŅĐģŌĐ°ĐŊ",
        "prefix": "ĐĐ°ŅŅĐ°ŅŅŅ",
        "uptime": "ŌĐžŅŅĐģŌĐ°ĐŊ ĐēĐĩĐˇĐĩŌŖ",
        "branch": "ĐĶŠĐģŅĐŧŅ",
        "cpu_usage": "CPU ŌĐžĐģĐ´Đ°ĐŊŅĐŧŅ",
        "ram_usage": "RAM ŌĐžĐģĐ´Đ°ĐŊŅĐŧŅ",
        "send_info": "ĐĐžŅ ŅŅŅĐ°ĐģŅ Đ°ŌĐŋĐ°ŅĐ°Ņ",
        "description": "âšī¸ ĐĐĩĐēĐĩ ĐŧĶĐģŅĐŧĐĩŅŅĐĩŅŅŌŖŅĐˇĐ´Ņ ŌĐžŅŌĐ°Ņ",
        "_ihandle_doc_info": "ĐĐžŅ ŅŅŅĐ°ĐģŅ Đ°ŌĐŋĐ°ŅĐ°Ņ",
        "up-to-date": (
            "<emoji document_id=5370699111492229743>đ</emoji> <b>ĐĐ°ŌŖĐ°ŅŅŅĐģŌĐ°ĐŊ</b>"
        ),
        "update_required": (
            "<emoji document_id=5424728541650494040>đ</emoji> <b>ĐĐ°ŌŖĐ°ŅŅŅ"
            " ŅĐ°ĐģĐ°Đŋ ĐĩŅŅĐģĐĩĐ´Ņ</b> <code>.update</code>"
        ),
        "_cfg_cst_msg": (
            "ĐĐĩĐēĐĩ ŅĐ°ĐąĐ°ŅĐģĐ°ĐŧĐ° Ō¯ŅŅĐŊ Đ°ŌĐŋĐ°ŅĐ°Ņ. {me}, {version}, {build}, {prefix},"
            " {platform}, {upd}, {uptime}, {cpu_usage}, {ram_usage}, {branch} ĐēŅĐģŅ"
            " ŅĶŠĐˇĐ´ĐĩŅĐ´Ņ ŌĐžĐģĐ´Đ°ĐŊĐ° Đ°ĐģĐ°ŅŅĐˇ"
        ),
        "_cfg_cst_btn": "ĐĐĩĐēĐĩ ŅŌ¯ĐšĐŧĐĩ Ō¯ŅŅĐŊ Đ°ŌĐŋĐ°ŅĐ°Ņ. ĐĸŌ¯ĐšĐŧĐĩŅŅĐŊ ĐļĐžŅ Ō¯ŅŅĐŊ ĐąĐžŅ ŌĐ°ĐģĐ´ŅŅŅŌŖŅĐˇ",
        "_cfg_banner": "ĐĄŅŅĐĩŅ Ō¯ŅŅĐŊ URL",
        "setinfo_no_args": (
            "<emoji document_id=5370881342659631698>đĸ</emoji> <b>ĐŌĐŋĐ°ŅĐ°ŅŅŅ ĶŠĐˇĐŗĐĩŅŅŅ Ō¯ŅŅĐŊ"
            " ĐĩŅŅĐĩŌŖĐĩ ĐĩĐŊĐŗŅĐˇĐąĐĩŌŖŅĐˇ</b>"
        ),
        "setinfo_success": (
            "<emoji document_id=5436040291507247633>đ</emoji> <b>ĐŌĐŋĐ°ŅĐ°Ņ ŅĶŅŅŅ"
            " ĶŠĐˇĐŗĐĩŅŅŅĐģĐ´Ņ</b>"
        ),
        "desc": (
            "<emoji document_id=6318565919471699564>đ</emoji> <b>Hikka</b>\n\nĐĐ°ĐšĐ´Đ°ĐģŅ"
            " ĐąĐžŅ ŌĐžŅŅĐŧŅĐ°ĐģĐ°ŅŅ ĐąĐ°Ņ. ĐŅŅĐ°ĐģŅ: ĐĐŊĐģĐ°ĐšĐŊ ĐŗĐ°ĐģĐĩŅĐĩŅ, ŅĐžŅĐŧĐ°, ŅŅĐˇŅĐŧ, Đ°ĐŊĐ¸ĐŧĐ°ŅĐ¸ŅĐģŅ"
            " emoji ĐļĶĐŊĐĩ ĐąĐ°ŅŌĐ°ĐģĐ°Ņ. ĐĐ°ĐšĐ´Đ°ĐģŅ ĐąĐžŅ - ŅĐĩĐģĐĩĐŗŅĐ°Đŧ Đ°ĐēĐēĐ°ŅĐŊŅŅĐŊĐ´Đ° ŅŅĐēĐĩ ŌĐžŅŅĐģŌĐ°ĐŊ"
            " ĐąĐ°ŌĐ´Đ°ŅĐģĐ°ĐŧĐ°. ĐĄĶŠĐšĐģĐĩŅŅ ĐąĐžĐšŅĐŊŅĐ° ĶŅĐĩĐēĐĩŅŅŅ ŌŅĐģŅŌĐ° ĐąĐžĐģĐ°Đ´Ņ. ŌĐžŅŅĐŧŅĐ° Đ°ŌĐŋĐ°ŅĐ°Ņ Ō¯ŅŅĐŊ"
            ' <a href="https://github.com/hikariatama/Hikka">GitHub</a>'
        ),
    }

    strings_tt = {
        "owner": "ĐĐ´Đ°ŅĶŅĐĩ",
        "version": "ĐĐĩŅŅĐ¸Ņ",
        "build": "ĐĐ¸ĐģĐ´",
        "prefix": "ĐŅĐĩŅĐ¸ĐēŅ",
        "uptime": "ĐĸĶŅŅĐ¸ĐąĐ¸ Đ˛Đ°ĐēŅŅŅ",
        "branch": "ĐĐ¸ŅĐĩĐģĐĩĐē",
        "cpu_usage": "CPU ŌŅĐĩĐģĐŧĐ°ŅŅ",
        "ram_usage": "RAM ŌŅĐĩĐģĐŧĐ°ŅŅ",
        "send_info": "ĐĐžŅ ŅŅŅŅĐŊĐ´Đ° ĐŧĶĐŗŅĐģŌ¯ĐŧĐ°ŅĐŊŅ ŌĐ¸ĐąĶŅŌ¯",
        "description": "âšī¸ Đ¨ĶŅŅĐ¸ ĐŧĶĐŗŅĐģŌ¯ĐŧĐ°ŅŅŌŖŅĐˇĐŊŅ ŅŅŅŅ",
        "_ihandle_doc_info": "ĐĐžŅ ŅŅŅŅĐŊĐ´Đ° ĐŧĶĐŗŅĐģŌ¯ĐŧĐ°Ņ",
        "up-to-date": (
            "<emoji document_id=5370699111492229743>đ</emoji> <b>Đ¯ŌŖĐ°ŅŅŅĐģĐŗĐ°ĐŊ</b>"
        ),
        "update_required": (
            "<emoji document_id=5424728541650494040>đ</emoji> <b>Đ¯ŌŖĐ°ŅŅŅĐģŅ"
            " ŅĐ°ĐģĶĐŋ Đ¸ŅĐĩĐģĶ</b><code>.update</code>"
        ),
        "_cfg_cst_msg": (
            "Đ¨ĶŅŅĐ¸ ŅĶĐąĶŅ ĐŧĶĐŗŅĐģŌ¯ĐŧĐ°ŅŅ. {me}, {version}, {build}, {prefix}, {platform},"
            " {upd}, {uptime}, {cpu_usage}, {ram_usage}, {branch} ĐēŌ¯ŅĐĩŅĐŧĶĐģĶŅĐĩĐŊ ŌĐ¸ĐąĶŅŌ¯"
            " ĐŧĶŠĐŧĐēĐ¸ĐŊ"
        ),
        "_cfg_cst_btn": "Đ¨ĶŅŅĐ¸ ŅĶŠĐšĐŧĶ ĐŧĶĐŗŅĐģŌ¯ĐŧĐ°ŅŅ. ĐĸĶŠĐšĐŧĶĐŊĐĩ ŅĐšĐŧĐ°ĐŗŅŅ, ĐąŅŅ ŌĐ¸ĐąĶŅŌ¯",
        "_cfg_banner": "ĐĄŌ¯ŅĶŅ URL-Ņ",
        "setinfo_no_args": (
            "<emoji document_id=5370881342659631698>đĸ</emoji> <b>ĐĶĐŗŅĐģŌ¯ĐŧĐ°ŅĐŊŅ"
            " Ō¯ĐˇĐŗĶŅŅŌ¯ ĶŠŅĐĩĐŊ, ĐŧĶĐŗŅĐģŌ¯ĐŧĐ°ŅĐŊŅ ĐēĐĩŅŅĐĩĐŗĐĩĐˇ</b>"
        ),
        "setinfo_success": (
            "<emoji document_id=5436040291507247633>đ</emoji> <b>ĐĶĐŗŅĐģŌ¯ĐŧĐ°Ņ"
            " ĐŧĶŠĐŧĐēĐ¸ĐŊ ĐąŅĐģĐ´Ņ</b>"
        ),
        "desc": (
            "<emoji document_id=6318565919471699564>đ</emoji> <b>Hikka</b>\n\nĐŅĐģĐģĐ°ĐŊŅŅŅ"
            " ĐąĐžŅŅ ĐŧĐžĐŊĐ´Đ° ĐąĐĩŅ ĐēĶŠĐšĐģĶŌ¯ĐģĶŅĐŊĐĩ ĐēŌ¯ŅŅĶŅĶ: ĐžĐŊĐģĐ°ĐšĐŊ ĐŗĐ°ĐģĐĩŅĐĩŅ, ŅĐžŅĐŧĐ°, ŅĶĐ˛ĐĩŅŅĶ,"
            " ŅĐŧĐžĐ´ĐļĐ¸ ŌģĶĐŧ ĐąĐ°ŅĐēĐ°ĐģĐ°ŅŅ. ĐŅĐģĐģĐ°ĐŊŅŅŅ ĐąĐžŅŅ Telegram Đ°ĐēĐēĐ°ŅĐŊŅŅĐŊĐ´Đ° Đ¸ŅĶĐŋĐģĶĐŊĶ. Đ§Đ°Ņ"
            " ĶŠŅĐĩĐŊ ĐēŌ¯ŅŅĶŅĐŧĶĐģĶŅ Đ°ŅĐ°ĐąŅĐŊŅĐ° Đ¸ŅĶĐŋĐģĶĐŊĶ. ĐĐ°ŅĐēĐ° ĐŧĶĐŗŅĐģŌ¯ĐŧĐ°Ņ ĶŠŅĐĩĐŊ <a href="
            '"https://github.com/hikariatama/Hikka">GitHub</a>'
        ),
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "custom_message",
                doc=lambda: self.strings("_cfg_cst_msg"),
            ),
            loader.ConfigValue(
                "custom_button",
                ["đ Support chat", "https://t.me/hikka_talks"],
                lambda: self.strings("_cfg_cst_btn"),
                validator=loader.validators.Union(
                    loader.validators.Series(fixed_len=2),
                    loader.validators.NoneType(),
                ),
            ),
            loader.ConfigValue(
                "banner_url",
                "https://github.com/hikariatama/assets/raw/master/hikka_banner.mp4",
                lambda: self.strings("_cfg_banner"),
                validator=loader.validators.Link(),
            ),
        )

    def _render_info(self, inline: bool) -> str:
        try:
            repo = git.Repo(search_parent_directories=True)
            diff = repo.git.log([f"HEAD..origin/{version.branch}", "--oneline"])
            upd = (
                self.strings("update_required") if diff else self.strings("up-to-date")
            )
        except Exception:
            upd = ""

        me = '<b><a href="tg://user?id={}">{}</a></b>'.format(
            self._client.hikka_me.id,
            utils.escape_html(get_display_name(self._client.hikka_me)),
        )
        build = utils.get_commit_url()
        _version = f'<i>{".".join(list(map(str, list(version.__version__))))}</i>'
        prefix = f"ÂĢ<code>{utils.escape_html(self.get_prefix())}</code>Âģ"

        platform = utils.get_named_platform()

        for emoji, icon in {
            "đ": "<emoji document_id=5449599833973203438>đ§Ą</emoji>",
            "đ": "<emoji document_id=5449468596952507859>đ</emoji>",
            "â": "<emoji document_id=5407025283456835913>đą</emoji>",
            "đ": "<emoji document_id=6332120630099445554>đ</emoji>",
            "đĻž": "<emoji document_id=5386766919154016047>đĻž</emoji>",
            "đ": "<emoji document_id=5359595190807962128>đ</emoji>",
            "đŗ": "<emoji document_id=5431815452437257407>đŗ</emoji>",
            "đļ": "<emoji document_id=5407025283456835913>đą</emoji>",
            "đââŦ": "<emoji document_id=6334750507294262724>đââŦ</emoji>",
            "âī¸": "<emoji document_id=5469986291380657759>âī¸</emoji>",
            "đģ": "<emoji document_id=5471952986970267163>đ</emoji>",
        }.items():
            platform = platform.replace(emoji, icon)

        return (
            (
                "<b>đ Hikka</b>\n"
                if "hikka" not in self.config["custom_message"].lower()
                else ""
            )
            + self.config["custom_message"].format(
                me=me,
                version=_version,
                build=build,
                prefix=prefix,
                platform=platform,
                upd=upd,
                uptime=utils.formatted_uptime(),
                cpu_usage=utils.get_cpu_usage(),
                ram_usage=f"{utils.get_ram_usage()} MB",
                branch=version.branch,
            )
            if self.config["custom_message"]
            else (
                f'<b>{{}}</b>\n\n<b>{{}} {self.strings("owner")}:</b> {me}\n\n<b>{{}}'
                f" {self.strings('version')}:</b> {_version} {build}\n<b>{{}}"
                f" {self.strings('branch')}:"
                f"</b> <code>{version.branch}</code>\n{upd}\n\n<b>{{}}"
                f" {self.strings('prefix')}:</b> {prefix}\n<b>{{}}"
                f" {self.strings('uptime')}:"
                f"</b> {utils.formatted_uptime()}\n\n<b>{{}}"
                f" {self.strings('cpu_usage')}:"
                f"</b> <i>~{utils.get_cpu_usage()} %</i>\n<b>{{}}"
                f" {self.strings('ram_usage')}:"
                f"</b> <i>~{utils.get_ram_usage()} MB</i>\n<b>{{}}</b>"
            ).format(
                *map(
                    lambda x: utils.remove_html(x) if inline else x,
                    (
                        utils.get_platform_emoji()
                        if self._client.hikka_me.premium and not inline
                        else "đ Hikka",
                        "<emoji document_id=5373141891321699086>đ</emoji>",
                        "<emoji document_id=5469741319330996757>đĢ</emoji>",
                        "<emoji document_id=5449918202718985124>đŗ</emoji>",
                        "<emoji document_id=5472111548572900003>â¨ī¸</emoji>",
                        "<emoji document_id=5451646226975955576>âī¸</emoji>",
                        "<emoji document_id=5431449001532594346>âĄī¸</emoji>",
                        "<emoji document_id=5359785904535774578>đŧ</emoji>",
                        platform,
                    ),
                )
            )
        )

    def _get_mark(self):
        return (
            {
                "text": self.config["custom_button"][0],
                "url": self.config["custom_button"][1],
            }
            if self.config["custom_button"]
            else None
        )

    @loader.inline_handler(
        thumb_url="https://img.icons8.com/external-others-inmotus-design/344/external-Moon-round-icons-others-inmotus-design-2.png"
    )
    @loader.inline_everyone
    async def info(self, _: InlineQuery) -> dict:
        """Send userbot info"""

        return {
            "title": self.strings("send_info"),
            "description": self.strings("description"),
            **(
                {"photo": self.config["banner_url"], "caption": self._render_info(True)}
                if self.config["banner_url"]
                else {"message": self._render_info(True)}
            ),
            "thumb": (
                "https://github.com/hikariatama/Hikka/raw/master/assets/hikka_pfp.png"
            ),
            "reply_markup": self._get_mark(),
        }

    @loader.command(
        ru_doc="ĐŅĐŋŅĐ°Đ˛ĐģŅĐĩŅ Đ¸ĐŊŅĐžŅĐŧĐ°ŅĐ¸Ņ Đž ĐąĐžŅĐĩ",
        it_doc="Invia informazioni sul bot",
        de_doc="Sendet Informationen Ãŧber den Bot",
        tr_doc="Bot hakkÄąnda bilgi gÃļnderir",
        uz_doc="Bot haqida ma'lumot yuboradi",
        es_doc="EnvÃ­a informaciÃŗn sobre el bot",
        kk_doc="ĐĐžŅ ŅŅŅĐ°ĐģŅ Đ°ŌĐŋĐ°ŅĐ°Ņ ĐļŅĐąĐĩŅĐĩĐ´Ņ",
    )
    @loader.unrestricted
    async def infocmd(self, message: Message):
        """Send userbot info"""

        if self.config["custom_button"]:
            await self.inline.form(
                message=message,
                text=self._render_info(True),
                reply_markup=self._get_mark(),
                **(
                    {"photo": self.config["banner_url"]}
                    if self.config["banner_url"]
                    else {}
                ),
            )
        else:
            await utils.answer_file(
                message,
                self.config["banner_url"],
                self._render_info(False),
            )

    @loader.unrestricted
    @loader.command(
        ru_doc="ĐŅĐŋŅĐ°Đ˛Đ¸ŅŅ Đ¸ĐŊŅĐžŅĐŧĐ°ŅĐ¸Ņ ĐŋĐž ŅĐ¸ĐŋŅ 'Đ§ŅĐž ŅĐ°ĐēĐžĐĩ ĐĨĐ¸ĐēĐēĐ°?'",
        it_doc="Invia informazioni del tipo 'Cosa Ã¨ Hikka?'",
        de_doc="Sende Informationen Ãŧber den Bot",
        tr_doc="Bot hakkÄąnda bilgi gÃļnderir",
        uz_doc="Bot haqida ma'lumot yuborish",
        es_doc="Enviar informaciÃŗn sobre el bot",
        kk_doc="ĐĐžŅ ŅŅŅĐ°ĐģŅ Đ°ŌĐŋĐ°ŅĐ°Ņ ĐļŅĐąĐĩŅŅ",
    )
    async def hikkainfo(self, message: Message):
        """Send info aka 'What is Hikka?'"""
        await utils.answer(message, self.strings("desc"))

    @loader.command(
        ru_doc="<ŅĐĩĐēŅŅ> - ĐĐˇĐŧĐĩĐŊĐ¸ŅŅ ŅĐĩĐēŅŅ Đ˛ .info",
        it_doc="<testo> - Cambia il testo in .info",
        de_doc="<text> - Ãndere den Text in .info",
        tr_doc="<metin> - .info'da metni deÄiÅtir",
        uz_doc="<matn> - .info'dagi matnni o'zgartirish",
        es_doc="<texto> - Cambiar el texto en .info",
        kk_doc="<ĐŧĶŅŅĐŊ> - .info ĐŧĶŅŅĐŊŅĐŊ ĶŠĐˇĐŗĐĩŅŅŅ",
    )
    async def setinfo(self, message: Message):
        """<text> - Change text in .info"""
        args = utils.get_args_html(message)
        if not args:
            return await utils.answer(message, self.strings("setinfo_no_args"))

        self.config["custom_message"] = args
        await utils.answer(message, self.strings("setinfo_success"))
