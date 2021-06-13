from flask import *
from flask.helpers import flash, get_debug_flag
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/create', methods=('GET', 'POST'))

def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'write title.'

        if error is not None:
            flash(error)

        else:
            db = get_debug_flag()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')