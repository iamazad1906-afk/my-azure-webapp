from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Azure Web App</title>
    </head>
    <body>
        <h1>Hello from my Azure Web App! 🚀</h1>
        <p>This application is deployed using GitHub and Azure DevOps.</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run()
