
import re

def string_separator(word:str):
   
   word_list = re.findall('[a-zA-Z][^A-Z]*', word)
   my_list =[] 
   
   for val in word_list:
      val = val.lower()
      my_list.append(val)
   return my_list

words = "helloWorldThere"
if type(words) == str:
   wrod_list= string_separator(words)
   print(' '.join(wrod_list))
else:
   print("try again! parameter is not string ")
   
