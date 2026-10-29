from aiogram import Router, types, filters
rt = Router()
@rt.message()
async def forward_date(msg: types.Message):
    print(msg.forward_date)