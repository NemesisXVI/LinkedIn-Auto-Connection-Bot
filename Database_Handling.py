import mysql.connector
from prettytable import PrettyTable




class DataBase:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="your_database"
        )
        self.mycursor = self.db.cursor()


    def Describe(self,describe=False):
      self.mycursor.execute("Describe profile")
      rows = self.mycursor.fetchall()
      table = PrettyTable()
      table.field_names = ["Field", "Type", "Null", "Key", "Default", "Extra"]
      for row in rows:
        table.add_row(row)

      if describe:
        print(table)
      field_column = [row[0] for row in rows]
      return field_column

    def Show_Content(self):

      table = PrettyTable()
      table.field_names = self.Describe()
      self.mycursor.execute("Select * from profile")
      rows = self.mycursor.fetchall()
      for row in rows:
        table.add_row(row)
      print(table)


if __name__=="__main__":
    db_obj = DataBase()
    db_obj.Describe(describe=True)
    # db_obj.Show_Content()
  #   db_obj.mycursor.execute("INSERT INTO profile VALUES ('abc','Marketing Manager','abc.linkedin',87819,'abc.xyz@gmail','Sent')")
  #   db_obj.db.commit()
  # mycursor.execute("delete from profile")
    db_obj.Show_Content()



