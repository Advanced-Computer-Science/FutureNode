from flask import Flask

app = Flask(__name__)

# Ignore PEP 8: E402 on line 6
import futurenode.views

if __name__ == '__main__':
    app.run()
