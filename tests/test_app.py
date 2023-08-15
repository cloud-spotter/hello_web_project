# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

# === 03 Test-driving a route: Exercise One ===

'''
When: I make a GET request to /
Then: I should get a 200 response
'''
def test_get_wave(web_client):
    #Simulate sending a GET request to /wave?name=Dana
    #This returns a response object we can test against:
    response = web_client.get('/wave?name=Dana')

    #Assert that the status code was 200 (OK)
    assert response.status_code == 200

    #Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'I am waving at Dana'

'''
When: I make a POST request to /submit
And: I send a name and message as body parameters
Then: I should get a 200 response with the right content
'''
def test_post_submit(web_client):
    #Simulate sending a POST request to /submit with a name and message
    #Again, this returns a response object we can test against:
    response = web_client.post('/submit', data={'name': 'Dana', 'message': 'Hello'})

    #Assert that the status code was 200 (OK)
    assert response.status_code == 200

    #Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: Hello'

'''
When: I make a POST request to /count_vowels
And: I send 'eee' as the body parameter test
Then: I should get a 200 response with 3 in the message
'''
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

'''
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
'''
def test_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200 
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

'''
When: I make a POST request to/count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
'''
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

# === 03 Test-driving a route: Exercise Two ===

'''
SORT ROUTE
POST /sort-names
    Parameters:
    names: Joe,Alice,Zoe,Julia,Kieran
Expected response (200 OK)
'''
def test_sort_names_gets_200_OK_status(web_client):
    response = web_client.post('/sort-names', data={'text': "Joe,Alice,Zoe,Julia,Kieran"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice,Joe,Julia,Kieran,Zoe"

'''
POST /submit
    Parameters: none
    Expected response (400 Bad Request)
'''
def test_sort_names_returns_400_with_no_parameters(web_client):
    response = web_client.post('/sort-names', data={'text': ''})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Please provide a list of strings (comma-separated)"
# HAD TO ASK PEERS FOR HELP ON THIS ONE!

# === 03 Test-driving a route: Challenge ===

'''
# GET /names
#   Expected response (200 OK)
'''
"""
Julia, Alice, Karim, Eddie
"""
def test_add_name(web_client):
    #Simulate sending a GET request to /wave
    response = web_client.get('/name')
    #Assert that the status code was 200 (OK)
    assert response.status_code == 200 #passed! At last!
    assert response.data.decode('utf-8') == "Julia,Alice,Karim"

# GET /names?add=Eddie
# Expected response is the string returned with Eddie added
# Expected status_code == 200 (OK)

def test_add_name_to_names(web_client):
    response = web_client.get('/name?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Julia,Alice,Karim,Eddie"