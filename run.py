from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def rootRoute():
    dishNames = ["Easy-chicken-tikka-masala",
                 "Smoked-pulled-pork-recipe",
                 "Crock-pot-ribs-slow-cooker-ribs",
                 "Best-twice-baked-potatoes-recipe",
                 "6-ingredient-lazy-day-chili"]
    return render_template('layout.html', my_var="HOME PAGE", dishNames = dishNames)

if __name__ == '__main__':
    app.run(debug=True)
