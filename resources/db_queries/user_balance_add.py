from resources.modules import json_serializable

from resources.db_queries.connection import db


def upd_balance(token, balance):

	id_card = db.q_execute(
		'''
		select
			cast(id_card as varchar(40)) 
		from 
			dev.fct_cards fc 
		where fc.id_user = cast( '%s' as uniqueidentifier)
		'''
		% token
	)[0][0]
	print(id_card)
	return db.insert(
		'''INSERT INTO dev.fct_card_replenishment (purpose_of_payment,id_card,transaction_sum)
			VALUES ('Пополнение карты', '%s', cast('%s' as numeric(22,2)))'''
		% (id_card, balance)
	)
    

def user_balance(token):

	return db.q_execute(
		'''
		select
			cast(fc.acc_balance as varchar)
		from 	
			dev.fct_cards fc 
		where fc.id_user = cast( '%s' as uniqueidentifier)
		'''
		% token
	)[0][0]
