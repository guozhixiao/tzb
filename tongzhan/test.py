from .model.sensitivePersonnelModel import *

if __name__ == '__main__':
    res = SensitivePersonnelModel.getAll()
    print(res)