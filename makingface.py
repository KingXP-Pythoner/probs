def main():
    convertit()

def convertit():
    concern = input("How are you today?").replace(":(","🙁").replace(":)","🙂")
    print(concern)


main()