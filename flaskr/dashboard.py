import os
from flask import Flask, render_template, Blueprint, flash, g, request, redirect
from . import models

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

class URLDashboard:
    def __init__(self, urlpath, status_type):
        self.urlpath = urlpath
        self.status_type = status_type

@bp.route('/<option>', methods=('GET', 'POST'))
def show_dashboard(option):
    urls = models.MURL.get_all()
    urlsDashboard = []
    for url in urls:
        url_id = url.id
        url_processment = models.MURLPROCESSMENT.getByUrlId(url_id)
        if (url_processment is None):
            continue
        status_id = url_processment.status_id
        status_type = models.MSTATUSTYPE.getById(status_id)
        urlsDashboard.append(URLDashboard(url.urlpath, status_type.description))
        if (option is None):
            option = 0
    buttonPressed = option
    return render_template("dashboard.html", urls=urlsDashboard, buttonPressed=buttonPressed)

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