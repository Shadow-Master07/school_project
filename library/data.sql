Create database Library;
Use Library;
Create table books (book_name varchar(50), book_code varchar(50), total int, subject varchar(50));
Create table issue (name varchar(50), reg_no varchar(10), book_code int, issue varchar(50));
Create table submit (name varchar(50), reg_no varchar(10), book_code int, submit  varchar(50));