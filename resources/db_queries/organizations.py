from resources.modules import json_serializable

from resources.db_queries.connection import db
from json import dumps


def org_inf(token):

	org = db.q_execute(
		'''
		select 
			o.org_name,
			dss.svc_sector_name,
			cast(o.org_rating as varchar(3)),
			o.address,
			o.org_image,
			o.org_short_desc,
			o.id_organization,
			dss.[sysname],
			o.org_email 
		from dev.fct_organizations o
		left join dev.fct_org_services ou
		on o.id_organization = ou.id_organization 
		left join dev.dim_services ds 
		on ou.id_svc = ds.id_svc 
		left join dev.dim_services_sector dss 
		on ds.id_svc_sector = dss.id_svc_sector 
		where o.id_organization = cast( '%s' as uniqueidentifier)
		'''
		% token
	)[0]

	org_achs = db.q_execute(
		'''
		select
			da.org_ach_name ,
			cast(0 as bit) st,
			da.org_attch_image,
			cast(0 as int) prc,
			da.org_ach_desc 
		from
		dev.dim_org_achievements da 
		where da.id_organization = cast( '%s' as uniqueidentifier)
		'''
		% token
	)

	org_svc = db.q_execute(
		'''
		select 
			ds.svc_name,
			fos.[image],
			ds.svc_desc,
			cast(fos.bonuses_qnt as varchar(10)),
			cast(fos.org_svc_cost as varchar(10)),
			'' link
		from 
		dev.fct_org_services fos 
		left join dev.dim_services ds 
		on ds.id_svc = fos.id_svc 
		where fos.id_organization = cast( '%s' as uniqueidentifier)
		'''
		% token
	)
	
	rspns = json_serializable('json')

	rspns.add_features('org',
		{
		"name": org[0],
		"type": org[1],
		"rating": org[2],
		"adress": org[3],
		"img": org[4],
		"smallcontent": org[5],
		"link": org[6],
		"systname": org[7],
		"mail": org[8]
		} 
	)

	rspns.add_feature_list('achievments')
	for item in org_achs:

		rspns.data[0]['achievments'].append(
			{'name': item[0], 'status': item[1], 'img': item[2], 'progressbar': item[3], "tooltip": item[4]})


	rspns.add_feature_list('uslugi')
	for item in org_svc:
		rspns.data[0]['uslugi'].append(
			{
			"name": item[0],
			"img": item[1],
			"content": item[2],
			"bonuce": item[3],
			"price": item[4],
			"link": item[5]
		})

	return dumps(rspns.data[0])


def org_list(token):

	list_org = db.q_execute(
		'''
		select
			o.org_name,
			dss.svc_sector_name,
			cast(o.org_rating as varchar(10)),
			o.address,
			o.org_image,
			o.org_short_desc,
			cast(o.id_organization as varchar(50)),
			dss.[sysname] 
		from dev.fct_organizations o 
		left join dev.fct_org_services ou
		on o.id_organization = ou.id_organization 
		left join dev.dim_services ds 
		on ou.id_svc = ds.id_svc 
		left join dev.dim_services_sector dss 
		on ds.id_svc_sector = dss.id_svc_sector 
		where dss.[sysname] = '%s'
		'''
		% token
	)

	rspns = []

	for item in list_org:
		rspns.append(
			{
				"name": item[0],
				"type": item[1],
				"rating": item[2],
				"adress": item[3],
				"img": item[4],
				"smallcontent": item[5],
				"link": item[6],
				"systname": item[7]
			}
		)

	return dumps(rspns)
	