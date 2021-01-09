#!/usr/bin/python3
# coding: utf-8
        
def quicksort(lst):
  if len(lst) == 0:
    return lst
  pivot = lst[len(lst) // 2]
  # renvoie 3 listes composées des elts triés par rapport à l’elt pivot.
  left = [x for x in lst if x < pivot]
  middle = [x for x in lst if x == pivot]
  right = [x for x in lst if x > pivot]
  return quicksort(left) + middle + quicksort(right)


lst = [1, -7, 2, 4, 10, 3, -5, 9, 6, 8, 6, 0]
print (“Liste d’entiers relatifs avant le tri :”, lst)
print (“Liste d’entiers relatifs après le tri :”, quicksort(lst))

------------------------------------------------------------------- Analyse de la condition de récurrence -----------------------------------------------------------
L’élément, objet de la récurrence,  doit évoluer grâce aux traitements vers la condition qui permet de quitter la fonction récursive.
