#!/usr/bin/env python3
# coding=utf-8
from random import choice
import argparse
import flask
import re
import os

# Global variables
SECURE = False
SUPPORTED_ERROR_CODES = {428, 429, 400, 401, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418,
                         422, 431, 500, 501, 502, 503, 504, 505}


libertarian = (
    "A truly free society must allow ",
    "To truly be liberated we must enable ",
    "It is a fundamental right for ",
    "After we take over and leave everyone alone, we will authorize ",
    "Only in a Libertarian utopia will we enable ",
    "Unlike the Statists, we will allow "
)

subject = (
    "five year old children ",
    "ethnic minorities ",
    "convicted felons ",
    "college students ",
    "Ron Paul, Rand Paul, and Ayn Rand ",
    "the homeless ",
    "business owners ",
    "gay couples "
)

action = (
    "to fire people based only on their sexual orientation.",
    "to own and operate rocket launchers.",
    "to perform open heart surgery with a coat hanger.",
    "to defend their marijuana fields with fully automatic machine guns."
)


root = "notes"

# App variables
app = flask.Flask(__name__)


def page_error(error):
    text="Try again"
    return flask.render_template('index.html', page_name=str(error), text=text, title="Error")


for code in SUPPORTED_ERROR_CODES:
    app.register_error_handler(code, page_error)


@app.route('/favicon.ico')
def favicon():
    return flask.send_from_directory(os.path.join(app.root_path, 'static'),
                                     'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/")
def index():
    text = choice(libertarian) + choice(subject) + choice(action)
    return flask.render_template('index.html', title="Libertarian Policy Generator", text=text)


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='The host name or ip address to run on', type=str, default='0.0.0.0')
    parser.add_argument('--port', help='The port number the web server will use', type=int, default=5000)
    parser.add_argument('--cert', help='The SSL certificate', type=str)
    parser.add_argument('--key', help='The SSL private key', type=str)
    parser.add_argument('-d', '--debug', help='Enable debugging mode', action="store_true")
    parser.add_argument('-v', '--verbose', help='Enable verbose mode', action="store_true")
    args = parser.parse_args()

    # Use SSL if keys were supplied
    global SECURE
    SECURE = bool(args.key) and bool(args.cert)

    # Display basic info based on command line arguments
    if args.verbose: print("Verbose mode activated")
    if args.debug: print("Debug mode activated")
    if bool(args.cert) != bool(args.key):
        print("ERROR! --cert and --key must be used together")
        exit(1)
    if args.verbose or args.debug:
        if SECURE:
            print("Using HTTPS on port %d" % args.port)
        else:
            print("Using HTTP on port %d" % args.port)
    if SECURE:
        try:
            context = (args.cert, args.key)
            if args.debug:
                app.run(port=args.port, debug=True, ssl_context=context, host=args.host)
            else:
                app.run(port=args.port, debug=False, ssl_context=context, host=args.host)
        except Exception as e:
            if args.debug:
                print(e)
                exit(2)
            else:
                print("ERROR! Invalid certificate ,key, or host")
                print("Use --debug for more info")
                exit(2)
    else:
        app.run(port=args.port, debug=args.debug, host=args.host)
