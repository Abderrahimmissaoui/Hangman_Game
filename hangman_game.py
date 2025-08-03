import random
hangman_stages=['''
  +---+
      |
      |
      |
      |
      |
=========
'''
,
'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
, 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
'''  
,  
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
'''
, 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''
,
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''
, 
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''
, 
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]  

words=["good", "bad", "ugly", "sad", 'moon']
random_word=random.choice(words)
display=["_"]*len(random_word)
print("\n\nTERMINAL\n")
print(' '.join(display),"\n")
print(hangman_stages[0])

lives=6
guessed_letters=[]

while "_" in display and lives>0:
  guessed=input("\nPlease guess a letter: ")
  if guessed in guessed_letters:
    print("\nYou already guessed that. Please try again. ")
    print(f"\nYou have {lives} more lives.")
    continue

  guessed_letters.append(guessed)

  if guessed not in random_word:
    lives-=1
    print(hangman_stages[6-lives])
    print(' '.join(display),"\n")
    print(f"You have {lives} more tries.")
  else:
    for position in range(len(random_word)):
      if random_word[position]==guessed:
        display[position]=guessed
    print(' '.join(display),"\n")
    print(f"You have {lives} more tries.")

if lives==0:
  print("\n\n****** YOU LOSE ******")
  print(hangman_stages[-1])
else:
  print("\n\n****** YOU WIN ******\n\n  ")
      
       
      
  