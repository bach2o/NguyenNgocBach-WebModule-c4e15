from flask import *
import mlab
from models.service import Service
from random import randint, choice
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

@app.route('/service')
def service():
    service = Service.objects
    return render_template('service.html', all_services = service)

@app.route('/service/update-service/<service_id>', methods=['GET','POST'])
def modify(service_id):
    service_detail = Service.objects().with_id(service_id)
    if request.method == 'GET': # request là function của Flask, là thông tin của người dùng gửi đến server(yêu cầu,thông tin cá nhân,...)
        return render_template('modify.html', service = service_detail)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = int(form['yob'])
        phone = form['phone']
        gender = form['gender']
        service_detail.update(set__name = name, yob = yob, phone = phone, gender = gender)
        service_detail.reload()
        # return render_template('modify.html', service = service_detail)
        return "{0}, {1}, {2}, {3} updated".format(name, yob, phone, gender)
    # return render_template('modify.html')

@app.route('/service/<service_id>')
def detail(service_id):
    service_detail = Service.objects().with_id(service_id)
    return render_template('detail.html', service = service_detail)


@app.route('/search/<int:gender>/')
def search(gender):
    service = Service.objects(gender=0)
    # service = Service.objects(yob__lte = 1998)
    # service = Service.objects
    return render_template('search.html', all_services = service)


@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html', services = services)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects().with_id(service_id)

    if service_to_delete == None:
        return "Not found"

    service_to_delete.delete()

    return redirect(url_for('admin'))

@app.route('/new-service', methods=['GET', 'POST'])
def create():
    if request.method == 'GET': # request là function của Flask, là thông tin của người dùng gửi đến server(yêu cầu,thông tin cá nhân,...)
        return render_template('new-service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = int(form['yob'])
        phone = form['phone']
        gender = form['gender']
        new_service = Service(name = name,
                              yob = yob,
                              phone = phone,
                              gender = gender,
                              status = choice([True, False])
                              )
        new_service.save()

        return "{0} {1} {2} posted and saved".format(name, yob, phone)




if __name__ == '__main__':
  app.run(debug=True)
