from PyQt6.QtCore import QRect, QDateTime
from PyQt6.QtGui import QMouseEvent, QPixmap, QPaintEvent, QPainter

from TemplateRoom import TemplateRoom


class Living(TemplateRoom):
    def __init__(self, parent=None):
        super(Living, self).__init__(parent)

        self.init_room("Living.jpg")

        self.offset_balloon_x = 550
        self.offset_balloon_y = 10
        self.offset_balloon_length = 450
        self.offset_balloon_width = 100
        self.set_offset_mouth(560, 110, 10, 10)

        self.hitbox_tv = QRect(100, 90, 350, 375)
        self.append_hitbox(self.hitbox_tv)

        self.hitbox_clock = QRect(475, 300, 125, 400)
        self.append_hitbox(self.hitbox_clock)

        self.text_line_1 = "Du bist im Wohnzimmer"
        self.text_line_2 = "angekommen. Schau doch"
        self.text_line_3 = "etwas fernsehen."
        self.text_line_4 = ""
        self.text_line_5 = ""
        self.text_line_6 = ""

        self.__show_qr = False
        self.__pixmap = QPixmap("qr.png")

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Living, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_tv.contains(mouse_pos):
            self.text_line_1 = "Statt Fernsehen, sehe"
            self.text_line_2 = "dir die Projektvideos"
            self.text_line_3 = "unserer Schule an."
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.__show_qr = True

            self.update()

        if self.hitbox_clock.contains(mouse_pos):
            # Requirement 2.5

            self.text_line_1 = ""
            self.text_line_2 = ""
            self.text_line_3 = ""
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.__show_qr = False

            self.update()

    def paintEvent(self, a0: QPaintEvent) -> None:
        super(Living, self).paintEvent(a0)

        # Requirement 2.6
