import time

def get_account_ids_to_run (account_ids_list, number_slices = 15, minute=0):

    account_ids_to_return = []

    len_list = len(account_ids_list)
    # create similar list, just indices
    index_list = list(range(len_list))

    if len_list > 0: # not empty list
        len_step = int(len_list/number_slices)
        if len_step > 0: # step size must be bigger than 0
            restante = len_list % number_slices
            #print("---- LEN STEP------")
            #print(len_step)
            index_list_indices = index_list[::len_step]
            #print("_____________________________________")
            #print("_________________SLICES______________")
            #print("_____________________________________")
            contador = 0
            for x in index_list:
                if x in index_list_indices:        
                    contador = contador + 1 ## cuantas veces 
                    if contador == number_slices:
                        lista_por_intervalo = account_ids_list[x:x+len_step+restante]
                        account_ids_to_return.append(lista_por_intervalo)
                        #print(lista_por_intervalo)
                        break
                    else:        
                        lista_por_intervalo = account_ids_list[x:x+len_step]
                        account_ids_to_return.append(lista_por_intervalo)
                        #print(lista_por_intervalo)
            return account_ids_to_return[minute]
                    #if len(lista_por_intervalo) > 0:                    
        else: # less than number of slices, returns all list
            account_ids_to_return = account_ids_list
    return account_ids_to_return

def wait_a_minute(minute=60):
    while True:
        print("This prints once a minute.")
        time.sleep(minute)
        break

if __name__ == "__main__":

    # settings
    number_list_example = 33 # size of example list
    every_x_minute = 15 # ever 15 minutes

    lista_example = [f'1{x:03}' for x in range(number_list_example)] # generates an example list
    print("............ original list example .....................")
    print(lista_example)
    print("............ answer .....................")
    for minute in range(15):         
        answer = get_account_ids_to_run(lista_example, every_x_minute, minute)
        print("minute {} .... answer {}".format(minute, answer))
        wait_a_minute()
