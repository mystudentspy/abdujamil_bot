from aiogram import Router, types, filters
import datetime
rt = Router()
@rt.message()
async def test(msg: types.Message):
   print(msg.forward_from_message_id)

