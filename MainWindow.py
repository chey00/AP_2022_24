from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import pyqtSlot

from House import House
from Living import Living
from Sleeping import Sleeping


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Abschlussprüfung PG 2022/24")

        super().__init__(parent)
        self.__set_of_rooms = set()

        self.current_room = House(parent)
        self.setup_new_room()

    def setup_new_room(self):
        self.current_room.setHitBoxVisible(True)
        self.current_room.leave_room.connect(self.change_room)
        self.current_room.new_room.connect(self.renew_room)

        self.setCentralWidget(self.current_room)

    @pyqtSlot(str)
    def renew_room(self, new_room):
        if new_room == "Living.jpg":
            self.current_room = Living()
            self.setup_new_room()
        elif new_room == "Sleeping.jpg":
            self.current_room = Sleeping()
            self.setup_new_room()
        elif new_room == "House.jpg":
            self.current_room = House()
            self.setup_new_room()

    @pyqtSlot(str)
    def change_room(self, old_room):
        if old_room == "Sleeping.jpg":
            self.current_room = House()
            self.setup_new_room()
        elif old_room == "Living.jpg":
            self.current_room = House()
            self.setup_new_room()
