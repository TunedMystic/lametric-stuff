import datetime
import random

from flask import (
    Flask, jsonify, make_response,
    render_template, request
)

import humanize


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


# --------------------------------------------------------
# Util functions

def random_money(max_amount=1000000):
    return humanize.intcomma(
        random.randint(1, max_amount)
    )


def format_date(date):
    return date.strftime('%b, %Y')


def get_month_start(date=None):
    date = datetime.datetime.now() if not date else date
    return datetime.datetime(date.year, date.month, 1)

# --------------------------------------------------------


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


@app.route('/abd1cbe4857f83b76d0b5e1c85644791ffaa8e94', methods=['GET'])
def ep1():
    response_data = {
        'date': datetime.datetime.now().isoformat()
    }

    return make_response(
        jsonify(**response_data),
        200,
        CORS_HEADERS
    )


@app.route('/c6d9e5a8724984c0e3233c95f18c0642e375d142', methods=['GET'])
def ep2():
    date = format_date(get_month_start())
    dollar = random_money()
    number = random.randint(1, 600)
    retailers = random.randint(400, 800)

    quotes = [
        {
            'text': 'LL is Amazing!',
            'icon': 'a2867'
        },
        {
            'text': 'Your cannabis, our platform!',
            'icon': 'a4353'
        },
        {
            'text': 'Shop LL now!',
            'icon': 'i4473'
        }
    ]

    random_quote_1 = random.choice(quotes)
    random_quote_1['index'] = 3

    random_quote_2 = random.choice(quotes)
    random_quote_2['index'] = 5

    response_data = {
        'frames': [
            {
                'text': '.............'.join(['Leaflink' for i in range(3)]),
                'icon': 'i5039',
                'index': 0
            },
            {
                'text': '{} in orders for {}!'.format(dollar, date),
                'icon': 'i34',
                'index': 1
            },
            {
                'text': '{} orders for {}!'.format(number, date),
                'icon': 'i3235',
                'index': 2
            },
            random_quote_1,
            {
                'text': '{} Retailers on LeafLink!'.format(retailers),
                'icon': 'i5039',
                'index': 4
            },
            random_quote_2,
        ]
    }

    return make_response(
        jsonify(**response_data),
        200,
        CORS_HEADERS
    )


if __name__ == '__main__':
    app.run(debug=True, port=7000)
