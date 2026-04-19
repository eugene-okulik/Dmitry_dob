text = """Etiam tincidunt neque erat, quis molestie enim imperdiet vel. 
          Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"""

list_word = text.split()
result = []
for i in list_word:
    if i[-1].isalpha():
        result.append(i + 'ing')
    elif i.endswith('.'):
        i = i[:-1]
        result.append(i + 'ing.')
    elif i.endswith(','):
        i = i[:-1]
        result.append(i + 'ing,')

print(' '.join(result))
