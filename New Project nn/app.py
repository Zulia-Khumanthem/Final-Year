from flask import Flask ,  render_template
import pickle
 #vector =pickle.load(open("vectorizer.pkl",'rb'))

 #model = pickle.load(open("model.pkl",'rb'))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("./index.html")

# @app.route("/prediction",methods=['GET','POST'])
# def prediction():
#    if requests.method == "POST":
#     news =requests.form['news']  
#     print(news) 
   

    
#    else:
#       return render_template("predict.html") 

if __name__ == '__main__':
    app.run()
    