from django.http import JsonResponse
from .controller import Controller
from ..model.sensitivePersonnelModel import FaceRecognitionIndexModel
import face_recognition
import logging
import numpy as np
logger = logging.getLogger(__name__)

# 定义个空数组
known_face_encodings = []


class FaceController(Controller):

    def __init__(self):
        super.__init__(self)

    def face_recognition(request):

        try:
            a = request.POST.get("url")
            id = request.POST.get("id")

            url = '/Users/guozhixiao/Downloads/' + a

            face_image = face_recognition.load_image_file(url)

            face_locations = face_recognition.face_locations(face_image)
            if face_locations == []:
                return JsonResponse(Controller.errorJson(1000, "ok", ))

            face_encodings = face_recognition.face_encodings(face_image)[0]
            # 将numpy array类型转化为列表
            encoding__array_list = face_encodings.tolist()

            # 将列表里的元素转化为字符串
            encoding_str_list = [str(i) for i in encoding__array_list]

            # 拼接列表里的字符串
            encoding_str = ','.join(encoding_str_list)


            # 数据库字符串拼接出来
            # 转换list
            dlist = encoding_str.strip(' ').split(',')
            # 将list中str转换为float
            dfloat = list(map(float, dlist))
            arr = np.array(dfloat)

            known_face_encodings.append(arr)

            results = face_recognition.compare_faces(known_face_encodings, face_encodings, tolerance=0.8)
            print(results)
            res = FaceRecognitionIndexModel.update({'sensitive_personnel_id': id}, {'face_recognition': encoding_str})
            return JsonResponse(Controller.successJson(0, "ok", res))
        except Exception as e:
            return JsonResponse(Controller.errorJson(1000,"ok",e))