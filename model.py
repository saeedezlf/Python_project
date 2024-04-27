from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt


class ContactsModel:
    def __init__(self) -> None:
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        tableModel = QSqlTableModel()
        tableModel.setTable("contacts")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID", "Name", "Job", "Phone")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel
