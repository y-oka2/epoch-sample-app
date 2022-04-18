#!/bin/bash

pip install Flask flask-cors requests pytz markdown
pip install pytest pytest-cov

pytest --setup-show tests/ -v -s --cov=.

