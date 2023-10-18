import random as ram
print("r for rock")
print("p for paper")
print("s for scissor")
l = ["rock", "paper", "scissor"]
ucount = 0
ccount = 0
draw = 0
for i in range (5):
    x = input("Enter your choice: ")
    n = ram.choice(l)
    print(f"my choice is {n}")
    if x == n:
        print("Draw")
        draw += 1

    elif ((x == "r" and n == "scissor") or (x == "s" and n == "paper") or (x == "p" and n == "rock")):
        print("you win :(")
        ucount += 1

    else:
        print("computer win :)")
        ccount += 1
print(f"result:  your score {ucount}  "
      f"computer score {ccount} "
      f"Draw {draw}")


