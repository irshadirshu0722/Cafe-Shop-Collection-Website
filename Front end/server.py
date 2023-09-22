from flask import Flask,render_template,request,redirect
import requests
from form import AddCaffe
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
Bootstrap5(app)
app.secret_key="bwefewoufvwefvoew"
@app.route('/')
def home():
    print("enter")
    return render_template("home.html")

@app.route('/add-cafe',methods = ["POST","GET"])
def addcafe():
    form = AddCaffe()
    if request.method=="POST":
        print(form.name.data,form.seats.data)
        param ={
            "name":form.name.data,
            "map_url":form.map_url.data,
            "img_url":form.map_url.data,
            "loc":form.place.data,
            "sockets":form.has_sockets.data,
            "toilet":form.has_toilet.data,
            "wifi":form.has_wifi.data,
            "calls":form.can_take_calls.data,
            "seats":form.seats.data,
            "coffee_price":form.coffee_price.data
        }
        response = requests.post("http://127.0.0.1:5004/add",params=param)
        print(response.status_code)
        return redirect('/')

    return render_template("add_cafe.html",form=form)
@app.route("/search_result",methods=["POST","GET"])
def searchcafe():
    print("enter")
    if request.method =="POST":
        search_loc = request.form.get("search")
        if search_loc=="all":
            response = requests.get(f"http://127.0.0.1:5004/all")




        else:
            response  = requests.get(f"http://127.0.0.1:5004/search?loc={search_loc}")



        data = (response.json()['cafes'])

        print(data)
        return  render_template('Cafe.html',cafes = data)
@app.route('/delete/<int:id>')
def delete(id):
    print(id)
    response   =requests.delete(f"http://127.0.0.1:5004/report-closed/{id}?api-key=TopSecretAPIKey")
    return redirect("/")
if __name__ == '__main__':
    app.run(debug=True,port=5003)