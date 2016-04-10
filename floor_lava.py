#todo- locked closet door. Maybe monster in closet. Item under bed.

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
            print "Which door are you trying to open, your CLOSET DOOR or the EXIT DOOR?"
    elif x.lower() == "open closet" or x.lower() == "open closet door" or x.lower() == "closet door" or x.lower() == "closet":
        player_clothing = "uniform"
        print "You've done it! You manage to get the closet door open, and grab your SCHOOL UNIFORM. It's difficult on your floating towel, but you manage to change into it, letting your pajamas burn up in the lava."
        return player_clothing

    elif x.lower() == "exit" or x.lower() == "open exit" or x.lower() == "open exit door" or x.lower() == "go exit" or x.lower() == "move exit" or x.lower() == "leave room" or x.lower() == "leave":
        if player_location == "towel" and player_clothing == "uniform":
            print "You open the door. You see your mother putting breakfast on the table. You sigh, and the floor cools back to carpet. Time for school. Congrats, " + name + "! You won the game! For now..."
            game_complete = True
            return game_complete
        elif player_location == "towel" and player_clothing == "pajamas":
            print "You can't go to school in your pajamas! You go to one of those schools with uniforms."
        elif player_location == "bed" and player_clothing == "pajamas":
            print "You have to get out of bed before you can leave."
        elif player_location == "bed" and player_clothing == "uniform":
            print "wait what, no, you shouldn't get back into bed after putting on your uniform what are you doing."

    elif x.lower() == "help":
        print "This is your standard test based adventure game! Type commands to see what works. If you're stuck, try using 'look'!"

    elif x.lower() == "cry":
        print "You begin to weep. You're scared of starting the fourth grade, which is why you've constructed these elaborate fantasy scenarios to cope. You lead a rich inner life. The tears sizzle as they hit the lava."

    elif x.lower() == "get towel" or x.lower() == "grab towel" or x.lower() == "pick up towel" or x.lower() == "pick towel up" or x.lower() == "take towel":
        print "You can't get the towel. It's too far away, and you'd have to stick your hand into lava to get it off the ground anyway."
    elif x.lower() == "put on uniform" or x.lower() == "put uniform on" or x.lower() == "uniform":
        if player_clothing == "pajamas":
            print "Your UNIFORM is still hanging in your CLOSET."
        elif player_clothing == "uniform":
            print "You're already wearin your SCHOOL UNIFORM."

    elif x.lower() == "the floor is not lava":
        game_complete = True
        print "Your childlike innocence dies. The floor is just carpet. You get ready for school, but the spark of imagination is gone from you forever. You've completed the game... but at a terrible price."
        return game_complete
    elif x.lower() == "dennis":
        print "Nice try, Thy Dungeonman."
    elif x.lower() == "get ye flask":
        print "You can't get ye flask. Now you need to sit around wondering why in the world you can't get ye flask."
    elif x.lower() == "look self" or x.lower() == "look at self" or x.lower() == "look at myself":
        print "You're wearing your pajamas. They have polar bears on them. Your mom has a matching pair. It's dorky as hell but also you love them."
    elif x.lower() == "go bed" or x.lower() == "go to bed" or x.lower() == "get back into bed" or x.lower() == "get back in bed" or x.lower() == "get in bed" or "jump into bed":
        if player_location == "bed":
            print "You're already in bed. You're supposed to be getting OUT of bed, ya dang dingus."
        elif player_location == "towel":
            player_location = "bed"
            print "sigh. you get back into bed. it's now 7:15 and your mom is mad."

    else:
        print "I didn't recognize that command."

while game_complete == False:
    action = raw_input("What will you do? ")
    get_input(action)
