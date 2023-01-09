-- Active: 1673083792786@@127.0.0.1@3306@car

create table vehicle
	(vin		varchar(7),
	 brand		varchar(20),
	 model		varchar(20),
	 style		varchar(20),
	 primary key (vin,brand,model,style)
	);
CREATE INDEX brand_id ON vehicle(brand);
CREATE INDEX model_id ON vehicle(model);
CREATE INDEX style_id ON vehicle(style);

create table price
	(brand		varchar(20),
	 model		varchar(20),
	 style		varchar(20),
	 price		numeric(10) check (price > 0),
	 primary key (brand,model,style),
	 foreign key (brand) references vehicle (brand)
	 	on delete cascade,
	 foreign key (model) references vehicle (model)
	 	on delete cascade,
	 foreign key (style) references vehicle (style)
	 	on delete cascade

	 );
create table engines
	(engine_id				varchar(5),
	 model				varchar(5),
	 supplier_id		varchar(5), 
	 supplier_name				varchar(20) not null, 
	 engine_date 				DATE,
	 primary key (engine_id,supplier_id,supplier_name,engine_date)
	);
create table transmissions
	(trans_id				varchar(5),
	 model				varchar(5),
	 supplier_id		varchar(5), 
	 supplier_name				varchar(20) not null, 
	 trans_date 				DATE,
	 primary key (trans_id,supplier_id,supplier_name,trans_date)
	);
create table options
	(vin			varchar(7),
	 color			varchar(10) not null, 
	 engine_id			varchar(10), 
	 trans_id 	varchar(10), 
	 primary key (vin),
	 foreign key (vin) references vehicle (vin)
		on delete cascade,
	 foreign key (engine_id) references engines (engine_id),
	 foreign key (trans_id) references transmissions (trans_id)
	);



create table dealer_inventory
	(dealer_id			varchar(5),
	 dealer_name		varchar(20) not null,
	 buy_in_date		DATE, 
	 vin		varchar(7),
	 primary key (dealer_id,buy_in_date,vin),
	 foreign key (vin) references vehicle (vin)
	 	on delete cascade
	);
create table deal
	(deal_date		DATE, 
	 dealer_id	varchar(5),
	 cust_id 	varchar(5),
	 vin		varchar(7),
	 primary key (deal_date,dealer_id,vin,cust_id),
	 foreign key (vin) references vehicle (vin)
	 	on delete cascade,
	 foreign key (dealer_id) references dealer_inventory (dealer_id)
	);

CREATE INDEX customer_id ON deal(cust_id);
create table customer
	(cust_id 			varchar(5), 
	 cust_name			varchar(20) not null,
	 address		varchar(30) not null,
	 phone			varchar(20) not null, 
	 gender			varchar(7) not null,
	 annual_income	numeric(10,0) check (annual_income > 0),
	 primary key (cust_id),
	);


create table plant_inventory
	(plant_id 			varchar(5), 
	 plant_name			varchar(20) not null,
	 assembly_date  DATE,
	 vin			varchar(7),
	 primary key (plant_id,assembly_date,vin),
	 foreign key (vin) references vehicle (vin)
		on delete cascade
	);


create table admins
	(admin_name		varchar(10),
	 passwd			varchar(15),
	 primary key (admin_name,passwd)
	);
insert into admins value('root','test');

create table dealers
	(dealer_id		varchar(5),
	 dealer_name	varchar(20),
	 dlpasswd			varchar(15),
	 primary key (dealer_id,dealer_name,dlpasswd)
	);

