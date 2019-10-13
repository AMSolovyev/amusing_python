words = input('Input text')
words = words.lower()

i = 0
quantity = 0
result = {i: quantity}
while i == len(words):
    for i in words:
        if words[i] == words[i + 1]:
            quantity += 1
            result[i].append(quantity)
        elif words[i] != words[i + 1]:
            quantity = 1
            result[i].append(quantity)
        i += 1
print(result)


if __name__ == '__main__':
    data = 'Editors, who receive no royalties or expenses \
     and who are only very rarely commissioned by the Society, \
      are encouraged to approach the Editorial Secretary with  \
      a detailed proposal of the text they wish to suggest to  \
      the Society early in their work; interest may be expressed \
       at that point, but before any text is accepted for publication  \
       the final typescript must be approved by the Council  \
       (a body of some twenty scholars), and then assigned a place  \
       in the printing schedule. The Society now has a stylesheet  \
       to guide editors in the layout and conventions acceptable within \
        its series. No prescriptive set of editorial principles is laid  \
        down, but it is usually expected that the evidence of all relevant \
         medieval copies of the text in question will have been  \
         considered, and that the texts edited will be complete whatever  \
         their length. Editions are directed at a scholarly readership  \
         rather than a popular one; though they normally provide a glossary \
          and notes, no translation is provided.'
    print(result)
