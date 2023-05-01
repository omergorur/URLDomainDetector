from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6 import uic
from tld import get_fld
import sys
from mytablewidget import MyTableWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the .ui file
        uic.loadUi("gui.ui", self)
        self.setWindowTitle("URL Domain Detector")
        # Connect the button to the function
        self.button.clicked.connect(self.submit)
        self.button_2.clicked.connect(self.temizle)


    def temizle(self):
        self.text_area.setPlainText("")



    def submit(self):
        self.table.sortItems(-1)
        # Clear the table
        self.table.setRowCount(0)
        # Get the urls from the text area
        urls = self.text_area.toPlainText().split("\n")
        # Loop through the urls
        for url in urls:
            # Get the domain using tld module
            try:
                domain = get_fld(url)
            except:
                # Skip the invalid url
                continue
            # Add a new row to the table
            row = self.table.rowCount()
            self.table.insertRow(row)
            # Set the domain and url in the table cells
            self.table.setItem(row, 0, QTableWidgetItem(domain))
            self.table.setItem(row, 1, QTableWidgetItem(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()