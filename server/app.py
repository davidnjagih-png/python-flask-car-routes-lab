#!/usr/bin/env python3

from flask import Flask

# Models currently in the Flatiron Cars fleet.
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

app = Flask(__name__)


@app.route('/')
def index():
    """Default route: introduces the company."""
    return 'Welcome to Flatiron Cars'


@app.route('/<model>')
def model(model):
    """Report whether the requested model is in the fleet.

    The lookup is case-sensitive, matching the names in existing_models.
    """
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    return f'No models called {model} exists in our catalog'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
