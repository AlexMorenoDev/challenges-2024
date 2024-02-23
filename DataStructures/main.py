"""
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 * - También se debe proponer una operación de finalización del programa.
"""

class Contact:
    def __init__(self, name, phone_num):
        self.name = name
        self.phone_num = phone_num

    def __str__(self):
        return f"{self.name} - {self.phone_num}"


def insert_contact(new_contact: Contact, contact_list: list):
    for contact in contact_list:
        if contact.phone_num == new_contact.phone_num:
            print("ERROR: A contact with that phone number already exists!")
            return
    contact_list.append(new_contact)
    print("INFO: Contact inserted successfully!")


def update_contact(contact_id: int, contact_list: list, new_name: str, new_phone_num: str):
    if new_name or new_phone_num:
        index = contact_id - 1
        if new_name:
            contact_list[index].name = new_name
        if new_phone_num:
            contact_list[index].phone_num = new_phone_num
        print("INFO: Contact updated successfully!")


def delete_contact(contact_id: int, contact_list: list):
    try:
        contact_list.remove(contact_list[contact_id-1])
        print("INFO: Contact deleted successfully!")
    except ValueError:
        print("ERROR: Target contact to delete doesn´t exist")


def search_contact(contact_list: list, target_name: str, target_phone_num: str):
    found_contacts = []

    if not target_name and not target_phone_num:
        return found_contacts

    for contact in contact_list:
        # if case: both filters are used (name and phone number). Else case: only one of them is used
        if target_name and target_phone_num:
            if contact.name == target_name and contact.phone_num == target_phone_num:
                found_contacts.append(contact)
                # Two contacts with the same phone number cannot exist, so it is not necessary to carry on searching
                break
        else:
            if contact.name == target_name or contact.phone_num == target_phone_num:
                found_contacts.append(contact)
                if target_phone_num:
                    # It cannot exist two contacts with the same phone number, so it is not necessary to carry on searching
                    break

    return found_contacts


def show_contacts(contact_list: list):
    print("--------------------------------")
    if len(contact_list) > 0:
        for i, contact in enumerate(contact_list):
            print(f"{i+1}. {contact.name} - {contact.phone_num}")
    else:
        print("EMPTY LIST")
    print("--------------------------------")


def is_valid_phone_num(phone_num: str, required: bool):
    if phone_num:
        length = 0
        try:
            for char in phone_num:
                int(char)
                length += 1
        except ValueError:
            print("ERROR: Entered phone number must only contain digits")
            return False
        
        if length > 11:
            print("ERROR: Entered phone number length cannot be greater than 11")
            return False
    else:
        if required:
            print("ERROR: Phone number is empty and it is required to create a new contact")
            return False
    
    return True


def input_name_and_phone(input_name_msg: str, input_phone_msg: str, data_required: bool):
    while True:
        new_name = input(input_name_msg)
        if new_name or (not new_name and not data_required):
            break
        print("ERROR: Name is empty and it is required to create a new contact")
        
    while True:
        new_phone_num = input(input_phone_msg)
        if is_valid_phone_num(new_phone_num, data_required):
            break
                
    return new_name, new_phone_num


def input_number(input_number_msg, start: int, end: int):
    while True:
        try:
            input_number = int(input(input_number_msg))
            if input_number < start or input_number > end:
                if start != end:
                    print(f"ERROR: Entered value must be a number between {start} and {end}")
                else:
                    print(f"ERROR: Entered value must be {start}, because only one contact is registered")
            else:
                break
        except ValueError:
            print("ERROR: Entered value must be a number")

    return input_number


def main():
    contact_list = []
    
    while True:
        print("CONTACT LIST")
        print("--------------------------------")
        print("Options:")
        print("\t1. Add new contact")
        print("\t2. Update existing contact")
        print("\t3. Delete existing contact")
        print("\t4. Search a contact")
        print("\t5. Exit")
        
        contact_list_length = len(contact_list)
        option = input_number("Select an option (1-5): ", 1, 5)
        match option:
            case 1:
                new_name, new_phone_num = input_name_and_phone("Enter contact name: ", "Enter contact phone number (max. 11 digits): ", True)
                insert_contact(Contact(new_name, new_phone_num), contact_list)
            case 2:
                show_contacts(contact_list)
                if contact_list_length > 0:
                    contact_id = input_number("Select a contact to update entering its id: ", 1, contact_list_length)
                    print("NOTE: If you don't want to update a specific field, leave it empty and press ENTER")
                    new_name, new_phone_num = input_name_and_phone("Enter contact new name: ", "Enter contact new phone number (max. 11 digits): ", False)
                    update_contact(contact_id, contact_list, new_name, new_phone_num)
            case 3:
                show_contacts(contact_list)
                if contact_list_length > 0:
                    contact_id = input_number("Select a contact to delete entering its id: ", 1, contact_list_length)
                    delete_contact(contact_id, contact_list)
            case 4:
                if contact_list_length > 0:
                    name_filter, phone_num_filter = input_name_and_phone("Enter name to search: ", "Enter phone number to search (max. 11 digits): ", False)
                    if name_filter == "":
                        name_filter = None
                    if phone_num_filter == "":
                        phone_num_filter = None
                    matching_contacts = search_contact(contact_list, name_filter, phone_num_filter)
                    show_contacts(matching_contacts)
            case 5:
                print("Finishing program...")
                break
        
        if len(contact_list) == 0:
            print("INFO: There are not any contacts registered. Before updating, deleting or searching contacts, at least one should be added to the list")
        input("Press ENTER to continue...")


if __name__ == "__main__":
    main()