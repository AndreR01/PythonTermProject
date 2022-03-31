from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def rootRoute():
    return render_template('mainpage.html', my_var="whats up")

if __name__ == '__main__':
    app.run(debug=True)
