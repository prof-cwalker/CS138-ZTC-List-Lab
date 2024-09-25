'''
DEVELOPER: Sara Solano
COLLABORATOR(S): Catherine Walker
'''
""" This program is to create 10 Loteria tabla and to call out Loteria card names.
"""
##### IMPORTS #####
import random 

##### FUNCTION DEFINITIONS #####
def create_list_from_file(file_name):
  '''Generates a cleaned list of items from the given file. Format of file should be number, item_name.'''
  list = open(file_name).readlines()
  name_list = []
  for i in range(0,len(list)):
    temp = list[i].split(",")
    name_list.append(temp[1].strip())
  return name_list

def make_tabla(list_of_items, output_name):
  '''Generates a 4x4 game tabla of distinct random elements of the given list. Writes the tabla to given file name.'''
  tabla = random.sample(list_of_items, 16)
  with open(output_name, 'w') as f:
    f.write("-"*93 + "\n")
    for i in range(0,4):
      f.write(f"| {'':20} | {'':20} | {'':20} | {'':20} |\n")
      f.write(f"| {tabla[i]:20} | {tabla[i+4]:20} | {tabla[i+8]:20} | {tabla[i+12]:20} |\n")
      f.write(f"| {'':20} | {'':20} | {'':20} | {'':20} |\n")
      f.write("-"*93 + "\n")

#def replace_offensive_cards(cards):
    
    
def play_game(loteria_cards):
    random.shuffle(loteria_cards)
    i = 0
    while i<len(loteria_cards):
        print("The Loteria card selected is:", loteria_cards[i])
        another_card = input("Would you like to call another card?(Y for yes and N for no): ").upper()
        if another_card[0] == "N":
            print("Thank you have a good day!")
            break
        i = i+1
    print("That's the end of the deck.")


##### MAIN PROGRAM #####
def main():
  #call function to make list of Loteria names
  loteria_names = create_list_from_file("loteriaNames.csv")

  #replace problematic names
  
  #call functions to make tabla 10 times
  for i in range(1,11):
    make_tabla(loteria_names,"table"+str(i))

  #Select random name until user says to stop.
  play_game(loteria_names)
  

if __name__ == "__main__":
  main()


  

