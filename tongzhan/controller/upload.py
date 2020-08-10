from django.http import JsonResponse
from .controller import Controller
import os
import time

class UploadController(Controller):

    def __init__(self):
        super.__init__(self)

    # 上传文件
    def upload(request):
        # 获取前端传输的文件对象
        file_obj = request.FILES.get('file')
        if not file_obj:
            return JsonResponse(Controller.errorJson(1000, "请选择上传文件", ""))
        # 获取文件类型
        img_type = file_obj.name.split('.')[1]
        # 将文件类型中的数据大写全部转换成小写
        img_type = img_type.lower()
        if img_type in ['png', 'jpg', 'jpeg', 'gif']:
            # 将图片存到指定目录
            # 获取当前时间的时间戳
            timestr = str(time.time()).replace('.', '')
            # 获取程序需要写入的文件路径
            path = os.path.join('tongzhan/static/{0}.{1}'.format(timestr, img_type))
            # 根据路径打开指定的文件(以二进制读写方式打开)
            f = open(path, 'wb+')
            # chunks将对应的文件数据转换成若干片段, 分段写入, 可以有效提
            for chunk in file_obj.chunks():
                f.write(chunk)
            f.close()

            res = {
                'path': path,
            }

            return JsonResponse(Controller.successJson(0, "", res), safe=False)
        else:
            # 存储失败, 返回错误信息
            return JsonResponse(Controller.errorJson(305, "暂不支持该类型", ""))