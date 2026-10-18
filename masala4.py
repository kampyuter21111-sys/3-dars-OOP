class Taqvim:
    def kabisami(self, yil):
        """Grigoriyan yil kabisa yili ekanini tekshiradi."""
        return (yil % 4 == 0 and yil % 100 != 0) or yil % 400 == 0

    def hijriyga(self, milodiy_yil):
        """Grigoriyan (milodiy) yilni hijriy yilga o'tkazadi."""
        return round((milodiy_yil - 622) * 33 / 32)

    def grigoriyanga(self, hijriy_yil):
        """Hijriy yilni grigoriyan (milodiy) yilga o'tkazadi."""
        return round(hijriy_yil * 32 / 33 + 622)


if __name__ == "__main__":
    t = Taqvim()
    print("2026 milodiy ->", t.hijriyga(2026), "hijriy")
    print("1448 hijriy ->", t.grigoriyanga(1448), "milodiy")
    for y in (2000, 1900, 2024, 2026):
        print(y, "kabisa yili" if t.kabisami(y) else "kabisa yili emas")
