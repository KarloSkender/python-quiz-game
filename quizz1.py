import random


def main():
    score = 0

    questions = [
        "Koja je glavna funkcija Python print()?",
        "Koji tip podatka je 'Hello' u Pythonu?",
        "Koja petlja se koristi kad ne znaš točan broj ponavljanja?",
        "Koji operator znači 'jednako'?",
        "Što radi random.choice()?"
    ]

    answers = [
        ["A) Unosi podatke od korisnika", "B) Ispisuje podatke na ekran", "C) Briše varijable", "D) Stvara petlju"],
        ["A) int", "B) float", "C) string", "D) bool"],
        ["A) for", "B) while", "C) if", "D) def"],
        ["A) =", "B) ==", "C) !=", "D) >="],
        ["A) Briše listu", "B) Sortira listu", "C) Bira slučajan element", "D) Spaja stringove"]
    ]

    right_answers = ["B", "C", "B", "B", "C"]

    for i in range(5):
        print(questions[i])

        for answer in answers[i]:
            print(answer+"\n")
        print()

        guess = input("Unesi točan odgovor (A, B, C ili D): ").upper()

        if guess == right_answers[i]:
            print("Točan odgovor\n")
            score += 1
        else:
            print("Pogrešan odgovor\n")


    percent=(score/5)*100

    print(f"Imali ste {score} točnih odgovora,a to je {percent}%")


if __name__ == "__main__":
    main()