from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Invalid API endpoint"

@app.route('/api/get_flights')
def get_flights():
    return "{'key':'value'}"

if __name__ == '__main__':
    app.run(port=1337)
