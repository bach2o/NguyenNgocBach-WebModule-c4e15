from flask import Flask, render_template
app = Flask(__name__)
import random

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "Hello C4E 15"

@app.route('/sỉn/<name>')
def sỉn(name):
    return 'hi ' + name
@app.route('/sum/<int:num1>/<int:num2>')
def sum(num1, num2):
    sum = num1 + num2
    return str(sum)
@app.route('/html')
def heading():
    return '<h1>CLGT</h1>'
@app.route('/blog')
def blog():
    name_list = ['Con gà con', 'Hay lắm bạn hiền', 'Đậu xanh rau cũng xanh', 'Những nguyên lý cơ bản của chủ nghĩa Mác Lênin', 'Một ngày đẹp trời khi code của bạn không có bug', 'How to code like a boss', 'Hướng dẫn cách nấu món gà rán']
    article_name = random.choice(name_list)
    posts = [
        {
        "content": 'Phân',
        "author": 'Đăm Săn'
        },
        {
        "content": 'Tích Phân',
        "author": 'Đăm Săn 2'
        },
        {
        "content": 'Nguyên Phân',
        "author": 'Đăm Săn 3'
        },
        {
        "content": 'Phân Chia',
        "author": 'Đăm Săn 4'
        },

    ]

    return render_template('blog.html', article_title = article_name, posts=posts)
@app.route('/user/<user_name>')
def user(user_name):
    # users = [
    #     {
    #     "name": 'A',
    #     "author": 'Đăm Săn'
    #     },
    #     {
    #     "name": 'B',
    #     "author": 'Đăm Săn 2'
    #     },
    #     {
    #     "name": 'C',
    #     "author": 'Đăm Săn 3'
    #     },
    #     {
    #     "name": 'D',
    #     "author": 'Đăm Săn 4'
    #     },
    # ]
    names = ['A','B','C','D']
    for name in names:
        # if user_name == users['name']:
        if user_name == name:
            return render_template('user.html', user_name=name)
        else:
            return render_template('user.html', name ="Not found")
if __name__ == '__main__':
  app.run(debug=True)
