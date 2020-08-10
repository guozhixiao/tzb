import face_recognition
from django.conf import settings
import logging
import time
import hashlib
import cv2
logger = logging.getLogger(__name__)
#
#
# class IndexController(Controller):
#
#     def __init__(self):
#         super.__init__(self)
#
#     def face(self):
#         face_image = face_recognition.load_image_file('/Users/guozhixiao/Downloads/timg (2).jpeg')
#         # 提取人脸编码 人脸的信息
#         face_encodings = face_recognition.face_encodings(face_image)
#         print(face_encodings)
#
#         # 人脸坐标位置 只取脸
#         face_locations = face_recognition.face_locations(face_image)
#
#         # 数据库人脸
#         face2 = face_encodings  # 查询数据库人脸循环做对比
#         print(type(face_encodings))
#         for i in face_encodings:
#             res = face_recognition.compare_faces([i], face2, tolerance=0.8)
#             print(res)
#             if res == [True]:
#                 print(111)
#             elif res == [False]:
#                 print(123)
#
#         # 人脸比较
#         results = face_recognition.compare_faces([i],face2, tolerance=0.8)
#         # print(results)
# md5加密
def md5(password):
    md5 = hashlib.md5()
    # 进行加密，python2可以给字符串加密，python3只能给字节加密
    md5.update(password.encode())
    password_md5 = md5.hexdigest()

    return password_md5

if __name__ == '__main__':
        try:
            url = '/Users/guozhixiao/Downloads/' + '1596770859.jpg'
            print(url)
            face_image = face_recognition.load_image_file(url)

            face_locations = face_recognition.face_locations(face_image)

            for i, element in enumerate(face_locations):
                currtime = time.time()
                x, y, w, h = element
                print(element)
                face = face_image[x:w, h:y]
                md5_file = md5(str(currtime))
                print(md5_file)
                url = "/Users/guozhixiao/Downloads/%s.jpg" % md5_file
                time.sleep(1)
                cv2.imwrite(url, face)
            # for face_location in face_locations:
            #     print(face_location)
            #     x, y, w, h = face_location
            #
            #     face = face_image[x:w, h:y]
            #     cv2.imshow("",face)
            #
            #
            #     md5_file = md5(str(currtime))
            #
            #     url = "/Users/guozhixiao/Downloads/%s.jpg" % md5_file
            #     print(face.dtype)
            #     cv2.imwrite(url, face)



            # for fl in range(len(face_locations)):
            #     zuobiao = face_locations[fl]
            #
            #     x, y, w, h = zuobiao
            #
            #     face = face_image[x:w, h:y]
            #
            #     md5_file = md5(str(currtime))
            #
            #
            #     url = "1.jpg"
            #     print(face.dtype)
            #     cv2.imwrite(url, face)
            #     cv2.waitKey(0)

            # face_encodes = face_recognition.face_encodings(face_image)
            # print(face_encodes[0])
            #
            # x, y, w, h = face_locations[0]
            #
            # face_images = face_image[x:w, h:y]
            #
            # url = "/Users/guozhixiao/Downloads/%s.jpg" % "123456"
            # cv2.imwrite(url, face_images)
            #
            #
            #
            # res = numpy_string(face_image)

        except Exception as e:

            pass