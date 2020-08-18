import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tzb.settings")# project_name 项目名称
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

from .models import SensitivePersonnel
from .models import FaceRecognitionIndex
from .models import Face
from .models import TempleFace
from .models import Ipcamera

# 敏感人员信息表
class SensitivePersonnelModel():
    # 查询所有数据
    def getAll(where={}):
        return SensitivePersonnel.objects.values().order_by('id')

    # 根据条件查询一条
    def getOne(where):
        return SensitivePersonnel.objects.filter(**where).values().first()

    # 修改人脸信息
    def update(where,data):
        return SensitivePersonnel.objects.filter(**where).update(**data)


# 敏感人员人脸识别码表
class FaceRecognitionIndexModel():
    def getAll(where={}):
        return FaceRecognitionIndex.objects.values().order_by('id')

    # 修改人脸信息
    def update(where,data):
        return FaceRecognitionIndex.objects.filter(**where).update(**data)


class FaceModel():
    def create(data):
        return Face.objects.create(**data)

    #根据条件查询一条
    def getOne(where):
        return Face.objects.filter(**where).values().first()

# 寺庙摄像头截取人脸
class TempleFaceModel:
    def create(data):
        return TempleFace.objects.create(**data)

# 获取摄像头信息
class IpCameraModel:
    def getOne(where):
        return Ipcamera.objects.filter(**where).values().first()


