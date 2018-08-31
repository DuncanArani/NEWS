class Highlights:
    '''
    Highlights class to define highlights Objects
    '''

    def __init__(self,id,title,comments,image,vote_average,vote_count):
        self.id =id
        self.title = title
        self.sammary = sammary
        self.image = "https://image.tmdb.org/t/p/w500/" + image
        self.vote_average = vote_average
        self.vote_count = vote_count



class Comments:

    all_comments = []

    def __init__(self,highlights_id,title,imageurl,comments):
        self.highlights_id = highlights_id
        self.title = title
        self.imageurl = imageurl
        self.comments = comments


    def save_comments(self):
        Comments.all_comments.append(self)


    @classmethod
    def clear_comments(cls):
        Comments.all_comments.clear()

    @classmethod
    def get_comments(cls,id):

        response = []

        for comments in cls.all_comments:
            if comments.highlights_id == id:
                response.append(comments)

        return response