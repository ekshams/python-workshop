from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return("Hello, welcome to Flask!!!!")

@app.route('/account/<id>')
def account(id):    
    return('message from account:'+ id)

@app.route('/account', methods = ['GET'])
def account_by_name():
    return('the passed account name is:'+ request.args.get('name'))

@app.route('/account', methods = ['POST'])
def create_account():
    return ('hello from account post')

@app.route('/product', methods = ['POST'])
def create_product():
    data = request.get_json()
    return (data)



if __name__ == '__main__':
    app.run(debug=True)
