from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("pishak"))
async def mushuk(msg: types.Message):
    await msg.answer("")