from flask import (
    Blueprint, flash, g, render_template, request
)
from . import models

bp = Blueprint('input', __name__, url_prefix='/')

@bp.route('/', methods=('GET', 'POST'))
def get_input():
    if request.method == 'POST':
        # Get URLs from JSON
        from . import db
        from flask_migrate import migrate, upgrade
        db.drop_all()
        migrate()
        upgrade()
        error = None
        if not request.is_json:
            error = 'Not a JSON file'
        else:
            input_data = request.get_json()
            g.sites = input_data['sites']
            g.callback = input_data['callback']
            g.status = {}
            for site in g.sites:
                g.status[site] = 'Not processed'
                url = models.MURL(site)
                url.save()
                status = models.MSTATUSTYPE('Not processed')
                status.save()
                processment = models.MURLPROCESSMENT(url.id, status.id)
                processment.save()

        if error is None:
            return render_template('processing.html')
        flash(error)

    urls = models.MURLPROCESSMENT.get_all()
    if urls is not None:
        g.sites = [models.MURL.query.get(s.url_id).urlpath for s in urls]
        g.status = {models.MURL.query.get(s.url_id).urlpath : models.MSTATUSTYPE.query.get(s.status_id).description for s in urls}
        g.callback = "" #get from DB
        return render_template('processing.html')

    return render_template('input.html')
