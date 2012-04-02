from flask import Blueprint, render_template, request

from twilio import twiml


main = Blueprint('main', __name__)


def index(name=None):
    """Will contain login/status page"""
    return render_template('index.html', name=name)

@main.route("/voice")
def voice():
    """Hello! Goodbye."""
    from_number = request.args.get('From', None)
    response = twiml.Response()
    response.say("Thanks for calling. Goodbye.")
    return str(response)

@main.route("/sms")
def sms():
    """A basic echo responder"""
    response = twiml.Response()
    message = request.args.get('Body', None)
    response.sms("Thanks for texting the following: '%s'\nGood bye." % message)
    return str(response)
