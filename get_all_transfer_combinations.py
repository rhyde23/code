"""
#Change these to include more later, just testing
rating_factors = list(reversed(list(range(75, 85))))
age_factors = list(reversed(list(range(22, 27))))
position_factors = [
	'GK', 
	'RWB', 
	'LWB', 
	'LB', 
	'RB', 
	'CB', 
	'CM', 
	'CDM', 
	'CAM',
	'CF', 
	'LM', 
	'LW',
	'RM', 
	'RW',
	'ST'
]

transfer_combinations = {}


for position_factor in position_factors :
	for rating_factor in rating_factors :
		for age_factor in age_factors :
			transfer_combinations['|'.join([position_factor, str(rating_factor), str(age_factor)])] = []

print(transfer_combinations)
"""

import requests, re, html
from bs4 import BeautifulSoup


def form_link(page_number) :
	return 'https://www.fifacm.com/players?page='+str(page_number)+'&leagues=13'

def scrape(link) :
    page = requests.get(link)
    soup = html.unescape(str(BeautifulSoup(page.content, 'html.parser')))
    return soup

def main() :
	transfer_combinations = {}
	for page_number in range(1, 23) :
		soup = scrape(form_link(page_number))
		names = [name for name in re.findall('>[^<>]+</a> </div>', soup)[4:][:-2] if name != '> </a> </div>']
		print(names)
		for i in range(len(names)) :
			try :
				section_of_code = soup.split(names[i])[1].split(names[i+1])[0]
			except :
				section_of_code = soup.split(names[i])[1].split('Exclude Results')[0]
			displayed = [dis.replace(' ', '').replace('>', '').replace('<', '') for dis in re.findall('>[^<>]+<', section_of_code) if not dis in ['> <', '> | <', '> R.Face<', '>|<']]
			displayed[0] = displayed[0].split(',')[0]
			value = displayed[6][1:]
			k_replaced = '000'
			m_replaced = '000000'
			if '.' in value :
				point = value.split('.')[1][:-1]
				k_replaced = k_replaced[:-(len(point))]
				m_replaced = m_replaced[:-(len(point))]
			value = value.replace('K', k_replaced).replace('M', m_replaced).replace('.', '')
			displayed[6] = int(value)
			position, rating, age, value = displayed[0], int(displayed[2]), int(displayed[5]), int(displayed[6])
			key = '|'.join([position, rating, age])
			if key in transfer_combinations :
				transfer_combinations[key].append(value)
			else :
				transfer_combinations[key] = [[value]]
			print(position, rating, age, value)
			print()
			print()
			print()
			print()
			print()
		#print(names)
		quit()

main()
