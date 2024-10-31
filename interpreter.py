def load_instructions(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    return lines

def konversi_ke_biner(angka, basis):
    if basis == 10:
        return bin(int(angka))[2:]
    elif basis == 8:
        return bin(int(angka, 8))[2:]
    elif basis == 16:
        return bin(int(angka, 16))[2:]

def konversi_ke_oktal(angka, basis):
    if basis == 10:
        return oct(int(angka))[2:]
    elif basis == 2:
        return oct(int(angka, 2))[2:]
    elif basis == 16:
        return oct(int(angka, 16))[2:]

def konversi_ke_desimal(angka, basis):
    return str(int(angka, basis))

def konversi_ke_heksadesimal(angka, basis):
    if basis == 10:
        return hex(int(angka))[2:].upper()
    elif basis == 2:
        return hex(int(angka, 2))[2:].upper()
    elif basis == 8:
        return hex(int(angka, 8))[2:].upper()

def is_valid_input(angka, basis):
    """Check if the input number is valid based on its base."""
    try:
        if basis == 2:
            int(angka, 2)
        elif basis == 8:
            int(angka, 8)
        elif basis == 10:
            float(angka) 
        elif basis == 16:
            int(angka, 16)
        return True
    except ValueError:
        return False

def baca_perintah(file_path):
    instructions = load_instructions(file_path)
    perintah_konversi_ke = instructions[0]
    perintah_input = instructions[1]
    perintah_basis_angka = instructions[2]
    perintah_hasil_konversi = instructions[3]
    perintah_berhenti = instructions[4]

    konversi_otomatis = None
    input_otomatis = None
    basis_otomatis = None

    for basis in ["BINER", "OKTAL", "DESIMAL", "HEKSADESIMAL"]:
        if basis in perintah_konversi_ke:
            konversi_otomatis = basis
            break

    if len(perintah_input.split()) > 2:
        input_otomatis = perintah_input.split()[-1]

    if len(perintah_basis_angka.split()) > 3:
        basis_otomatis = int(perintah_basis_angka.split()[-1])

    while True:
        if konversi_otomatis:
            perintah = konversi_otomatis
        else:
            print(perintah_konversi_ke)
            perintah = input().strip().upper()

        if perintah == perintah_berhenti:
            print("Program dihentikan.")
            break
        elif perintah in ["BINER", "OKTAL", "DESIMAL", "HEKSADESIMAL"]:

            if input_otomatis:
                angka = input_otomatis
            else:
                print(perintah_input)
                angka = input()

            if basis_otomatis:
                basis_awal = basis_otomatis
            else:
                print(perintah_basis_angka)
                basis_awal = int(input())

            if not is_valid_input(angka, basis_awal):
                print("Format tidak valid.")
                break  

            if perintah == "BINER":
                hasil = konversi_ke_biner(angka, basis_awal)
            elif perintah == "OKTAL":
                hasil = konversi_ke_oktal(angka, basis_awal)
            elif perintah == "DESIMAL":
                hasil = konversi_ke_desimal(angka, basis_awal)
            elif perintah == "HEKSADESIMAL":
                hasil = konversi_ke_heksadesimal(angka, basis_awal)

            print(perintah_hasil_konversi)
            print(hasil)

            if konversi_otomatis and input_otomatis and basis_otomatis:
                break
        else:
            print("Perintah tidak dikenali.")

file_path = 'test.oll'
baca_perintah(file_path)
