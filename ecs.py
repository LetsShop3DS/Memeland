from core import app
from flask import Response, session
#eShop's ECS (ECommerceSOAP) server. Handles all sorts of things.

'''
Personal note to Nintendo: WHEN THE FUCK WILL YOU SEPERATE SOAP URLS
'''
@app.route("/sessiontest", methods=['GET', 'POST'])
def sessiontest():
    return session['name']