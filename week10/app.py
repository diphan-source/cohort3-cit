from unittest import result
from flask import Flask , render_template , request , redirect , url_for

app = Flask(__name__)

fruits = [ 'apple' , 'banana' , 'mango']

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return 'you have reached the hello page'


@app.route('/html')
def html():
    message = """
    <h1> Welcome to  webpage </h1>
    <p> This is  new webpage, come and check it out </p>
    """
    return message


# url /sayhello/john => Hello John
@app.route('/say-hello/<name>')
def say_hello(name):
    # return f"Hello {name}"
    # return "Hello {}".format(name)
    return render_template('hello.html', name=name)


# url /add/1/2 => 1 + 2 = 3

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    mydict = {
        'num1': num1,
        'num2': num2,
        'result': num1 + num2
    }
    
    return render_template('calc.html', mydict=mydict)

# query parameters route 
# add?num1=1&num2=2 => 1 + 2 = 3
@app.route('/add')
def add_query():
    num1 = request.args['num1']
    num2 = request.args.get('num2')
    result = int(num1) + int(num2)
    return f"{num1} + {num2} = {result}"

# /fruits => apple, banana, orange
@app.route('/fruits', methods=['GET', 'POST'])
def add_fruits():
    if request.method == 'POST':
        fruit = request.form['fruit']
        
        if not fruit:
            return "Please enter a fruit"

        fruits.append(fruit)
        return redirect('/fruits')

    return render_template('fruits.html', fruits=fruits)

#  /fruits/1 => apple
@app.route('/fruits/<int:index>')
def get_fruit(index):
    if index > len(fruits):
        return "Fruit not found"
    return fruits[index - 1]

# /fruits/banana => banana
@app.route('/fruits/<string:name>')
def get_fruit_name(name):
    if name not in fruits:
        return "Fruit not found"
    return name




if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='127.0.0.1', port=3000, debug=True)