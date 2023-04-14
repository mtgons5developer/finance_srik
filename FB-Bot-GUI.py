import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # create 5 tables
        table1 = QTableWidget()
        table2 = QTableWidget()
        table3 = QTableWidget()
        table4 = QTableWidget()
        table5 = QTableWidget()
        
        # set table dimensions and headers
        table1.setColumnCount(2)
        table1.setRowCount(5)
        table1.setHorizontalHeaderLabels(['Header1', 'Header2'])
        
        table2.setColumnCount(3)
        table2.setRowCount(4)
        table2.setHorizontalHeaderLabels(['Header1', 'Header2', 'Header3'])
        
        table3.setColumnCount(4)
        table3.setRowCount(3)
        table3.setHorizontalHeaderLabels(['Header1', 'Header2', 'Header3', 'Header4'])
        
        table4.setColumnCount(5)
        table4.setRowCount(2)
        table4.setHorizontalHeaderLabels(['Header1', 'Header2', 'Header3', 'Header4', 'Header5'])
        
        table5.setColumnCount(2)
        table5.setRowCount(6)
        table5.setHorizontalHeaderLabels(['Header1', 'Header2'])
        
        # populate tables with data
        for i in range(5):
            for j in range(2):
                table1.setItem(i, j, QTableWidgetItem('Data{}{}'.format(i+1,j+1)))
        
        for i in range(4):
            for j in range(3):
                table2.setItem(i, j, QTableWidgetItem('Data{}{}'.format(i+1,j+1)))
                
        for i in range(3):
            for j in range(4):
                table3.setItem(i, j, QTableWidgetItem('Data{}{}'.format(i+1,j+1)))
                
        for i in range(2):
            for j in range(5):
                table4.setItem(i, j, QTableWidgetItem('Data{}{}'.format(i+1,j+1)))
                
        for i in range(6):
            for j in range(2):
                table5.setItem(i, j, QTableWidgetItem('Data{}{}'.format(i+1,j+1)))
        
        # create a layout and add tables to it
        layout = QVBoxLayout()
        layout.addWidget(table1)
        layout.addWidget(table2)
        layout.addWidget(table3)
        layout.addWidget(table4)
        layout.addWidget(table5)
        
        self.setLayout(layout)
        self.setWindowTitle('Tables')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
