from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()


class Register(StatesGroup):
    name = State()
    age = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('✨ Добро пожаловать в магазин гирлянд из букв! ✨', reply_markup=kb.main)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Выберите нужный раздел в меню.')

@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите материал гирлянды:', reply_markup=kb.catalog)

@router.callback_query(F.data.startswith('material_'))
async def material_selected(callback: CallbackQuery):
    material = callback.data.split('_')[1]
    materials_info = {
        'cardboard': 'Картон: лёгкий, матовый, подходит для интерьера.',
        'plastic': 'Пластик: прочный, можно использовать на улице.',
        'plywood': 'Фанера: натуральный материал, можно красить.',
        'metal': 'Металл: стильный и долговечный вариант.',
    }
    await callback.answer('✅ Вы выбрали материал')
    await callback.message.answer(materials_info[material])

@router.message(F.text == 'Общая информация')
async def general_info(message: Message):
    await message.answer('Выберите вопрос:', reply_markup=kb.general_info)

@router.message(F.text == 'Заказ и доставка')
async def delivery_info(message: Message):
    await message.answer('Выберите вопрос по доставке:', reply_markup=kb.delivery)

@router.message(F.text == 'Оплата')
async def payment_info(message: Message):
    await message.answer('Выберите вопрос по оплате:', reply_markup=kb.payment)

@router.message(F.text == 'Возврат и гарантии')
async def returns_info(message: Message):
    await message.answer('Выберите вопрос по возврату:', reply_markup=kb.returns)

@router.message(F.text == 'Контакты и поддержка')
async def contacts_info(message: Message):
    await message.answer('Как с нами связаться:', reply_markup=kb.contacts)

@router.callback_query(F.data == 'info_what_is')
async def what_is_garland(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "Гирлянда из букв — это декоративная гирлянда, состоящая из отдельных букв, цифр или символов. "
        "Используется для украшения интерьеров, фотосессий, свадеб и праздников."
    )
