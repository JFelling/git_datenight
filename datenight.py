import random

#read in file of list of ideas for each location
with open('IdeasLists', 'r+') as ideas:
    general = ideas.readline().strip()
    DC = ideas.readline().strip()
    Rochester = ideas.readline().strip()
    Ithaca = ideas.readline().strip()

#format lists so the output looks right
date_ideas_general = general.split(", ")
date_ideas_DC = DC.split(", ")
date_ideas_Rochester = Rochester.split(", ")
date_ideas_Ithaca = Ithaca.split(", ")

#to test that it's reading the file correctly
#print(general)
#print(DC)
#print(Rochester)
#print(Ithaca)

#function for pulling a random date idea based on user input for location
def generate_idea(location):
    if location.lower() == "general":
        general_date = random.sample(date_ideas_general, 1)
        return("Your date idea is " + str(general_date[0]) + ". Have a great date!")
    elif location.upper() == "DC":
        DC_date = random.sample(date_ideas_DC, 1)
        return("Your date idea is " + str(DC_date[0]) + ". Have a great date!")
    elif location.title() == "Rochester":
        Rochester_date = random.sample(date_ideas_Rochester, 1)
        return("Your date idea is " + str(Rochester_date[0]) + ". Have a great date!")
    elif location.title() == "Ithaca":
        Ithaca_date = random.sample(date_ideas_Ithaca, 1)
        return("Your date idea is " + str(Ithaca_date[0]) + ". Have a great date!")
    else:
        return("I'm sorry. I do not recognize that location.")

#function for adding a date idea to a specific location based on user input
def add_idea(location):
    if location.lower() == "general":
        general_date_idea = input("Awesome! You're adding a date to the general dates category. Type your date idea and hit enter. ")
        general_date_idea_formatted = general_date_idea.title()
        for date in date_ideas_general:
            if general_date_idea_formatted not in date_ideas_general:
                date_ideas_general.append(general_date_idea_formatted)
            else: continue
        return("Thanks for helping other users by adding a date idea!")
    elif location.upper() == "DC":
        DC_date_idea = input("Awesome! You're adding a date to the DC dates category. Type your date idea and hit enter. ")
        DC_date_idea_formatted = DC_date_idea.title()
        for date in date_ideas_DC:
            if DC_date_idea_formatted not in date_ideas_DC:
                date_ideas_DC.append(DC_date_idea_formatted)
            else: continue
        return("Cool beans! You added a date idea for our DC friends! You're the best!")
    elif location.title() == "Rochester":
        Rochester_date_idea = input("Awesome! You're adding a date to the Rochester dates category. Type your date idea and hit enter. ")
        Rochester_date_idea_formatted = Rochester_date_idea.title()
        for date in date_ideas_Rochester:
            if Rochester_date_idea_formatted not in date_ideas_Rochester:
                date_ideas_Rochester.append(Rochester_date_idea_formatted)
            else: continue
        return("You're rad! Thank you, friend! We're always looking for more things to do in Rochester!")
    elif location.title() == "Ithaca":
        Ithaca_date_idea = input("Awesome! You're adding a date to the Ithaca dates category. Type your date idea and hit enter. ")
        Ithaca_date_idea_formatted = Ithaca_date_idea.title()
        for date in date_ideas_Ithaca:
            if Ithaca_date_idea_formatted not in date_ideas_Ithaca:
                date_ideas_Ithaca.append(Ithaca_date_idea_formatted)
            else: continue
        return("You're so cool, rainbows are jealous of you. We've added your idea to the Ithaca list!")
    else:
        return("I'm sorry. I do not recognize that location.")

run = True
while run:
    #intro text to run
    print("Welcome to Date Night, our randomized date night idea generator! Ever find yourself in the same pattern with a partner date after date? Feel stuck for ideas when deciding how to impress that special someone on your first night out? You've come to the right place!")
    print("Date Night gives you a random date idea from user-generated lists of ideas. Ideas are sorted by location, so you can search for date ideas specific to your area, or general ideas.")
    print("Date Night also lets you add your own ideas to the date idea lists, so you and other Date Night users have even more possibilities!")

    #input section: generate or add date idea
    category = input("Let's get started! If you would like a randomly generated date idea, type generate. If you would like to add an idea to the date lists, type add idea. Then press Enter. ")

    #code to randomly generate an idea from the list, depending on location
    if category.lower() == "generate":
        generate = input("Great! Let's generate an idea for you! What location would you like an idea for? You can type general, DC, Rochester, or Ithaca, and press Enter. ")
        print(generate_idea(generate))

        #code to return to initial interface
        restart = input("Would you like to return to the main menu? Type Y for yes, and N for no. Then press Enter. ")
        if restart.upper() == "N":
            run = False
            print("Thanks for stopping by!")

    #code to add date ideas to location specific lists
    elif category.lower() == "add idea":
        idea = input("Awesome! Let's get you to the right list to add a date night! What location do you want to add a date night for? You can type general, DC, Rochester, or Ithaca, and then hit Enter. ")
        print(add_idea(idea))

        #test if the ideas were added to the list
        #print(date_ideas_general)
        #print(date_ideas_DC)
        #print(date_ideas_Rochester)
        #print(date_ideas_Ithaca)    

        #code to return to initial interface
        restart = input("Would you like to return to the main menu? Type Y for yes, and N for no. Then press Enter. ")
        if restart.upper() == "N":
            run = False
            print("Thanks for stopping by!")
    
        #format idea lists to be able to write to file
        new_list_general = ', '.join(date_ideas_general)
        new_list_DC = ', '.join(date_ideas_DC)
        new_list_Rochester = ', '.join(date_ideas_Rochester)
        new_list_Ithaca = ', '.join(date_ideas_Ithaca)

        #write new ideas to the file       
        ideas = open('IdeasLists', 'w')
        ideas.write(new_list_general + "\n")
        ideas.write(new_list_DC + "\n" )
        ideas.write(new_list_Rochester + "\n")
        ideas.write(new_list_Ithaca + "\n")
        ideas.flush()
        ideas.close
    
    else:
        print("I'm sorry. That is not a valid input.")

        restart = input("Would you like to return to the main menu? Type Y for yes, and N for no. Then press Enter. ")
        if restart.upper() == "N":
            run = False
            print("Thanks for stopping by!")

ideas.close