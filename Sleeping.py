from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class Sleeping(TemplateRoom):
    def __init__(self, parent=None):
        super(Sleeping, self).__init__(parent)

        self.init_room("Sleeping.jpg")

        self.offset_balloon_x = 450
        self.offset_balloon_y = 10
        self.offset_balloon_length = 550
        self.offset_balloon_width = 50
        self.set_offset_mouth(500, 60, 10, 10)

        self.hitbox_alarm_clock = QRect(925, 600, 75, 100)
        self.append_hitbox(self.hitbox_alarm_clock)

        self.text_line_1 = "Höre ich da etwa den Wecker?"
        self.text_line_2 = ""
        self.text_line_3 = ""
        self.text_line_4 = ""
        self.text_line_5 = ""
        self.text_line_6 = ""

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(Sleeping, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_alarm_clock.contains(mouse_pos):
            self.text_line_1 = "Tatsächlich, es klingelt..."
            self.text_line_2 = ""
            self.text_line_3 = ""
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            # Requirement 2.7

            self.update()
