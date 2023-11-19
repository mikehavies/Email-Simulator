### --- OOP Email Simulator --- ###

# --- Email Class --- #

# Create the class, constructor and methods to create a new Email object.
class Email(object):

    # class variable
    has_been_read = False

    # Declare the class variables, with default values, for emails. 
    def __init__(self, email_address, subject_line, email_content):
         # Initialise the instance variables for emails.
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True
    
  

# --- Lists --- #
# Initialise an empty list to store the email objects.
Inbox = []


# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    
    # Create 3 sample emails and add it to the Inbox list. 
    mum_email = Email("mum@msn.net", "Missing Biscuits", "My biscuits have mysteriously gone missing, and your appetite was spoiled at dinner. You may be 37, but that won't stop me.")
    amazon_email = Email("noreply@amazon.com", "Return Order", "Dear valued customer, We appreciate your order was not delivered, and photos of it being destroyed was emailed to you as well. For this service we are going to have to charge you an additional $15 plus a $10 addministration fee. Our customer 'support' team will be round to lock your toilet and install an electronic lock that will only be compatible with an amazon gift card, shortly. We await yoour grateful response soon. Yours, Bezos xxx")
    charlie_email = Email("charlesIII@royalhouse.gov.uk", "Advice", "Dear subject, I am writing to you as you have been chosen via lottery to provide support for your King. I require an answer to the following. A tradesman was overheard saying he will leave a floater after fixing the plumping at the royal toilets. What does this mean? Is this something for me? Is it a gift from a grateful subject to his benevolent King? One likes gifts! I look forward to your response. Yours lovingly, His Majesty the Right Honorable and Expedient Majesty of Great Britain and Northern Ireland and all members of the greater Commonwealth, including Devon, Charlie xxx")
    
    #add the email objects to the list Inbox
    Inbox.append(mum_email)
    Inbox.append(amazon_email)
    Inbox.append(charlie_email)


    # Create a function which prints the email’s subject_line, along with a corresponding number.
def list_emails():
    
    print("INBOX\n")
    for count, item in enumerate(Inbox):
        print(count+1, Inbox[count].subject_line)


# Create a function which displays a selected email.
def read_email(index):

    print(f"\nFrom: " + Inbox[index].email_address + "\nSubject: " + Inbox[index].subject_line + "\nContent: " + Inbox[index].email_content + "\n")
    
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    Inbox[index].mark_as_read()




# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
    # Blank line for presentation
    print()
       
    if user_choice == 1:
        # add logic here to read an email
        # List the emails in the inbox
        list_emails()

        while True:
            
            # DEFENSIVE ensure pupil HAS entered a number using try
            try:
                user_choice = int(input(f'''\nWhich email would you like to read? Enter a number between 1 and {len(Inbox)} .\n'''))
                
                # DEFENSIVE check user has entered a valid email number
                if not 1 <= user_choice <= len(Inbox):
                    print("\nPlease choose a valid email.")
                else:
                    read_email(user_choice-1)
                    break
            
            # If user did not enter a number, ask them to repeat
            except ValueError:
                print("\nPlease only enter a number.")


    elif user_choice == 2:
    # add logic here to view unread emails

        print("\nYour unread emails are:\n")
        # Check to see if an email has been read and prints its subject line if it has not.
        for count, item in enumerate(Inbox):
            if Inbox[count].has_been_read == False:
                print(count+1, Inbox[count].subject_line)
        print()
    
    elif user_choice == 3:
    # add logic here to quit appplication
        print("Goodbye!\n")
        break

    else:
        print("Oops - incorrect input.")

