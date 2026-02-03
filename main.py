Questions = [
    ["What is the capital of India?", "Mumbai", "New Delhi", "Kolkata", "Chennai", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["Who wrote the Ramayana?", "Valmiki", "Kalidasa", "Tulsidas", "Ved Vyasa", 1],
    ["What is the largest ocean?", "Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean", 4],
    ["Which animal is known as the King of the Jungle?", "Tiger", "Elephant", "Lion", "Leopard", 3],
    ["What is the national bird of India?", "Peacock", "Eagle", "Parrot", "Sparrow", 1],
    ["Which gas do plants absorb?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 3],
    ["Who invented the light bulb?", "Nikola Tesla", "Thomas Edison", "Newton", "Einstein", 2],
    ["What is the currency of Japan?", "Yuan", "Won", "Yen", "Dollar", 3],

    ["Which is the smallest continent?", "Asia", "Europe", "Australia", "Africa", 3],
    ["Who is known as the Father of the Nation (India)?", "Nehru", "Subhash Chandra Bose", "Gandhi", "Bhagat Singh", 3],
    ["What is the square root of 144?", "10", "11", "12", "13", 3],
    ["Which sport is MS Dhoni famous for?", "Football", "Cricket", "Hockey", "Tennis", 2],
    ["Which festival is known as the Festival of Lights?", "Holi", "Eid", "Christmas", "Diwali", 4],
    ["Which device is used to measure temperature?", "Barometer", "Thermometer", "Hygrometer", "Anemometer", 2],
    ["What is H2O commonly known as?", "Oxygen", "Hydrogen", "Salt", "Water", 4],
    ["Which country is known as the Land of the Rising Sun?", "China", "Thailand", "Japan", "Korea", 3],
    ["How many days are there in a leap year?", "364", "365", "366", "367", 3],
    ["What is the hardest natural substance?", "Gold", "Iron", "Diamond", "Silver", 3]
]

prize_money = [
    1000,
    2000,
    5000,
    10000,
    20000,
    40000,
    80000,
    160000,
    320000,
    640000,
    1250000,
    2500000,
    5000000,
    7500000,
    10000000
]

for i in range(len(Questions)):
    q=Questions[i]
    print(f"\nQuestion for ₹{prize_money[i]}")
    print(q[0])
    print(f"1. {q[1]}")
    print(f"2. {q[2]}")
    print(f"3. {q[3]}")
    print(f"4. {q[4]}")



    answer = int(input("Enter your answer (1-4): "))

    if answer == q[5]:
        print(f"Correct! You won ₹{prize_money[i]}")
    else:
        print(f"Wrong answer! The Correct Answer was {q[5]}")
        break
