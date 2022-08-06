COIN_TYPES = []
coin_data = []
last_coin_id = 1

def set_year():
    print('Please enter the coin year: ')
    coin_data.append(input())

def add_type():
    print('Enter new coin type: ')
    id = len(COIN_TYPES) + 1
    new_type = str(id)+ ': ' + input()
    COIN_TYPES.append(new_type)
    with open("./database/coin_types.txt", "a") as f:
        f.write("\n'" + new_type+"'")
        f.close()

def set_type():
    print('Please select the Coin Type('+ str(COIN_TYPES) + ' or N for New Coin' +'): ')
    user_input = input()
    if user_input == 'N':
        add_type()
        coin_data.append(COIN_TYPES[-1])
    else:
        coin_type = int(user_input)
        coin_data.append(COIN_TYPES[coin_type])       
    

    set_year()

def setup_product():
    coin_data.clear()
    set_type()

def setup():
    with open("./database/coin_types.txt", "r") as f:
        for type in f.readlines():
            COIN_TYPES.append(type.replace("'", '').replace('\n', ''))
        f.close()

setup()

while True:
    setup_product()
    print("You want to add " + coin_data[0] + " from " + coin_data[1] + " is that correct? (Y/N)")
    if input() == 'y' or input() == 'Y':
        with open("./database/coins.csv", "r+") as f:
            last_coin_id = len(f.readlines())
            id = last_coin_id
            f.write(str(id) +', '+ str(coin_data[0]) + ', ' +  str(coin_data[1]) + ', ' + 'N/A\n')
            f.close()
        print('Coin '+ str(id) +' successfully added!\n\n')
    else:
        setup_product()