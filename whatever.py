def capital_indexes(word):
 char_list = []
 for index, x in enumerate(word):
   if x.isupper():
     char_list.append(index) 
   print (char_list)
a = 'hElLo'
capital_indexes(a)
