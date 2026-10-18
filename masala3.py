import sys
sys.stdout.reconfigure(encoding="utf-8")


class String:
    def __init__(self, matn):
        self.matn = matn

    @staticmethod
    def _kichikmi(h):
        k = ord(h)
        return 97 <= k <= 122 or 1072 <= k <= 1103 or k == 1105

    @staticmethod
    def _kattami(h):
        k = ord(h)
        return 65 <= k <= 90 or 1040 <= k <= 1071 or k == 1025

    def to_lower(self):
        natija = ""
        for h in self.matn:
            k = ord(h)
            if 65 <= k <= 90 or 1040 <= k <= 1071:
                natija += chr(k + 32)
            elif k == 1025:          # Ё -> ё
                natija += chr(1105)
            else:
                natija += h
        return natija

    def to_upper(self):
        natija = ""
        for h in self.matn:
            k = ord(h)
            if 97 <= k <= 122 or 1072 <= k <= 1103:
                natija += chr(k - 32)
            elif k == 1105:          # ё -> Ё
                natija += chr(1025)
            else:
                natija += h
        return natija

    def is_lower(self):
        harf_bor = False
        for h in self.matn:
            if self._kattami(h):
                return False
            if self._kichikmi(h):
                harf_bor = True
        return harf_bor

    def is_upper(self):
        harf_bor = False
        for h in self.matn:
            if self._kichikmi(h):
                return False
            if self._kattami(h):
                harf_bor = True
        return harf_bor


if __name__ == "__main__":
    s = String("Salom Dunyo 123")
    print(s.to_lower())   
    print(s.to_upper())  
    print(s.is_lower())  
    print(s.is_upper())   
    print(String("hello").is_lower())   
    print(String("HELLO 1").is_upper()) 
    print(String("Привет").to_upper())  
    print(String("123").is_lower())     
