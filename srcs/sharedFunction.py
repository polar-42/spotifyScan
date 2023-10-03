def getTimeReadable(time):
    if type(time) is not int:
        print("printTime didn't receive an int")
        return

    second = 0
    minutes = 0
    hours = 0
    day = 0

    second = time / 1000

    minutes = second / 60
    second = second % 60

    hours = minutes / 60
    minutes = minutes % 60

    day = hours / 24
    hours = hours % 24

    if second > 30:
        minutes = minutes + 1

    s = ""
    if day >= 1:
        s = (str(int(day)) + " days, " + str(int(hours)) +
             " hours and " + str(int(minutes)) + " minutes")
    elif hours >= 1:
        s = (str(int(hours)) + " hours and " + str(int(minutes)) + " minutes")
    elif minutes >= 1:
        s = (str(int(minutes)) + " minutes")
    else:
        s = (str(int(second)) + " seconds")
    return s
