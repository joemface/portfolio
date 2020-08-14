from flask import Flask, render_template

def page_not_found(e):
  return render_template('_404.html'), 404

def create_app():
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)
    return app

