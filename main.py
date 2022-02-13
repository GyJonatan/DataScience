def happyBirthday(birthdays):
    # Wish happy birthday to those who celebrate it.
    for bd in birthdays:
        if bd[2]:
            print(f'Happy birthday {bd[0]}')


def duringSchool(birthdays):
    # Print the name of those whose birthday happens to be between sept-dec and jan-may
    for bd in birthdays:
        month = int(bd[1].split('/')[1])
        if month < 7 or month > 8:
            print(bd[0])


def kidsThatCelebrate(birthdays):
    # Print the name and the age (one star for each age) for those that celebrate their birthday
    # and happen to be 10 years old or younger.
    for bd in birthdays:
        if bd[2] and bd[3] < 11:
            print(f'{bd[0]}: {"*" * bd[3]} ({bd[3]})')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # columns: Name, day/month, doesCelebrate, age
    BIRTHDAYS = (
        ("James", "9/8", True, 9),
        ("Shawna", "12/6", True, 22),
        ("Amaya", "28/2", False, 8),
        ("Kamal", "29/4", True, 19),
        ("Sam", "16/7", False, 22),
        ("Xan", "14/3", False, 34))

    happyBirthday(BIRTHDAYS)
    duringSchool(BIRTHDAYS)
    kidsThatCelebrate(BIRTHDAYS)
