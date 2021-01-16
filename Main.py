import sys
from core.Adder import Adder

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit('Received an illegal number of arguments.')

    try:
        input = (int) (sys.argv[1])
    except ValueError:
         sys.exit('Received an invalid argument. Please enter an integer.')

    print(Adder.threeAdder(input))

'''
from flask import Flask, jsonify, abort
app = Flask(__name__)

@app.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400

@app.route('/', methods=['GET'])
def hello():
    return jsonify(about='Hello, WP!')

@app.route('/threeadder/<num>', methods=['GET'])
def one_adder(num):
    try:
        input = (int) (num)
    except ValueError:
         abort(400, description='Received an invalid argument. Please enter an integer.')

    return jsonify({'result': 3 + input})

if __name__ == '__main__':
    app.run(debug=True)
'''