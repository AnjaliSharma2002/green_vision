import os
import sys

def error_message_detail(error,error_detail):
    try:
        _,_,exc_tb = error_detail.exc_info()

        if exc_tb is None:
            return f"Error occurred: {str(error)}"
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]", format(
            file_name,exc_tb.tb_lineno,str(error)
        )
        return error_message
    except Exception as e:
        return f"Error occured: {str(error)}. Additionally, error in exception handling: {str(e)}"
    

class ForestException(Exception):
    def __init__(self,error_message,error_detail = sys):

        super().__init(error_message)
        self.error_message = error_message_detail(
            error_message,error_detail = error_detail
        )
        
    def __str__(self):
        return self.error_message