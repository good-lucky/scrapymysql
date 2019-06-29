import  pymysql

class mysqlPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            db='scrapymysql',
            user='root',
            passwd='root',
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            '''insert into mingyan(tag, cont)value (%s, %s)''', (item['tag'], item['cont'],)
        )
        self.connect.commit()
        return item
