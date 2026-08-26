"""Vstupní bod aplikace Počítadlo životů."""

import sys

from PySide6.QtWidgets import QApplication, QMessageBox

from main import MainWindow


def main() -> None:
    app = QApplication(sys.argv)

    try:
        window = MainWindow()
    except Exception as error: 
        QMessageBox.critical(
            None,
            "Chyba při spuštění",
            f"Aplikaci se nepodařilo spustit:\n{error}",
        )
        sys.exit(1)

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
