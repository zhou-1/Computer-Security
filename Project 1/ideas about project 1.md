# challenge 3 and 5
challenges here are binary files with only English characters <br/>
we can use CAESAR method with ceasar.py <br/>
After decoding, we find the results here are format of English characters  

# challenge 1 and 2
There are steps we followed to decode  
step 1: Find the coincidence of each displacement (like how mant times value of the first displacement appear in whole text)  
step 2: Create a curve graph for each displacement and coincidence of each displacement  
step 3: Find the high point in the graph, figure out the relationship between them (find any multiple of a number, like displacement 13, 26, 39, 52....)   
step 4: That basic number (i.e. 13 mentioned in step 13) is the key length  
step 5: <b> guess step </b> Use XOR method with Xor.py to do following thing: cyper text (after encode) XOR key to get the password
Since e is the most frequent one in English, space (" ") is the most frequent one in all plain text/original text with not only English
we then use space here to XOR cyper text in keylength place (i.e. first, 14th, 27th, 40th, 53rd....) since first character of key is same
Then we get password  
step 6: Use XOR method with Xor.py to XOR password and whole cyper text to get plain text/original text (before encode)

*encode process in challenge 1 2 3 and 5 only shift certain places of each letter/character (like A ☞ B， B ☞ C， C ☞ D....)
*will be "easier" than the last one
*challenge 4 is the last one which is more difficult since encode process here will shift random places of each letter/character
(like A ☞ C, B ☞ F, C ☞ J, D ☞ P....)
*we need to detect each number for different letter

# challenge 4
random number generator <br/>
need to figure out how it works  <br/>
and find out each number ?   <br/>
