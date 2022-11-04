from datetime import datetime

class HorarioDoSistema:
    def __init__(self):
        
        pass

    def get_horario_sistema(self):
        hora_atual = datetime.strftime(datetime.now(), "%H:%M:%S")
        
        return hora_atual

    def get_data_sistema(self):
        hoje = datetime.now()
        data_atual = hoje.strftime("%d/%m/%y")
        
        return data_atual



class Criarlog:
    def __init__(self):
        self.diretorio_de_escrita_local = 'var\log\log.txt'
        self.get_date = HorarioDoSistema()
        self.hora = self.get_date.get_horario_sistema()
        self.data = self.get_date.get_data_sistema()

    def criar_txt_log(self, texto_log):
        self.texto_log = texto_log
        with open(self.diretorio_de_escrita_local, 'a') as f:
            f.write(f'{self.texto_log} do dia {self.data} as {self.hora}\n\n')




