import mysql.connector

db_config = {
	'user':'ece1779'
	'password':'some_password'
	'host':'127.0.0.1'
	'database':'ece1779'
}

db = mysql.connector.connect(user = db_config['user'],
                             passwod = db_config['password'],
                             )
