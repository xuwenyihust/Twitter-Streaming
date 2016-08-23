class table:

	def __init__(self, conn):
		self.conn = conn
		self.c = conn.cursor()

	def create_db(self, name):
		self.c.execute('CREATE DATABASE IF NOT EXISTS ' + name)
		self.conn.commit()
		print('>>> Database ' + name + ' created!')
		print('-'*50)

	def use_db(self, name):
		self.c.execute('USE '+ name)		
		self.conn.commit()
		print('>>> Use ' + name + ' DataBase!')
		print('-'*50)

	def clean_db(self):
		self.c.execute('SHOW TABLES')
		tables = self.c.fetchall()
		for table in tables:
			self.c.execute('DROP TABLE ' + table[0])
		self.conn.commit()
		print('>>> Database Cleaned!')
		print('-'*50)
	
	def show_tables(self):
		self.c.execute('SHOW TABLES')
		#self.conn.commit()
		tables = self.c.fetchall()
		tables_0 = [table[0] for table in tables]
		print('>>> Show tables!')
		print(tables_0)
		print('-'*50)

	def create_table(self, name):
		self.c.execute('CREATE TABLE IF NOT EXISTS ' + name)
		self.conn.commit()
		print('>>> Table '+ name + ' created!')
		print('-'*50)

	def describe_table(self, name):
		self.c.execute('DESCRIBE ' + name)
		print('>>> Describe table ' + name + '!')
		info = self.c.fetchall()
		for x in info:
			print(x)
		print('-'*50)

	def head(self, n, name):
		self.c.execute('SELECT * FROM ' + name + ' LIMIT ' + str(n))	
		info = self.c.fetchall()
		print('>>> Show first '+ str(n) + '  lines of table!')
		for x in info:
			print(x)
		print('-'*50)


