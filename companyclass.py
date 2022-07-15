import sqlite3
class Company:
    def __init__(self):
        self.name = None
        self.equity = None
        self.funding = None
        self.revenue = None
        
    def add_companies(self, name, equity, funding, revenue):
        try: 
            db = sqlite3.connect('database.db')
            curr = db.cursor()
            details = [name, equity, funding, revenue]
            query = '''INSERT INTO Companies(name, equity, funding, revenue)
                    VALUES(?, ?, ?, ?)'''
            curr.execute(query, details)
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print("Error in connecting to database : ", error) 
            db.close()
    
    def get_details(self):
        try: 
            db = sqlite3.connect('database.db')
            curr = db.cursor()
            curr.execute('''SELECT * FROM Companies''')
            res = curr.fetchall()
            for i in res:
                print(i)
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print("Error in connecting to database : ", error) 
            db.close()