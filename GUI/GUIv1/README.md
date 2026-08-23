# Počítadlo životů

Jednoduchá desktopová aplikace v PySide6 pro počítání životů ve
stolních/karetních hrách (2, 4 nebo 6 hráčů), s možností nastavit
každému hráči vlastní barvu.

## Instalace

```bash
python -m venv venv
source venv/bin/activate      # na Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Spuštění

```bash
python app.py
```

## Struktura projektu

| Soubor        | Účel                                                        |
|---------------|--------------------------------------------------------------|
| `app.py`      | Vstupní bod - spouští aplikaci                                |
| `main.py`     | Hlavní okno, menu, přepínání mezi obrazovkami                 |
| `tlacitko.py` | Jedno počítadlo životů (widget se +/- a výběrem barvy)         |
| `styles.py`   | Všechny barvy, rozměry a stylesheety na jednom místě           |

## Ovládání

- Na úvodní obrazovce zvol počet hráčů.
- Každé počítadlo se ovládá tlačítky **+** / **-**, nebo přímým
  přepsáním čísla.
- Tlačítko **Barva** otevře nabídku barev pozadí.
- **Zpět do menu** ukončí aktuální hru (s potvrzením).
- V nabídce **Aplikace → Konec** (Ctrl+Q) aplikaci ukončíš.
