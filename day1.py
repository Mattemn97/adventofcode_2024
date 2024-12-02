def calculate_total_distance(left_list, right_list):
    """
    Calcola la distanza totale tra le liste ordinate.
    """
    # Ordina entrambe le liste
    left_list.sort()
    right_list.sort()

    # Calcola la somma delle differenze assolute
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return total_distance


def read_lists_from_file(file_path):
    """
    Legge due liste da un file. Ogni riga deve contenere due numeri separati da uno spazio.
    """
    left_list = []
    right_list = []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list


def main():
    # Chiede all'utente il percorso del file
    file_path = input("Inserisci il percorso del file contenente le liste: ").strip()

    try:
        # Legge le liste dal file
        left_list, right_list = read_lists_from_file(file_path)

        # Calcola la distanza totale
        total_distance = calculate_total_distance(left_list, right_list)

        # Mostra il risultato
        print(f"La distanza totale tra le liste è: {total_distance}")

    except FileNotFoundError:
        print(f"Errore: il file '{file_path}' non è stato trovato.")
    except ValueError:
        print("Errore: il file deve contenere due numeri interi per riga, separati da uno spazio.")


if __name__ == "__main__":
    main()
