from database_handle import *
import sys
from PySide6 import QtCore, QtWidgets

        
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Booking')
        self.resize(400, 200)
        self.setStyleSheet("padding :15px")
        
        
        self.btn_contacts_show = QtWidgets.QPushButton('Ver os Contatos Salvos', clicked=self.open_contacts_window)
        self.btn_add_contact_window = QtWidgets.QPushButton('Adicionar um novo contato', clicked=self.open_window_add_contact)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.btn_contacts_show)
        self.layout.addWidget(self.btn_add_contact_window)
        
        
    def open_contacts_window(self):
        self.window_see_contacts = ContactsWidget()
        self.close()
        self.window_see_contacts.show()
        
    def open_window_add_contact(self):
        self.window_add_contact = AddNewContactsWindow()
        self.close()
        self.window_add_contact.show()


class ContactsWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("padding :15px")
        self.resize(850, 350)
        self.database = ConsultaBanco()
        self.setWindowTitle('Contatos')
        self.window_add_contact = AddNewContactsWindow()
        self.table_widget = QtWidgets.QTableWidget(5,5)
        self.table_widget.setColumnCount(3)
        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()
        self.table_widget.setColumnWidth(0,150)
        self.table_widget.setColumnWidth(1,150)
        self.table_widget.setColumnWidth(2, 250)
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.setHorizontalHeaderLabels(['nome', 'numero', 'email'])
        
        self.button_add_contact = QtWidgets.QPushButton('Adicionar um novo contato',clicked = self.open_window_add_contact)
        
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.table_widget)
        self.layout.addWidget(self.button_add_contact)
        
        self.construct_table()
    def construct_table(self):
        sql_data = self.database.get_all_contacts()
        self.table_widget.setRowCount(50)
        tablerow = 0
        
        for row in sql_data:
            self.table_widget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.table_widget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.table_widget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow+=1
            
    def open_window_add_contact(self):
        
        self.close()
        self.window_add_contact.show()
            

class AddNewContactsWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("padding :15px")
        self.resize(400, 200)
        
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
        name = str(self.name.text())
        email = str(self.email.text())
        phone_number = str(self.phone_number.text())
        db = EnvioBanco(name,phone_number, email )
        db_send = db.send_dados_para_tabela_contatos()
        print(name, email, phone_number)
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
        self.window_contact = ContactsWidget()
        self.close()
        self.window_contact.show()
        
class WindowHandle(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        pass
    def close_main_window(self):
       pass 
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())