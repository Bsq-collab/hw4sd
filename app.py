from flask import Flask
app= Flask(__name__)

@app.route("/jojo")


def hello_world():
	return "No Way Jose"

@app.route("/lele")
def test2():
        return "it's working"


@app.route("/last")
def test3():
        return "wooo :-)"
if __name__ == "__main__":
        app.debug = True
	app.run()

