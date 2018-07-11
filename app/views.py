from flask import redirect, render_template, request, url_for

from app import app
from app.models import *

@app.route('/')
@app.route('/lists/')
def index():
    lists = List.query.all()
    return render_template('list/index.html', lists=lists)


@app.route('/lists/<id>')
def get_list(id):
    list = List.query.filter_by(id=id).first()

    return render_template('list/list_index.html', list=list)
