from flask import render_template
from . import main
from ..requests import get_source
from ..models import Source

# Views
@main.route('/')
def index():

    ''',
    View root page function that returns the index page and its data
    '''

    # Getting top news highlights
    business = get_source('business')
    sports = get_source('sports')
    technology = get_source('technology')
    general = get_source('general')

    # title = 'Home - Welcome to the number 1 news highlighting website online'

    

    
    return render_template('index.html', business = business, sports =sports, technology = technology, general =general )


# @main.route('/highlights/<int:id>')
# def highlights(id):

#     '''
#     View highlights page function that returns the highlights  details page and its data
#     '''
#     highlights = get_highlight(id)
#     title = f'{highlights.title}'
#     comments= comments.get_comments(highlights.id)

#     return render_template('highlights.html',title = title,highlights = highlights,comments = comments)



# @main.route('/search/<highlights_topic>')
# def search(highlights_name):
#     '''
#     View function to displays the search results
#     '''
#     highlights_name_list = highlight_name.split(" ")
#     highlights_name_format = "+".join(highlights_name_list)
#     searched_highlights = search_highlights(highlights_name_format)
#     title = f'search results for {highlights_topic}'
#     return render_template('search_form.html',highlights = searched_highlights)


# @main.route('/highlights/comments/new<int:id>', methods = ['GET','POST'])
# def new_comments(id):

#     form = commentsForm()

#     highlights = get_highlights(id)

#     if form.validate_on_submit():
#         title = form.title.data
#         comments = form.comments.data

#         new_comments = Comments(highlights.id,title,highlights.image,comments)
#         new_comments.save_comments()

#         return redirect(url_for('highlights',id = highlights.id ))

#     title = f'{highlights.title} comments'
#     return render_template('new_comments.html',title = title, comments_form=form, highlights=highlights)
