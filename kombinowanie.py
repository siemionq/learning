

command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if not started:
            print("you can not stop stopped car")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("""
start - odpalanie silnika
stop - zatrzymanie silnika
quit - wyjście
        """)
    elif command == "quit":
        break
    else:
        print("wybierz dostępną opcje, wpisz 'help'")