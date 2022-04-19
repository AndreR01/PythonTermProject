import json
import csv

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def rootRoute():
    dishNames = ["Easy Chicken Tikka Masala",
                 "Smoked Pulled Pork",
                 "Crock Pot Ribs",
                 "Best Twice Baked Potatoes",
                 "Banana Breakfast Cookies"]
    return render_template('layout.html', my_var="HOME PAGE", dish_list=dishNames)


@app.route("/dish/<dishID>")
def showDish(dishID):
    dishID = int(dishID)
    filename = ""
    with open('dishes.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', escapechar='\\')
        for index, row in enumerate(filereader):
            if (index + 1) == dishID:
                filename = row[1].strip()

    #         dishNames.append(row[0])
    #             dish = row
    with open(filename, "r") as infile:
        data = json.load(infile)
        print(data["recipeName"])

    return render_template('dish.html', dish=data, )


@app.route('/handle_data', methods=['POST'])
def handle_data():
    filename = "newRecipe.json"
    recipeName = request.form['recipeName']
    if len(recipeName) < 6:
          return render_template('uploadError.html')
    userRecipe = {"recipeName": (recipeName),
                  "recipeDesc": (request.form['recipeDesc']),

                  }
    with open(filename, "w") as infile:
        json.dump(userRecipe, infile)
    return rootRoute()

@app.route("/upload")
def upload_recipe():
    return render_template('formsubmit.html')





# TODO Create home page content block
# TODO Form to submit and delete recipes
#

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
