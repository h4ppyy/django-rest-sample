create table if not exists book (
	id int primary key auto_increment,
	book_name varchar(255) not null,
	created_at datetime default now()
);
