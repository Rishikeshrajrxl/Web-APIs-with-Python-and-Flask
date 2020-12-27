import flask
from flask import request,jsonify

app = flask.Flask(__name__)
app.config["DEBUG"]=True

# created some test data 
books = [
                {
                    'id' :0,
                    'title' : 'A fire upon the deep',
                    'author' : 'Vernor Vinge',
                    'first_sentence' : 'The coldsleep itself was dreamless',
                    'Year_published' : '1992'},
                {   'id': 1,
                    'title': 'The Ones Who Walk Away From Omelas',
                    'author': 'Ursula K. Le Guin',
                     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
                     'published': '1973'},
                {   'id': 2,
                    'title': 'Dhalgren',
                    'author': 'Samuel R. Delany',
                     'first_sentence': 'to wound the autumnal city.',
                    'published': '1975'}
        ]

@app.route('/',methods=['GET'])
def home():
     return "<h1>Distance Reading Archive</h1><p>This site is a prototype API for reading of science fiction novel.</p>"
       

# A route to return all the data
@app.route('/api/v1/resources/books/all',methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books',methods=['GET'])
def api_id():
    # check if id is provided in the request
    # if id is provided then assign it to the variable
    #If no id is provided then sshow an error message.

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error : NO id field is provided."

    # create an empty list for result
    result=[]

    # loop through the data matches the id
    for book in books:
         if book['id']==id:
             result.append(book)

    return jsonify(result)

app.run()

