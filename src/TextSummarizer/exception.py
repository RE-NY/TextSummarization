import sys     #this lib has info about all the exceptions that occurs in runtime.
import logging
from TextSummarizer.logging import logger   # This is reqd to save it in logs folder.


def error_message_info(error, error_detail : sys):
    _, _, exc_tb = error_detail.exc_info() #Only the last third info of this function is useful as traceback.
    file_name = exc_tb.tb_frame.f_code.co_filename
    message = '''
    An Error occured in the python script name : [{0}], line number : [{1}], error message : [{2}]'''.format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return message
    
#For any help see python exception documentation

class CustomException(Exception):
    def __init__(self, error_message, error_detail : sys):
        super().__init__(error_message)
        self.error_message = error_message_info(error_message, error_detail = error_detail)
    
    def __str__(self):
        return self.error_message
    


#So the idea that with every exception we will convert it to customexception then log it with the logger file
#and then use logging.INFO to put it inside the file!.


# if __name__ == "__main__":

#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e, sys)