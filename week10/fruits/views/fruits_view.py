from flask import Blueprint , render_template, request, redirect
from fruits.models import Fruit


views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/hello')
def hello():
    return 'you have reached the hello page'


@views.route('/html')
def html():
    message = """
    <h1> Welcome to  webpage </h1>
    <p> This is  new webpage, come and check it out </p>
    """
    return message


# url /sayhello/john => Hello John
@views.route('/say-hello/<name>')
def say_hello(name):
    # return f"Hello {name}"
    # return "Hello {}".format(name)
    return render_template('hello.html', name=name)


# url /add/1/2 => 1 + 2 = 3

@views.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    mydict = {
        'num1': num1,
        'num2': num2,
        'result': num1 + num2
    }
    
    return render_template('calc.html', mydict=mydict)

# query parameters route 
# add?num1=1&num2=2 => 1 + 2 = 3
@views.route('/add')
def add_query():
    num1 = request.args['num1']
    num2 = request.args.get('num2')
    result = int(num1) + int(num2)
    return f"{num1} + {num2} = {result}"

# /fruits => viewsle, banana, orange
# @views.route('/fruits', methods=['GET', 'POST'])
# def add_fruits():
#     if request.method == 'POST':
#         fruit = request.form['fruit']
        
#         if not fruit:
#             return "Please enter a fruit"

#         fruits.viewsend(fruit)
#         return redirect('/fruits')

#     return render_template('fruits.html', fruits=fruits)


@views.route('/fruits', methods=['GET', 'POST'])
def add_fruits():
    if request.method == 'POST':
        name = request.form['name']
        color = request.form['color']
        price = request.form['price']
        fruit = Fruit(name=name, color=color, price=price)
        fruit.save()
        return redirect('/fruits')
        

    fruits = Fruit.get_all()
    return render_template('fruits.html', fruits=fruits)


#  /fruits/1 => viewsle
@views.route('/fruits/<int:index>')
def get_fruit(index):
    if index > len(fruits):
        return "Fruit not found"
    return fruits[index - 1]

# /fruits/banana => banana
@views.route('/fruits/<string:name>')
def get_fruit_name(name):
    if name not in fruits:
        return "Fruit not found"
    return name
