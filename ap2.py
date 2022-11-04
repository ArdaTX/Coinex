from api import Coins
from flask import Flask, render_template,request
import requests


app = Flask(__name__)

crypto  = Coins()




@app.route("/")
def hello():

    dumps = crypto.get_top_10()
    
    
    for dump in dumps:
        dump['quote']['USD']['price'] = '$ '  + "{:.2f}".format(dump['quote']['USD']['price'])

    return render_template('index.html', **locals())
    





if __name__ == "__main__":
    app.run(debug="false")


