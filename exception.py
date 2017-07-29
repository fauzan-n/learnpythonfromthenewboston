while True:
    try:
        fav = int(input("What is your favorite number?\n"))
        print(10/fav)
        break
    except ValueError:
        print("Make sure and enter a number")
    except ZeroDivisionError:
        print("Dont pick zerooooooo dude")
    finally:
        print("looping lagi aaaaaah")

