import requests 
import logging
import re

from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup


API_TOKEN = 'token'
logging.basicConfig(level=logging.INFO)
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

HOST = 'https://steamcommunity.com/'
URL = 'https://store.steampowered.com/specials#tab=TopSellers'
HEADERS = {
	'title' : 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}


def get_html(url, params=''):
	r = requests.get(url, headers = HEADERS, params = params)
	return r


def get_content(html):
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find('div', id='TopSellersRows').find_all('a', class_='tab_item')
	cards = []

	for item in items:
		cards.append ({
			'lol' : soup.find('a', class_='tab_item').get('href'),
			'title' : item.find('div', class_='tab_item_name').get_text(strip = True),
			})
	

html = get_html(URL)
lol = get_content(html.text)
title = get_content(html.text)



@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(title)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)













