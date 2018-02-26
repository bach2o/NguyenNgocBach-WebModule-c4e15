from flask import Flask, render_template
app = Flask(__name__)

@app.route('/user/<username>')
def user(username):
    users = {
            "Bach":  {
                    "Name": "Nguyễn Ngọc Bách",
                    "Age": 19
                    },
            "Cuong": {
                    "Name": "Quật Văn Cường",
                    "Age": 29
                    },
            }

    if username in users:
        content = users[username]
        return render_template('user.html', content = content)
    else:
        return "Not_found"

if __name__ == '__main__':
  app.run(debug=True)
