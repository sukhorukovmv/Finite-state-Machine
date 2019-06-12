Finite-state-Machine
=====================
![Finite-state-Machine](./fsm.png)
Введение
-----------------------------------

pip3 install -r requipments/development.txt
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL='postgresql://DBUSERNAME:DBPASSWORD@localhost/DBNAME'
Запускай makefile для добавления переменных окружения
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py runserver


#Работа с базой 
установка
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -
sudo apt-get update 
sudo apt-get install postgresql postgresql-contrib
contrib предоставляет некоторый дополнительный функционал и утилиты):
основные команды
sudo -u postgres psql - зайти без смены сесси
\q                    - выйти из базы

create user username with password 'password';  - создание пользователя 
create database vscale_db;                      - создание базы 
grant all privileges on database vscale_db to username; - где vscale_db — название базы данных, выбранное на шаге 5, а username — имя пользователя, заданное на шаге 4.
psql -h localhost vscale_db username - зайти в базу под пользователем

alter user postgres with password 'root'; - изменить пароль пользователя 

\dt - просмотр таблиц в базе 

psql databasename < data_base_dump - накатить бэкап




