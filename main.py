#Phyton Quiz Game

questions = ("I. Pana in ce an, tara noastra s-a numit Republica Populara Romana?",
            "II. In ce oras s-a nascut Gheorghe Ghiorghiu Dej?", 
            "III. In ce tara a mers pentru ultima oara intr-o vizita oficiala Nicolae Ceausescu, inainte de a fi executat?",
            "IV. In ce an a platit Romania intreaga datorie externa?",
            "V. In ce oras au fost executati sotii Ceausescu?"
            )

options = (("A. 1958", "B. 1974", "C. 1965"),
           ("A. Vaslui", "B. Bucuresti", "C. Barlad"),
           ("A. Iran", "B. China", "C. Coreea de Nord"),
           ("A. 1986", "B. 1988", "C. 1989"),
           ("A. Targoviste", "B. Targu Jiu", "C. Targu Ocna"),
           )

answers = ("C", "C", "A", "C", "A")

guesses = []

score = 0

number_of_questions = 0

for question in questions:
    print("-------------------------")
    print(question)
    print("-------------------------")
    for option in options[number_of_questions]:
        print(option)
        
        
    guess = input("Introduceti (A, B, C): ").upper()
    guesses.append(guess)
    if guess == answers[number_of_questions]:
        score += 1
        print("CORECT!")
    else:
        print("GRESIT!")
        print(f"{answers[number_of_questions]} este raspunsul corect!")
    number_of_questions += 1
    
print("-------------------------")

print("        Rezultate        ")

print("-------------------------")

print("raspuns: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("incercari: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)

print(f"Scorul tau este: {score}%")

if score > 50:
    print("Se vede ca ai invatat! Bravo")
else:
    print("Pune mana pe carte bro :'( ")
