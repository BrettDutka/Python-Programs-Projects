from Contact import Contact  # Imports the class
from PhoneBook import PhoneBook  # Imports the class


def test_getName(contact):
    return contact.getName()


def get_all_contacts(phB):
    """
    1. Read in the contacts.txt file
    2. Create new contacts for each line in the file
    """

    f = open("Laboratory/Lab10/contacts.txt", "r")
    contacts = f.read().split("\n")
    f.close()

    print("Data from the file")
    print(contacts)

    print()
    for c in contacts:
        l = c.split(", ")

        name = l[0].split(" ")
        phone = l[1]
        email = l[2]
        birthday = l[3].split(".")

        newContact = Contact(name, phone, email, birthday)
        print(newContact)

        phB.addContact(newContact)


def groupMessage(phB):
    print()
    print("We are going to send a groupchat")

    phB.groupChat("I got your number saved")


if __name__ == "__main__":
    ########################################################################
    # Testing Contact
    ########################################################################
    print("~" * 60)
    print("{:^60}".format("Testing Contact Class"))
    print("~" * 60)
    c1 = Contact(["Nick", "J", "Mobley"], 8123357216, "njmobley@iu.edu", "12.11.1998")
    c2 = Contact(["Larry", "Gates"], 48138138, "gatesla@iu.edu", "15.04.1995")
    c3 = Contact(
        ["Sup", "a", "man"], 8541836418, "callsuper@dailyplanet.org", "15.4.1903"
    )
    c4 = Contact(
        ["This", "Little", "Name"], 123456789, "smollName@littleworld.com", "18.05.1955"
    )
    contactList = [c1, c2, c3, c4]
    print("Testing getName")
    print("-" * 60)
    print("Expected Results")
    print("Nick J Mobley")
    print("Larry Gates")
    print("Sup a man")
    print("This Little Name")
    print("Your Results ~~~~~~~~~~~~~~~~~~~~")
    print(c1.getName())
    print(c2.getName())
    print(c3.getName())
    print(c4.getName())
    print("-" * 60)
    print("Testing __str__")
    print("-" * 60)
    print("Expected Results")
    print("Contact: Nick J Mobley - (8123357216)")
    print("Contact: Larry Gates - (48138138)")
    print("Contact: Sup a man - (8541836418)")
    print("Contact: This Little Name - (123456789)")
    print("Your Results ~~~~~~~~~~~~~~~~~~~")
    print(c1)
    print(c2)
    print(c3)
    print(c4)
    print("-" * 60)
    print("Testing call")
    print("-" * 60)
    print("Expected Results")
    print("Expected Results")
    print("Dialing Nick ...")
    print("Dialing Larry ...")
    print("Dialing sup ...")
    print("Dialing This ...")
    print("Your Results")
    c1.call()
    c2.call()
    c3.call()
    c4.call()
    print("-" * 60)
    print("Testing sendBirthdayText")
    print("-" * 60)
    print("Expected Results")
    print("To Nick:")
    print("\tHappy Birthday Nick!")
    print("To Larry:")
    print("\tHappy Birthday Larry!")
    print("To Sup")
    print("\tHappy Birthday Sup!")
    print("To Little:")
    print("\tHappy Birthday Little!")
    print("Your Reuslts:")
    c1.sendBirthdayText()
    c2.sendBirthdayText()
    c3.sendBirthdayText()
    c4.sendBirthdayText()
    print("-" * 60)
    print("Testing updateNumber")
    print("-" * 60)
    print("Expected Results")
    c1.updateNumber(48128546)
    c2.updateNumber(48126879)
    c3.updateNumber(48430546)
    c4.updateNumber(26979487)
    print("Contact: Nick J Mobley - (48128546)")
    print("Contact: Larry Gates - (48126879)")
    print("Contact: Sup a man - (48430546)")
    print("Contact: This Little Name - (26979487)")
    print("Your Results ~~~~~~~~~~~~~~~~~~~")
    print(c1)
    print(c2)
    print(c3)
    print(c4)

    ########################################################################
    # Testing Phonebook
    ########################################################################
    print("~" * 60)
    print("{:^60}".format("Testing PhoneBook Class"))
    print("~" * 60)
    PB = PhoneBook()  # Initializes a instance of the class PhoneBook

    print("Testing get_all_contacts (addContact)")
    get_all_contacts(PB)
    # We do not need to return the PhoneBook instance because
    #   we are modifying the variable in memory

    print()
    print(PB)

    print()
    print("-" * 30)
    print("Testing addContact with a dictionary")
    tempD = {
        "name": ["Nick", "J", "Mobley"],
        "number": 8123357216,
        "email": "njmobley@iu.edu",
        "birthday": "12.11.1998",
    }
    PB.addContact(tempD)
    for con in PB.contactList:
        print("\t", con)

    print()
    print("-" * 30)
    print("Testing getContactCount (result should be 5)")
    print("\t", PB.getContactCount(), PB.getContactCount() == 5)

    print()
    print("-" * 30)
    print("Testing findContact")
    print("\tLooking for `{}` and found {}".format("Mobley", PB.findContact("Mobley")))
    print("\tLooking for `{}` and found {}".format("Gate", PB.findContact("Gate")))

    print()
    print("-" * 30)
    print("Testing groupChat")
    groupMessage(PB)
