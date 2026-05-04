with open("story.txt", 'r') as f:
    story = f.read()

words = set()
start_before_word = -1

start_index = '<'
end_index = '>'

for i, char in enumerate(story):
    if char == start_index:
        start_before_word = i    # position of

    if char == end_index and start_before_word != -1:
        word = story[start_before_word: i+1]     # position of >
        words.add(word)
        start_before_word = -1

answers = {}

for word in words:
    answer = input(f"Enter the word for :{word}")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])


print(story)
