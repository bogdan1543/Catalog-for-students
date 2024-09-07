def bubble_sort(the_list,key=lambda x: x,cmp=lambda x,y: x>y,reverse=False):
    """
    Functie de sortare folosind metoda bulelor cu complexitate O(n^2)
    :param the_list: lista de sortat
    :param key: cheia dupa care se sorteaza
    :param cmp: functia de comparare
    :param reverse: 1 sau 0 daca sirul sa fie invers sau nu
    :return: lista sortata
    """
    ok=False
    while not ok:
        ok=True
        for index in range(len(the_list)-1):
            if cmp(key(the_list[index]),key(the_list[index+1])):
                the_list[index],the_list[index+1]=the_list[index+1],the_list[index]
                ok=False

    if reverse:
        the_list.reverse()

    return the_list

def shell_sort(the_list,key=lambda x: x,cmp=lambda x,y: x>y,reverse=False):
    """
    Functie de sortare folosind metoda bulelor cu complexitate O(n^2)
    :param the_list: lista de sortat
    :param key: cheia dupa care se sorteaza
    :param cmp: functia de comparare
    :param reverse: 1 sau 0 daca sirul sa fie invers sau nu
    :return: lista sortata
    """
    n=len(the_list)
    gap=n//2

    while gap>0:
        for index in range(gap,n):
            temp=the_list[index]

            ad_index=index
            while ad_index>=gap and cmp(key(the_list[ad_index-gap]),key(temp)):
                the_list[ad_index]=the_list[ad_index-gap]
                ad_index-=gap
            the_list[ad_index]=temp

        gap//=2

    if reverse:
        the_list.reverse()

    return the_list