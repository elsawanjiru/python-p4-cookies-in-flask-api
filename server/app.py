from flask import Flask, session, jsonify, request, make_response

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secret key for security

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):
    session["hello"] = session.get("hello") or "World"
    session["goodnight"] = session.get("goodnight") or "Moon"

    response = make_response(jsonify({
        'session': {
            'session_key': key,
            'session_value': session[key],
            'session_accessed': session.accessed,
        },
        'cookies': [{cookie: request.cookies[cookie]}
            for cookie in request.cookies],
    }), 200)

    response.set_cookie('mouse', 'Cookie')

    return response

if __name__ == '__main__':
    app.run(port=5555)
