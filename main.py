#функции и аргументы с перевернутой расстановкой переменных
def greet(name, name_2):
	print("Hello!")
	print("my")
	print(f"Niggaz {name} {name_2}")

greet("Eric", "Gangster")

def greet_with(name_with, location):
	print(f"Hello {name_with}")
	print(f"What is it in {location}?")

greet_with(location="Tosno", name_with="Eric")