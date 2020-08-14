from flask import request,url_for
from flask import Flask, session, render_template
import functions
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
app = functions.create_app()
# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

#dialect+driver://username:password@host:port/database
DATABASE_URL= "postgres://kjgyeljykmpjug:c020562ddc1e963034da169d55850473b5be3a2aa85e13758d0a82563e94925a@ec2-3-208-50-226.compute-1.amazonaws.com:5432/d6srv92ha5qdug"

# Set up database
engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))

#main home page
@app.route("/")
def index():  
    return render_template('index.html')

if __name__ == '__main__':
    app.run()