import pymysql

db_ini = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "passwd": "root",
    "db": "adventureworks"
}

db = pymysql.connect(**db_ini)
cu = db.cursor()
cu.execute("select * from AddressType")
# print(cu.fetchall())
for result in cu.fetchall():
    print(result[0], result[1])

# insert_sql = "insert into AddressType (name,rowguid) values('测试','123456789')"
# cu.execute(insert_sql)
# db.commit()
# name_new = '测试编辑5'
# update_sql = "update AddressType set name='"+name_new+"' where name='测试'"
# print(update_sql)
# cu.execute(update_sql)
# db.commit()
# update_query = "select * from AddressType where AddressTypeID=9"
# cu.execute(update_query)
# results = cu.fetchall()
# if results[0][1] == name_new:
#     print("编辑成功")

# delete_sql = "delete  from AddressType where name='"+name_new+"'"
# cu.execute(delete_sql)
# db.commit()

# delete_query = "select * from AddressType where name='"+name_new+"'"
# cu.execute(delete_query)
# results = cu.fetchall()
# print(results)
# if len(results) == 0:
#     print("删除成功")

db.close()
