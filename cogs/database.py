import pymysql

class Session(object):
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                     user='kisak',
                     password='LKRg8nsruBtgkgkmgRYub5xsZSf9QW',
                     db='kisak-bot',
                     charset='utf8',
                     cursorclass=pymysql.cursors.DictCursor)