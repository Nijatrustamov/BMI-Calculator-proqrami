import tkinter as tk
from tkinter import messagebox

class BMICalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("BMI Hesaplayıcı")

        # Kilo girişi
        self.label_kilo = tk.Label(master, text="Kilonuz (kg):")
        self.label_kilo.pack()

        self.entry_kilo = tk.Entry(master)
        self.entry_kilo.pack()

        # Boy girişi
        self.label_boy = tk.Label(master, text="Boyunuz (metre):")
        self.label_boy.pack()

        self.entry_boy = tk.Entry(master)
        self.entry_boy.pack()

        # Hesapla butonu
        self.hesapla_button = tk.Button(master, text="Hesapla", command=self.calculate_bmi)
        self.hesapla_button.pack()

        # Sonuç etiketi
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate_bmi(self):
        try:
            kilo = float(self.entry_kilo.get())
            boy = float(self.entry_boy.get())

            if kilo <= 0 or boy <= 0:
                raise ValueError("Sıfırdan büyük değer girilmeli")

            bmi = kilo / (boy * boy)
            sonuc = self.bmi_yorum(bmi)

            self.result_label.config(text=f"BMI: {bmi:.2f} - {sonuc}")
        except ValueError:
            messagebox.showerror("Hatalı Giriş", "Lütfen geçerli sayısal değerler girin.")

    def bmi_yorum(self, bmi):
        if bmi < 18.5:
            return "Zayıf"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Kilolu"
        else:
            return "Obez"

# Ana uygulama penceresi
root = tk.Tk()
app = BMICalculatorApp(root)
root.mainloop()
