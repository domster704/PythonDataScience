import eel
from programs_parser import domofond_parser

eel.init('web')
city = {
			"Камчатский край": "1",
			"Марий Эл": "2",
			"Чечня": "3",
			"Оренбургская область": "4",
			"Ямало-Ненецкий АО": "5",
			"Забайкальский край": "6",
			"Ярославская область": "7",
			"Владимирская область": "8",
			"Бурятия": "9",
			"Калмыкия": "10",
			"Белгородская область": "11",
			"Вологодская область": "12",
			"Волгоградская область": "13",
			"Калужская область": "14",
			"Ингушетия": "15",
			"Кабардино-Балкария": "16",
			"Иркутская область": "17",
			"Ивановская область": "18",
			"Астраханская область": "19",
			"Карачаево-Черкесия": "20",
			"Новгородская область": "21",
			"Курганская область": "22",
			"Костромская область": "23",
			"Краснодарский край": "24",
			"Магаданская область": "25",
			"Нижегородская область": "26",
			"Кировская область": "27",
			"Липецкая область": "28",
			"Мурманская область": "29",
			"Курская область": "30",
			"Мордовия": "31",
			"Хакасия": "32",
			"Карелия": "33",
			"Якутия": "34",
			"Татарстан": "35",
			"Адыгея": "36",
			"Омская область": "37",
			"Пензенская область": "38",
			"Псковская область": "39",
			"Северная Осетия": "40",
			"Башкортостан": "41",
			"Пермский край": "42",
			"Ростовская область": "43",
			"Дагестан": "44",
			"Приморский край": "45",
			"Орловская область": "46",
			"Томская область": "47",
			"Тверская область": "48",
			"Удмуртия": "49",
			"Ставропольский край": "50",
			"Ульяновская область": "51",
			"Хабаровский край": "52",
			"Смоленская область": "53",
			"Ханты-Мансийский АО": "54",
			"Челябинская область": "55",
			"Самарская область": "56",
			"Тульская область": "57",
			"Тамбовская область": "58",
			"Тюменская область": "59",
			"Свердловская область": "60",
			"Сахалинская область": "61",
			"Рязанская область": "62",
			"Республика Алтай": "63",
			"Чувашия": "64",
			"Чукотский АО": "65",
			"Брянская область": "66",
			"Еврейская АО": "67",
			"Алтайский край": "68",
			"Калининградская область": "69",
			"Архангельская область": "70",
			"Кемеровская область": "71",
			"Амурская область": "72",
			"Воронежская область": "73",
			"Красноярский край": "74",
			"Ненецкий АО": "75",
			"Тыва": "76",
			"Коми": "77",
			"Новосибирская область": "78",
			"Саратовская область": "79",
			"Ленинградская область": "80",
			"Московская область": "81",
			"Крым": "82",
		}


@eel.expose
def neuronet_with_url(url):
	data = domofond_parser.get_data_by_link(url)
	print(data)
	from new_tens import getDataFromReadyNeural
	per = getDataFromReadyNeural(data)
	print(per)
	return [round(per), data[2]]


@eel.expose
def neuronet_with_list_url(list_url):
	data = []
	for i in list_url:
		data.append(domofond_parser.get_data_by_link(i))

	from new_tens import getDataFromReadyNeural
	list_cost = []
	for i in data:
		list_cost.append(getDataFromReadyNeural(i))

	for i in range(len(data)):
		data[i].append(list_cost[i])
	print([round(min(list_cost), 2), list_cost.index(min(list_cost))])
	return [data, round(min(list_cost), 2), list_cost.index(min(list_cost))]


@eel.expose
def neuronet_with_data(data):
	data[-1] = city[data[-1]]
	print(data)
	from new_tens import getDataFromReadyNeural
	per = getDataFromReadyNeural(data)
	print(per)
	return round(per)


eel.start('index.html', size=(1024, 720))
