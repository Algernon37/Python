import View 
import Model
import Text

def start():
    while True:
        choice = View.main_menu()
        match choice:
            case 1:
                Model.open_pb()
                View.print_message(Text.load_successful)
            case 2:
                Model.save_pb()
                View.print_message(Text.save_successful)
            case 3:
                pb = Model.get_pb()
                View.print_contact(pb,Text.load_error)
            case 4:
                contact = View.input_contact(Text.new_contact, Text.cancel_input )
                name = Model.add_contact(contact)
                View.print_message(Text.new_contact_sucessful(name))
            case 5:
                contact = View.input_contact(Text.input_contact, Text.cancel_input)
                name = Model.find_contact(contact)
                View.print_message(Text.find_contact(name))
            case 6:
                index = View.input_index(Text.index_modify_contact, pb, Text.load_error)
                contact = View.input_contact(Text.input_contact, Text.cancel_input)
                name = Model.modify_contact(index, contact)
                View.print_message(Text.modify_contact(name))
            case 7:
                pb = Model.get_pb()
                index = View.input_index(Text.index_del_contact, pb, Text.load_error)
                name = Model.del_contact(index)
                View.print_message(Text.del_contact(name))
            case 8:
                break