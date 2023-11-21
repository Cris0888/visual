from flask import Flask,render_template, redirect
from flaskext.mysql import MySQL


programa= Flask(__name__)
mysql=MySQL()
programa.config['MYSQL_DATABASE_HOST']='localhost'
programa.config['MYSQL_DATABASE_PORT']=3306
programa.config['MYSQL_DATABASE_USER']='root'
programa.config['MYSQL_DATABASE_PASSWORD']=''
programa.config['MYSQL_DATABASE_DB']='consultorio'
mysql.init_app(programa)

@programa.route('/')
def conexion():
    return render_template('login.html')

if __name__=="__main__":
        programa.run(debug=True,port=3306)

