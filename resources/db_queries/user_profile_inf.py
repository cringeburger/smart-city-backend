from resources.db_queries.connection import db

from resources.modules import json_serializable

from json import dumps


def get_user_inf(token):

    # Данные пользователя
    us_data = db.q_execute(
        '''select 
			fu.image,
			fu.user_fio
		from dev.fct_user fu
		where 
			fu.id_user = cast( '%s' as uniqueidentifier) '''
        % token
    )[0]

    # Данные достижений
    us_ach_data = db.q_execute(
        ''' 
		select top 4
			da.ach_name,
			ua.ach_status,
			da.attch_image,
			cast((ua.progress*1.0)/(da.ach_end_point*1.0)*100.0 as int),
			da.ach_desc
		from 
			dev.fct_user_achievements ua
		join dev.dim_achievements da 
			on da.id_achievement = ua.id_achievement 
		where ua.id_user = cast( '%s' as uniqueidentifier)
		'''
        % token
    )

    # Данные карты
    us_card_data = db.q_execute(
        '''
		select
			fc.acc_num,
			cast(fc.acc_balance as varchar),
			cast(fc.acc_bns_balance as varchar)
		from 	
			dev.fct_cards fc 
		where fc.id_user = cast( '%s' as uniqueidentifier)
		'''
        % token
    )[0]

    # Данные транзакций
    us_transactions = db.q_execute(
        '''
		select
			'Пополнение' tp,
			'Умная карта' org,
			cast(fcr.transaction_sum as varchar),
			convert(varchar, fcr.transaction_dttm, 103)
		from 
			dev.fct_cards fc 
		left join dev.fct_card_replenishment fcr
			on fc.id_card = fcr.id_card
		where fc.id_user = cast( '%s' as uniqueidentifier)
		union all 
		select
			'Списание' tp,
			fo.org_name ,
			cast(fwo.transaction_sum as varchar),
			convert(varchar, fwo.transaction_dttm, 103) 
		from 
			dev.fct_cards fc 
		left join dev.fct_write_offs fwo 
			on fc.id_card = fwo.id_card
		left join dev.fct_organizations fo 
			on fwo.id_organization = fo.id_organization 
		where fc.id_user = cast( '%s' as uniqueidentifier)
		'''
        % (token, token)
    )

    rspns = json_serializable('json')

    rspns.add_features('img', us_data[0])
    rspns.add_features('fio', us_data[1])
    rspns.add_feature_list('achievments')
    rspns.add_features('card', {
                       'number': us_card_data[0], 'balance': us_card_data[1], "bonuce": us_card_data[2]})
    # dat.add_feature_list('events')
    rspns.add_feature_list('subscribes')
    rspns.add_feature_list('transaction')

    for item in us_ach_data:
        rspns.data[0]['achievments'].append(
            {'name': item[0], 'status': item[1], 'img': item[2], 'progressbar': item[3], "tooltip": item[4]})

    rspns.data[0]['subscribes'].append(
        {'name': 'dad', 'img': 'https://sun1-84.userapi.com/s/v1/if1/9Kq86zbwk3njs6BgBuY9fRSVgr-enaUwuQX2kHIUC4nfDMd8XkA51s8FxBka-TNG4ew29is0.jpg?size=100x0&quality=96&crop=0,420,1320,1320&ava=1', 'content': 'kekw', 'adress': 'kekw', 'link': 'штош'})

    for item in us_transactions:
        rspns.data[0]['transaction'].append(
            {'type': item[0], 'recipient': item[1], 'value': item[2], 'data': item[3]})

    return dumps(rspns.data[0])
