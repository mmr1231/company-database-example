import sqlite3
class Database:
    def __init__(self,db):

        self.con=sqlite3.connect(db)
        self.cor=self.con.cursor()

        sql='''
        CREATE TABLE if not exists employees(
        id integer primary key,
        name text,age text,
        job text,email text,
        mobile text,address text


        )
        
        
        '''
        self.cor.execute(sql)
        self.con.commit()
    def   insert(self,name,age,job,email,mobile,address) :
        self.cor.execute('insert into employees values (NULL,?,?,?,?,?,? )',
                   (name,age,job,email,mobile,address) )   
        self.con.commit ()  
    def fatch (self):
        self.cor.execute('SELECT * FROM employees' )
        rows=self.cor.fetchall()   
        return rows
    def romove (self,id):
        self.cor.execute('delete from employees where id=? ',(id,))
        self.con.commit()

    def update (self,id,name,age,job,email,mobile,address):
        self.cor.execute('update employees set name=?,age=?,mobile=?,email=?,job=?,address=? where id=?',
                        (name,age,mobile,email,job,address,id) )
        self.con.commit()