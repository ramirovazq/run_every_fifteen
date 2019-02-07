import time

def get_account_ids_to_run (account_ids_list, number_slices = 15, minute=0):

    account_ids_to_return = []
    len_list = len(account_ids_list)

    # create copy of account_ids_list
    ids_copy = account_ids_list.copy()

    answer_list = [[] for x in range(number_slices)] # [[],[],[],[]] lenght of number_slices

    while len(ids_copy) > 0:
        for x in range(number_slices):
            try:
                value = ids_copy.pop()
                answer_list[x].append(value)            
            except IndexError:
                break

    # this lists shows how many alements per item
    list_index  = [len(y) for y in answer_list]

    initial_index = 0
    for z in list_index:
        end = initial_index + z
        account_ids_to_return.append(account_ids_list[initial_index:end])
        initial_index = end

    return account_ids_to_return[minute]



def wait_a_minute(minute=60):
    while True:
        time.sleep(minute)
        break

if __name__ == "__main__":

    # settings
    number_list_example = 25 # size of example list
    fifteen_slices = 15 # ever 15 minutes

    example_list = [f'2{x:03}' for x in range(number_list_example)] # generates an example list
    print("............ example list .....................")
    print(example_list)
    print("............ original Lenght of example list ..............")
    print(len(example_list))
    print("............ answer .....................")
    while True: # always working, run as a deamon for better results
        for minute in range(fifteen_slices):         
            answer = get_account_ids_to_run(example_list, fifteen_slices, minute)
            print("minute {} .... answer {}".format(minute, answer))
            wait_a_minute(1)# wait_a_minute() a minute
