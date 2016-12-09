import datetime

from flask import (
    Flask, jsonify, make_response,
    render_template, request
)

# Create application.
app = Flask(__name__)
application = app

CORS_HEADERS = {
    'Access-Control-Allow-Origin': "*",
    'Access-Control-Allow-Methods': 'HEAD, GET, OPTIONS',
    'Access-Control-Allow-Headers': ','.join([
        'Origin',
        'Accept',
        'Content-Type',
        'X-Requested-With',
        'X-CSRF-Token'
    ])
}


@app.route('/', methods=['GET'])
def ep0():
    response_data = {
        'msg': 'wats up'
    }

    return make_response(
        jsonify(**response_data),
        200,
        CORS_HEADERS
    )


@app.route('/4bd1cbe4857f83b76d0b5e1c85644791ffaa8e94', methods=['GET'])
def ep1():
    response_data = {
        'date': datetime.datetime.now().isoformat()
    }

    return make_response(
        jsonify(**response_data),
        200,
        CORS_HEADERS
    )
