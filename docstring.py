def fat (n):
    
    ##Docstring 3 aspas("") e depois disso chama o help
    """fatorial de n n é número inteiro """
    if (n ==1):
        return 1
    return (n*fat(n-1))

help(fat)
