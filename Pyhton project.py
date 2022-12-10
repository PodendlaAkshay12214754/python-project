d = input("enter your name:")
while True:
    print("Hi", d, "PLEASE SELECT YOUR CONVERTER OR CALCULATOR:")
    print("    If you want Time converter     ENTER '1'    ")
    print("    If you want Temperature converter     ENTER '2'    ")
    print("    If you want Currency converter    ENTER'3'    ")
    print("    If you want Age calculator    ENTER '4'    ")
    print("    If you want Length converter     ENTER '5'    ")
    f = int(input("ENTER:"))
    if f == 1:
        print("                'TIME CONVERTER'    ")
        print("IF YOU WANT TO CONVERT:")
        print("    HOURS TO MINUTES:", "  Enter 'a'")
        print("    HOURS TO SECONDS: ", "  Enter 'b'")
        y = input("Enter 'a' or 'b' :")
        if y == "a":
            z = int(input("Enter value in HOURS(like 12,15,etc..):"))
            print(z * 60, "minutes")
        elif y == "b":
            z = int(input("Enter value in HOURS(like 12,15,etc..):"))
            print(z * 60 * 60, "seconds")
        else:
            print("CHOOSE THE RIGHT OPTION")
    elif f == 2:
        print("            'TEMPERATURE CONVERTER'    ")
        print("IF YOU WANT TO CONVERT:")
        print("    Celsius(C) to Fahrenheit(F) ", "  Enter 'a'")
        print("    Fahrenheit(F) to Celsius(C) ", "  Enter 'b'")
        y = input("Enter 'a' or 'b' :")
        if y == "a":
            z = int(input("Enter value in Celsius:"))
            print("The value of", z, " Celsius in Fahrenheit is")
            print(((z * 1.8) + 32))
        elif y == "b":
            z = int(input("Enter value in Fahrenheit:"))
            print("The value of", z, " Fahrenheit in Celsius is")
            print(((z - 32) * (5 / 9)))
        else:
            print("CHOOSE THE RIGHT OPTION")
    elif f == 3:
        print("              'CURRENCY CONVERTER'    ")
        print("SELECT THE CURRENCY TO WHICH YOU WANT TO CONVERT ")
        print("a.rupees to 'Dollar'", "enter", "a")
        print("b.rupees to 'Euro'", "enter", "b")
        print("c.rupees to 'Dinar'", "enter", "c")
        print("d.rupees to 'Chinese yuan'", "enter", "d")
        print("e.rupees to 'Taka'", "enter", "e")
        x = input('enter:')
        if x == "a":
            A = int(input("enter value in rupees:"))
            print(A / 80,"Dollars")
        elif x == "b":
            A = int(input("enter value in rupees:"))
            print(A / 104,"Euro")
        elif x == "c":
            A = int(input("enter value in rupees:"))
            print(A / 22,"Dinar")
        elif x == "d":
            A = int(input("enter value in rupees:"))
            print(A / 12,"Yuan")
        elif x == "e":
            A = int(input("enter value in rupees:"))
            print(A / 0.8,"Taka")
        else:
            print("CHOOSE RIGHT OPTION")
    elif f == 5:
        print("                'LENGTH CONVERTER'    ")
        print("IF YOU WANT TO CONVERT:")
        print("  KILOMETERS TO MILES ENTER 'a'")
        print("  MILES TO KILOMETERS ENTER 'b'")
        print("  FEETS TO  INCHES ENTER 'c'")
        print("  INCHES TO FEETS ENTER 'd'")
        q = input("ENTER:")
        if q == "a":
            x = int(input("Enter no.of KILOMETERS:"))
            print(x * 0.62,"MILES")
        if q == "b":
            x = int(input("Enter no.of MILES:"))
            print(x / 0.62,"KILOMETERES")
        elif q == "c":
            x = int(input("Enter no.of FEETS:"))
            print(x * 12,"INCHES")
        elif q == "d":
            x = int(input("Enter no.of INCHES:"))
            print(x / 12,"FEETS")
        else:
            print("CHOOSE THE RIGHT OPTION")
    elif f == 4:
        print("              'AGE CALCULATOR'    ")
        x = int(input("Year you born:"))
        y = int(input("Month you born(enter month in numbers like jan=1 feb=2):"))
        z = int(input("Date you born:"))
        v = int(input("Current Year:"))
        u = int(input("Current month(enter month in numbers like jan=1 feb=2):"))
        w = int(input("Current date:"))
        if y > u:
            if z == w:
                print((v - 1) - x, "years", 12 - (y - u), "months", z - w, "days")
            elif z > w:
                print((v - 1) - x, "years", 11 - (y - u), "months", 30 - (z - w), "days")
            elif z < w:
                print((v - 1) - x, "years", 12 - (y - u), "months", (w - z), "days")
        elif y == u:
            if z == w:
                print(v - x, "years", (y - u), "months", z - w, "days")
            elif z > w:
                print((v - 1) - x, "years", 11 - (y - u), "months", 30 - (z - w), "days")
            elif z < w:
                print(v - x, "years", (y - u), "months", (w - z), "days")
        elif y < u:
            if z == w:
                print(v - x, "years", (u - y), "months", z - w, "days")
            elif z > w:
                print(v - x, "years", (u - 1) - y, "months", 30 - (z - w), "days")
            elif z < w:
                print(v - x, "years", (u - y), "months", (w - z), "days")
    else:
        print("ENTER THE RIGHT OPTION ")