CREATE database ALUNO;

use ALUNO;
CREATE table IF NOT EXISTS tb_test(

id integer primary key auto_increment ,
nome varchar(100),
numero int,
email varchar(200),
dateBirth varchar(200)
);
SELECT * FROM tb_alunos;
USE tb_alunos;
INSERT into tb_alunos values (id,"Matheus Albuquerque",7867839,"matheusalbuquerque34@gmail.com","17/08/2001",82116773);
UPDATE  tb_alunos SET RA = "82116773" WHERE  id=1; 
ALTER TABLE  tb_alunos add column RA int;





 




