from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_highlights,search_highlights
from .forms import CommentsForm
from ..models import Comments

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting top news highlights
    top_highlights = get_highlights('trending_top-highlights')
    bussiness_highlights = get_highlights('trending_bussiness-Highlights')
    sports_highlights = get_highlights('trending_sports-Highlights')
    entertainment_highlights = get_highlights('trending_entertainment-Highlights')

    title = 'Home - Welcome to the number 1 news highlighting website online'

    search_highlights = request.args.get('highlights_query')

    if search_highlights:
        return redirect(url_for('search',highlights_topic=search_highlights))
    else:
        return render_template('index.html', title = title, top_highlights = get_highlights('top_news-highlights'), bussiness_highlights = trending_bussiness-highlights, sport_highlights= trending_sports-highlights,entertainment_highlights = get_highlights('trending_entertainment-Highlights') )


@main.route('/highlights/<int:id>')
def movie(id):

    '''
    View highlights page function that returns the highlights  details page and its data
    '''
    highlights = get_highlight(id)
    title = f'{highlights.title}'
    comments= comments.get_comments(highlights.id)

    return render_template('highlights.html',title = title,highlights = highlights,comments = comments)



@main.route('/search/<highlights_topic>')
def search(movie_name):
    '''
    View function to displays the search results
    '''
    highlights_topic_list = highlight_topic.split(" ")
    highlights_topic_format = "+".join(highlights_topic_list)
    searched_highlights = search_highlights(highlights_topic_format)
    title = f'search results for {highlights_topic}'
    return render_template('search_form.html',movies = searched_highlights)


@main.route('/highlights/comments/new<int:id>', methods = ['GET','POST'])
def new_comments(id):

    form = commentsForm()

    highlights = get_highlights(id)

    if form.validate_on_submit():
        title = form.title.data
        comments = form.comments.data

        new_comments = Comments(highlights.id,title,highlights.image,comments)
        new_comments.save_comments()

        return redirect(url_for('highlights',id = movie.id ))

    title = f'{highlights.title} comments'
    return render_template('new_comments.html',title = title, comments_form=form, highlights=highlights)
