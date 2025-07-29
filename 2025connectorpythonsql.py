# import mysql.connector
# def insert_data(id, name, email,city_id):
    
#     mydb= mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="roottoor",
#         database="jayavardhan_ece"
#     )
#     print("connected ")


#     mycursor=mydb.cursor()
#     sql="INSERT INTO city2 (id,name,email,city_id) VALUES (%s,%s,%s,%s)"
#     val = [id, name, email,city_id]
#     mycursor.execute(sql, val)

#     mydb.commit()
#     mycursor.close()
#     mydb.close()
#     print(mycursor.rowcount, "record inserted.")

# id = input("enter the id")
# name = input("enter the name")
# email = input("enter the email")
# city_id = input("enter the cityid")

# insert_data(id, name, email,city_id)





