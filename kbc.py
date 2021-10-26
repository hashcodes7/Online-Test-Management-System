from kbc1 import Questions, Answers


def game():
    i = 0
    Q = 0
    Rs = 0
    while i < 27:
        i = i + 1
        print(Questions[Q])
        Ans = str(input("Enter your Option!"))
        if Ans == Answers[Q]:

            if Rs == 0:
                Rs = Rs + 5000
            else:
                Rs = Rs * 5
                print("It's the right Answers! Your Current Amount is", Rs, "Rs")
        else:
           if Rs == 0:

              print("It's the Wrong Answers! You have Won Nothing!")
              Restart()
              break
           else:
            print("It's the Wrong Answer! You have Won nothing!", Rs, "Rs")
            Restart()
            break
        Q = Q + 1


def Restart():
    print("Do Want to Play Again?(y/N)")
    Replay = input()

    if Replay == "y" or Replay =="Y":
        game()


game()
