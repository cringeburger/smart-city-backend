from resources.modules import hash_pass, json_serializable

from resources.db_queries.connection import db


def check_user_login(login, password):
	
	data = db.q_execute(
		'''select 
			f.user_login, 
			f.user_password, 
			cast(f.id_user as varchar(50)), 
			ut.user_type_name 
		from 
			dev.fct_user f
		join dev.dim_user_types ut 
			on ut.id_user_type = f.id_user_type '''
		)

	for item in data:
		if login.lower() == item[0] and hash_pass.hash_check(item[1], password) == True:
			result = json_serializable('rsp')
			result.add_features('login', str(item[0]))
			result.add_features('token', str(item[2]))
			result.add_features('role', str(item[3]))
			return result.data[0]
	
	return 'wrong'
