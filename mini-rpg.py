
print ("------------------------ENTER THE DOUNGEON-----------------------")

print("Hello adventurer! Are you rady to enter this dungeon? Yes[1] No [0]: ")
enter = int(input())
if (enter == 1):
    print("Check your inventory to see if yuou are ready!")
elif (enter == 0):
    print("Ok! Could be dengerous, come back when you're ready!")
else:
    print("Invalid!")

equip = input("Do you have your equipment? What are you bringing?  ")
if (equip == "Sword and Shield" or "Shield and Sword" or "sword and shield" or "shield and sword"):
    print("So you're a fighter! Great! Your total health is (8 hp). Good Luck!")
    print("You enter the dungeon and its cold and humid, you look around and its hard to see, but you see just enough to realize that there ar tow way you can go")
    way = input("Which way do you choose? Right or Left?  ")
    if (way == "Left" or "left"):
       open =  input ("You go left and as you are walking down this path you can see a treasure chest. Do you open[Yes/No]:  ")
       if (open == "yes" or "Yes"):
           print ("The chest comes to life! and attacks you! (5 hp)")
           action1 = input("What do you do?[Run/Fight]:  ")
           if (action1 == "run" or "Run"):
              print ("Maybe this dungeon isn't for you. You go home, you'll go back another day!")
           elif (action1 == "fight" or "Fight"):
              print("You fight the Mimic, and ou win, but with some scratches [2hp], Better go home and come back another day")
           else:
               ("Invalid!")

       elif (open == "no" or "No"):
            print("You go back to the area with the bifurcation and go right")
           
       else:
           print("Invalid!")


    elif (way == "Right" or "right"):
        print("You enter the dungeon and its cold and humid, you look around and its hard to see, but you see just enough to realize that there ar tow way you can go")
        open =  input ("You go left and as you are walking down this path you can see a treasure chest. Do you open[Yes/No]:  ")
        if (open == "yes" or "Yes"):
           print ("The chest if full of gold! you now have [50 gold pieces])")
        elif(open == "no" or "No"):
            print("You go back to the area with the bifurcation and go right")
        else: 
            print("Invalid!")

    else:
        print("Ivalid!")

elif (equip == "wand" or "Wand" or "staff" or "Staff"):
    print("So you're a Wizard! Great! Your total health is (5 hp). Good Luck!")
    print("You enter the dungeon and its cold and humid, you look around and its hard to see, but you see just enough to realize that there ar tow way you can go")
    way = input("which way do you choose? Right or Left?:  ")
    if (way == "Left" or "left"):
         open =  input ("You go left and as you are walking down this path you can see a treasure chest. Do you open[Yes/No]:  ")
         if (open == "yes" or "Yes"):
             print ("The chest comes to life! and attacks you! (3 hp)")
             action1 = input("What do you do?[Run/Fight]:  ")
             if (action1 == "run" or "Run"):
              print ("Maybe this dungeon isn't for you. You go home, you'll go back another day!")
             elif (action1 == "fight" or "Fight"):
                print("You cast a spell on the Mimic, and ou win, but with some scratches [1hp], Better go home and come back another day")
             else: 
                 print("invalid!")
       
         elif(open == "no" or "No"):
              print("You go back to the area with the bifurcation and go right")
           
         else:
             print("Invalid!")


    elif (way == "Right" or "right"):
          print("You enter the dungeon and its cold and humid, you look around and its hard to see, but you see just enough to realize that there ar tow way you can go")
          open =  input ("You go left and as you are walking down this path you can see a treasure chest. Do you open[Yes/No]:  ")
          if (open == "yes" or "Yes"):
           print ("The chest if full of gold! you now have [50 gold pieces])")
          elif(open == "no" or "No"):
            print("You go back to the area with the bifurcation and go right")
          else: 
              print("invalid!")
    else:
        print("Ivalid!")


else:
    print("Invalid!")