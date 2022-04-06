import csv

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

@app.route("/dish/<dishName>")
def showDish(dishName):
    dish = {}
    dishNames = []
    with open('dishes.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', escapechar='\\')
        for row in filereader:
            dishNames.append(row[0])
            if row[0] == dishName:
                dish = row
    return render_template('dish.html', dish_list=dishNames, dish=dish)


if __name__ == '__main__':
    app.run(debug=True)
