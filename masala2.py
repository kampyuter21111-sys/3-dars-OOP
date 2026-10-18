import sys
sys.stdout.reconfigure(encoding="utf-8")


class Convertor:
    
    EN_RU = {
        "yo": "ё", "yu": "ю", "ya": "я", "ye": "е",
        "sh": "ш", "ch": "ч", "zh": "ж", "ts": "ц", "kh": "х",
        "a": "а", "b": "б", "d": "д", "e": "е", "f": "ф", "g": "г",
        "h": "х", "i": "и", "j": "ж", "k": "к", "l": "л", "m": "м",
        "n": "н", "o": "о", "p": "п", "q": "к", "r": "р", "s": "с",
        "t": "т", "u": "у", "v": "в", "w": "в", "x": "х", "y": "й", "z": "з",
    }

 
    RU_EN = {
        "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e",
        "ё": "yo", "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k",
        "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
        "с": "s", "т": "t", "у": "u", "ф": "f", "х": "kh", "ц": "ts",
        "ч": "ch", "ш": "sh", "щ": "shch", "ъ": "", "ы": "i", "ь": "",
        "э": "e", "ю": "yu", "я": "ya",
    }

    @staticmethod
    def _katta_harf(s):
        return s != s.lower()

    def en_to_ru(self, matn):
        natija = ""
        i = 0
        while i < len(matn):
            
            ikki = matn[i:i + 2].lower()
            bir = matn[i].lower()
            if len(ikki) == 2 and ikki in self.EN_RU:
                harf = self.EN_RU[ikki]
                katta = matn[i].isupper()
                i += 2
            elif bir in self.EN_RU:
                harf = self.EN_RU[bir]
                katta = matn[i].isupper()
                i += 1
            else:
                natija += matn[i]  #
                i += 1
                continue
            natija += harf.upper() if katta else harf
        return natija

    def ru_to_en(self, matn):
        natija = ""
        for belgi in matn:
            kichik = belgi.lower()
            if kichik in self.RU_EN:
                harf = self.RU_EN[kichik]
                if belgi.isupper():
                    harf = harf.capitalize()
                natija += harf
            else:
                natija += belgi
        return natija


if __name__ == "__main__":
    c = Convertor()
    print(c.en_to_ru("Salom dunyo"))         
    print(c.en_to_ru("Yoqut yulduz yashil"))  
    print(c.ru_to_en("Привет мир"))         
    print(c.ru_to_en("Ёлка, юла, яблоко"))   
