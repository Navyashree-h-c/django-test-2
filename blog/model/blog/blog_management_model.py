from blog.model.blog.blog_model import BlogModel
import logging

logger = logging.getLogger(__name__)

class BlogManagement():

    def get_list_of_blogs():
        '''
        get_list_of_blogs: returns list of blogs

        '''
        # fetching list of profile
        logger.debug("This is a debug message")
        logger.info("This is an info message")
        logger.error("This is an error message")
        return BlogModel.get_list_of_blogs()

    def get_blog_by_id(id):
        '''
        get_blog_by_id: returns list of blogs by id

        Agrs:
            id: integer id
        
        '''
        
        logger.debug("Fetching Blog by id - {id}".format(id=id))
        logger.info("Fetching Blog by id.")
        return BlogModel.get_blog_by_id(id)