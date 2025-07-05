amount = int(input("Enter the amount: "))

print("\nMinimum number of notes required:")

if amount >= 2000:
    note_2000 = amount // 2000
    amount = amount % 2000
    print("2000 x", note_2000)

if amount >= 500:
    note_500 = amount // 500
    amount = amount % 500
    print("500 x", note_500)

if amount >= 200:
    note_200 = amount // 200
    amount = amount % 200
    print("200 x", note_200)

if amount >= 100:
    note_100 = amount // 100
    amount = amount % 100
    print("100 x", note_100)

if amount >= 50:
    note_50 = amount // 50
    amount = amount % 50
    print("50 x", note_50)

if amount >= 20:
    note_20 = amount // 20
    amount = amount % 20
    print("20 x", note_20)

if amount >= 10:
    note_10 = amount // 10
    amount = amount % 10
    print("10 x", note_10)

if amount >= 5:
    note_5 = amount // 5
    amount = amount % 5
    print("5 x", note_5)

if amount >= 2:
    note_2 = amount // 2
    amount = amount % 2
    print("2 x", note_2)

if amount >= 1:
    note_1 = amount // 1
    amount = amount % 1
    print("1 x", note_1)
