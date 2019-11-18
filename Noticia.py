import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["noticia"]

def adicionar_noticia():
    titulo = input("Digite o titulo da noticia: ")
    autor = input("Digite o nome do autor da noticia: ")
    texto = input("Digite o corpo da noticia: ")
    
    
    mydict = {"titulo": titulo, "autor": autor, "texto": texto}
    
    mycol.insert_one(mydict)
    print("Inserido com sucesso!")
    exibirMenu()
    
def exibirMenu():
	print("1 - Cadastrar uma nova noticia")
	print("2 - Pesquisar noticia")
	print("3 - Editar noticia")
	print("4 - Excluir noticia")
	print("5 - Sair")
	opcao = int(input("Escolha uma opcao: "))
	return opcao
    
def listarNoticia():
    for x in mycol.find({},{"_id": 0, "titulo": 1, "autor": 1, "texto": 1}):
        print(x)
            
    print("Fim da lista!")
    exibirMenu()
    
def pesquisarNoticia():
   while  True:
       opcao = menuPesquisa()
       if opcao == 1:
           pesquisaTitulo()
       elif opcao == 2:
           quisaAutor()
       elif opcao == 3:
		   pesquisaTexto
       elif opcao == 4:
           listarNoticia()
	   elif opcao == 5:
		   exibirMenu()

def menuPesquisa():
    print("1 - Procurar pelo titulo")
	print("2 - Procurar pelo autor")
	print("3 - Procurar pelo texto")
    print("4 - Listar todas")
	print("5 - Voltar")
	opcao = int(input("Escolha uma opcao: "))
	return opcao

def pesquisaTitulo():
    keyword = input("Digite o titulo que esta procurando: ")
    myquery = {"titulo": keyword}
    
    mydoc = mycol.find(myquery)
    
    for x in mydoc:
        print(x)
     
    print("Fim da lista!")
    menuPesquisa()

def pesquisaAutor():
    keyword = input("Digite o autor que esta procurando: ")
    myquery = {"autor": keyword}
    
    mydoc = mycol.find(myquery)
    
    for x in mydoc:
        print(x)
     
    print("Fim da lista!")
    menuPesquisa()
    
def pesquisaTexto():
    keyword = input("Digite o texto que esta procurando: ")
    myquery = {"texto": keyword}
    
    mydoc = mycol.find(myquery)
    
    for x in mydoc:
        print(x)
     
    print("Fim da lista!")
    menuPesquisa() 
    
def deletarNoticia():
    keyword = input("Digite o titulo que deseja apagar: ")
    myquery = {"titulo": keyword}
    
    mycol.delete_one(myquery)
    print("Operação realizado com sucesso!")
    
def editarNoticiaTitulo():
   keyword = input("Digite o titulo que deseja editar: ")
   keywordEdit = input("Digite o novo titulo: ")
   
   myquery = {"titulo": keyword}
   newvalue = {"$set": {"titulo": keywordEdit}}
   
   mydoc.update_one(myquery, newvalue)
    
   for x in mydoc.find():
       print(x)
     
   print("Fim da lista!")
   menuPesquisa()
    
def editarNoticiaAutor():
   keyword = input("Digite o titulo que deseja editar: ")
   keywordEdit = input("Digite o novo autor: ")
   
   myquery = {"titulo": keyword}
   newvalue = {"$set": {"autor": keywordEdit}}
   
   mydoc.update_one(myquery, newvalue)
    
   for x in mydoc.find():
       print(x)
     
   print("Fim da lista!")
   menuPesquisa()

def editarNoticiaTexto():
   keyword = input("Digite o titulo que deseja editar: ")
   keywordEdit = input("Digite o novo texto: ")
   
   myquery = {"titulo": keyword}
   newvalue = {"$set": {"texto": keywordEdit}}
   
   mydoc.update_one(myquery, newvalue)
    
   for x in mydoc.find():
       print(x)
     
   print("Fim da lista!")
   menuPesquisa()
   
def menuEditar():
    print("1 - Editar o titulo")
	print("2 - Editar o autor")
	print("3 - Editar o texto")
    print("4 - Listar todas")
	print("5 - Voltar")
	opcao = int(input("Escolha uma opcao: "))
	return opcao
   
def editarNoticia():
   while  True:
       opcao = menuEditar()
       if opcao == 1:
           editarNoticiaTitulo()
        elif opcao == 2:
			editarNoticiaAutor()
		elif opcao == 3:
			editarNoticiaAutor
        elif opcao == 4:
            listarNoticia()
		elif opcao == 5:
			exibirMenu()

while  True:
		opcao = exibirMenu()
		if opcao == 1:
			inserirNoticia()
		elif opcao == 2:
			pesquisarNoticia()
		elif opcao == 3:
			editarNoticia()
		elif opcao == 4:
			deletarNoticia()
		elif opcao == 5:
			break