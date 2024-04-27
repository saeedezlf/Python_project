from PyQt5.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QMainWindow,
    QWidget,
    QTableView,
    QAbstractItemView,
    QPushButton,
)
from model import ContactsModel


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("my Plants")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.contactsModel = ContactsModel()
        self.setupUI()

    def setupUI(self):
        self.table = QTableView()
        self.table.setModel(self.contactsModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()

        self.addButton = QPushButton("Add...")
        self.deleteButton = QPushButton("Delete..")
        self.clearAllButton = QPushButton("Clear All..")

        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)

        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)
