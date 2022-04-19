import json
import csv
import os

from flask import Flask, render_template, request

app = Flask(__name__)


def getExistingDishes():
    dishes = []
    with open('dishes.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', escapechar='\\')
        for index, row in enumerate(filereader):
            dishes.append((row[0].strip(), row[1].strip()))
    return dishes

def deleteDish(indexToDelete):
    indexToDelete = int(indexToDelete)
    currentDishes = getExistingDishes()
    fileToDelete = ""
    with open("dishes.csv", "w") as f:
        for index, row in enumerate(currentDishes):
            if index != indexToDelete:
                #DANGER ZONE!
                #os.remove(row[1])
                f.write(row[0] + ", " + row[1] + "\n")

def getDishNames():
    dishNames = []
    for i in getExistingDishes():
        dishNames.append(i[0])
    return dishNames;

@app.route("/")
def rootRoute():

    return render_template('home.html', my_var="HOME PAGE", dish_list=getDishNames())


@app.route("/dish/<dishID>")
def showDish(dishID):
    dishID = int(dishID)
    filename = ""

    for index, row in enumerate(getExistingDishes()):
        if (index + 1) == dishID:
            filename = row[1].strip()


#         dishNames.append(row[0])
#             dish = row
    with open(filename, "r") as infile:
        data = json.load(infile)
        print(data["recipeName"])

    return render_template('dish.html', dish=data, dish_list=getDishNames())

@app.route('/delete')
def delete():
    dishes = getExistingDishes()

    return render_template('delete.html', dishes = dishes, dish_list=getDishNames())


@app.route('/handle_delete', methods=['POST'])
def handle_delete():
    deleteIndex = request.form['recipeDelete']
    deleteDish(deleteIndex)
    return rootRoute()


@app.route('/handle_data', methods=['POST'])
def handle_data():
    recipeName = request.form["recipeName"]
    filename = recipeName.replace(" ", "") + ".json";
    if len(recipeName) < 6:
        return render_template('uploadError.html')
    userRecipe = {"recipeName": (recipeName),
                  "recipeDesc": (request.form["recipeDesc"]),
                  "recipeServeSize": (request.form["recipeServeSize"]),
                  "recipeURL": (request.form["recipeURL"]),
                  "recipeIngredients": (request.form["recipeIngredients"]),
                  "recipeInstructions": (request.form["recipeInstructions"])

                  }
    with open("dishes.csv", "a") as csvFile:
        csvFile.write(recipeName + ", " + filename + "\n")
    with open(filename, "w") as infile:
        json.dump(userRecipe, infile)
    return rootRoute()


@app.route("/upload")
def upload_recipe():
    return render_template('formsubmit.html', dish_list=getDishNames())


def test_method():
    dict_var = "World!"
    test_dict = {"Hello": dict_var}

    with open("test.json", "w") as outfile:
        json.dump(test_dict, outfile)

    with open("chickenTikka.json", "r") as infile:
        data = json.load(infile)
        print(data["recipeName"])


if __name__ == '__main__':
    app.run(debug=True)
