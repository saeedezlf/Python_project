from PyQt5.QtWidgets import QApplication
from views import Window
from database import createConnection
import sys


def main():
    app = QApplication(sys.argv)
    if not createConnection("contact.sqlite"):
        sys.exit(1)
    win = Window()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
