import os
import sys
from flask import Flask, render_template, request
import giphypop
app = Flask(__name__)

#This is the indext page
@app.route('/')
def index():
    return render_template('index.html')

#This is the about page
@app.route('/about')
def about():
    return render_template('about.html')

#This is the error when no search term is entered
@app.route('/nonresults')
def nonresults():
    return render_template('nonresults.html')

#This is the search results
@app.route('/results')
def results():
    #Request user for a search keyword
    key = request.values.get('key')
    g = giphypop.Giphy()
    results = g.search(key) 
    try:
    #returns the list of gif image links
        return render_template('results.html', results=results, key=key)
    #return the error page when no search term is entered
    except AssertionError:
        return render_template('nonresults.html')

#This is the 'cool' search results
@app.route('/coolresults')
def coolresults():
    #Add 'cool' to search keyword
    coolkey = request.values.get('coolkey')
    g = giphypop.Giphy()
    coolresults = g.search('cool ' + coolkey) 
    try:
    #returns the list of gif image links
        return render_template('coolresults.html', coolresults=coolresults, coolkey=coolkey)
    #return the error page when no search term is entered
    except AssertionError:
        return render_template('nonresults.html')


port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)







