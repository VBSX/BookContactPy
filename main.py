from database_handle import *
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal, QObject

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Booking')
        self.resize(400, 200)
        self.window_add_contact = AddNewContactsWindow()
        self.window_see_contacts = ContactsWidget()
        
        self.btn_contacts_show = QtWidgets.QPushButton('Ver os Contatos Salvos', clicked=self.open_contacts_window)
        self.btn_add_contact_window = QtWidgets.QPushButton('Adicionar um novo contato', clicked=self.open_window_add_contact)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.btn_contacts_show)
        self.layout.addWidget(self.btn_add_contact_window)
        
        
    def open_contacts_window(self):
        self.close()
        self.window_see_contacts.show()
        
    def open_window_add_contact(self):
        
        self.close()
        self.window_add_contact.show()


class ContactsWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.database = ConsultaBanco()
        
        self.table_widget = QtWidgets.QTableWidget()
        self.table_widget.setColumnWidth(2, 250)
        self.table_widget.setColumnWidth(0,250)
        self.table_widget.setHorizontalHeaderLabels(['nome', 'numero', 'email'])
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.table_widget)
        
    def construct_table(self):
        sql_data = self.database.get_all_contacts()
        for row in sql_data:
            print(row)

class AddNewContactsWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 200)
        self.window_contact = ContactsWidget()
        self.name = QtWidgets.QLineEdit(alignment=QtCore.Qt.AlignCenter)
        self.name.setPlaceholderText("Coloque o nome")
        
        self.email = QtWidgets.QLineEdit(alignment=QtCore.Qt.AlignCenter)
        self.email.setPlaceholderText("Coloque o email")
        
        self.phone_number = QtWidgets.QLineEdit(alignment=QtCore.Qt.AlignCenter)
        self.phone_number.setPlaceholderText("Coloque o numero do telefone")
        
        self.btn_call_database_add = QtWidgets.QPushButton('Adicionar contato', clicked=self.send_database)
        
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.name)
        self.layout.addWidget(self.phone_number)
        self.layout.addWidget(self.email)
        self.layout.addWidget(self.btn_call_database_add)
        
    def send_database(self):
        name = self.name.text()
        email = self.email.text()
        phone_number = self.phone_number.text()
        db = EnvioBanco(name, email, phone_number)
        db_send = db.send_dados_para_tabela_contatos()
        
        if self.verify_fields() == True:
            
            if db_send == True:
                self.show_dialog('Contato salvo!')
                self.show_contact_window()
                
            else:
                self.show_dialog(db_send)
                
                
        else:
            self.show_dialog('Prencha todos os campos!')
    
    
    def verify_fields(self):
        name = self.name.text()
        email = self.email.text()
        phone_number = self.phone_number.text()
        
        if name and email and phone_number:
            return True
        
        
    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)
        
    def show_contact_window(self):
        self.close()
        self.window_contact.show()
        
class BookContact:
    def __init__(self):
        pass
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())