from flask import (
    Blueprint, flash, g, render_template, request
)
from . import models
import urllib.request
import json

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
            g.status = {}
            for site in g.sites:
                g.status[site] = 'Not processed'
                url = models.MURL(site)
                url.save()
                status = models.MSTATUSTYPE('Not processed')
                status.save()
                processment = models.MURLPROCESSMENT(url.id, status.id)
                processment.save()
                processment.startProcessing()
            prohibited = models.MURLPROHIBITION.get_all()
            prohibited_urls = [models.MURL.query.get(s.url_id).urlpath for s in prohibited]
            URLS = models.MURL.get_all()
            prohibited_sites = [{"url": models.MURL.query.get(s.url_id).urlpath,
                "restricted": True,
                "reasons": [x.reason for x in models.MREASONSPROHIBITION.query.filter_by(url_id=s.url_id).all()]} for s in prohibited]
            allowed_sites = [{"url": url.urlpath,
                "restricted": False,
                "reasons": []} for url in URLS if url.urlpath not in prohibited_urls]
            sites = prohibited_sites + allowed_sites
            sites = json.dumps(sites)
            sites = str(sites)
            req = urllib.request.Request(g.callback, data=sites)

        if error is None:
            g.prohibited = prohibited_urls
            g.reasons = {x['url'] : x['reasons'] for x in prohibited_sites}
            return render_template('output.html')
        flash(error)

    urls = models.MURLPROCESSMENT.get_all()
    if urls:
        g.sites = [models.MURL.query.get(s.url_id).urlpath for s in urls]
        g.status = {models.MURL.query.get(s.url_id).urlpath : models.MSTATUSTYPE.query.get(s.status_id).description for s in urls}
        g.callback = "" #get from DB
        return render_template('processing.html')

    return render_template('input.html')

@bp.route('/clear', methods=('GET', 'POST'))
def clear():
    from . import db
    from flask_migrate import migrate, upgrade
    db.drop_all()
    migrate()
    upgrade()
    return 'cleared'
