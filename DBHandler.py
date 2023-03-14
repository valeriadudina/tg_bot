import psycopg2
import json
import data_validator

class DBHandler():
    def __init__(self, name):
        self.name = name
        self.fields = self.get_fields()
    def fill_fields(self):
        ret = ""
        conn_pd = psycopg2.connect(dbname='dbname', user='user',
                               password='password',
                               host='host',
                               port=25060)
        cursor = conn_pd.cursor()
        if data_validator.validate_inn(self.fields[2]) == 'valid data':
            if data_validator.validate_snils(self.fields[3]) == 'valid data':
                if data_validator.validate_date(self.fields[4]) ==  'valid data':
                    ret = "Данные добавлены в 1С"
                    select_user = "UPDATE dbname SET name= %s, config_id= %s, pipedrive_id= %s, is_top= %s WHERE id = %s;"
                    cursor.execute(select_user,(self.fields[1],self.fields[2], self.fields[3],self.fields[4],self.fields[5], self.fields[6], self.fields[7], self.fields[8], self.fields[9], self.fields[10], self.fields[11]), )


                else:
                    ret = "Неверная дата начала работы, введите еще раз"
                    fields_list = list(self.fields)
                    fields_list[4] = ""
                    self.fields = tuple(fields_list)

            else:
                ret = "Неверный СНИЛС, введите еще раз"
                fields_list = list(self.fields)
                fields_list[3] = ''
                self.fields = tuple(fields_list)

        else:
            ret = 'Неверный ИНН, введите еще раз'
            fields_list = list(self.fields)
            fields_list[2] = ""
            self.fields = tuple(fields_list)

        return ret

    def get_fields(self):
        conn_pd = psycopg2.connect(dbname='dbname', user='user',
                               password='password',
                               host='host',
                               port=25060)
        cursor = conn_pd.cursor()

        select_user = "select * from dbname where name = %s"
        cursor.execute(select_user,(self.name,) )
        record = cursor.fetchall()

        return record



def to_fill_data():
    conn_pd = psycopg2.connect(dbname='dbname', user='user',
                               password='password',
                               host='host',
                               port=25060)
    cursor = conn_pd.cursor()
    #TODO dopisat'
    select_user = "select * from dbname where inn='' or snils ='' limit 5"
    cursor.execute(select_user, )
    records = cursor.fetchall()
    return records

def find_extra(extra_person):
    conn_pd = psycopg2.connect(dbname='dbname', user='user',
                               password='password',
                               host='host',
                               port=25060)
    cursor = conn_pd.cursor()

    select_user = f"select * from dbname where name ={extra_person} "
    cursor.execute(select_user, )
    record = cursor.fetchall()
    return record



