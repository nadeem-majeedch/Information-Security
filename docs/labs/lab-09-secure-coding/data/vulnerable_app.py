"""vulnerable_app.py - DELIBERATELY INSECURE training app for LAB-09.

SAFETY: run ONLY on your isolated lab machine, bound to 127.0.0.1.
This file contains seeded weaknesses for you to find and fix. Never deploy it
on any network reachable by others. See docs/lab-safety-policy.md.
"""

import hashlib
import os

from flask import Flask, request

app = Flask(__name__)

# WEAKNESS 1: credential stored in source code
API_KEY = "sk_live_FAKE_73Jd02KslZ91"


# WEAKNESS 2: password stored as unsalted MD5
def check_password(user, pw):
    stored = {"student": "5f4dcc3b5aa765d61d8327deb882cf99"}  # md5 of a weak password
    return stored.get(user) == hashlib.md5(pw.encode()).hexdigest()


# WEAKNESS 3: SQL injection - query built by string concatenation
def lookup_user(uid):
    query = f"SELECT name, email FROM users WHERE id = '{uid}'"
    # (pretend this runs against a database)
    return query


# WEAKNESS 4: path traversal - unsanitized file read
def read_note(filename):
    with open(os.path.join("/var/notes", filename)) as fh:
        return fh.read()


# WEAKNESS 5: dangerous eval on user input
def calc(expr):
    return eval(expr)


# WEAKNESS 6: admin route with no authorization check
@app.route("/admin/delete_user", methods=["POST"])
def admin_delete():
    uid = request.form["uid"]
    return f"deleted {uid} (pretend)"


# WEAKNESS 7: Flask debug mode left on in production-style launch
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
