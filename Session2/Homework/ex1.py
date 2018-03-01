from flask import Flask, render_template
import mlab
from models.customer import Customer
mlab.connect()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer')
def customer():
    customers = Customer.objects()
    return render_template('customer.html', customers = customers)

# @app.route('/search/<gender>/<contacted>')
# def search(gender,contacted):
#     customers = Customer.objects(gender = int(gender) , contacted = int(contacted))
#     return render_template('search.html', customers = customers)

@app.route('/search/<gender>/<contacted>/<numbers_of_people>')
def search(gender,contacted,numbers_of_people):
    customers = Customer.objects(gender = int(gender) , contacted = int(contacted)) 
    return render_template('search.html', customers = customers, numbers_of_people = numbers_of_people)



if __name__ == '__main__':
  app.run(debug=True)
