secret_word="snake"
guess=""
guess_count=0
guess_limit=3
out_of_guesses=False

# while (guess !=secret_word):
#  guess=input("enter guess: ")
#  guess_count +=1
#  if(guess==secret_word):
#    print("congratulation! you won")
#  else:
#    print("sorry you lost!").
while(guess!=secret_word and not(out_of_guesses)):
    if guess_count< guess_limit:
        guess=input("enter guess: ")
        guess_count+=1
    else:
        out_of_guesses=True
if out_of_guesses:
    print("out of guesses,you lose!")
else:
    print("you win!")