import sys

def error_message(error, error_detail: sys):
    _,_,err_tb = error_detail.exc_info()
    fname = err_tb.tb_frame.f_code.co_filename
    lineno = err_tb.tb_lineno
    errmsg = str(error)

    error_message = "Error occured in [{0}] at line [{1}]: [{2}]".format(fname, lineno, errmsg)
    return error_message


class CustomException(Exception):
    def __init__(self, error_msg, error_detail: sys):
        super().__init__(error_msg)
        self.error_message = error_message(error_msg, error_detail=error_detail)

    def __str__(self):
        return self.error_message