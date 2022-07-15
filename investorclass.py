import sqlite3
class Investor:
    def __init__(self):
        self.name = None
        self.equity = None
        self.funds = None
    
    def add_investor(self, name, equity, funds):
        try: 
            db = sqlite3.connect('database.db')
            curr = db.cursor()
            details = [name, equity, funds]
            query = '''INSERT INTO Investors(name, equity, funds)
                    VALUES(?, ?, ?)'''
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
            curr.execute('''SELECT * FROM Investors''')
            res = curr.fetchall()
            for i in res:
                print(i)
            db.commit()
            db.close()
        except sqlite3.Error as error:
            print("Error in connecting to database : ", error) 
            db.close()