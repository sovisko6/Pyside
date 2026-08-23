"""Widget jednoho počítadla životů s tlačítky +/- a menu pro výběr barvy."""

from __future__ import annotations

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QMenu,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from styles import BACKGROUND_OBJECT_NAME, COLOR_CHOICES, tlacitko_stylesheet

STARTING_LIVES_TWO_PLAYERS = 20
STARTING_LIVES_MANY_PLAYERS = 40

MIN_LIVES = -999
MAX_LIVES = 999


class Tlacitko(QWidget):
    """Editovatelné počítadlo životů s tlačítky +/- a menu pro barvu pozadí."""

    def __init__(self, color: str = "gray", player_count: int = 2) -> None:
        super().__init__()
        self.setObjectName(BACKGROUND_OBJECT_NAME)

        self._lives = (
            STARTING_LIVES_TWO_PLAYERS
            if player_count == 2
            else STARTING_LIVES_MANY_PLAYERS
        )

        self._lives_input = self._build_lives_input()
        self._plus_button, self._minus_button, self._menu_button = self._build_buttons()

        self.setLayout(self._build_layout())
        self._apply_color(color)

    def _build_lives_input(self) -> QLineEdit:
        """Vytvoří textové pole pro zobrazení a editaci počtu životů."""
        field = QLineEdit(str(self._lives))
        field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        field.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        field.setValidator(QIntValidator(MIN_LIVES, MAX_LIVES, self))
        field.textChanged.connect(self._on_text_changed)
        return field

    def _build_buttons(self) -> tuple[QPushButton, QPushButton, QPushButton]:
        """Vytvoří tlačítka +, - a menu pro výběr barvy."""
        plus_button = QPushButton("+")
        minus_button = QPushButton("-")
        menu_button = QPushButton("Barva")

        for button in (plus_button, minus_button, menu_button):
            button.setSizePolicy(
                QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
            )

        plus_button.clicked.connect(self._increment)
        minus_button.clicked.connect(self._decrement)

        color_menu = QMenu(self)
        for label, color in COLOR_CHOICES:
            # *args zachytí cokoliv, co PySide6 signálu triggered pošle
            # (někdy bool, někdy nic) - proto nesmí mít pevný počet argumentů.
            color_menu.addAction(label, lambda *args, c=color: self._apply_color(c))
        menu_button.setMenu(color_menu)

        return plus_button, minus_button, menu_button

    def _build_layout(self) -> QHBoxLayout:
        """Poskládá vstupní pole a tlačítka do finálního layoutu."""
        buttons_layout = QVBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        buttons_layout.setSpacing(5)
        buttons_layout.addWidget(self._plus_button)
        buttons_layout.addWidget(self._minus_button)
        buttons_layout.addWidget(self._menu_button)

        layout = QHBoxLayout()
        layout.addWidget(self._lives_input, 7)
        layout.addLayout(buttons_layout, 3)
        return layout

    def _on_text_changed(self, text: str) -> None:
        """Synchronizuje interní hodnotu s ručně zadaným textem."""
        if text in ("", "-"):
            return
        self._lives = int(text)

    def _increment(self) -> None:
        self._lives += 1
        self._lives_input.setText(str(self._lives))

    def _decrement(self) -> None:
        self._lives -= 1
        self._lives_input.setText(str(self._lives))

    def _apply_color(self, color: str) -> None:
        """Nastaví barvu pozadí widgetu a styl vnitřních prvků."""
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(tlacitko_stylesheet(BACKGROUND_OBJECT_NAME, color))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Tlacitko()
    window.setWindowTitle("Nové Počítadlo")
    window.resize(500, 250)
    window.show()
    sys.exit(app.exec())
