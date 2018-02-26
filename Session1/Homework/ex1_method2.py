from flask import Flask, render_template
app = Flask(__name__)
import math

@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    BMI= round((weight / (height*height)*10000),2)
    comment = ""
    if BMI < 16:
        comment = " You are severely underweight."
    elif 16 <= BMI < 18.5:
        comment = " You are underweight."
    elif 18.5 <= BMI < 25:
        comment = " You are normal."
    elif 25 <= BMI < 30:
        comment = " You are overweight."
    elif BMI >= 30:
        comment = " You are obese."

    return render_template('bmi.html', BMI = BMI, comment = comment)


if __name__ == '__main__':
  app.run(debug=True)
