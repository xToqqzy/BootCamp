# Add a contact with first name and last name (only alphabet), multiple (unique) e-mails (containing at least one '@'), multiple (unique) phone numbers.
# Also, an ID should be generated which should be 1 higher than the highest current ID.
# Remove a contact by ID.
# List all contacts sorted by first_name in descending order.
# Merge duplicate contacts (when choosing [M] Merge contacts). Contacts with the exact same full name (first and last name combined) should be merged.
# The e-mails and phone numbers of the duplicate contacts should be added to the the first duplicate contact (contact with the highest ID).
# The other duplicate contcts should be deleted from the addressbook.
# Contacts are read from the provided JSON file and should be updated with new or removed contacts.


def contacts(contacts, term):
    for contact in contacts:
        if term in contact['FirstName'] or term in contact['LastName'] or term in contact['Emails'] or term in contact['Phonenumbers']:
            return True
    return False


def main():
    while True:
        action = input(
            "[A] Add contact\n[L] Contact List\n[M] Merge contacts \n[R] Remove contacts\n")
