from urllib.request import urlopen
from bs4 import BeautifulSoup
import mlab
from models.service import Service
from random import randint, choice
from faker import Faker

mlab.connect()

quote_page = "http://naruto.wikia.com/wiki/Sasuke_Uchiha"

page = urlopen(quote_page)

soup = BeautifulSoup(page, "html.parser")

image = soup.find('table', class_ = 'infobox box colored bordered innerbordered fill-td type-character list-noicon float-right-clear')
for img in image.findAll('img'):
    link = img.get('src')
    if "scale-to-width-down/300" in link:
        image = link
        break

name = soup.find('h1', class_ = 'page-header__title').text

# description = soup.find('div', class_ = "mw-content-ltr mw-content-text").findAll('p')
# for p in description:
#     if "is a" in p:
#         description = p
#         break
#
# print(description)
# height = soup.find('table', class_ = 'infobox box colored bordered innerbordered fill-td type-character list-noicon float-right-clear').find('span', class_ ='smw-highlighter smwttinline').span

fake = Faker()
service = Service(
    image ,
    name ,
    yob = 0,  # Year of birth
    gender = 1, #0: female, 1: male
    height = 151,
    measurements = [67,55,64], # List
    phone=fake.phone_number(),
    address = "Hidden Leaf Village",
    description = "Sasuke Uchiha (うちはサスケ, Uchiha Sasuke) is one of the last surviving members of Konohagakure's Uchiha clan. After his older brother, Itachi, slaughtered their clan, Sasuke made it his mission in life to avenge them by killing Itachi. He is added to Team 7 upon becoming a ninja and, through competition with his rival and best friend, Naruto Uzumaki, Sasuke starts developing his skills. ",
    status = choice([True, False])
                )
service.save()
