import pyttsx3

engine = pyttsx3.init()
print("Welcome to PJ Bank")
account = input("What type of bank account do you operate?\n")
engine.say(f"You operate {account} account.")
engine.runAndWait()
pr = input("Are you satisfied with our services?\n")
if pr == "yes" or "yes" or "YES" or "Y":
    engine.say("Thank you.")
else:
    engine.say("How might we improve our services\n")
engine.runAndWait()
complain = input("How might we improve our services\n")
engine.say("Your input is very much appreciated.")
engine.runAndWait()
ask = input("Are there other things you will like to talk about?\n")
if ask == "y" or "yes" or "YES" or "Y":
    engine.say("Ok please input.")
else:
    engine.say("Your input is very much appreciated")
engine.runAndWait()
recommend = input("Would you recommend PJ Bank to your relatives and friends?\n")
if recommend == "y" or "yes" or "YES" or "Y":
    engine.say("Thanks for your thoughtfulness.")
else:
    engine.say("Your input is appreciated.")
engine.runAndWait()
accountBalance = int(input("Enter your token number.\n"))
engine.say(f"Is your token number?{accountBalance}")
engine.save_to_file(f"Is your token number {accountBalance}", "account.mp3")
engine.runAndWait()
print("Account Number: XXXXXXXX456\n"
      "Account Balance: $15450\n"
      "Number of Withdrawals from past month: 15\n"
      "Number of Withdrawals from past week: 5")
print("Thanks for banking with us.")