from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route

@app.route('/count/<int:number>')
def count(number):
    count = '\n'.join([str(i) for i in range(number)])
    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, num2, operation):
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        'div': num1 / num2,
        '%': num1 % num2
    }
    result = operations.get(operation)
    if result is None:
        return 'Operation not recognized. Please use one of the following: + - * div %'
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)