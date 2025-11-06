text_input = input('Enter a word:')

isPalendrome = True

if ((len(text_input) % 2) == 0):
    max_range = len(text_input) / 2
else:
    max_range = round(len(text_input) / 2) - 1
    
max_range = int(max_range)
    
for i in range(0, max_range + 1):
    if (text_input[i] != text_input[-1 -i]):
        isPalendrome = False
        break
    
print(f"Word is palendrome? {isPalendrome}")