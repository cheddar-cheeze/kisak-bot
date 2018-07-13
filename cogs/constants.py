import pymysql.cursors
embed_color = 0xffbc77
db = pymysql.connect(host='localhost',
                     user='kisak',
                     password='',
                     db='kisak-bot',
                     charset='utf8',
                     cursorclass=pymysql.cursors.DictCursor)