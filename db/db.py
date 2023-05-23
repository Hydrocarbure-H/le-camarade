import conf
import mysql.connector


# Connect to the database
def connect():
    db_user, db_pass, db_host, db_name = conf.db_creds()
    try:
        mydb = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name
        )
        return mydb
    except Exception as e:
        print(e)
        return None


def connectfirsttime():
    db_user, db_pass, db_host, db_name = conf.db_creds()
    try:
        mydb = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
        )
        construct(mydb)
        fill(mydb)
        return "Database cleaned, created and filled !"
    except Exception as e:
        print(e)
        return "Error while cleaning, creating and filling the database !"


def construct(db):
    # Create a db with a name lecamarade
    mycursor = db.cursor()
    # Delete the database if it exists
    mycursor.execute("DROP DATABASE IF EXISTS lecamarade")
    mycursor.execute("CREATE DATABASE IF NOT EXISTS lecamarade")
    mycursor.execute("USE lecamarade")

    # Create a table users with id, pseudo
    mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, pseudo VARCHAR(255))")

    # Create a table actions with id, user_id, action, date
    mycursor.execute(
        "CREATE TABLE actions (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, action VARCHAR(255), date DATETIME)")

    # Create a table template_actions with id, name, value
    mycursor.execute("CREATE TABLE template_actions (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), value INT)")
    db.commit()


def fill(db):
    camarades = conf.camarades()
    # Insert some users
    mycursor = db.cursor()
    sql = "INSERT INTO users (pseudo) VALUES (%s)"
    val = [
        camarades[0],
        camarades[1],
        camarades[2],
        camarades[3],
        camarades[4]
    ]
    for v in val:
        mycursor.execute(sql, (v,))

    # Insert some template actions
    sql = "INSERT INTO template_actions (name, value) VALUES (%s, %s)"
    val = [
        ("haha", 5),
        ("drift", 10),
        ("insult", -10),
        ("other", -15),
        ("camarade", 1)
    ]
    for v in val:
        mycursor.execute(sql, v)
    db.commit()
