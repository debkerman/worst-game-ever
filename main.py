import sys
import time
import pygame

pygame.init()
W = 1280
H = 720

sc = pygame.display.set_mode((W,H))
fps = 5
start_time = time.time()
stock = []
money = 0
date =[1,1,2200]
calender = [31,28,31,30,31,30,31,31,30,31,30,31]
clock = pygame.time.Clock()
day = 1


def datechange():
    if date[0] <= calender[date[1] - 1]:
        date[0] += 1
    if date[0]  > calender[date[1] - 1]:
        if date[1] != 12:
            date[0] = 1
            date[1] += 1
        else:
            date[0], date[1] = 1, 1
            date[2] += 1


def trade():
    tmp_money = 0
    for i in range(0,len(resources)):
        if resources[str(i)]['trade amount'] != 0:
            resources[str(i)]['stockpile'] += resources[str(i)]['trade amount']
            tmp_money += resources[str(i)]['trade amount'] * resources[str(i)]['cost']
        else:
            tmp_money += resources[str(i)]['stockpile'] * resources[str(i)]['cost']
            resources[str(i)]['stockpile'] = 0
    return(tmp_money)


def production():
    for i in range(0,len(buildings)):
        if buildings[str(i)]['level'] != 0 and buildings[str(i)]['active'] == True:
            for j in range(0,len(buildings[str(i)]['production'])):
                a = buildings[str(i)]['production amount'][j]
                b = buildings[str(i)]['level']
                resources[buildings[str(i)]['production'][j]]['production amount'] = (a * b)
        else:
            pass


def consumption():
    for i in range(0,len(buildings)):
        if buildings[str(i)]['level'] != 0 and buildings[str(i)]['active'] == True:
            for j in range(0,len(buildings[str(i)]['consumption'])):
                if buildings[str(i)]['consumption'][j] != 'none':
                    a = buildings[str(i)]['consumption amount'][j]
                    b = buildings[str(i)]['level']
                    resources[buildings[str(i)]['consumption'][j]]['consumption amount'] = (a * b)
                else:
                    pass
        else:
            pass


def stockpile():
    for i in range(0,len(resources)):
        resources[str(i)]['stockpile'] += resources[str(i)]['production amount'] - resources[str(i)]['consumption amount']


def energy():
    tmp = 0
    for i in range(0,len(buildings)):
        if buildings[str(i)]['active'] == True:
            tmp += buildings[str(i)]['energy consumption'] * buildings[str(i)]['level']
    return(tmp)


resources = {'0': {'name': 'iron ore', 'cost': 105, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': True, 'trade amount': 0},
             '1': {'name': 'copper ore', 'cost': 4400, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '2': {'name': 'aluminum ore', 'cost': 300 ,'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '3': {'name': 'tin ore', 'cost': 11000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '4': {'name': 'lead ore', 'cost': 800, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '5': {'name': 'chrome ore', 'cost': 140, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '6': {'name': 'nickel ore', 'cost': 49, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '7': {'name': 'titanium ore', 'cost': 4800, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '8': {'name': 'magnesium ore', 'cost': 280, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '9': {'name': 'rare earth metals ore', 'cost': 8000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '10': {'name': 'lithium ore', 'cost': 10000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '11': {'name': 'tungsten ore', 'cost': 180, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '12': {'name': 'uranium ore', 'cost': 78000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '13': {'name': 'cobalt ore', 'cost': 30000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '14': {'name': 'boron ore', 'cost': 4200, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '15': {'name': 'zinc ore', 'cost': 2450, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '16': {'name': 'silver ore', 'cost': 565530, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '17': {'name': 'gold', 'cost': 64300000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '18': {'name': 'graphite', 'cost': 1600, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '19': {'name': 'gems', 'cost': 8000000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '20': {'name': 'platinum', 'cost': 27000000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '21': {'name': 'salt', 'cost': 250, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '22': {'name': 'clay', 'cost': 17, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '23': {'name': 'sand', 'cost': 30, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '24': {'name': 'building stone', 'cost': 50,'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '25': {'name': 'sulfur', 'cost': 500, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '26': {'name': 'wheat', 'cost': 200, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '27': {'name': 'corn', 'cost': 110, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '28': {'name': 'sunflower', 'cost': 240, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '29': {'name': 'rice', 'cost': 300, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '30': {'name': 'buckwheat', 'cost': 240, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '31': {'name': 'onion', 'cost': 400, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '32': {'name': 'potato', 'cost': 150, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '33': {'name': 'cabbage', 'cost': 280, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '34': {'name': 'carrot', 'cost': 200, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '35': {'name': 'tomato', 'cost': 350, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '36': {'name': 'pumpkin', 'cost': 210, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '37': {'name': 'cucumber', 'cost': 300, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '38': {'name': 'soy', 'cost': 150, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '39': {'name': 'peas', 'cost': 250, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '40': {'name': 'cotton', 'cost': 1500, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '41': {'name': 'linen', 'cost': 1200, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '42': {'name': 'grape', 'cost': 1800, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '43': {'name': 'tea', 'cost': 25000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '44': {'name': 'coffee', 'cost': 15000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '45': {'name': 'lemon', 'cost': 1900, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '46': {'name': 'orange', 'cost': 1700, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '47': {'name': 'olive', 'cost': 500, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '48': {'name': 'mushrooms', 'cost': 450, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '49': {'name': 'raspberry', 'cost': 750, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '50': {'name': 'strawberry', 'cost': 800, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '51': {'name': 'watermelon', 'cost': 100, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '52': {'name': 'beetroot', 'cost': 100, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '53': {'name': 'kiwi', 'cost': 450, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '54': {'name': 'plum', 'cost': 500, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '55': {'name': 'cherry', 'cost': 650, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '56': {'name': 'apple', 'cost': 400, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '57': {'name': 'apricot', 'cost': 800, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '58': {'name': 'pear', 'cost': 800, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '59': {'name': 'walnut', 'cost': 1500, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '60': {'name': 'spices', 'cost': 30000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '61': {'name': 'caoutchouc', 'cost': 2000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '62': {'name': 'chicken meat', 'cost': 2000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '63': {'name': 'chicken egg', 'cost': 1250, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '64': {'name': 'rabbit meat', 'cost': 2500, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '65': {'name': 'rabbit hide', 'cost': 4000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '66': {'name': 'duck meat', 'cost': 2800, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '67': {'name': 'lamb meat', 'cost': 2000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '68': {'name': 'wool', 'cost': 1800, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '69': {'name': 'turkey meat', 'cost': 2200, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '70': {'name': 'pork', 'cost': 1800, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '71': {'name': 'cow milk', 'cost': 2000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '72': {'name': 'cow hide', 'cost': 1200, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '73': {'name': 'pork', 'cost': 1500, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '74': {'name': 'freshwater fish', 'cost': 1800, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '75': {'name': 'saltwater fish', 'cost': 1900, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '76': {'name': 'crustaceans', 'cost': 2800, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '77': {'name': 'green algae', 'cost': 1800, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '78': {'name': 'brown algae', 'cost': 500, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '79': {'name': 'chem algae', 'cost': 650, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '80': {'name': 'bamboo', 'cost': 40, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '81': {'name': 'poplar', 'cost': 80, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '82': {'name': 'oak', 'cost': 110, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '83': {'name': 'aspen', 'cost': 50, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '84': {'name': 'pine', 'cost': 75, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '85': {'name': 'cedar', 'cost': 300, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '86': {'name': 'flour', 'cost': 300, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '87': {'name': 'vegetable oil', 'cost': 1000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '88': {'name': 'pasta', 'cost': 340, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '89': {'name': 'bread', 'cost': 350, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '90': {'name': 'cereals', 'cost': 330, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '91': {'name': 'canned food', 'cost': 500, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '92': {'name': 'cheese', 'cost': 4000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '93': {'name': 'vinegar', 'cost': 150, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '94': {'name': 'alcohol', 'cost': 600, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '95': {'name': 'leather', 'cost': 5000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '96': {'name': 'nutrients', 'cost': 50, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '97': {'name': 'paper', 'cost': 1000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '98': {'name': 'compost', 'cost': 10, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '99': {'name': 'fertilizer', 'cost': 50, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '100': {'name': 'canned food', 'cost': 1000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '101': {'name': 'jam', 'cost': 1200, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '102': {'name': 'juice', 'cost': 2000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '103': {'name': 'leather', 'cost': 5000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '104': {'name': 'textile', 'cost': 2000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '105': {'name': 'rubber', 'cost': 8000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '106': {'name': 'medicine', 'cost': 5000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '107': {'name': 'steel', 'cost': 610, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': True, 'trade amount': 0},
             '108': {'name': 'aluminum', 'cost': 1600, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '109': {'name': 'titanium', 'cost': 20000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '110': {'name': 'magnesium', 'cost': 2700, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '111': {'name': 'processed rare earth metals', 'cost': 30000, 'production amount': 0, 'stockpile': 0, 'consumption amount': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '112': {'name': 'quartz', 'cost': 800, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '113': {'name': 'glass', 'cost': 500, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '114': {'name': 'stone dust', 'cost': 90, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '115': {'name': 'stone slab', 'cost': 200, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '116': {'name': 'crushed stone', 'cost': 80, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '117': {'name': 'brick', 'cost': 45, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '118': {'name': 'plastic', 'cost': 250, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '119': {'name': 'boron nitride', 'cost': 18000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '120': {'name': 'tungsten carbide', 'cost': 25000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '121': {'name': 'ceramic composite', 'cost': 8800, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '122': {'name': 'cheese', 'cost': 4000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '123': {'name': 'pesticide', 'cost': 8000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '124': {'name': 'boron nitrate', 'cost': 18000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '125': {'name': 'glassware', 'cost': 1200, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '126': {'name': 'plastic', 'cost': 250, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '127': {'name': 'wires', 'cost': 10000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '128': {'name': 'paint', 'cost': 8000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '129': {'name': 'chemfuel', 'cost': 120, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '130': {'name': 'uniform', 'cost': 15000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '131': {'name': 'clothes', 'cost': 40000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '132': {'name': 'kitchenware', 'cost': 12000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '133': {'name': 'electronic components', 'cost': 40000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '134': {'name': 'instruments', 'cost': 15000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '135': {'name': 'electric instruments', 'cost': 20000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '136': {'name': 'railroad transport', 'cost': 5000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '137': {'name': 'bus', 'cost': 30000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '138': {'name': 'appliances', 'cost': 60000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '139': {'name': 'supermagnets', 'cost': 15000000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '140': {'name': 'nuclear fuel', 'cost': 10000000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '141': {'name': 'tritium', 'cost': 30000000000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '142': {'name': 'radioactive scrap', 'cost': 0, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '143': {'name': 'computers', 'cost': 480000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '144': {'name': 'spaceship', 'cost': 50000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},
             '145': {'name': 'antimatter', 'cost': 2100000000000, 'production amount': 0, 'consumption amount': 0, 'stockpile': 0, 'embargo': False, 'trade': False, 'trade amount': 0},

             }

buildings = {'0': {'name': 'iron ore mining industry', 'level': 1,  'production': ['0'], 'production amount': [600], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '1': {'name': 'copper ore mining industry', 'level': 0,  'production': ['1'], 'production amount': [150], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '2': {'name': 'aluminum ore mining industry', 'level': 0,  'production': ['2'], 'production amount': [400], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '3': {'name': 'tin ore mining industry', 'level': 0,  'production': ['3'], 'production amount': [80], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '4': {'name': 'lead ore mining industry', 'level': 0,  'production': ['4'], 'production amount': [200], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '5': {'name': 'chrome ore mining industry', 'level': 0,  'production': ['5'], 'production amount': [200], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '6': {'name': 'nickel ore mining industry', 'level': 0,  'production': ['6'], 'production amount': [200], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '7': {'name': 'titanium ore mining industry', 'level': 0,  'production': ['7'], 'production amount': [500], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '8': {'name': 'magnesium ore mining industry', 'level': 0,  'production': ['8'], 'production amount': [250], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '9': {'name': 'rare earth metals ore mining industry', 'level': 0,  'production': ['9'], 'production amount': [400], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '10': {'name': 'lithium ore mining industry', 'level': 0,  'production': ['10'], 'production amount': [60], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '11': {'name': 'tungsten ore mining industry', 'level': 0,  'production': ['11'], 'production amount': [90], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '12': {'name': 'uranium ore mining industry', 'level': 0,  'production': ['12'], 'production amount': [50], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '13': {'name': 'cobalt ore mining industry', 'level': 0,  'production': ['13'], 'production amount': [30], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '14': {'name': 'boron ore mining industry', 'level': 0,  'production': ['14'], 'production amount': [100], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '15': {'name': 'zinc ore mining industry', 'level': 0,  'production': ['15'], 'production amount': [90], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '16': {'name': 'silver ore mining industry', 'level': 0,  'production': ['16'], 'production amount': [2], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '17': {'name': 'gold mining industry', 'level': 0,  'production': ['17'], 'production amount': [0.0005], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '18': {'name': 'graphite mining industry', 'level': 0,  'production': ['18'], 'production amount': [110], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '19': {'name': 'gems mining industry', 'level': 0,  'production': ['19'], 'production amount': [0.0001], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '20': {'name': 'platinum mining industry', 'level': 0,  'production': ['20'], 'production amount': [0.0002], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '21': {'name': 'salt mining industry', 'level': 0,  'production': ['21'], 'production amount': [50], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '22': {'name': 'clay mining industry', 'level': 0,  'production': ['22'], 'production amount': [500], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '23': {'name': 'sand mining industry', 'level': 0,  'production': ['23'], 'production amount': [400], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '24': {'name': 'stone mining industry', 'level': 0,  'production': ['24'], 'production amount': [1100], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '25': {'name': 'sulfur mining industry', 'level': 0,  'production': ['25'], 'production amount': [50], 'consumption': ['none'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '26': {'name': 'asteroid mining', 'level': 0,  'production': ['0', '1', '2', '5', '6', '7', '8', '17'], 'production amount': [2000, 800, 1500, 1000, 1000, 1500, 400, 0.02], 'consumption': ['none'], 'consumption amount': ['none'], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '27': {'name': 'wheat field', 'level': 0, 'production': ['26'], 'production amount': [7], 'consumption': ['0'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},
             '28': {'name': 'corn field', 'level': 0, 'production': ['27'], 'production amount': [15], 'consumption': ['0'], 'consumption amount': [0], 'energy consumption': 10, 'active': True, 'construction': {'money': 800000, 'time': 60}},

             }


#for i in range(0,len(resources)):
while True:
    day += 1
    if date[0] == calender[date[1] - 1]:
        production()
        consumption()
        stockpile()
    if date[1] == 12 and date[0] == 31:
        money += trade()
    print(date,day,money,resources['0']['stockpile'])
    datechange()
    clock.tick(fps)
