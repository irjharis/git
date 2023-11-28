from flask import Flask,request,render_template
# main
app=Flask(__name__)

## Routes always gives route

@app.route('/')     # home page /  get request method default      first open terminal and open file python ap.py then open link 0.0.0. that one 
def welcome():
    return render_template("index.html")    # #render_template("index.html")

@app.route('/aboutus')  # /aboutus      write after home page 
def aboutus():
    return "We are ineuron"

@app.route('/demo',methods=['POST'])    # post request method
def math_operation():
    if(request.method=='POST'):
        operation=request.json['operation']     # json file in operation
        num1=request.json['num1']
        num2=request.json['num2']
        result=0

        if operation=="add":
            result=num1+num2
        elif operation=="multiply":
            result=num1*num2
        elif operation=='division':
            result=num1/num2
        else:
            result=num1-num2

        return "The operation is {} and the result is {}".format(operation ,result)

@app.route('/operation',methods=['POST'])
def operation():
    if(request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=0

        if operation=="add":
            result=num1+num2
        elif operation=="multiply":
            result=num1*num2
        elif operation=='division':
            result=num1/num2
        else:
            result=num1-num2

        return render_template("result.html",result=result)
 

# main
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000) # 0.0.0.0 map into local ip address , 
    

