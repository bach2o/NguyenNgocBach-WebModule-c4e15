from flask import Flask, render_template
app = Flask(__name__)

@app.route('/about-me/')
def about_me():
    return render_template('aboutme.html')

@app.route('/school')
def index():
    return redirect("http://techkids.vn")
if __name__ == '__main__':
  app.run(debug=True)
