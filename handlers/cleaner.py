# ππππ ππππ ππππ πππππ πππππππππ @SHAILENDRA34 | 
# ππππ« πππ«π¨ π©π©π₯π¬ ππ₯π’π¬π‘ ππ¨π§'π­ π«ππ¦π¨π―π π­π‘π’π¬ π₯π’π§π ππ«π¨π¦ π‘ππ«π π


import os
from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.filters import command, other_filters
from helpers.decorators import authorized_users_only, errors
from helpers.filters import command, other_filters

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command(["rmf"]) & other_filters)
@errors
@authorized_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("`π BΓΌtΓΌn endirilmiΕ fayllar silindi `")
    else:
        await message.reply_text("`FaylΔ±n tΙmizlΙndiyi tapΔ±ldΔ±`")

        
@Client.on_message(command(["rmw"]) & other_filters)
@errors
@authorized_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw_files)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("`TΙmizlik qurulur ποΈ`")
    else:
        await message.reply_text("`Fayllar hazΔ±rdΔ±r`")


@Client.on_message(command(["clean"]) & other_filters)
@errors
@authorized_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("`β TΙmizlΙndi`")
    else:
        await message.reply_text("`β TΙmizlΙmΙ uΔurludur`")
