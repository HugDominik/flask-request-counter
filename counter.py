from flask import Flask, request, render_template
app = Flask(__name__)


counter = 0


@app.route('/request-counter')
def request_counter_simple():
    global counter
    counter += 1
    return str(counter)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )