from flask import Flask, render_template

my_code=Flask(__name__)

@my_code.route("/")
def home():
 return render_template("home.html")

@my_code.route("/about")
def about():
 return render_template("about.html")

if __name__=="__main__":
 #execute the server when this program is run directly .DOnt execute server if this program is imported
 my_code.run(debug=True)

#shows detailed errors when debug is true
