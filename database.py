from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QMessageBox


def _createPlantsTable():
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(50) NOT NULL,
            job VARCHAR(50),
            phone VARCHAR(15)
        )
        """
    )


def createConnection(databaseName):
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None, "plant db", f"Databese Error: {connection.lastError().text()}"
        )
        return False
    _createPlantsTable()
    return True
