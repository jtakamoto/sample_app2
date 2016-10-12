from flask import Flask, render_template, request
import giphypop
app = Flask(__name__)

def get_stock_price(ticker):
    quotes = getQuotes(ticker)
    price = quotes[0]['LastTradePrice']
    return "The price of {} is {}".format(ticker, price)

@app.route('/')
def index():
    name = request.values.get('name', 'Nobody')
    greeting = "Hello {}".format(name)
    return render_template('index.html', greeting=greeting)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/results')
def results():
    stock = request.values.get('stock')
    g = giphypop.Giphy()
    results = g.search(stock) 
    for result in results:
        return render_template('results.html', price=result.media_url)

app.run(debug=True)






# returns a list of objects
#results = g.search('cats') 


    #print(result.media_url)
    #print(result.url)

