import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    msg = (f'Hey, {message.from_user.full_name} this is bot for voting to best teacher. '
           'To see all commands print /help'
    )
    await message.answer(msg)


@dp.message(Command('help'))
async def command_help_handler(message: Message) -> None:
    msg = '''
    Available commands:
        /help - show help
        /start - start bot
        /vote - vote to teacher
    '''
    await message.answer(msg)

@dp.message(Command('vote'))
async def command_vote_handler(message: Message) -> None:
    msg = 'Start vote'
    await message.answer(msg)
    

@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    