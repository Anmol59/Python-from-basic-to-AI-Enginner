color=input("Enter the color:")

match color:
    case "Green":
        print("GO")
    case "Red":
        print("STOP")
    case "Yellow":
        print("LOOK")
    case _:
        print("Wrong color!")
            
