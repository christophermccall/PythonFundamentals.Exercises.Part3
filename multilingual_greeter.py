language_list = [
	'English',
	'Spanish',
	'French'
]

name_prompt_list = [
	'What is your name?'+'\n',
	'¿Cómo te llamas?'+'\n',
	'Comment t\'appelles-tu?'+'\n',
]

greeting_list =[
	'Hi There,',
	'¡Hola,',
	'Bonjour,'
]


def menu():
	for lang in language_list:
		print(f'{language_list.index(lang)+1}: {lang}')


def language_input():
	choice = input("Please select a language: ")
	return int(choice)-1


def ask_name(language_choice):
	for prompt in name_prompt_list:
		if language_choice == name_prompt_list.index(prompt):
			return input(prompt)


def greet(language_choice, user_name):
	for greeting in greeting_list:
		if language_choice == greeting_list.index(greeting):
			print(f'{greeting} {user_name}!')
			break


menu()
choice = language_input()
name = ask_name(choice)
greet(choice, name)

# def name_input():
# 	name = input("please enter your name:")
# 	return name
# greet(name_input())
