from flask import Flask
from flask import request

sample = Flask(__name__)

@sample.route("/")
def main():
    return "Te estás conectando desde la IP: " + request.remote_addr + "\n"

if __name__ == "__main__":
        sample.run(host="0.0.0.0", port=8000)