# -*- coding: utf-8 -*-

class Controller:

    def __index__(self):
        self.name = self.__class__.name

    # 错误回调
    def errorJson(code=1000, msg='ok', data=[]):
        return {
            'code': str(code),
            'msg': str(msg),
            'body': data
        }

    # 成功回调
    def successJson(code=0, msg='ok', data=[]):
        return {
            'code': str(code),
            'msg': str(msg),
            'body': data
        }
