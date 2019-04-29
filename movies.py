from flask import Flask, render_template, redirect, url_for, request
from modules import convert_to_dict, make_ordinal

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# Flask-Bootstrap requires this line
Bootstrap(app)

# create a list of dicts
movies_list = convert_to_dict("movies_clean.csv")

# create a class for the form
class SearchForm(FlaskForm):
    text = StringField('Type full or partial text to search for:', validators=[Required()] )
    submit = SubmitField('Search')

# first route for search aka sort of like homepg
@app.route('/',  methods=['GET', 'POST'] )
def search():
    form = SearchForm()
    message = ""

    # make three empty lists
    ids_list = []
    name_list = []
    pairs_list = []

    if request.method == "POST":
        # get the inputs from the form
        text = request.form.get("text")

        # loop to find ALL movies who match inputs
        # but ONLY those who match
        for movie in movies_list:
            if text.lower() in movie['Movie'].lower():
                ids_list.append(movie['Number'])
                name_list.append(movie['Movie'])

        pairs_list = zip(ids_list, name_list)

        message = "Sorry, no match was found."

    # some more code will go here
    if len(ids_list) == 1:
        return redirect( url_for('detail', num=ids_list[0] ) )
    elif len(ids_list) > 0:
        return render_template('index.html', pairs=pairs_list, the_title="Search Results")
    else:
        return render_template('search.html', form=form, message=message)

# second route
@app.route('/movie/<num>')
def detail(num):
    for movie in movies_list:
        if movie['Number'] == num:
            mov_dict = movie
            break
    # a little bonus function, imported
    ord = make_ordinal( int(num) )
    return render_template('movie.html', mov=mov_dict, ord=ord, the_title=mov_dict['Movie'])

# third route
@app.route( '/index' )
def index():
    ids_list = []
    name_list = []
    pairs_list = []
    # fill one list with the number of each movie and
    # fill the other with the name of each movie
    for movie in movies_list:
        ids_list.append(movie['Number'])
        name_list.append(movie['Movie'])
        # zip() is a built-in function that combines lists
        # creating a new list of tuples
    pairs_list = zip(ids_list, name_list)

    return render_template('index.html', pairs=pairs_list, the_title="Movie Index")

# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
