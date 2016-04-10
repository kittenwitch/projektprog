def dodawanie(a, b):
	print(a+b)

def get_info():
	print("program kalkulator. Autor: Kasia")

get_info()

try:	
	l1 = int(input())
	l2 = int(input())	
	print(dodawanie(l1, l2))
except:
	print("program zakonczyl sie nieoczekiwanym bledem")
	print("mozesz go zglosic pod adresem pomoc@autor.pl")
	

