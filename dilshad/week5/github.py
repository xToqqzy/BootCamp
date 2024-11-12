def ontvanger(user_input):
    nieuw = ""
    teller = 0
    while teller < len(user_input):
        if teller % 2 == 0:
            nieuw += user_input[teller].upper()
        else:
            nieuw += user_input[teller]
        teller += 1
    return nieuw
