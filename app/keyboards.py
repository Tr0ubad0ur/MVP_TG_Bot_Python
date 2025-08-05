from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Общая информация')],
    [KeyboardButton(text='Заказ и доставка')],
    [KeyboardButton(text='Оплата')],
    [KeyboardButton(text='Возврат и гарантии')],
    [KeyboardButton(text='Контакты и поддержка')],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню...')


catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Картон', callback_data='material_cardboard')],
    [InlineKeyboardButton(text='Пластик', callback_data='material_plastic')],
    [InlineKeyboardButton(text='Фанера', callback_data='material_plywood')],
    [InlineKeyboardButton(text='Металл', callback_data='material_metal')],
])

general_info = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Что такое гирлянда из букв?', callback_data='info_what_is')],
    [InlineKeyboardButton(text='Материалы изготовления', callback_data='info_materials')],
    [InlineKeyboardButton(text='Размеры букв', callback_data='info_sizes')],
])

delivery = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Как сделать заказ?', callback_data='delivery_order')],
    [InlineKeyboardButton(text='Способы доставки', callback_data='delivery_methods')],
    [InlineKeyboardButton(text='Стоимость доставки', callback_data='delivery_cost')],
    [InlineKeyboardButton(text='Сроки изготовления', callback_data='delivery_time')],
])

payment = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Способы оплаты', callback_data='payment_methods')],
    [InlineKeyboardButton(text='Оплата при получении', callback_data='payment_on_delivery')],
])

returns = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Товар с дефектом', callback_data='return_defect')],
    [InlineKeyboardButton(text='Возврат товара', callback_data='return_refund')],
])

contacts = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Написать в WhatsApp', url='https://wa.me/номер')],
    [InlineKeyboardButton(text='Написать в Telegram', url='tg://resolve?domain=ник_менеджера')],
    [InlineKeyboardButton(text='Позвонить', callback_data='call_phone')],
])
