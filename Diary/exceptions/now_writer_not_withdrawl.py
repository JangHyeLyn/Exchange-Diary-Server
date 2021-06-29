from rest_framework.exceptions import APIException

class NowWriterNotWithdrwal(APIException):
    status_code = 400
    default_detail = '현재 다이어리 작성자는 탈퇴 불가능'
    default_code = 'ERROR_NOW_WRITER_NOT_WITHDRAWL'