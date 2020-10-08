#guess the number game
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)
speak('welcome to the game   guess the number')
speak('you have 10 choices to guess the number')
speak('choose wisely ')
import random
print('you have entered the game\n'
      'you have a total of 10 guesses\n'
      'try your luck now\n')
n=random.randint(0,100)
guess=0
print('Enter a choice')
speak('Enter a choice')
while(guess<10):
    choice = int(input())
    if choice > n:
             print('the entered no. is greater\n')
             speak('the entered number is greater')
    elif choice < n:
             print('the entered no. is smaller\n')
             speak('the entered number is smaller')
    elif choice==n:
             print('CONGRATS you hve guessed the correct no.')
             speak('CONGRATS you hve guessed the correct number')
             print('you found in',guess+1,'guesses')
             # speak('you found in',guess+1,'guesses')
             break
    print('you have',9-guess,'no. of guesses left')
    print('enter your next choice')
    speak('enter your next choice')
    guess+=1
print('the correct number is', n)
if guess>9:
    print('LOSER')
    speak('LOSER')
    print('GAME OVER')
    speak('GAME OVER')
