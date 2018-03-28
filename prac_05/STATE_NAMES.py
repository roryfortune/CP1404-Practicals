stateNames = {"QLD": "Queensland",
              "ACT": "Australian Capital Territory",
              "NT": "Northern Territory",
              "VIC": "Victoria",
              "WA": "Western Australia",
              "TAS": "Tasmania",
              "NSW": "New South Wales"}

states = input("Enter short state: ").upper()
while states != "":
    if states in stateNames:
        print(states, "=", stateNames[states])
    else:
        print("Error: Short state is invalid")
    states = input("Enter a short state: ").upper()

    
