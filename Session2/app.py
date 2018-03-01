from flask import Flask, render_template
import mlab
from models.service import Service
mlab.connect()

# BooleanField là True/False
app = Flask(__name__)
#
# service = Service(name = 'Cat',
#     yob = 2018,
#     gender = 0,
#     height = 100,
#     phone = '0123456789',
#     status = True)
#
# service.save()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>/')
def search(gender):
    service = Service.objects(gender=0)
    # service = Service.objects(yob__lte = 1998)
    # service = Service.objects
    return render_template('search.html', all_services = service)



if __name__ == '__main__':
  app.run(debug=True)
