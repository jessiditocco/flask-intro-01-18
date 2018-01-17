"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page. <a href='/hello'>hello</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method="GET">
          What's your name? <input type="text" name="person"><br>
          Choose your compliment:
          <input type="radio" name="compliment" value="awesome">awesome
          <input type="radio" name="compliment" value="terrific">terrific
          <input type="radio" name="compliment" value="fantastic">fantastic
          <input type="radio" name="compliment" value="neato">neato
          <input type="radio" name="compliment" value="fantabulous">fantabulous
          <input type="radio" name="compliment" value="wowza">wowza
          <input type="radio" name="compliment" value="oh-so-not-meh">oh-so-not-meh
          <input type="radio" name="compliment" value="brilliant">brilliant
          <input type="radio" name="compliment" value="ducky">ducky
          <input type="radio" name="compliment" value="coolio">coolio
          <input type="radio" name="compliment" value="incredible">incredible
          <input type="radio" name="compliment" value="wonderful">wonderful
          <input type="radio" name="compliment" value="smashing">smashing
          <input type="radio" name="compliment" value="lovely">lovely <br>
          <input type="submit" value="Submit">
        </form>
        
        # <form action="/diss">
        #   Would you like to hear a diss instead?
        #   Choose your diss:
        #   <input type="radio" name="diss" value="mean">mean
        #   <input type="radio" name="diss" value="rude">rude
        #   <input type="radio" name="diss" value="stupid">stupid
        #   <input type="radio" name="diss" value="ugly">ugly
        #    <input type="submit" value="Submit">
        #   </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    # compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


@app.route('/diss')
def diss_person():

    player = request.args.get("person")
    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """.format(player=player, diss=diss)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
