import requests

teams_adress_A = {'palmeiras' : 'palmeiras/1963', 'internacional' : 'internacional/1966', 'flamengo' : 'flamengo/5981', 'fluminense' : 'fluminense/1961',
'corinthians' : 'corinthians/1957', 'athletico paranaense' : 'athletico/1967', 'atletico mineiro' : 'atletico-mineiro/1977',
'america mineiro' : 'america-mineiro/1973', 'fortaleza' : 'fortaleza/2020', 'botafogo' : 'botafogo/1958', 'santos' : 'santos/1968',
'sao paulo' : 'sao-paulo/1981', 'bragantino' : 'red-bull-bragantino/1999', 'goias' : 'goias/1960', 'coritiba' : 'coritiba/1982',
'ceara' : 'ceara/2001', 'cuiaba' : 'cuiaba/49202', 'atletico goianiense' : 'atletico-goianiense/7314', 'avai' : 'avai/7315', 'juventude' : 'juventude/1980'}

teams_adress_B = {'cruzeiro' : 'cruzeiro/1954', 'gremio' : 'gremio/5926', 'vasco' : 'vasco-da-gama/1974', 'bahia' : 'bahia/1955', 'ituano' : 'ituano/2025',
'londrina' : 'londrina/2022', 'sport' : 'sport-recife/1959', 'sampaio correa' : 'sampaio-correa/2005', 'criciuma' : 'criciuma/1984', 'crb' : 'crb/22032',
'guarani' : 'guarani/1972', 'vila nova' : 'vila-nova/2021',  'ponte preta' : 'ponte-preta/1969', 'tombense' : 'tombense/87202', 'chapecoense' : 'chapecoense/21845',
'csa' : 'csa/2010', 'novorizontino' : 'novorizontino/135514', 'brusque' : 'brusque-fc/21884', 'operario' : 'operario/39634', 'nautico' : 'nautico/2011'}

browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}

base_api = 'https://api.sofascore.com/api/v1/team/'
end_api = '/statistics/overall'

def choose_team(time: str):
  data_list = []
  cont_url_list = 0
  cont_data_list = 0

  division = input(str('Em qual divisão está o time? ')).upper()

  if division == 'A':
    serie = '325'
    id_team = teams_adress_A[time.lower()][-4:]
    enpoint_17 = '13100'
    enpoint_18 = '16183'
    enpoint_19 = '22931'
    enpoint_20 = '27591'
    enpoint_21 = '36166'
    enpoint_22 = '40557'

  elif division == 'B':
    serie = '390'
    id_time = teams_adress_B[time.lower()][-4:]
    enpoint_17 = ''
    enpoint_18 = '16184'
    enpoint_19 = '22932'
    enpoint_20 = '27593'
    enpoint_21 = '36162'
    enpoint_22 = '40560'

  middle_api = f'/unique-tournament/{serie}/season/'

  url_17 = base_api + id_time + middle_api + enpoint_17 + end_api
  url_18 = base_api + id_time + middle_api + enpoint_18 + end_api
  url_19 = base_api + id_time + middle_api + enpoint_19 + end_api
  url_20 = base_api + id_time + middle_api + enpoint_20 + end_api
  url_21 = base_api + id_time + middle_api + enpoint_21 + end_api
  url_22 = base_api + id_time + middle_api + enpoint_22 + end_api

  urls_list = [url_17, url_18, url_19, url_20, url_21, url_22]

  for url in urls_list:
    api_link = requests.get(url, headers = browsers).json()
    if not 'error' in api_link:
        data_list.append(api_link['statistics'])
        if urls_list.index(urls_list[cont_url_list]) == 0:
            data_list[cont_data_list]['ano'] = 2017
        elif urls_list.index(urls_list[cont_url_list]) == 1:
            data_list[cont_data_list]['ano'] = 2018
        elif urls_list.index(urls_list[cont_url_list]) == 2:
            data_list[cont_data_list]['ano'] = 2019
        elif urls_list.index(urls_list[cont_url_list]) == 3:
            data_list[cont_data_list]['ano'] = 2020
        elif urls_list.index(urls_list[cont_url_list]) == 4:
            data_list[cont_data_list]['ano'] = 2021
        elif urls_list.index(urls_list[cont_url_list]) == 5:
            data_list[cont_data_list]['ano'] = 2022
        
        cont_data_list+=1
    cont_url_list+=1

  return data_list