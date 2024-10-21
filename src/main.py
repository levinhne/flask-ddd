from flask import Flask, request
from auth.routers import auth_blueprint

# __name__: tên của module hiện tại
app = Flask(__name__)

# Đăng ký blueprint auth_pb vào app
app.register_blueprint(auth_blueprint)

@app.route("/")
def hello_world():
    app.logger.info("Hello, World!")
    app.logger.info("HTTP Method: %s", request.method)
    return "<p>Hello, World!</p>"

@app.route("/<username>")
def hello_user(username):
    return f"<p>Hello, {username}!</p>"

@app.route("/<username>/<int:age>")
def hello_user_age(username, age):
    return f"<p>Hello, {username}! You are {age} years old.</p>"

if __name__ == '__main__':
    app.run(debug=True)