import functools

from flask import (
        Blueprint, flash, g, redirect, render_template, request, session, url_for
        )
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('input', __name__, url_prefix='/')

@bp.route('/', methods=('GET', 'POST'))
def get_input():
    if request.method == 'POST':
        # Get URLs from JSON
        error = None
        if not request.is_json:
            error = 'Not a JSON file'
        else:
            input_data = request.get_json()
            g.sites = input_data['sites']
            g.callback = input_data['callback']
            # TODO: Insert on Database

        if error is None:
            return redirect(url_for('processing.processing'))

        flash(error)

    return render_template('input.html')
