from flask import Flask, redirect, render_template, request, url_for
import random, string
import time
import pprint

import util
from db import SQLAlchemy

db = SQLAlchemy()

def run_app():
    # explicit template_folder (defaults to 'templates' at root of project)
    app = Flask(__name__, template_folder='templates')

    from models import Link
    
    db.initialize('mssql+pyodbc://@localhost/UNBIG?driver=ODBC+Driver+17+for+SQL+Server?trusted_connection=yes')
    # t = Link.get_url_by_id(url_id='VyFVXAR2')
    # print(t.url)
    #db.setup_db()

    #Link.insert_url('oiu23lkd9', 'www.someurl.com')

    @app.route('/')
    def home():
        print('HOME')
        return render_template('home.html')

    
    @app.route('/share/<string:url_id>')
    def share(url_id):
        print('SHARE')
        return render_template('share.html', url_id=url_id)


    @app.route('/<path:uid>')
    def get(uid):
        # print(f'uid: {uid}')
        # print(request.url)
        # print(request.full_path)
        pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(request.environ)
        url = Link.get_url_by_id(url_id=uid)
        print('url object:')
        print(url)
        pp.pprint(url)

        if url is not None:
            #return render_template('go.html', url=url)
            return redirect(url.url, 301)
        else:
            return render_template('not-found.html')


    @app.route('/create', methods=['POST'])
    def create():
        
        # gen id
        url_id = util.generate_id(8)

        # save to DB
        Link.insert_url(url_id, request.form['url'])

        # return link to page
        return redirect(url_for('share', url_id=url_id))


    app.run(debug=True)