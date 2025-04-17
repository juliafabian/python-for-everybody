# Schreibe eine Funtion namens remove_all, die eine Liste und einen Wert entgegennimmt 
# und alle Vorkommen des Wertes aus der Liste entfernt
# Die Funktion soll die Liste in-place verändern und als Ergebnis None zurückgeben

# my try: def remove_all(lst, object):
    
#     for i in lst:
#         if object in lst:
#             lst.remove(object)
#     return lst

# Ahmeds correction:        
def remove_all(lst, object):
    while object in lst:
        lst.remove(object)
    return lst


    
test_lst = ['a', 'b', 'c', 'b', 'd', 'e', 'b']
remove_all(test_lst, 'b')
print(test_lst)

fruit = ['banana', 'apple', 'banana', 'kiwi', 'banana', 'pineapple']
remove_all(fruit, 'banana')
print(fruit)