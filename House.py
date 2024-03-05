from PyQt6.QtCore import QRect
from PyQt6.QtGui import QMouseEvent

from TemplateRoom import TemplateRoom


class House(TemplateRoom):
    def __init__(self, parent=None):
        super(House, self).__init__(parent)

        self.init_room("House.jpg")

        self.offset_balloon_x = 10
        self.offset_balloon_y = 10
        self.offset_balloon_length = 400
        self.offset_balloon_width = 100
        self.set_offset_mouth(310, 110, 10, 10)

        # Requirement 2.1

        # Requirement 2.2
        self.hitbox_gate = None

        self.hitbox_door = None

        self.hitbox_bush = None

        self.hitbox_window = None

        # Requirement 2.3
        self.text_line_1 = ""
        self.text_line_2 = ""
        self.text_line_3 = ""
        self.text_line_4 = ""
        self.text_line_5 = ""
        self.text_line_6 = ""

        # Requirement 2.4

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(House, self).mousePressEvent(ev)

        mouse_pos = ev.pos()

        if self.hitbox_gate.contains(mouse_pos):
            self.text_line_1 = "Treten Sie ein. Die"
            self.text_line_2 = "Haustür ist viel-"
            self.text_line_3 = "leicht offen."
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.update()

        elif self.hitbox_door.contains(mouse_pos):
            # Requirement 2.4
            self.text_line_1 = "Doch verschlossen!"
            self.text_line_2 = "Der Schlüssel liegt"
            self.text_line_3 = "am roten Strauch."
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            self.update()

        elif self.hitbox_bush.contains(mouse_pos):
            self.text_line_1 = "Du findest den"
            self.text_line_2 = "Haustürschlüssel."
            self.text_line_3 = ""
            self.text_line_4 = ""
            self.text_line_5 = ""
            self.text_line_6 = ""

            # Requirement 2.4

            self.update()

        elif self.hitbox_window.contains(mouse_pos):
            self.new_room.emit("Sleeping.jpg")
