# # q1

number = int(input("enter a number : "))

number_divided = []

for i in range(1, number):
    if number % i == 0:
        number_divided.append(i)

number_divided.sort(reverse=True)

print(", ".join(map(str, number_divided)))

# # q2

count = 0
total = 0

while True:
    if count == 0:
        prompt = "Please enter number #1: "
    else:
        avg = total / count
        prompt = f"Please enter number #{count + 1} (avg={avg:.0f}. Sum={total}): "

    try:
        number = float(input(prompt))
    except ValueError:
        print("enter a number!")
        continue

    if number < 0:
        break

    count += 1
    total += number

print("Thank you. Goodbye.")

# # q3

entered_words = set()

while True:
    word = input("Please type a word: ")

    if word in entered_words:
        print(f"You entered the word {word} twice. Good bye…")
        break

    entered_words.add(word)

