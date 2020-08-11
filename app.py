from flask import Flask, redirect

app = Flask(__name__)

data = {
    'a1234': 'www.google.com',
    'b1234': 'www.microsoft.com',
    'c1234': 'www.github.com'
}

@app.route("/<string:id>")
def get(id):
    #return jsonify({"name":"Brett", "age":29})
    #return {"name":"Brett", "age":29}, 200
    return redirect("http://" + data[id], 302)

if __name__ == "__main__":
    app.run(debug=True)