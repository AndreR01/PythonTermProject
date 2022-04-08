import csv

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def rootRoute():
    dishNames = ["Easy Chicken Tikka Masala",
                 "Smoked Pulled Pork",
                 "Crock Pot Ribs",
                 "Best Twice Baked Potatoes",
                 "6 Ingredient Lazy Day Chili"]
    return render_template('layout.html', my_var="HOME PAGE", dish_list=dishNames)

@app.route("/dish/<dishID>")
def showDish(dishID):
    dishID = int(dishID)
    dish = {}
    dishNames = []
    with open('dishes.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', escapechar='\\')
        for index, row in enumerate(filereader):
            dishNames.append(row[0])
            if (index+1) == dishID:
                dish = row
    return render_template('dish.html', dish_list=dishNames, dish=dish, image=dish[2], ingredients=dish[3], instructions=[4])

#TODO Create home page content block
#TODO Form to submit and delete recipes
#


if __name__ == '__main__':
    app.run(debug=True)
