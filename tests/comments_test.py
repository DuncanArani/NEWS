import unittest
from models import comments
Comments = comments.Comments

class TestComments(unittest.TestCase):

    # def setUp(self):
    #     self.new_comments = Comments(12345,'comments for highlights',"https://image.tmdb.org/t/p/w500/jdjdjdjn",'This is the best highlights that has ever existed')


    def tearDown(self):
        Comments.clear_comments()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comments.Comments))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comments.highlights_id,12345)
        self.assertEquals(self.new_comments.title,'comments for highlights')
        # self.assertEquals(self.new_comments.imageurl,"")
        self.assertEquals(self.new_comments.Comments,'This is the best highlights that has ever existed')


    def test_save_comments(self):
        self.new_comments.save_comments()
        self.assertTrue(len(Comments.all_comments)>0)


    def test_get_comments_by_id(self):
        
        self.new_comments.save_comments()
        got_comments = Comments.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)


if __name__ == '__main__':
    unittest.main()
