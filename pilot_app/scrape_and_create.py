from urllib.request import urlopen
from bs4 import BeautifulSoup
import mlab
from models.service import Service
from random import randint, choice
from faker import Faker

mlab.connect()

quote_page = "http://naruto.wikia.com/wiki/Jiraiya"

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
    yob = -38,  # Year of birth
    gender = 1, #0: female, 1: male
    height = 191,
    measurements = [85,62,85], # List
    phone=fake.phone_number(),
    address = "Hidden Leaf Village",
    description = "Jiraiya (自来也) was one of Konohagakure's Sannin. Famed as a hermit and pervert of stupendous ninja skill, Jiraiya travelled the world in search of knowledge that would help his friends, the various novels he wrote, and, posthumously, the world in its entirety – knowledge that would be passed on to his godson and final student, Naruto Uzumaki. ",
    status = choice([True, False])
                )
service.save()
