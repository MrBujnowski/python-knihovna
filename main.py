import csv
import json

class KnihovniSystem:
    def __init__(self, nazev_souboru):
        self.soubor = nazev_souboru
        self.knihy = self.nacti_knihy()

    def nacti_knihy(self):
        try:
            with open(self.soubor, 'r', encoding="UTF-8") as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            print("Soubor nebyl nalezen.")
        except FileExistsError:
            print("Soubor neexistuje.")
        except:
            print("Něco se nepovedlo.")
        finally:
            return []
    def uloz_knihy(self, json_soubor):
        try:
            with open(json_soubor, 'x', encoding="UTF-8") as x:
                x.write(json.dumps(self.knihy, indent=4))
        except:
            print("Chyba.")

system = KnihovniSystem("knihy.csv")
print(system.knihy[0]["nazev_knihy"])