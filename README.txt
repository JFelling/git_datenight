OVERVIEW
The Date Night project was designed to fulfil the requirements of Codecademy's CS 101:Intro to Programming portfolio project: Python Terminal Game. The project asked students to "research, brainstorm, and build a basic terminal program of your choice for your friends and family to play with." Specifically, the instructions included:
  1. Build a terminal program using Python
  2. Add at least one interactive feature using input()
  3. Use Git version control
  4. Use the command line and file navigation

For this project, I decided to create a "game" to help solve the age old problem of having no idea what to do for date night. Inspired by a story performed on The Moth podcast, the game allows users to input ideas for date nights, or to generate a random idea for what to do on their next night out. Ideas can either be general, or location specific. As my friend group is largely split over 3 main geographical areas, the program currently reflects those three locations: Washington, DC; Ithaca, NY; and Rochester, NY.

INSTRUCTIONS FOR USE
The program is written in Python, and was created using Vistual Studio (VS) Code. In it's current itteration, the program can only be run in a terminal, using either a code editor or command prompt. 

To run the program, download datenight.py and IdeasList files. Open datenight.py in a code editor or command prompt to use. 

EXPLANATION OF CODE
The code initializes by importing random, and reading in and formatting the lists of date night ideas for each location. It includes commented lines of code for testing that the lists have been imported correctly, should that be necessary. The code then defines a function for generating a date idea based upon a user input of location, including edge cases. It then defines a function for adding user generated ideas to the appropriate date ideas list and formatting the input to match. After the functions are defined, the rest of the code sets up print statements and options for user input to either add or generate random date ideas. If addind an idea, the code includes writing the idea back to the IdeasLists file in the appropriate location. Each option ends by allowing the user to restart or end the program. 

AREAS FOR FURTHER DEVELOPMENT
As this project was a basic terminal game, there are a number of areas for further development outside the scope of the original project. These areas include:
  1. User interface and expereince, including on a web and/or app platform.
  2. Expanded location options and date night idea lists.
  3. Functionality to allow users to add new location options.
  4. Ability to categorize ideas as indoor/outdoor, warm weather/cold weather, etc.
  5. Functionality to interface with a weather application and suggest ideas that are weather appropriate (ex. only indoor ideas if it is forecast to rain).
  6. Further filters for date nights.
  7. User logins and profiles, which could include the ability to maintin a history of date ideas generated and/or used, track submitted date ideas, share photos  from dates, and rate and review date idea experiences.
  8. Functionality to prevent users adding date ideas that are inappropriate or gibberish. 

ACKNOWLEDGEMENTS
Thank you to my dad for help troubleshooting!
