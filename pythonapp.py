from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home_page():
    return render_template("index.html")
@app.route('/math',methods=['POST'])
def math_operation():
    if(request.method=='POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(ops == 'add'):
            result = num1 + num2
            output = 'Addition of ' + str(num1) + ' and ' + str(num2) + " is " + str(result)
        elif(ops == 'subtract'):
            result = num1-num2
            output = 'Subtraction of ' + str(num1) + ' and ' + str(num2) + " is " + str(result)
        elif(ops == 'multiply'):
            result = num1*num2
            output = 'Multiplication of ' + str(num1) + ' and ' + str(num2) + " is " + str(result)
        elif(ops == 'divide'):
            result = num1/num2
            output = 'Division of ' + str(num1) + ' and ' + str(num2) + " is " + str(result)
        return render_template('results.html',result=output)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0")
