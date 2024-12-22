import random

def pogodi_broj():
    print("Dobrodošao u igricu 'Pogodi broj'!")
    print("Računar će izabrati broj između 1 i 100, a tvoj zadatak je da ga pogodiš.")

    tajni_broj = random.randint(1, 100)
    pokusaji = 0

    while True:
        try:
            unos = int(input("Unesi svoj broj: "))
            pokusaji += 1

            if unos < tajni_broj:
                print("Previše mali broj! Pokušaj ponovo.")
            elif unos > tajni_broj:
                print("Previše veliki broj! Pokušaj ponovo.")
            else:
                print(f"Čestitamo! Pogodio si broj {tajni_broj} nakon {pokusaji} pokušaja.")
                break
        except ValueError:
            print("Molimo te da uneseš validan broj!")

if __name__ == "__main__":
    pogodi_broj()
