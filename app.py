import requests
from flask import Flask, render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///weather.db'
db=SQLAlchemy(app)

class City(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200),nullable=False)

   

@app.route("/",methods=['GET','POST'])
def index():
    db.session.query(City).delete()
    if request.method=='POST':
        city_add=request.form['place']
        url="{token}"
        r=requests.get(url.format(city_add)).json()
        if len(r)==2:
            return "gjfk"
        else:
            try:
                obj=City(name=city_add)
                db.session.add(obj)
                db.session.commit()
            except:
                return "rhrir"

    cities=City.query.all()
<<<<<<< HEAD
    url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=b2bd45294f6c0c2b5ec818fd86bb3b9a&units=metric"
=======
    url="{token}"
>>>>>>> 9cc1926b2c43ccff7b5212ff605dac1e3d42bedc
    weather_data=[]
    for city in cities:
        r=requests.get(url.format(city.name)).json()
        print(r)
        weather={
        'id':city.id,
        'city':city.name,
        'tem':r['main']['temp'],
        'dis':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon']
            } 
        weather_data.append(weather)
    return render_template('index.html',weather_data=weather_data)

@app.route('/delete/<int:id>')
def delete(id):
    delete = City.query.get_or_404(id)
    try:
            db.session.delete(delete)
            db.session.commit()
            return redirect('/')
    except:
            return "there is an issue"

if __name__=="__main__":
    app.run(debug=True)
