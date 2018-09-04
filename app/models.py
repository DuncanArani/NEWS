class Highlights:
    '''
    Highlights class to define highlights Objects
    '''

    def __init__(self, id, author, title, description, url, urlToImage, publishedAt):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

class Source:
    
    #sources class to define source objects


    def __init__(self, id, title, description, url, category, country):
        self.id = id
        self.title = title
        self.description = description
        self.link = url
        self.type = category
        self.place = country

class Articles:
        
    #categories class to define category objects
    

    def __init__(self, id, title, description, url, urlToImage, publishedAt):
        self.id =id 
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt


# class Comments:

#     all_comments = []

#     def __init__(self,highlights_id,title,imageurl,comments):
#         self.highlights_id = highlights_id
#         self.title = title
#         self.imageurl = imageurl
#         self.comments = comments


#     def save_comments(self):
#         Comments.all_comments.append(self)


#     @classmethod
#     def clear_comments(cls):
#         Comments.all_comments.clear()

#     @classmethod
#     def get_comments(cls,id):

#         response = []

#         for comments in cls.all_comments:
#             if comments.highlights_id == id:
#                 response.append(comments)

#         return response



# class Highlights:
        
#     #highlights class to define  objects headlines
    

#     def __init__(self, title, description, url, urlToImage, publishedAt):
#         self.title = title
#         self.description = description
#         self.url = url
#         self.urlToImage = urlToImage
#         self.publishedAt = publishedAt
