import sqlite3
from system_handle import *

class EnvioBanco:
    def __init__(self, nome_do_contato, numero_do_telefone, email):
        self.nome_do_contato = nome_do_contato
        self.numero_do_telefone = numero_do_telefone
        self.email = email
        self.sys_date = HorarioDoSistema()
        self.data_agora = self.sys_date.get_data_sistema()
        self.hora_agora = self.sys_date.get_horario_sistema()
        self.banco = sqlite3.connect('contatos.db')
        self.cursor = self.banco.cursor()

    def fechar_banco(self):
        self.banco.close()

    def send_dados_para_tabela_contatos(self):
        try:
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS cadastro_contatos (nome text, numero numeric, email text, "
                "data_consulta numeric, hora_consulta numeric) ")
            self.cursor.execute(
                "INSERT INTO cadastro_contatos (nome, numero, email, data_consulta, hora_consulta) "
                "VALUES ('" + self.nome_do_contato + "','" + self.numero_do_telefone + "', '" + self.email + "', '" +
                self.data_agora + "', '" + self.hora_agora + "')")
            self.banco.commit()
            self.fechar_banco()
            
            return  True

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ", erro)
            
            return erro.text()



class ConsultaBanco:
    def __init__(self):
        self.erro_log = Criarlog()
        self.banco = sqlite3.connect('contatos.db')
        
        
    def fechar_banco(self):
        self.banco.close()

    def get_contact_by_name(self,name):
        cursor_get_price = self.banco.cursor()
        cursor_get_price.execute(
            f"SELECT nome,numero,emal FROM cadastro_contatos WHERE name LIKE '%{name}%' "
            # f"AND data_consulta BETWEEN '{initial_consult_date}' AND '{final_consult_date}'"
            )
        data_database = cursor_get_price.fetchall()

        return data_database

    def get_all_contacts(self):
        try:
            self.cursor_get_all_contacts = self.banco.cursor()
            self.cursor_get_all_contacts.execute(
                f"SELECT nome, numero, email FROM cadastro_contatos")
            self.retornar_contatos = self.cursor_get_all_contacts.fetchall()

            return self.retornar_contatos

        except sqlite3.Error as erro:
            self.erro_log.criar_txt_log(
                f"Erro ao retornar dados do nome, "
                f"codigo do erro {erro}")
            print(
                f"\nErro ao retornar dados do nome, "
                f"codigo do erro ",erro)
            self.fechar_banco()
            
            return erro
        
if __name__ == "__main__":
    b = ConsultaBanco()
    print(b.get_all_contacts())