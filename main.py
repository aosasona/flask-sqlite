from flask import Flask, request, make_response, jsonify
import sqlite3
import db

app = Flask(__name__)


"""
Connect To Sqlite
"""


def connectdb():
    conn = sqlite3.connect('local.db')
    conn.row_factory = sqlite3.Row
    return conn


"""
Default route
"""


@app.route("/")
def default():
    default_res = {
        "status": "ok",
        "text": "Success, the API is on!"
    }

    return jsonify(default_res)


"""
Fetch All Users
"""


@app.route("/users")
def index():
    conn = connectdb()
    cur = conn.cursor()
    try:
        users = []
        cur.execute("SELECT * FROM users")
        results = cur.fetchall()
        for i in results:
            user = {"first_name": i["first_name"], "last_name": i["last_name"], "email": i["email"]}
            users.append(user)
        if len(users) > 0:
            return jsonify({"status": "ok", "data": users})
        else:
            return jsonify({"status": "error", "text": "Oops! No users yet."})
    except:
        return jsonify(status="error")
    finally:
        conn.close()


"""
Add New User
"""


@app.route("/users/add", methods=["POST"])
def add_user():
    data = dict(request.form)
    if "first_name" in data and "last_name" in data and "email" in data and data is not None:
        conn = connectdb()
        cur = conn.cursor()

        try:
            cur.execute("INSERT INTO users (first_name, last_name, email) VALUES(?, ?, ?)", (data["first_name"],
                                                                                             data["last_name"],
                                                                                             data["email"]))
            conn.commit()
            result = jsonify({"status": "ok", "id": cur.lastrowid})
            return result
        except:
            error_res = jsonify({"status": "error", "text": "Possible reason: User already exists!"})
            return error_res
        finally:
            conn.close()
    else:
        error_res = {
            "status": "error",
            "text": "All fields are required",

        }
        return jsonify(error_res)


if __name__ == "__main__":
    app.run(debug=True)
