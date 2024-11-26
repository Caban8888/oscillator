import numpy as np
import matplotlib.pyplot as plt


def angular_frequency(f):
    return 2 * np.pi * f

def amplitude(omega, b):
    return (F_0 / m) / np.sqrt(np.power((np.power(omega, 2) - np.power(omega_0, 2)), 2) + np.power(b*omega/m, 2))

def damped_vibration_energy(f, b):
    return k * np.power(amplitude(f, b), 2) / 2

def undamped_vibration_energy(f):
    return k * np.power(amplitude(f, 0), 2) / 2

while True:
    try:
        F_0 = float(input("Wprowadź wartość modułu siły wymuszającej (J): "))
        
        if F_0 <= 0:
            print("Wartość modułu siły nie może być mniejsza od 0")
            continue
    except ValueError:
        print("Wprowadzono błędy ciąg znaków. Wprowadź liczbę.")
    else:
        break

while True:
    try:
        m = float(input("Wprowadź wartość masy (kg): "))

        if m <= 0:
            print("Masa nie może być mniejsza lub równa 0")
            continue
    except ValueError:
        print("Wprowadzono błędy ciąg znaków. Wprowadź liczbę.")
    else:
        break

while True:
    try:
        b = float(input("Wprowadź wartość współczynnika tłumienia (kg/s): "))

        if b < 0:
            print("Współczynnika tłumienia nie może być mniejszy od 0")
            continue
    except ValueError:
        print("Wprowadzono błędy ciąg znaków. Wprowadź liczbę.")
    else:
        break

while True:
    try:
        k = float(input("Wprowadź wartość współczynnika sprężystości (k): "))

        if k < 0:
            print("Współczynnik sprężystości nie może być mniejszy od 0")
            continue
    except ValueError:
        print("Wprowadzono błędy ciąg znaków. Wprowadź liczbę.")
    else:
        break

while True:
    try:
        f = float(input("Wprowadź wartość częstotliwości wymuszającej (Hz): "))
        
        if f < 0:
            print("Częstotliwość wymuszająca nie może być mniejsza od 0")
            continue
    except ValueError:
        print("Wprowadzono błędy ciąg znaków. Wprowadź liczbę.")
    else:
        break

omega_0 = np.sqrt(k / m)
omegas = np.linspace(omega_0*0.5, omega_0*2, 1000)

print(f"Amplituda drgań dla częstotliwości {f} wynosi {amplitude(angular_frequency(f), 0)} m")

plt.figure(1)
plt.plot(omegas, amplitude(omegas, 0))
plt.xlabel("Częstość wymuszająca (Hz)")
plt.ylabel("Amplituda (m)")
plt.title("Wykres amplitudy drgań nietłumionych w funkcji częstości wymuszającej")

plt.figure(2)
plt.plot(omegas, undamped_vibration_energy(omegas), label="Energia całkowita nietłumiona (J)")
plt.plot(omegas, damped_vibration_energy(omegas, b), label="Energia całkowita tłumiona (J)")
plt.xlabel("Częstość wymuszająca (Hz)")
plt.ylabel("Energia całkowita (J)")
plt.title("Wykres całkowitych energii drgań w funkcji częstości wymuszającej")
plt.legend()
plt.show()