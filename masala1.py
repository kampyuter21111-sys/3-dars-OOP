class Talaba:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age} yosh)"


class Kurs:
    def __init__(self, kurs_name, kurs_teacher):
        self.kurs_name = kurs_name
        self.kurs_teacher = kurs_teacher
        self.talabalar_soni = 0
        self.talabalar = []

    def add(self, new_student):
        self.talabalar.append(new_student)
        self.talabalar_soni += 1

    def delete(self, new_student):
        if new_student in self.talabalar:
            self.talabalar.remove(new_student)
            self.talabalar_soni -= 1
        else:
            print(f"{new_student.name} bu kursda yo'q!")

    def info_kurs(self):
        print(f"Kurs: {self.kurs_name} | O'qituvchi: {self.kurs_teacher} | Talabalar soni: {self.talabalar_soni}")
        for i, t in enumerate(self.talabalar, 1):
            print(f"  {i}. {t}")
        print()


if __name__ == "__main__":
    # 2 ta kurs
    python_kursi = Kurs("Python", "Aliyev Vali")
    java_kursi = Kurs("Java", "Karimov Salim")

  
    python_talabalar = [Talaba(f"PyTalaba{i}", 18 + i) for i in range(1, 11)]
    java_talabalar = [Talaba(f"JavaTalaba{i}", 18 + i) for i in range(1, 11)]

    for t in python_talabalar:
        python_kursi.add(t)
    for t in java_talabalar:
        java_kursi.add(t)

    print("=== Qo'shilgandan keyin ===")
    python_kursi.info_kurs()
    java_kursi.info_kurs()

    python_kursi.delete(python_talabalar[0])
    java_kursi.delete(java_talabalar[0])

    print("=== Haydalgandan keyin ===")
    python_kursi.info_kurs()
    java_kursi.info_kurs()
