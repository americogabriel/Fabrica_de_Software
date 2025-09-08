def gerarerro():
    raise  Exception("Deu erro de zero")

try:
    gerarerro()
except Exception as erro:
    print(erro)
finally:
    print("Terminou")
    

