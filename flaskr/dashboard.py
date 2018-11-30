import os
from flask import Flask, render_template, Blueprint, flash, g, request, redirect
from . import models

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

class URLDashboard:
    def __init__(self, urlpath, status_type, restriction, reasons):
        self.urlpath = urlpath
        self.status_type = status_type
        self.restriction = restriction
        self.reasons = reasons

def listToString(list):
    str = ""
    first = True
    for object in list:
        if first:
            str += ", "
        str += object
    return str
@bp.route('/<option>', methods=('GET', 'POST'))
def show_dashboard(option):
    urls = models.MURL.get_all()
    urlsDashboard = []
    buttonPressed = option
    prohibited = models.MURLPROHIBITION.get_all()
    prohibited_urls = [models.MURL.query.get(s.url_id).urlpath for s in prohibited]

    for url in urls:
        url_id = url.id
        url_processment = models.MURLPROCESSMENT.getByUrlId(url_id)
        if (url_processment is None):
            continue
        status_id = url_processment.status_id
        status_type = models.MSTATUSTYPE.getById(status_id)
        restriction = False
        reasonList = [x.reason for x in models.MREASONSPROHIBITION.query.filter_by(url_id=url_id).all()]
        reasons = listToString(reasonList)
        if (url.urlpath in prohibited_urls):
            restriction = True
        urlsDashboard.append(URLDashboard(url.urlpath, status_type.description, restriction, reasons))


    return render_template("dashboard.html", urls=urlsDashboard, buttonPressed=buttonPressed, prohibited_urls=prohibited_urls)

@bp.route('/buttonURL', methods=('GET', 'POST'))
def pressUrl():
    return redirect("/dashboard/0")

@bp.route('/buttonRestricoes', methods=('GET', 'POST'))
def pressRestricoes():
    return redirect("/dashboard/1")

@bp.route('/buttonOutput', methods=('GET', 'POST'))
def pressOutput():
    return redirect("/dashboard/2")

@bp.route('/', methods=('GET', 'POST'))
def get_main():
    return redirect("/dashboard/0")