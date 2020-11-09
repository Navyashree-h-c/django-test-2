from user.model.user.user_model import UserModel
import logging

logger = logging.getLogger(__name__)

class UserManagement():

    def get_list_of_users():
        '''
        get_list_of_users: returns list of users

        '''
        # fetching list of profile
        logger.debug("This is a debug message")
        logger.info("This is an info message")
        logger.error("This is an error message")
        return UserModel.get_list_of_users()

    def get_user_by_id(id):
        '''
        get_user_by_id: returns list of blogs by id

        Agrs:
            id: integer id
        
        '''
        
        logger.debug("Fetching User by id - {id}".format(id=id))
        logger.info("Fetching User by id.")
        return UserModel.get_user_by_id(id)