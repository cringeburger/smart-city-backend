create schema dev

-- Категории граждан
create table dev.dim_citizen_categories(
	id_citizen_category int identity(1,1) primary key,
	cat_name varchar(500)
);

-- Группы достижений
create table dev.dim_achievement_groups(
	id_achievement_group int identity(1,1) primary key,
	ach_gr_name varchar(500)
);

-- Льготы ТК
create table dev.dim_transport_card_privelleges(
	id_tr_card_prvlg int identity(1,1) primary key,
	id_citizen_category int references dev.dim_citizen_categories(id_citizen_category),
	discount varchar(3)
);

-- Пользователь
create table dev.fct_user(
	id_user uniqueidentifier primary key default newid(),
	user_fio varchar(300),
	user_email varchar(100),
	user_phone varchar(30),
	user_login varchar(100),
	user_password varchar(1000),
	id_citizen_category int references dev.dim_citizen_categories(id_citizen_category),
	id_user_type int references dev.dim_user_types(id_user_type),
);

-- Достижения
create table dev.dim_achievements(
	id_achievement int identity(1,1) primary key,
	ach_name varchar(100),
	ach_desc varchar(250),
	ach_end_point smallint,
	id_achievement_group int references dev.dim_achievement_groups(id_achievement_group),
	attch_image varchar(500)
);

-- Транспортные карты
create table dev.fct_transport_cards(
	id_transport_card uniqueidentifier primary key default newid(),
	tc_num varchar(100),
	id_tr_card_prvlg int references dev.dim_transport_card_privelleges(id_tr_card_prvlg),
	id_user uniqueidentifier references dev.fct_user(id_user)
);

-- Карты
create table dev.fct_cards(
	id_card uniqueidentifier primary key default newid(),
	id_user uniqueidentifier references dev.fct_user(id_user),
	acc_num varchar(30),
	acc_balance numeric(22,2),
	acc_bns_balance numeric(22,2)
);

-- Организации
create table dev.fct_organizations(
	id_organization uniqueidentifier primary key default newid(),
	id_org_owner uniqueidentifier references dev.fct_org_owner(id_org_owner),
	org_name varchar(100),
	legal_entity varchar(150),
	org_desc varchar(300),
	org_image varchar(1500),
	org_rating numeric(2,1) default 0,
	open_from varchar(5),
	open_to varchar(5),
	org_phone varchar(30),
	org_email varchar(100),
	org_vk varchar(100),
	org_tg varchar(100)
);

-- Списания
create table dev.fct_write_offs(
	id_write_off uniqueidentifier primary key default newid(),
	purpose_of_payment varchar(100),
	id_card uniqueidentifier references dev.fct_cards(id_card),
	id_organization uniqueidentifier references dev.fct_organizations(id_organization),
	transaction_dttm datetime default sysdatetimeoffset(),
	transaction_sum numeric(22,2)
);

-- Достижения организации
create table dev.dim_org_achievements(
	id_org_achievement int identity(1,1) primary key,
	id_organization uniqueidentifier references dev.fct_organizations(id_organization),
	org_ach_name varchar(100),
	org_ach_desc varchar(250),
	org_ach_end_point smallint,
	org_attch_image varchar(500)
);

-- Прогресс достижений организации
create table dev.fct_user_org_achievements(
	id_user_org_achievement int identity(1,1) primary key,
	id_user uniqueidentifier references dev.fct_user(id_user),
	id_org_achievement int references dev.dim_org_achievements(id_org_achievement),
	progress int,
	ach_status bit
);

-- Прогресс достижений
create table dev.fct_user_achievements(
	id_user_achievement int identity(1,1) primary key,
	id_user uniqueidentifier references dev.fct_user(id_user),
	id_achievement int references dev.dim_achievements(id_achievement),
	progress int,
	ach_status bit
);

-- Периоды
create table dev.dim_periods(
	id_period int identity(1,1) primary key,
	period_dt date,
	week_day varchar(20),
	period_start_dt smalldatetime,
	period_end_dt smalldatetime
);

-- Посещаемость
create table dev.fct_organization_attendance(
	id_attendance int identity(1,1) primary key,
	id_organization uniqueidentifier references dev.fct_organizations(id_organization),
	id_period int references dev.dim_periods(id_period),
	attnd_qnt int
);

-- Сфера услуг
create table dev.dim_services_sector(
	id_svc_sector int identity(1,1) primary key,
	svc_sector_name varchar(100)
);

-- Услуги
create table dev.dim_services(
	id_svc int identity(1,1) primary key,
	id_svc_sector int references dev.dim_services_sector(id_svc_sector),
	svc_name varchar(150),
	svc_desc varchar(200)
);

-- Угслуги организации
create table dev.fct_org_services(
	id_org_svc int identity(1,1) primary key,
	id_organization uniqueidentifier references dev.fct_organizations(id_organization),
	id_svc int references dev.dim_services(id_svc),
	org_svc_cost numeric(22,2),
	bonuses_qnt numeric(22,2)
);

-- Бронирование
create table dev.fct_client_booking(
	id_booking int identity(1,1) primary key,
	id_user uniqueidentifier references dev.fct_user(id_user),
	booking_dt smalldatetime,
	id_org_svc int references dev.fct_org_services(id_org_svc)
);

-- Отзывы
create table dev.fct_reviews(
	id_review int identity(1,1) primary key,
	id_org_svc int references dev.fct_org_services(id_org_svc),
	id_user uniqueidentifier references dev.fct_user(id_user),
	rating numeric(2,1),
	review_desc varchar(200)
);

-- Пополнение карты
create table dev.fct_card_replenishment(
	id_replenishment uniqueidentifier primary key default newid(),
	purpose_of_payment varchar(100),
	id_card uniqueidentifier references dev.fct_cards(id_card),
	transaction_dttm datetime default sysdatetimeoffset(),
	transaction_sum numeric(22,2)
)

-- Типы транзакций (для организации)
create table dev.dim_transaction_types(
	id_tr_type int identity(1,1) primary key,
	tr_type_name varchar(200)
);

-- Счет организации
create table dev.fct_org_accounts(
	id_org_acc uniqueidentifier primary key default newid(),
	id_organization uniqueidentifier references dev.fct_organizations(id_organization),
	acc_num varchar(30),
	acc_balance numeric(22,2)
);

-- Транзакции организации
create table dev.fct_org_transacrions(
	id_replenishment uniqueidentifier primary key default newid(),
	purpose_of_payment varchar(100),
	id_tr_type int references dev.dim_transaction_types(id_tr_type),
	id_org_acc uniqueidentifier references dev.fct_org_accounts(id_org_acc),
	transaction_dttm datetime default sysdatetimeoffset(),
	transaction_sum numeric(22,2)
);

-- Владелец организации
create table dev.fct_org_owner(
	id_org_owner uniqueidentifier primary key default newid(),
	org_owner_fio varchar(300),
	org_owner_login varchar(100),
	org_owner_password varchar(100)
	
);

-- Типы пользователя
create table dev.dim_user_types(
	id_user_type int identity(1,1) primary key,
	user_type_name varchar(500)
);