import os
from flask import Flask, request, Response

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# Request:
# GET /hello?name=David
@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name']

    #Send back friendly greeting with the name
    return f"Hello {name}"

#Request:
# POST /goodbye
#   With body parameter: name=Alice

@app.route('/goodbye', methods=['POST'])
def goodbye(): 
    name = request.form['name'] 
    # Send back friendly farewell with the name
    return f"Goodbye {name}!"

#Request
@app.route('/introduction', methods=['POST'])
def introduction():
    name = request.form['name']
    meet = request.form['meet']

    return f"Hi {name}! I'd like to introduce you to {meet}"

#Request
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message: {message}'

#Request (02 Building routes: Challenge)
@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']
    return f'I am waving at {name}'

#Request (03 Test-driving a route: Exercise One)
@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    vowels = 'aeiou'
    count = 0
    text = request.form['text'] 
    for char in text:
        if char in vowels:
            count += 1
    return f'There are {count} vowels in "{text}"'

#Request (03 Test-driving a route: Exercise Two)
@app.route('/sort-names', methods=["POST"])
def sort_names():
    # text = request.form['text']
    # split_text = text.split(",")
    # split_text.sort()
    # split_text_as_string = (',').join(split_text)
    # return split_text_as_string
    
    # 400 RESPONSE FOR NONE PARAMETER (NEEDED PEER HELP)
    text = request.form['text']
    if text == '':
        return Response("Please provide a list of strings (comma-separated)", status=400)
    else:
        split_text = text.split(",")
        split_text.sort()
        split_text_as_string = (',').join(split_text)
        return split_text_as_string

#Request (03 Test-driving a route: CHallenge)
@app.route('/name', methods=["GET"])
def add_name():
    predefined_names = ["Julia,Alice,Karim"]
    added_name = request.args.get('add')
    if added_name:
        predefined_names.append(added_name)
    return ",".join(predefined_names)




# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

