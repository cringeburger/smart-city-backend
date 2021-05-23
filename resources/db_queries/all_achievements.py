from resources.db_queries.connection import db

from resources.modules import json_serializable

from json import dumps


def all_achs(token):

	all_achs = db.q_execute(
		'''
		with tb1 as 
		(select
			da.ach_name,
			ua.ach_status,
			da.attch_image,
			cast((ua.progress*1.0)/(da.ach_end_point*1.0)*100.0 as int) prc,
			da.ach_desc
		from 
			dev.fct_user_achievements ua
		join dev.dim_achievements da 
			on da.id_achievement = ua.id_achievement 
		where ua.id_user = cast('%s' as uniqueidentifier)),
		tb2 as
		(select
			da.ach_name,
			cast(0 as bit) ach_status,
			da.attch_image,
			cast(0 as int) prc,
			da.ach_desc
		from
		dev.dim_achievements da )
		select * from tb1
		union all
		select * from tb2
		where tb2.ach_name not in (select ach_name from tb1)
		'''
		% token
	)
	
	rspns = json_serializable('json')
	rspns.add_feature_list('achievments')

	for item in all_achs:
		rspns.data[0]['achievments'].append(
			{'name': item[0], 'status': item[1], 'img': item[2], 'progressbar': item[3], "tooltip": item[4]})

	return dumps(rspns.data[0])
	