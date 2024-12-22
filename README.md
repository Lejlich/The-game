# Pogodi broj

"Pogodi broj" je jednostavna Python igra u kojoj igrač pokušava da pogodi broj koji računar nasumično odabere. Računar odabere broj između 1 i 100, 
a igrač mora da pogodi koji je to broj. 
Računar daje povratne informacije o tome da li je igračev broj manji ili veći od tajnog broja.

## Kako igrati?

1. Pokreni igru.
2. Računar nasumično odabere broj između 1 i 100.
3. Igrač unosi svoj broj u pokušaju da pogodi broj koji je računar odabrao.
4. Računar će obavestiti igrača da li je njegov broj manji ili veći od tajnog broja.
5. Igrač mora da ponovi unos dok ne pogodi broj.
6. Kada igrač pogodi broj, igra se završava, a računar prikazuje koliko pokušaja je bilo potrebno.

## Pravila igre:

- Igrač unosi broj između 1 i 100.
- Računar na osnovu unosa daje povratne informacije:
  - Ako je broj manji od tajnog broja, računar će reći "Previše mali broj! Pokušaj ponovo."
  - Ako je broj veći od tajnog broja, računar će reći "Previše veliki broj! Pokušaj ponovo."
  - Kada igrač pogodi broj, računar mu čestita i kaže koliko pokušaja je bilo potrebno.
- Igra se završava kada igrač pogodi broj.

## Tehnologija

- Python 3.x
- `random` biblioteka za generisanje nasumičnog broja.

## Instalacija i Pokretanje

1. **Kloniraj** repository na svoj računar:
   ```bash
   git clone https://github.com/Lejlich/Pogodi-broj.git
