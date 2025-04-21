from flask import Flask
import os
app = Flask(__name__)

@app.route('/user/<user_name>')
def get_user(user_name):
    users_file = open("users_log/users.txt", mode='a')
    users_file.write(user_name + "\n")
    return {"User": user_name}


if __name__ == '__main__':
    os.makedirs("users_log", exist_ok=True)
    app.run('0.0.0.0')