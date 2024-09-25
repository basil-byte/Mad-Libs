import csv
import sys
import textwrap

FILENAME = "rules.csv"


#exiting the program
def exit_program():
    print("Terminating program.")
    sys.exit()

#Read the rules from the file
def read_rules():
    try:
        rules = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                rules.append(row)
        return rules #this fills out the rules in a list from the rules.csv file
    except FileNotFoundError:
        print(f"Could not find {FILENAME} file.")
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()


#Display the rules
def list_rules(rules):
    for i, rules in enumerate(rules, start=1):
        print()
        print(textwrap.fill(f"{i}.{rules[0]} - {rules[1]}", 70)) #this prints the rules
    print()
    print("-----------------------------------------")
    print()
    display_menu()  #this brings us back to the menu


#Play the Christmas Story
def play_christmas():
    word = []
    items = ['Adjective', 'Noun', 'Person'
             ,'Noun', 'Verb' ,'Noun' 
             ,'Noun', 'Adjective','Adjective'
             ,'Person', 'Animal', 'Adjective'
             ,'Noun', 'Noun', 'Noun'
             ,'Adjective', 'Noun', 'Adjective',
             'Interjection'] #this instructs the user what type of word to enter
    
    for index, item in enumerate(items):
        word.append(input(item + ": ")) 
        # this requests the user to input a word for each item in the list 
        # and stores it in the word list.
        
    ChristmasStory = f"Dear Santa, I have been a very {word[0]} {word[1]} this year. I always help {word[2]} with chores around the {word[3]}. It’s my job to {word[4]} the {word[5]} and take out the {word[6]} everyday. I really hope that I am on the {word[7]} list this year. I have done a lot of {word[8]} things, so I think that I deserve it. I even helped {word[9]} feed the {word[10]} while they were on vacation. I have a few wishes this year. I would love to see a {word[11]} new {word[12]} underneath the tree with my name on it. It would make me the happiest {word[13]} on the {word[14]}! Oh, and if you could put a {word[15]} {word[16]} inside of my stocking, that would be {word[17]} too! {word[18]}, I love the holidays!"
    #this stores the story in a variable called ChristmasStory
    
    print()
    print("Christmas Story")
    print(textwrap.fill(ChristmasStory, width=50)) #this prints the story
    print()
    print("-----------------------------------------")
    print()
    display_menu() #this brings us back to the menu

#Play the Book Recommendation Story
def play_book():
    word = []
    items = ['Adjective', 'Adjective', 'Plural Noun'
            , 'Person', 'Genre' ,'Article of Clothing'
            , 'Noun', 'Plural Noun','Adjective'
            , 'Plural Noun', 'Plural Noun', 'Adjective'
            , 'Place', 'Part of Body', 'Adjective'
            , 'Noun', 'Adjective', 'Verb'
            , 'Plural Noun', 'Number'] #this instructs the user what type of word to enter

    for index, item in enumerate(items):
        word.append(input(item + ": "))
        # this requests the user to input a word for each item in the list 
        # and stores it in the word list.

    word[6] = word[6].title()
    word[9] = word[9].title()
    word[10] = word[10].title()

    BookStory = f"There are many {word[0]} ways to choose a/an {word[1]} book to read. First, you could ask for recommendations from your friends and {word[2]}. Just don’t ask Aunt/Uncle {word[3]} he/she only reads {word[4]} books with {word[5]}-ripping goddesses on the cover. If your friends and family are no help, try check out the '{word[6]} Review' in 'The City Times'. If the {word[7]} featured there are too {word[8]} for your taste, try something a little more low-brow, like 'The {word[9]} Magazine' or 'The {word[10]} Digest'. You could also choose a book the {word[11]}-fashioned way. Head to your local library or the {word[12]} library and browse the shelves until something catches your {word[13]}. Or, you could save yourself a whole lot of {word[14]} trouble and log on to www.book{word[15]}.org, the  {word[16]} new website to {word[17]} for books. With all the time you’ll save not having to search for {word[18]}, you can read at least {word[19]} more books!"

    print()
    print("Book Recommendation Story")
    print(textwrap.fill(BookStory, width=50)) #this prints the story
    print()
    print("-----------------------------------------")
    print()
    display_menu()  #this brings us back to the menu

#Display Menu
def display_menu():
    print("MAD LIBS")
    print()
    print("MENU - TYPE A COMMAND TO PLAY")
    print("rules - Learn the rules of the game")
    print("christmas -  Play Christmas game")
    print("book -  Play the Book Recommendation game")
    print("exit - Exit program")
    print()    


display_menu()
rules = read_rules()
while True:    
    command = input("Command: ")
    if command.lower() == "rules": #User types in rules to show rules
        list_rules(rules)
    elif command.lower() == "christmas": #User types in christmas to play the christmas game
        play_christmas()
    elif command.lower() == "book": #User types in book to play the book game
        play_book()
    elif command.lower() == "exit": #This exists the program
        break
    else:
        print("Not a valid command. Please try again.\n")
print("Ending Mad Libs Program")