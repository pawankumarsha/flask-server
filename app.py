import requests
from flask import Flask, render_template
app = Flask(__name__)
import time

@app.route('/', methods=['GET', 'POST'])
def movieapp():
   #url = "http://movie-quotes-2.herokuapp.com/api/v1/quotes/random"   
   #response = requests.get(url).json()
   time.sleep(5)
   return render_template("index.html", film='film', quote="quote")
 
if __name__ == '__main__':
   app.run(debug=False, host='0.0.0.0')

