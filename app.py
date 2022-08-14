from contextlib import redirect_stderr
import json
from operator import methodcaller
import uuid
import jsonify
from flask import redirect, url_for
from flask import Flask, request,\
    render_template

app=Flask(__name__)


def get_json_data():

    with open("data.json",'r') as json_file:
        data = json.load(json_file)
        
        # print('jsonData',data)

    return data

def store_json_data(data):

    with open("data.json", 'a') as outfile:
        json.dump(data, outfile)
    


@app.route('/')
def index():        
   return render_template('index.html')


@app.route('/commanlist', methods=['GET','POST'])
def commanlist():
   
    return render_template('commanlist.html')

userId = str(uuid.uuid1())


@app.route('/thanks', methods=['GET','POST'])
def thanks(): 
    if request.method=='POST':
        food=request.form.get('food')
        place=request.form.get('place')
        movie=request.form.get('movie')
        book=request.form.get('book')
        subject=request.form.get('subject')
        actor=request.form.get('actor')
        color=request.form.get('color')
        year=request.form.get('year')
        letter=request.form.get('letter')
        vehicle=request.form.get('vehicle')
        coffee=request.form.get('coffee')
        lang=request.form.get('lang')
        band=request.form.get('band')
        genre=request.form.get('genre')
        dessert=request.form.get('dessert')
        music=request.form.get('music')
        comedian=request.form.get('comedian')
        result={
            'food':food,
            'place':place,
            'movie':movie,
            'book':book,
            'subject':subject,
            'actor':actor,
            'color':color,
            'year':year,
            'letter':letter,
            'vehicle':vehicle,
            'beverage':coffee,
            'lang':lang,
            'band':band,
            'genre':genre,
            'dessert':dessert,
            'music':music,
            'comedian':comedian
        }
        #print(result)
        store_json_data(result)
    return render_template('thanks.html')


with open('data.json', 'r') as myfile:
    data = myfile.read()

@app.route("/display")
def display():
    jsonfile=jsonify(data)
    return render_template('display.html', title="page", jsonfile=jsonify(data))


if __name__=='__main__':
    app.run()(host='127.0.0.1', port=7000)

