hexColourCodes = {"BIEGE": "#f5f5dc",
                  "CORAL": "#ff7f50",
                  "FIREBRICK": "#b22222",
                  "GRAY": "#bebebe",
                  "KHAKI": "#f0e68c",
                  "LIGHT": "#eedd82",
                  "LINEN": "#faf0e6",
                  "MEDIUM": "#66cdaa",
                  "NAVYBLUE": "#000080",
                  "PURPLE": "#a020f0"}

colours = input("Enter a colour name: ").upper()
while colours != "":
    if colours in hexColourCodes:
        print(colours, "=", hexColourCodes[colours])
    else:
        print("Error: Colour name is invalid")
    colours = input("Enter a colour name for its hex code: ").upper()