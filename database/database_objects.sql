-- День недели для периодов
create trigger dev.weekday_add
on dev.dim_periods
after insert 
as 
begin
	set language russian
	update dev.dim_periods
	set week_day = datename(weekday, (select period_dt from inserted))
	where id_period = (select id_period from inserted)
end;

-- Пополнение счета юзера
create trigger dev.acc_user_add
on dev.fct_card_replenishment 
after insert
as 
begin
	update dev.fct_cards 
	set acc_balance = acc_balance + (select transaction_sum from inserted)
	where id_card = (select id_card from inserted)
end;

-- Списание со счета юзера
create trigger dev.acc_user_wr_off
on dev.fct_write_offs 
after insert 
as 
begin 
	update dev.fct_cards 
	set acc_balance = acc_balance - (select transaction_sum from inserted)
	where id_card = (select id_card from inserted)
end;

-- Пополнение счета организации
create trigger dev.org_acc_add
on dev.fct_org_transacrions 
after insert 
as 
begin 
	if (select t.tr_type_name from dev.dim_transaction_types t where t.id_tr_type = (select id_tr_type from inserted)) = 'Пополнение'
	update dev.fct_org_accounts 
	set acc_balance = acc_balance + (select transaction_sum from inserted)
	where id_org_acc = (select id_org_acc from inserted)
end;

-- Списание со счёта организации
create trigger dev.org_wr_off
on dev.fct_org_transacrions 
after insert 
as 
begin 
	if (select t.tr_type_name from dev.dim_transaction_types t where t.id_tr_type = (select id_tr_type from inserted)) = 'Списание'
	update dev.fct_org_accounts 
	set acc_balance = acc_balance - (select transaction_sum from inserted)
	where id_org_acc = (select id_org_acc from inserted)
end;


--номера карт
create sequence dev.org_card_num start with 1 increment by 1;
create proc dev.generate_org_card_num
@acc_num varchar(16) output
as select @acc_num = substring(cast(10000000000000000+(next value for dev.org_card_num) as varchar), 2, 16);


--Создание счёта юзера
create trigger dev.add_user_acc
on dev.fct_user 
after insert 
as 
begin 
	declare @acc_num varchar(16)
	exec dev.generate_org_card_num @acc_num output
	insert into dev.fct_cards(id_user, acc_num, acc_balance, acc_bns_balance)
	values((select id_user from inserted), @acc_num, 0, 0)
end;

--Создание счёта организации
create trigger dev.add_org_acc
on dev.fct_organizations 
after insert 
as 
begin 
	declare @acc_num varchar(30)
	exec dev.generate_org_card_num @acc_num output
	insert into dev.fct_org_accounts(id_organization, acc_num, acc_balance)
	values((select id_organization from inserted), @acc_num, 0)
end;
