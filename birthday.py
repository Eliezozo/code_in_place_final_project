def get_birthday_message(name: str, language: str) -> str:
    messages = {
        "1": "Joyeux anniversaire, {} !",
        "2": "Happy birthday, {}!",
        "3": "¡Feliz cumpleaños, {}!",
        "4": "Alles Gute zum Geburtstag, {}!",
        "5": "Buon compleanno, {}!",
        "6": "お誕生日おめでとうございます、{}！",
        "7": "عيد ميلاد سعيد، {}!",
    }
    template = messages.get(language)
    if template is None:
        template = messages["1"]
    return template.format(name)


def main() -> None:
    print("=== Souhaits d'anniversaire multilingues ===")
    name = input("Entrez le nom de la personne : ").strip()
    if not name:
        print("Le nom ne peut pas être vide. Veuillez relancer le programme.")
        return

    print("\nChoisissez la langue :")
    print("  1 - Français")
    print("  2 - English")
    print("  3 - Español")
    print("  4 - Deutsch")
    print("  5 - Italiano")
    print("  6 - 日本語")
    print("  7 - العربية")

    language = input("Votre choix (1-7) : ").strip()
    message = get_birthday_message(name, language)

    print("\nMessage :")
    print(message)


if __name__ == "__main__":
    main()
