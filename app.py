from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

clients = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/client", methods=["GET", "POST"])
def client():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        weight = request.form["weight"]
        program = request.form["program"]

        clients.append({
            "name": name,
            "age": age,
            "weight": weight,
            "program": program
        })

        return redirect(url_for("summary", name=name))

    return render_template("client.html")

@app.route("/summary/<name>")
def summary(name):
    client = next((c for c in clients if c["name"] == name), None)
    return render_template("summary.html", client=client)

if __name__ == "__main__":
    app.run(debug=True)