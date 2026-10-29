from aiogram import Router, types, F
rt = Router()
@rt.message(F.text)
async def text(msg: types.Message):
    await msg.answer("bu matn")