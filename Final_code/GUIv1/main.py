"""Hlavní okno aplikace Počítadlo životů."""

from __future__ import annotations

from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from styles import (
    GRID_COLUMNS,
    MENU_BUTTON_STYLE,
    PLAYER_COLORS,
    WINDOW_MIN_SIZE,
    WINDOW_SIZE,
    WINDOW_TITLE,
)
from tlacitko import Tlacitko

PLAYER_COUNTS = (2, 4, 6)


class MainWindow(QMainWindow):
    """Přepíná mezi výběrem počtu hráčů a herní obrazovkou."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(WINDOW_TITLE)
        self.resize(*WINDOW_SIZE)
        self.setMinimumSize(*WINDOW_MIN_SIZE)

        self._screens = QStackedWidget()
        self.setCentralWidget(self._screens)

        self._game_widget: Optional[QWidget] = None

        self._build_menu_screen()

    def _build_menu_screen(self) -> None:
        """Vytvoří úvodní obrazovku s výběrem počtu hráčů."""
        menu_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("Kolik hráčů bude hrát?")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        for player_count in PLAYER_COUNTS:
            button = QPushButton(f"{player_count} Hráči")
            button.setStyleSheet(MENU_BUTTON_STYLE)
            button.clicked.connect(
                lambda checked=False, count=player_count: self._start_game(count)
            )
            layout.addWidget(button)

        menu_widget.setLayout(layout)
        self._screens.addWidget(menu_widget)

    def _start_game(self, player_count: int) -> None:
        """Vytvoří a zobrazí herní obrazovku pro daný počet hráčů."""
        if player_count > len(PLAYER_COLORS):
            raise ValueError(
                f"Nemám dost barev pro {player_count} hráčů "
                f"(k dispozici je jen {len(PLAYER_COLORS)})."
            )

        game_widget = QWidget()
        main_layout = QVBoxLayout()

        grid = QGridLayout()
        grid.setSpacing(10)

        for index in range(player_count):
            counter = Tlacitko(color=PLAYER_COLORS[index], player_count=player_count)
            row, column = divmod(index, GRID_COLUMNS)
            grid.addWidget(counter, row, column)

        main_layout.addLayout(grid)

        back_button = QPushButton("Zpět do menu")
        back_button.clicked.connect(self._return_to_menu)
        main_layout.addWidget(back_button)

        game_widget.setLayout(main_layout)

        self._game_widget = game_widget
        self._screens.addWidget(game_widget)
        self._screens.setCurrentWidget(game_widget)

    def _return_to_menu(self) -> None:
        """Zeptá se na potvrzení a poté zahodí aktuální hru a vrátí se do menu."""
        answer = QMessageBox.question(
            self,
            "Opustit hru?",
            "Opravdu se chceš vrátit do menu? Aktuální stav hry se ztratí.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if answer != QMessageBox.StandardButton.Yes:
            return

        self._screens.setCurrentIndex(0)
        if self._game_widget is not None:
            self._screens.removeWidget(self._game_widget)
            self._game_widget.deleteLater()
            self._game_widget = None