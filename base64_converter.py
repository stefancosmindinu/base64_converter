"""
Base64 Converter
-----------------
Script simplu pentru conversia text/fișiere din și în Base64.

Utilizare:
    python base64_converter.py
"""

import base64


def encodeaza_base64(text):
    """Transformă un text (string) în Base64."""
    text_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(text_bytes)
    return base64_bytes.decode('utf-8')


def decodeaza_base64(text_base64):
    """Transformă un text Base64 înapoi în text normal."""
    base64_bytes = text_base64.encode('utf-8')
    text_bytes = base64.b64decode(base64_bytes)
    return text_bytes.decode('utf-8')


def encodeaza_fisier(cale_fisier):
    """Citește un fișier binar și returnează conținutul lui în Base64."""
    with open(cale_fisier, "rb") as f:
        continut = f.read()
    return base64.b64encode(continut).decode('utf-8')


def decodeaza_in_fisier(text_base64, cale_output):
    """Decodează un string Base64 și îl scrie într-un fișier binar."""
    continut = base64.b64decode(text_base64)
    with open(cale_output, "wb") as f:
        f.write(continut)


def meniu():
    print("=== Convertor Base64 ===")
    print("1. Encodează text în Base64")
    print("2. Decodează text din Base64")
    print("3. Encodează fișier în Base64")
    print("4. Decodează Base64 într-un fișier")
    print("0. Ieșire")

    while True:
        optiune = input("\nAlege o opțiune: ").strip()

        if optiune == "1":
            text = input("Introdu textul: ")
            print(f"Rezultat: {encodeaza_base64(text)}")

        elif optiune == "2":
            text = input("Introdu textul Base64: ")
            try:
                print(f"Rezultat: {decodeaza_base64(text)}")
            except Exception as e:
                print(f"Eroare la decodare: {e}")

        elif optiune == "3":
            cale = input("Calea către fișier: ").strip()
            try:
                print(f"Rezultat:\n{encodeaza_fisier(cale)}")
            except Exception as e:
                print(f"Eroare: {e}")

        elif optiune == "4":
            text = input("Introdu textul Base64: ")
            cale_output = input("Numele fișierului de output (ex: rezultat.png): ").strip()
            try:
                decodeaza_in_fisier(text, cale_output)
                print(f"Fișier salvat: {cale_output}")
            except Exception as e:
                print(f"Eroare: {e}")

        elif optiune == "0":
            print("La revedere!")
            break

        else:
            print("Opțiune invalidă, încearcă din nou.")


if __name__ == "__main__":
    meniu()
