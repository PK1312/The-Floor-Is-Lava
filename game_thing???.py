name = raw_input("Please enter your name: ")
print "Hello, " + name + ". You find yourself in your bedroom. The morning sun streams in through your blinds. It's 7 AM, and you need to get ready for school. It's the first day of 4th grade and you can't be late."

player_location = "bed"
player_clothing = "pajamas"
game_complete = False

def get_input(x):
    global player_location
    global player_clothing
    global game_complete
    if x.lower() == "get up" or x.lower() == "stand up" or x.lower() == "get out of bed" or x.lower() == "wake up" or x.lower() == "roll out of bed":
        if player_location == "towel":
            print "You're as up as you can get."
        elif player_location == "bed":
            print "You cannot. The floor is lava."

    elif x.lower() == "look" or x.lower() == "look room" or x.lower() == "look floor" or x.lower() == "look lava" or x.lower() == "look bedroom" or x.lower() == "look around":
        print "You look around your room. The floor glows redly, and you feel the heat rolling off it in waves. Floating conspiculously in the center of your room is a TOWEL. You can also see your CLOSET DOOR, behind which lies your school uniform. On the other side of the wall from your CLOSET DOOR is the EXIT."

    elif x.lower() == "get on towel" or x.lower() == "go to towel" or x.lower() == "go towel" or x.lower() == "stand on towel" or x.lower() == "get onto towel" or x.lower() == "get on to towel" or x.lower() == "get on the towel" or x.lower() == "jump towel" or x.lower() == "jump onto the towel" or x.lower() == "jump onto towel" or x.lower() == "jump on to the towl":
        player_location = "towel"
        print "You leap from the end of your bed and land deftly on the towel. You're now floating above an ocean of lava. It looks like you're close enough to reach the CLOSET DOOR, though."
        return player_location

    elif x.lower() == "open door" or x.lower() == "open" or x.lower() == "door":
        if player_location == "bed":
            print "You stretch your little arms as far as you can, but there's just too much lava between you and the door."
        elif player_location == "towel":
            print "Which door are you trying to open?"
    elif x.lower() == "open closet" or x.lower() == "open closet door" or x.lower() == "closet door" or x.lower() == "closet":
        player_clothing = "uniform"
        print "You've done it! You manage to get the closet door open, and grab your SCHOOL UNIFORM. It's difficult on your floating towel, but you manage to change into it, letting your pajamas burn up in the lava."
        return player_clothing

    elif x.lower() == "exit" or x.lower() == "open exit" or x.lower() == "open exit door" or x.lower() == "go exit" or x.lower() == "move exit" or x.lower() == "leave room" or x.lower() == "leave":
        if player_location == "towel" and player_clothing == "uniform":
            print "You open the door. You see your mother putting breakfast on the table. You sigh, and the floor cools back to carpet. Time for school. Congrats! You won the game!"
            game_complete = True
            return game_complete
        elif player_location == "towel" and player_clothing == "pajamas":
            print "You can't go to school in your pajamas! You go to one of those schools with uniforms."
        elif player_location == "bed" and player_clothing == "pajamas":
            print "You have to get out of bed before you can leave."
        elif player_location == "bed" and player_clothing == "uniform":
            print "wait what this shouldn't even be possible, what the heck did you do to break the game"
    else:
        print "I didn't recognize that command."

while game_complete == False:
    action = raw_input("What will you do? ")
    get_input(action)
