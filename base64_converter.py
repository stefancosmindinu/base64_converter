
import base64


def encodeaza_base64(text):
    text_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(text_bytes)
    return base64_bytes.decode('utf-8')


def decodeaza_base64(text_base64):
    base64_bytes = text_base64.encode('utf-8')
    text_bytes = base64.b64decode(base64_bytes)
    return text_bytes.decode('utf-8')


def encodeaza_fisier(cale_fisier):
    with open(cale_fisier, "rb") as f:
        continut = f.read()
    return base64.b64encode(continut).decode('utf-8')


def decodeaza_in_fisier(text_base64, cale_output):
    continut = base64.b64decode(text_base64)
    with open(cale_output, "wb") as f:
        f.write(continut)


def meniu():
    print("1. Encodează text în Base64")
    print("2. Decodează text din Base64")
    print("3. Encodează fișier în Base64")
    print("4. Decodează Base64 într-un fișier")
    print("0. Ieșire")

    while True:
        optiune = input("\nAlege o opțiune: ").strip()

        if optiune == "1":
            text = input("Enter Text: ")
            print(f"Rezultat: {encodeaza_base64(text)}")

        elif optiune == "2":
            text = input("Base64: ")
            try:
                print(f"Rez: {decodeaza_base64(text)}")
            except Exception as e:
                print(f"Eroare la decodare: {e}")

        elif optiune == "3":
            cale = input("file way: ").strip()
            try:
                print(f"Rezultat:\n{encodeaza_fisier(cale)}")
            except Exception as e:
                print(f"Eroare: {e}")

        elif optiune == "4":
            text = input("Base64: ")
            cale_output = input("Numele fișierului de output (ex: rezultat.png): ").strip()
            try:
                decodeaza_in_fisier(text, cale_output)
                print(f"save: {cale_output}")
            except Exception as e:
                print(f"Eroae: {e}")

        elif optiune == "0":
            print("Bye!")
            break

        else:
            print("try again.")


if __name__ == "__main__":
    meniu()
