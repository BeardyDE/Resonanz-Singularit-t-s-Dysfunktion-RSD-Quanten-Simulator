import numpy as np
import cmath
import random

# Globale Parameter mit Standardwerten
ALPHA = 1.732
OMEGA = 4.669
LAMBDA = 1e-9
PHI = 6.626e-34

def random_quantum_fluctuation():
    fluctuation = random.uniform(-1e-5, 1e-5)
    return fluctuation * np.tanh(random.random() * OMEGA)

def mitochondrial_resonance(matrix_energy):
    try:
        fluctuation = random_quantum_fluctuation()
        resonance = np.sin(matrix_energy / LAMBDA) * np.log(abs(matrix_energy + fluctuation))
        instability = np.tanh(resonance + PHI)
        return instability
    except ValueError:
        return np.nan

def neural_quantum_fluctuation(time, space):
    try:
        phase_shift = cmath.exp(1j * (time + space)) * OMEGA
        quantum_field = np.abs(phase_shift) * random.gauss(0, 1)
        return quantum_field
    except OverflowError:
        return 0.0

def recursive_singularity_detection(n, matrix_energy):
    if n <= 0:
        return random_quantum_fluctuation()
    
    instability = mitochondrial_resonance(matrix_energy)
    return recursive_singularity_detection(n-1, instability) + np.tanh(instability)

def rsd_simulation(time_series, space_series, alpha_mod, omega_mod):
    results = np.zeros((len(time_series), len(space_series)))
    global ALPHA, OMEGA

    ALPHA *= alpha_mod
    OMEGA *= omega_mod

    for t_index, t in enumerate(time_series):
        for s_index, s in enumerate(space_series):
            matrix_energy = random.uniform(0.1, 100)
            resonance = recursive_singularity_detection(50, matrix_energy)
            fluctuation = neural_quantum_fluctuation(t, s)
            results[t_index, s_index] = (resonance * fluctuation) / (abs(t - s + random_quantum_fluctuation()) + PHI)

    return results

def display_menu():
    print("\n*** Resonanz-Singularitäts-Dysfunktion (RSD) Quanten-Simulator ***")
    print("1. Starte Simulation")
    print("2. Ändere Parameter")
    print("3. Beenden")
    choice = input("Wähle eine Option (1/2/3): ")
    return choice

def main():
    time_series = np.linspace(0, 100, 500)
    space_series = np.linspace(-50, 50, 500)

    while True:
        choice = display_menu()

        if choice == '1':
            print("\nStarte Simulation...")
            try:
                alpha_mod = float(input("Geben Sie einen Modifikator für ALPHA ein (z.B. 1.5): "))
                omega_mod = float(input("Geben Sie einen Modifikator für OMEGA ein (z.B. 0.5): "))
                simulation_results = rsd_simulation(time_series, space_series, alpha_mod, omega_mod)
                print("Simulation der Resonanz-Singularitäts-Dysfunktion abgeschlossen.")
                print(f"Maximale Quanteninstabilität: {np.max(simulation_results):.5e}")
                print(f"Durchschnittliche Fluktuation: {np.mean(simulation_results):.5e}")
                print("Unbekannte Resonanz erreicht: ", np.any(np.isnan(simulation_results)))
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie numerische Werte ein.")
        elif choice == '2':
            print("\nÄndere Parameter:")
            global ALPHA, OMEGA, LAMBDA, PHI
            try:
                ALPHA = float(input("Neuer Wert für ALPHA: "))
                OMEGA = float(input("Neuer Wert für OMEGA: "))
                LAMBDA = float(input("Neuer Wert für LAMBDA: "))
                PHI = float(input("Neuer Wert für PHI: "))
                print("Parameter erfolgreich aktualisiert.")
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie numerische Werte ein.")
        elif choice == '3':
            print("Beende das Programm...")
            break
        else:
            print("Ungültige Auswahl. Bitte wählen Sie eine der angegebenen Optionen.")

if __name__ == "__main__":
    main()
