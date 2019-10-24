words_quantity = int(input())
vocabuler_list = []

count = 1
while count <= words_quantity:
    vocabuler = input().lower().split()
    count += 1
    vocabuler_list += vocabuler
      
string_quantity = int(input())

count2 = 1
full_words = []
while count <= string_quantity:
    words = input().lower().split()
    count2 += 1
    full_words += words
   
result_list = []
for x in vocabuler_list:
    while x in full_words:
        full_words.remove(x)
        full_words_without_repeat = set(full_words)

for i in full_words_without_repeat:
    print(i, sep='\n')