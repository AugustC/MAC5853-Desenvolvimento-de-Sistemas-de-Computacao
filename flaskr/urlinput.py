from flask import (
    Blueprint, flash, g, render_template, request
)

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
            g.status = {}
            for site in g.sites:
                g.status[site] = 'Not processed'
            g.callback = input_data['callback']
            # TODO: Insert on Database
            # TODO: Start processing URL's

        if error is None:
            return render_template('processing.html')
        flash(error)

    # sites = get sites from database
    sites = None
    if sites is not None:
        # TODO: Get data from database and put on g.sites, g.status, g.callback
        return render_template('processing.html')

    return render_template('input.html')
