import sqlite3
import uuid

conn = sqlite3.connect('haus.db', check_same_thread=False)
c = conn.cursor()

class User:

	def __init__(self, uid, assoc_name, address, phone, email):
		self.uid = uid
		self.assoc_name = assoc_name
		self.address = address
		self.phone = phone
		self.email = email
		return 

	def get_id(self):
		return self.uid

	def get_assoc_name(self):
		return self.assoc_name

	def get_address(self):
		return self.address

	def get_phone(self):
		return self.phone

	def get_email(self):
		return self.email

	def user_to_dictionary(self):
		return {'id':self.get_id(), 'assoc_name':self.get_assoc_name(), 'address':self.get_address(), 'phone':self.get_phone(), 'email':self.get_email()}

class Form:

	def __init__(self, uid, app_name, user_id):
		self.uid = uid
		self.app_name = app_name
		self.user_id = user_id

	def get_id(self):
		return self.uid

	def get_app_name(self):
		return self.app_name

	def get_user_id(self):
		return self.get_user_id

class CompletedForm:

	def __init__(self, uid, name, user_id, url):
		self.uid = uid
		self.name = name
		self.user_id = user_id
		self.url = url

	def get_id(self):
		return self.uid

	def get_name(self):
		return self.name

	def get_user_id(self):
		return self.user_id

	def get_url(self):
		return self.url

class Controller:

	def __init__(self): 
		return
	
	def create_tables(self):
		self.create_users_table()
		self.create_forms_tables()
		self.create_completed_forms_table()
		return

	def delete_tables(self):
		self.delete_users_table()
		self.delete_forms_table()
		self.delete_completed_forms_table()

	# --------------------- USERS TABLES ---------------------

	def create_users_table(self):
		c.execute('''CREATE TABLE users
             (id text, assoc_name text, address text, phone text, email text)''')
		conn.commit()
		return

	def delete_users_table(self):
		c.execute('''DROP TABLE users''')
		conn.commit()
		return
		

	def add_user(self, assoc_name, address, phone, email):
		uid = str(uuid.uuid1())
		t = (uid,assoc_name,address,phone,email)
		c.execute('INSERT into users values (?, ?, ?, ?, ?)', t)
		conn.commit()
		return

	# Gets all users as User objects
	def get_users(self):
		user_list = []
		for row in c.execute('SELECT * FROM users'):
			user_list.append( User(uid=row[0], assoc_name=row[1], address=row[2], phone=row[3], email=row[4]) )
		return user_list

	def get_users_by_assoc_name(self, assoc_name):
		t = (assoc_name,)
		user_list = []
		for row in c.execute('SELECT * FROM users WHERE assoc_name=?', t):
			user_list.append( User(uid=row[0], assoc_name=row[1], address=row[2], phone=row[3], email=row[4]) )
		return user_list

	def get_users_by_substring_of_assoc_name(self, assoc_name):
		t = ('%' + assoc_name + '%',)
		user_list = []
		for row in c.execute('SELECT * FROM users WHERE assoc_name LIKE ?', t):
			user_list.append( User(uid=row[0], assoc_name=row[1], address=row[2], phone=row[3], email=row[4]) )
		return user_list

	def get_users_by_address(self, address):
		t = (address,)
		user_list = []
		for row in c.execute('SELECT * FROM users WHERE address=?', t):
			user_list.append( User(uid=row[0], assoc_name=row[1], address=row[2], phone=row[3], email=row[4]) )
		return user_list

	def get_users_by_phone(self, phone):
		t = (phone,)
		user_list = []
		for row in c.execute('SELECT * FROM users WHERE phone=?', t):
			user_list.append( User(uid=row[0], assoc_name=row[1], address=row[2], phone=row[3], email=row[4]) )
		return user_list

	def get_users_by_email(self, email):
		t = (email,)
		user_list = []
		for row in c.execute('SELECT * FROM users WHERE email=?', t):
			user_list.append( User(uid=row[0], assoc_name=row[1], address=row[2], phone=row[3], email=row[4]) )
		return user_list

	def empty_users_table(self):
		c.execute('''DELETE FROM users''')
		conn.commit()
		return

	# --------------------- FORMS TABLES ---------------------


	def create_forms_tables(self):
		c.execute('''CREATE TABLE forms
             (id text, app_name text, user_id text)''')
		conn.commit()
		return

	def delete_forms_table(self):
		c.execute('''DROP TABLE forms''')
		conn.commit()
		return

	def add_form(self, app_name, user_id):
		uid = str(uuid.uuid1())
		t = (uid,app_name,user_id)
		c.execute('INSERT into forms values (?,?,?)', t)
		conn.commit()
		return

	def get_forms(self):
		form_list = []
		for row in c.execute('SELECT * FROM forms'):
			form_list.append( Form(uid=row[0], app_name=row[1], user_id=row[2]) )
		return form_list

	def get_forms_by_app_name(self, app_name):
		form_list = []
		t = (app_name,)
		for row in c.execute('SELECT * FROM forms WHERE app_name=?', t):
			form_list.append( Form(uid=row[0], app_name=row[1], user_id=row[2]) )
		return form_list

	def get_forms_by_user_id(self, user_id):
		form_list = []
		t = (user_id,)
		for row in c.execute('SELECT * FROM forms WHERE user_id=?', t):
			form_list.append( Form(uid=row[0], app_name=row[1], user_id=row[2]) )
		return form_list

	def empty_users_table(self):
		c.execute('''DELETE FROM forms''')
		conn.commit()
		return

	# --------------------- COMEPLETED FORMS TABLES ---------------------

	def create_completed_forms_table(self):
		c.execute('''CREATE TABLE completed_forms
             (id text, name text, user_id text, url text)''')
		conn.commit()
		return

	def delete_completed_forms_table(self):
		c.execute('''DROP TABLE completed_forms''')
		conn.commit()
		return

	def add_completed_form(self, name, user_id, url):
		uid = str(uuid.uuid1())
		t = (uid,name,user_id,url)
		c.execute('INSERT into completed_forms values (?, ?, ?, ?)', t)
		conn.commit()
		return

	def get_completed_forms(self):
		completed_form_list = []
		for row in c.execute('SELECT * FROM completed_forms'):
			completed_form_list.append( Form(uid=row[0], name=row[1], user_id=row[2], url=row[3]) )
		return completed_form_list

	def get_completed_forms_by_name(self, name):
		completed_form_list = []
		t = (name,)
		for row in c.execute('SELECT * FROM completed_forms WHERE name=?', t):
			completed_form_list.append( Form(uid=row[0], name=row[1], user_id=row[2], url=row[3]) )
		return completed_form_list

	def get_completed_forms_by_user_id(self, user_id):
		completed_form_list = []
		t = (user_id,)
		for row in c.execute('SELECT * FROM completed_forms WHERE user_id=?', t):
			completed_form_list.append( Form(uid=row[0], name=row[1], user_id=row[2], url=row[3]) )
		return completed_form_list

	def get_completed_forms_by_url(self, url):
		completed_form_list = []
		t = (url,)
		for row in c.execute('SELECT * FROM completed_forms WHERE url=?', t):
			completed_form_list.append( Form(uid=row[0], name=row[1], user_id=row[2], url=row[3]) )
		return completed_form_list

	def empty_users_table(self):
		c.execute('''DELETE FROM completed_forms''')
		conn.commit()
		return


