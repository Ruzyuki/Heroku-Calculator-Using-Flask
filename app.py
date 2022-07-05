from flask import Flask, render_template,jsonify,request
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])                          #To render homepage
def home_page():
    return render_template('index.html')

@app.route('/math', methods = ['POST'])                            #This will be called from UI
def math_operation():
    if (request.method=='POST'):
        operation= request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if(operation == 'add'):
            result = num1+num2
        if(operation == "subtract"):
            result = num1-num2
        if(operation == 'multiply'):
            result= num1*num2
        if(operation == 'divide'):
            result = num1/num2

        return render_template('finalpage.html',get = result)





if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)