
import sqlite3


def open_db():
    # create  a connection to the database
    global conn
    conn = sqlite3.connect('passwords.db')
    # create  a connection to the database
    global c

    c = conn.cursor()




def close_db():
    c.close()
    conn.close()


def create_table():

    open_db()

    c.execute('''
    
    CREATE TABLE IF NOT EXISTS passwords(
        application TEXT,
        password TEXT
    
    )
    
    
    ''')



    close_db()

def add_password(app,password):
    open_db()

    c.execute('''
    
    INSERT INTO passwords VALUES (?,?)
    
    ''',(app,password))

    conn.commit()


    close_db()



def show_database():

    open_db()

    c.execute('''
    
    SELECT * FROM passwords
    
    ''')

    data = c.fetchall()
    print("-" * 30)
    print(f'|{"Saved Passwords":>6}|')
    print("-" * 30)

    for row in data:
        print(f'{row[0]+":":<8}|{row[1]:<{28}}')
        print("-"*30)

    close_db()


def delete_password(app,password):

    open_db()


    c.execute('''
    
    DELETE FROM passwords
    WHERE application = (?) AND password = (?)
    
    ''',(app,password))

    conn.commit()



    close_db()

def search_appAndpassword(app,password):

    open_db()


    c.execute('''


     SELECT  * FROM passwords
     WHERE Application = (?) AND Password = (?)
   
    


    ''',(app,password))
  
    data= c.fetchall()

    return data


    close_db()

    


#if __name__ == "__main__":
    #pass




