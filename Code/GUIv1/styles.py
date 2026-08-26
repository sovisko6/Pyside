"Konstanty vzhledu: barvy, rozměry a stylesheety pro celou aplikaci."

# --- Hlavní okno ---------------------------------------------------------

WINDOW_TITLE = "Počítadlo životů"
WINDOW_SIZE = (400, 500)
WINDOW_MIN_SIZE = (300, 350)

# --- Menu (výběr počtu hráčů) --------------------------------------------

MENU_BUTTON_STYLE = "font-size: 38px; padding: 10px; margin: 5px;"
GRID_COLUMNS = 2


PALETTE = (
    ("Červená", "#c0392b"),
    ("Zelená", "#27ae60"),
    ("Modrá", "#2980b9"),
    ("Oranžová", "#e67e22"),
    ("Fialová", "#8e44ad"),
    ("Tyrkysová", "#16a085"),
    ("Šedá", "#7f8c8d"),
)

PLAYER_COLORS = tuple(color for _, color in PALETTE)
COLOR_CHOICES = PALETTE

# --- Počítadlo životů (Tlacitko) ------------------------------------------

BACKGROUND_OBJECT_NAME = "HlavniPozadi"


def tlacitko_stylesheet(background_object_name: str, color: str) -> str:
    """Vrátí QSS stylesheet pro jedno počítadlo s danou barvou pozadí."""
    return f"""
        #{background_object_name} {{
            background-color: {color};
        }}
        QLineEdit {{
            background-color: rgba(255, 255, 255, 220);
            color: black;
            font-size: 70px;
            font-weight: bold;
            border: 2px solid black;
            border-radius: 10px;
        }}
        QPushButton {{
            background-color: rgba(255, 255, 255, 220);
            color: black;
            font-size: 24px;
            font-weight: bold;
            border: 2px solid black;
            border-radius: 5px;
        }}
    """