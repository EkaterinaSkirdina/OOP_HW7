from model.Bottle_Water import Bottle_Water
from model.Hot_Drinks import Hot_Drinks
from model.Vending_Machine import Vending_Machine
from view.User_Interface import User_Interface


class Controller:

    def start(self):
        console = User_Interface
        bottle_list = [Bottle_Water("Cola", 150, 0.5),
                       Bottle_Water("Sprite", 150, 0.5),
                       Bottle_Water("Fanta", 150, 0.5),
                       Bottle_Water("Bon-Aqua", 100, 0.5)]
        vending_machine_bottle = Vending_Machine
        vending_machine_bottle.all_products = bottle_list
        console.print_message ('-------------Бутилированные напитки----------------')
        console.print_all_product(bottle_list)
        console.print_message(vending_machine_bottle.get_product('Cola', 0.5))

        hot_drinks_list = [Hot_Drinks("Coffee", 200, 0.3),
                        Hot_Drinks("Tea", 100, 0.3),
                        Hot_Drinks("Cacao", 150, 0.4),
                        Hot_Drinks("Milk", 100, 0.5)]        
        vm_hot_drinks = Vending_Machine
        vm_hot_drinks.all_products = hot_drinks_list
        console.print_message('----------------Горячие напитки------------------')
        console.print_all_product(vm_hot_drinks)
        console.print_message(vm_hot_drinks.get_product('Tea', 0.3))

