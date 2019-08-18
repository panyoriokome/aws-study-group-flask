from flask import Flask, jsonify, request

app = Flask(__name__)

programs = []

@app.route('/programs', methods=['GET'])
def get_programs():
    return jsonify(programs), 200

@app.route('/program/<title>', methods=['GET'])
def get_program(title):
    for program in programs:
        if title == program['title']:
            return jsonify(program)
    return jsonify({'message': 'Requested item was not found.'}), 404

@app.route('/program/<title>', methods=['POST'])
def make_program(title):
    program = request.get_json()
    programs.append(program)
    return jsonify(program), 201
        
app.run(host='0.0.0.0', port=80, debug=True)
