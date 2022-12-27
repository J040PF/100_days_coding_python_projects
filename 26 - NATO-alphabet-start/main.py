import pandas

student_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
word = input('say a word\n').upper()
final = []

for x in word:
    bibli = [row.code for (index, row) in student_data_frame.iterrows() if row.letter == x]
    final.append(bibli[0])

print(final)
