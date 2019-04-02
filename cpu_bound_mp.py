#!/usr/bin/env python3
import multiprocessing
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
    """utilise une pool de processus pour effectuer en parrallèle
    sur plusieurs CPU la fonction CPU bound
    
    :param numbers: liste d'entier
    :type numbers: list
    """

    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
print(f"Duration {duration} seconds")