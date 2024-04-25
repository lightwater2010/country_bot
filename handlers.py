from aiogram import types, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from countryinfo import CountryInfo
from translate import Translator
from keyboards import kb


router = Router()

class Country(StatesGroup):
    name = State()

@router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Привет!", reply_markup=kb)
@router.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("<b>/start</b> - начало\n<b>/help</b> - список команд\n<b>/search</b> - поиск страны", parse_mode="HTML")
@router.message(Command("search"))
async def search_1(message: types.Message, state: FSMContext):
    await state.set_state(Country.name)
    await message.answer("Введите название страны:")
@router.message(Country.name)
async def search_2(message: types.Message, state: FSMContext):
    translater = Translator(from_lang="ru", to_lang="en")
    country_name = translater.translate(message.text)
    await state.update_data(name=country_name)
    try:
        data = await state.get_data()
        country = CountryInfo(data['name'])
        name = country.name()
        capital = country.capital()
        population = country.population()
        currencies = ', '.join(country.currencies())
        timezones = ', '.join(country.timezones())
        region = country.region()
        languages = ', '.join(country.languages())
        await message.answer(f'{message.text.title()}, {region}:\nСтолица: {capital}\nНаселение: {population} человек\nВалюты: {currencies}\nЧасовые пояса: {timezones}\nЯзыки: {languages.upper()}')
        await state.clear()
    except KeyError:
        await message.answer("Извините но такой страны нет")
@router.message()
async def messages(message: types.Message):
    await message.answer("Извините я вас не понимаю")
