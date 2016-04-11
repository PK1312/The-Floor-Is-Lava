#todo- Maybe monster in closet. Item under bed.

name = raw_input("Please enter your name: ")
print "Hello, " + name + ". You find yourself in your bedroom. The morning sun streams in through your blinds. It's 7 AM, and you need to get ready for school. It's the first day of 4th grade and you can't be late."

player_location = "bed"
player_clothing = "pajamas"
game_complete = False
has_key = False

def get_input(x):
    global player_location
    global player_clothing
    global game_complete
    global has_key
    if x.lower() == "get up" or x.lower() == "stand up" or x.lower() == "get out of bed" or x.lower() == "wake up" or x.lower() == "roll out of bed":
        if player_location == "towel":
            print "You're as up as you can get."
        elif player_location == "bed":
            print "You cannot. The floor is lava."

    elif x.lower() == "look" or x.lower() == "look room" or x.lower() == "look floor" or x.lower() == "look lava" or x.lower() == "look bedroom" or x.lower() == "look around":
        print "You look around your room. The floor glows redly, and you feel the heat rolling off it in waves. Floating conspiculously in the center of your room is a TOWEL. You can also see your CLOSET DOOR, behind which lies your school uniform. On the other side of the wall from your CLOSET DOOR is the EXIT. Nex to your bed is the NIGHTSTAND, atop which you can see a SMALL BOX."

    elif x.lower() == "look nightstand" or x.lower() == "look at nightstand" or x.lower() == "examine nightstand" or x.lower() == "look night stand" or x.lower() == "look at night stand" or x.lower() == "examine night stand" or x.lower() == "look box" or x.lower() == "look at box" or x.lower() == "look at small box" or x.lower() == "look small box":
        print "It's a nightstand for your reading lamp. Atop the nightstand is a small box."
    elif x.lower() == "get box" or x.lower() == "get small box" or x.lower() == "open box" or x.lower() == "open small box":
        has_key = True
        print "You open the small box. Inside is a small brass key, which you slip into your pocket."
        return has_key

    elif x.lower() == "get on towel" or x.lower() == "go to towel" or x.lower() == "go towel" or x.lower() == "stand on towel" or x.lower() == "get onto towel" or x.lower() == "get on to towel" or x.lower() == "get on the towel" or x.lower() == "jump towel" or x.lower() == "jump onto the towel" or x.lower() == "jump onto towel" or x.lower() == "jump on to the towl":
        player_location = "towel"
        print "You leap from the end of your bed and land deftly on the towel. You're now floating above an ocean of lava. It looks like you're close enough to reach the CLOSET DOOR, though."
        return player_location

    elif x.lower() == "open door" or x.lower() == "open" or x.lower() == "door":
        if player_location == "bed":
            print "You strain to reach the closet door from the foot of your bed, but your tiny arms are simply not long enough to reach. If only there was a way to get closer to the door..."
        elif player_location == "towel":
            print "Which door are you trying to open, your CLOSET DOOR or the EXIT DOOR?"
    elif x.lower() == "open closet" or x.lower() == "open closet door" or x.lower() == "closet door" or x.lower() == "closet":
        if player_location == "towel" and has_key == True:
            player_clothing = "uniform"
            print "You've done it! You manage to get the closet door open, and grab your SCHOOL UNIFORM. It's difficult on your floating towel, but you manage to change into it, letting your pajamas burn up in the lava."
            return player_clothing
        elif player_location == "bed":
            print "You strain to reach the closet door from the foot of your bed, but your tiny arms are simply not long enough to reach. If only there was a way to get closer to the door..."
        elif player_location == "towel" and has_key == False:
            print "You jiggle the handle on your closet, but it's locked. You make mom lock it at night so the monster can't get you."
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
    elif x.lower() == "eat":
        print "You have nothing to eat. The smell of bacon wafts in from the kitchen, but you'll need to put on your uniform before you can get breakfast."
    elif x.lower() == "brush my teeth" or x.lower() == "brush teeth":
        print "Your toothbrush is in the bathroom. You cannot brush your teeth yet. Besides, you're not one of those weirdos who brushes their teeth before breakfast."
    elif x.lower() == "shower" or x.lower() == "take shower" or x.lower() == "take a shower" or x.lower() == "take a bath" or x.lower() == "take bath" or x.lower() == "bath":
        print "You're in your bedroom, you can't take a shower or bath here. Plus, the floor is lava, you have bigger issues on your mind."
    elif x.lower() == "look at towel" or x.lower() == "look towel" or x.lower() == "examine towel":
        print "A vertible island among this hellish sea that surrounds you, since it's still damp from the last time you used it."

    else:
        print "I didn't recognize that command."

while game_complete == False:
    action = raw_input("What will you do? ")
    get_input(action)
