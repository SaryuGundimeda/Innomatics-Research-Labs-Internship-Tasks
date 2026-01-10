from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    #get name from URL query parameter
    name = request.args.get("name")

    if name:
        return f"""
        <h1>Welcome, {name.upper()}</h1>
        <h1>Your name has {len(name)} letters</h1>
        <h1>Reversed Name: {name[::-1]}</h1>
        """
    else:
        return "<h2>Please enter your name in the URL like '/?name=your_name'</h2>"

if __name__ == "__main__":
    app.run(debug=True)