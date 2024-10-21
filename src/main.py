from flask import Flask, request
from auth.routers import auth_blueprint
from todo.routers import todo_blueprint

# __name__: tên của module hiện tại
app = Flask(__name__)

# Đăng ký blueprint auth_pb vào app
app.register_blueprint(auth_blueprint)
app.register_blueprint(todo_blueprint)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)