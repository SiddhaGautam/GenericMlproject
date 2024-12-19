import sys

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    lin_no=exc_tb.tb_lineno
    erro_msg=str(error)

    print("error caught in python script at:name->{0},line number->{1},error message->{2}".format(file_name,lin_no,erro_msg))

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail)