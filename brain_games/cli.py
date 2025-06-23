def welcome_user():
    print("Welcome to the Brain Games!")
    import prompt
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!") 
