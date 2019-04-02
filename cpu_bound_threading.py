#!/usr/bin/env python3
import concurrent.futures
import time


def cpu_bound(number):
    """un fonction simple qui fait la somme  des produits des nombres
    entre 0 et number-1  
    
    cette tache est très consommatrice de CPU 

    :param number: un entier pris dans la liste
    :type number: int
    :return: la somme des produits des nombres entre  
    :rtype: int
    """
    return sum(i * i for i in range(number))


def find_sums(numbers):
    """utilise une pool de thread pour effectuer en parrallèle 
    (mais sur un seul CPU) la fonction cpu_bound
    
    :param numbers: liste d'entier
    :type numbers: list
    """

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(cpu_bound, numbers)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
print(f"Duration {duration} seconds")