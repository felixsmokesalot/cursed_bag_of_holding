import  random
import  pickle

bag = []

items = ["torch","log","stick","arrow","abacus","acid vial", "alchemist's Supplies","alexandrite","alms box", "amber",
        "amethyst","amulet","antitoxin","aquamarine","Bagpipes","bag of ball berings(1,000)","banded Agate","Barding",
         "basket","battleaxe","bedroll","bell","birdpipes","bit and  bridle","black opal","black pearl","black sap",
        "black sapphire","blanket","blasting powder","blight ichor","block and tackle","block of incense", "bloodstone",
        "blowgun","blowgun needles","blue quartz","blue sapphire","blue spinel","book","boomerang","boots","bottle,Glass",
        "breastplate","brewer's Supplies","bucket","burglar's pack","calligrapher's supplies","caltrops(bag of 20)",
        "candle","carnelian","canoe","carpenter's tools", "cartographer's tools","case, crossbow bolt","case, map or scroll",
        "censer","chain(10 feet)","chain mail","chain shirt","chalcedony","chalk","chrysoberyl","chysoprase","citrine","climber's kit",
        "common clothes","costume","fine clothes","travelers clothes","cold weather clothing","club","cobbler's tools","component pouch",
        "cook's utensils","coral","crampons","crawler mucus","crossbow bolts","hand crossbow","heavy crossbow","light crossbow",
        "crowbar","crystal","dagger","dart","diamond","dice set","diplomat's pack","disguise kit","dogsled","duble-bladed Scimitar",
        "dragonchess set","dragons blood","dreamlily","drow poison","drudic focus","drum","dulcimer","Dungeoneer's Pack",
         "dust of the mummy","eberron dragonshard","eblem","emerald","energy cell","entertainer's pack","explorer's pack","eye agate",
        "feed","fire opal","fishing tackle","flail","flask","tankard","flute","forgery kit","garnet","glaive","glaur","grappling hook",
        "glassblower's tools","greateaxe","greatclub","greatsword","handaxe","healer's kit","helm","hematite","herbalism kit","hide",
        "holy symbol","holy water(flask)","horn","hourglass","hunting tarp","ink(1 ounce bottle)","ink pen","insect repellent-incense",
        "insect repellent-salve","ivana's whisper","jacinth","jade","jasper","javelin","jet(gemstone)","jeweler's tools",
        "jug","khyber dragonshard","ladder(10 foot)","lamp","lance","bullseye lantern","hooded lantern","lapis lazuli","leather",
        "leatherworker's tools","light hammer","little bag of sand","lock","long bow","longhorn","longsword","lute","lyre"
        "mace","magnifying glass","malachite","manacles","mason's tools","maul","mess kit","steel mirror","monster hunters pack",
        "moonstone","morningstar","moss agate","Muroosa balm","navigator's tools","net","obsidian","oil","olisuba leaf","onyx","opal"
        "orb","padded light armor","painters supplies","pan flute","paper one sheet","parchment one sheet","pearl","perfume","miners pick",
        "pike","piton","plate armour","playing card set","poisoner's kit","pole(10 foot)","iron pot","potion of healing","potters tools",
        "pouch","pride silk","priest's pack","quarterstaff","quartz","quiver","rain catcher","portable ram","rapier","rations(1day)",
        "reliquary","rhodochrosite","ring mail","robes","rod","hempen rope(50 feet)","silk rope(50 feet)","ruby","exotic saddle",
        "military saddle","saddle pack","riding saddle","saddlebags","sardonyx","scale mail","merchant's scale","scholar's pack",
         "scimitar","sealing wax","shawn","shield","shorbow","short sword","shovel","siberys dragonshard","sickle","signal whistle",
        "signet ring","sling","sling bullets","small knife","smiths tools","snowshoes","soap","songhorn","soothsalts","spear","spellbook",
        "spiked armor","iron spikes(10)","spinel","splint","spy glass","staff","stake(wooden)","star rose quartz","star ruby","star sapphire",
        "string","studded leather armor","tantan","tej","two person tent","theki root","thelarr","theives tools","three-dragon ante set",
        "tiger eye","tinder box","tinker's tools","tocken","topaz","torch","totem","tourmaline","trident","truth serum","turqoise",
        "vestments","vial","viol","wand","war pick","wargong","warhammer","waterskin","weavers tools","whetstone","whip","whistle-stick",
        "willoshade oil","woodcarvers tools","wooden staff","yarting","yellow sapphire"," yew wand","yklwa","zircon","zulkoon","spoon","soap",
        "pipe tabbaco",]

tavern_items = ["wooden plate","fork","couldren","tankard","ladel", "wooden bowl","log","kindling","spoon","knife"]

general_store_items = ["rations","rope 10","grapling hook","map", "ball bearings(bag of 1,000","basket","bedroll","bell","blanket",
                        "book","Dice set","Dragonchess set","playing cards set","three-dragon ante set","Bagpipes","drum","dulcimer",
                        "flute","1 lb of wheat", "1 lb of flour","1 lb of salt","1 lb of iron","1 lb of copper","1 yd of canvas",
                        "1 sq yd of cotton cloth", "1 lb of ginger","1 lb of cinnamon","1 lb of pepper","1 lb of cloves","1 lb of silver",
                        "1 sq yd of silk","1 lb of saffron","1 lb of gold","1 lb of platinum","riding saddle","feed","sled","bit and bridle",]

church_items = ["cerimonial knife","urn(filled wiht remains)","urn(empty)"]

smith_items = ["anvil","hammer","tongs(black smith tool)","leather apron","bag of 5 rivets","course file","fine file","whetstone",
        "flint and steel","lump of coal","chisel","punch","strait-peen sledgehammer","double faced sledghammer","hand mandrel",
        "bolster plate","rake","shovel","poker"]


def save_current():
    with open("test_bag" , "wb") as f:
        pickle.dump(bag, f)

def load_bag():
    global bag
    with open("test_bag", 'rb') as f:
        bag = pickle.load(f)

        print("\n")
        print(bag)
        print("\n")

def current_bag():

    bag=load_bag()



def add_to_bag():
    bag.append(input("What do you want to add?\n"))
    save_current()
    print("\n")
    print(bag)
    print("\n")


def remove_from_bag():
    
    try:
        random.shuffle(bag)
        removed_object = bag.pop()
        save_current()

        print("\n"+removed_object+"\n")
        print("\n")
        print(bag)
        print("\n")
    except:

        print("\nNothing is in the Bag!\n")
        action_select()


def add_random_item():
    
    
    while True:

        random_item=input("\nWhere are you? tavern, general store, smith, church or none\n").lower()

        
        if random_item=="tavern":
            random.shuffle(tavern_items)
            selected_item = tavern_items.pop()
            duplicated_item = selected_item

            tavern_items.append(duplicated_item)
            bag.append(selected_item)
            save_current()

            print("\n")
            print(selected_item)
            print("\n")
            print(bag)
            print("\n")
            break

        elif random_item=="general store":
            random.shuffle(general_store_items)
            selected_item = general_store_items.pop()
            duplicated_item = selected_item

            general_store_items.append(duplicated_item)
            bag.append(selected_item)
            save_current()

            print("\n")
            print(selected_item)
            print("\n")
            print(bag)
            print("\n")
            break

        elif random_item=="smith":
            random.shuffle(smith_items)
            selected_item=smith_items.pop()
            duplicated_item=selected_item

            smith_items.append(duplicated_item)
            bag.append(selected_item)
            save_current()

            print("\n")
            print(selected_item)
            print("\n")
            print(bag)
            print("\n")
            break

        elif random_item=="church":
            random.shuffle(church_items)
            selected_item=church_items.pop()
            duplicated_item=selected_item

            church_items.append(duplicated_item)
            bag.append(selected_item)
            save_current()


            print("\n")
            print(selected_item)
            print("\n")
            print(bag)
            print("\n")
            break 


        else:
            random.shuffle(items)
            selected_item = items.pop()
            duplicated_item = selected_item

            items.append(duplicated_item)
            bag.append(selected_item)
            save_current()

            print("\n")
            print(selected_item)
            print("\n")
            print(bag)
            print("\n")
            break

def starting_bag():

    while len(bag) <= 20:
        random.shuffle(items)
        selected_item = items.pop()
        duplicated_item = selected_item

        items.append(duplicated_item)
        bag.append(selected_item)
        save_current()

    else:
        print("\n")
        print(bag)
        print("\n")


def start_new_game():
    while True:

        a = input("would you like to start a new bag?")


        if a =="yes":
            starting_bag()

            break

        elif a == "no":
            load_bag()

            break


def action_select():
    while True:

        choice = input("What would you like to do? \n add item \n remove item \n add random item \n exit game\n\n")

        if choice == "add item":
            add_to_bag()

        elif choice == "remove item":
            remove_from_bag()

        elif choice == "add random item":

            add_random_item()

        elif choice == "exit game":
            quit()

        else:
            print("\n wrong selection try again\n")

       
def run_program():

    while True:

        start_new_game()

        action_select()

run_program()
