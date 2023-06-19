turmas = {}
alunos = {}
professores = {}
import json


def menu_principal():
    print(" ")
    print('{:=^40}'.format(' Gestão de turmas '))
    print('-' *40)
    print('''
    [ 1 ] Menu coordenador
    [ 2 ] Menu professor
    [ 3 ] Menu aluno
    [ 0 ] Sair''')
    print(" ") 

def menu_coordenador():
    print(" ")
    print('{:=^40}'.format(' Gestão do coordenador '))
    print('-' *40)
    print('''
    [ 1 ] Criar turma
    [ 2 ] Editar turma
    [ 3 ] Visualizar turma
    [ 4 ] Apagar turma
    [ 0 ] Sair''')
    print(" ")

def menu_professor():
    print(" ")
    print('{:=^40}'.format(' Gestão do professor '))
    print('-' *40)
    print('''
    [ 1 ] Cadastrar professor
    [ 2 ] Editar dados do professor
    [ 3 ] Visualizar professor cadastrado
    [ 4 ] Excluir professor
    [ 5 ] Visualização de turmas
    [ 6 ] Visualização de alunos
    [ 0 ] Sair''')
    print(" ")

def menu_aluno():
    print(" ")
    print('{:=^40}'.format(' Gestão do aluno '))
    print('-' *40)
    print('''
    [ 1 ] Cadastrar aluno
    [ 2 ]  Editar alunos
    [ 3 ] Visualizar aluno
    [ 4 ] Apagar aluno
    [ 0 ] Sair''')
    print(" ")

def cadastrar_turma(turmas, professores, alunos):
    disciplina = input("Digite o nome da disciplina (turma): ")
    if disciplina in turmas:
        print("A turma já existe")
    else:
        print("Professores disponíveis:")
        for matricula, nome in professores.items():
            print(f"Matrícula: {matricula} | Nome: {nome}")
        matricula_professor = int(input("Digite a matrícula do professor da turma: "))
        if matricula_professor not in professores:
            print("Professor não encontrado")
        else:
            print("Alunos disponíveis:")
            for matricula, nome in alunos.items():
                print(f"Matrícula: {matricula} | Nome: {nome}")
            alunos_turma = input("Digite as matrículas dos alunos da turma: ").split(" ")
            alunos_turma = [matricula.strip() for matricula in alunos_turma]
            alunos_turma = [matricula for matricula in alunos_turma if matricula in alunos]
            if alunos_turma:
                turmas[disciplina] = matricula_professor
                print(f"Turma de {disciplina} criada com sucesso")
                return turmas, professores, alunos
                
            else:
                print("Nenhum aluno válido selecionado")
        
def cadastrar_aluno(alunos):
    nome_aluno = input("Digite o nome do aluno: ")
    if nome_aluno.isnumeric() or nome_aluno == "" or nome_aluno == " ":
        print("Nome Inválido, espaços em branco ou números não são permitidos!")
    else:
        nome_composto = nome_aluno.split()
        if len(nome_composto) < 2:
            print("Nome invalido! O nome precisa ser composto.")
        else: 
            matricula = len(alunos)
            alunos[matricula] = nome_aluno
            print(f"O aluno {nome_aluno} cadastrado com sucesso, sua matrícula é {matricula}")
            return alunos

def cadastrar_professor(professores):
    nome = input("Digite o nome do professor: ")
    if nome.isnumeric() or nome == "":
        print("Números ou espaços em branco são inválidos.")
    else:
        nome_composto = nome.split()
        if len(nome_composto) < 2:
            print(" ")
            print("Nome inválido, ele deve ser nome composto.")
        else:
            matricula = len(professores)
            professores[matricula] = nome
            print(" ")
            print(f"Professor {nome} cadastrado com matrícula {matricula}")
            return professores

def editar_turma(turmas, professores, alunos):
    disciplina = int(input("Digite o nome da disciplina (turma) que deseja editar: "))
    if disciplina in turmas:
        print("Professores disponíveis:")
        for matricula, nome in professores.items():
            print(f"Matrícula: {matricula} | Nome: {nome}")
        matricula_professor = input("Digite a nova matrícula do professor da turma: ")
        if matricula_professor in professores:
            print("Alunos disponíveis:")
            for matricula, nome in alunos.items():
                print(f"Matrícula: {matricula} | Nome: {nome}")
            alunos_turma = input("Digite as novas matrículas dos alunos da turma (separe por virgula): ").split(",")
            alunos_turma = [matricula.strip() for matricula in alunos_turma]
            alunos_turma =  int(alunos_turma)
            alunos_turma = [matricula for matricula in alunos_turma if matricula in alunos]
            if alunos_turma:
                turmas[disciplina] = matricula_professor
                print(f"Turma de {disciplina} atualizada com sucesso")
                return turmas
            else:
                print("Nenhum aluno válido selecionado")
        else:
            print("Professor não encontrado")
    else:
        print("Turma não encontrada")

def editar_aluno(alunos):
    matricula = int(input("Digite a matrícula do aluno que deseja editar: "))
    if matricula in alunos:
        aluno = input("Digite o novo nome do aluno: ")
        alunos[matricula] = aluno
        print(" ")
        print(f"Aluno com matrícula {matricula} atualizado")
        return alunos
    else:
        print(" ")
        print("Aluno não encontrado")

def editar_professor(professores):
    matricula = int(input("Digite a matrícula do professor que deseja editar: "))
    if matricula in professores:
        professor = input("Digite o novo nome do professor: ")
        professores[matricula] = professor
        print(" ")
        print(f"Professor com matrícula {matricula} atualizado")
        return professores
    else:
        print(" ")
        print("Professor não encontrado")

def visualizar_turma(turmas, professores):
    disciplina = input("Digite o nome da disciplina (turma) que deseja visualizar: ")
    if disciplina in turmas:
        matricula_professor = turmas[disciplina]
        nome_professor = professores[matricula_professor]
        print(f"----- Turma de {disciplina} -----")
        print(f"Professor: {nome_professor}")
    else:
        print("Turma não encontrada")

def visualizar_turma_professor(turmas, professores):
    matricula = input("Digite a matrícula do professor: ")
    if matricula in professores:
        turmas_professor = [turma for turma, prof in turmas.items() if prof == matricula]
        if turmas_professor:
            print(f"----- Turmas do Professor com matrícula {matricula} -----")
            for turma in turmas_professor:
                print(f"Disciplina: {turma} | Professor: {professores[matricula]}")
        else:
            print(f"O professor com matrícula {matricula} não está associado a nenhuma turma")
    else:
        print("Professor não encontrado")

def visualizar_turma_alunos(turmas, alunos, professores):
    turma = input("Digite o nome da turma (disciplina): ")
    if turma in turmas:
        matricula_professor = turmas[turma]
        alunos_turma = [alunos[matricula] for matricula in alunos if matricula in turmas.values() and turmas[turma] == matricula]
        print(f"----- Alunos da turma de {turma} -----")
        print(f"Professor: {professores[matricula_professor]}")
        if alunos_turma:
            for aluno in alunos_turma:
                print(f"Aluno: {aluno}")
        else:
            print("Nenhum aluno matriculado nessa turma")
    else:
        print("Turma não encontrada")

def visualizar_alunos(alunos):
    if alunos:
        print("----- Alunos Cadastrados -----")
        print(" ")
        for matricula, nome in alunos.items():
            
            print(f"Matrícula: {matricula} | Nome: {nome}")
    else:
        print("Nenhum aluno cadastrado")

def visualizar_professsores(professores):
    if professores:
        print("----- Professores Cadastrados -----")
        print(" ")
        for matricula, nome in professores.items():
            print(f"Matrícula: {matricula} | Nome: {nome}")
    else:
        print("nenhum professor cadastrado")

def apagar_turma(turmas):
        turma = input("Digite a turma que deseja apagar: ")
        if turma in turmas:
             del turmas [turma]
             print(" ")
             print(f"Turma {turma} deletado com sucesso!")
             return turmas
        else:
            print("Nome não cadastrado")
            
        
def apagar_aluno(alunos):
     matricula = int(input("Digite a matrícula do aluno que deseja apagar: "))
     if matricula in alunos:
          del alunos [matricula]
          print(" ")
          print(f"Aluno de matrícula {matricula} deletado com sucesso!")
          return alunos
     else:
        print("Nome não cadastrado")
          

def apagar_professor(professores):
    matricula = int(input("Digite a matrícula do professor que deseja deletar: "))
    if matricula in professores:
         del professores[matricula]
         print(" ")
         print("Professor de matrícula {matricula} deletado com sucesso!")
         return professores
         
    else:
        print("Nome não cadastrado")
        

def salvar_dados(alunos, professores, turmas):
    with open("alunos.json", "w") as file:
        json.dump(alunos, file)
    with open("professores.json", "w") as file:
        json.dump(professores, file)
    with open("turmas.json", "w") as file:
        json.dump(turmas, file)

def carregar_dados():
    try:
        with open("alunos.json", "r") as file:
            alunos = json.load(file)
    except FileNotFoundError:
        alunos = {}
    try:
        with open("professores.json", "r") as file:
            professores = json.load(file)
    except FileNotFoundError:
        professores = {}
    try:
        with open("turmas.json", "r") as file:
            turmas = json.load(file)
    except FileNotFoundError:
        turmas = {}
    return alunos, professores, turmas

def interacao():
    while True:
        alunos, professores, turmas = carregar_dados()

        while True:
            menu_principal()
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                while True:
                    menu_coordenador()
                    opcao_coordenador = int(input("Digite a opção desejada: "))
                    print(" ")
                    if opcao_coordenador == 1:
                        cadastrar_turma(turmas, professores, alunos)
                    elif opcao_coordenador == 2:
                        editar_turma(turmas, professores, alunos)
                    elif opcao_coordenador == 3:
                        visualizar_turma(turmas, professores)
                    elif opcao_coordenador == 4:
                        apagar_turma(turmas)
                    elif opcao_coordenador == 0:
                        break
                    else:
                        print("Opção inválida")
            elif opcao == 2:
                while True:
                    menu_professor()
                    opcao_professor = int(input("Digite a opção desejada: "))
                    print(" ")
                    if opcao_professor == 1:
                        cadastrar_professor(professores)
                    elif opcao_professor == 2:
                        editar_professor(professores)
                    elif opcao_professor == 3:
                        visualizar_professsores(professores)
                    elif opcao_professor == 4:
                        apagar_professor(professores)
                    elif opcao_professor == 5:
                        visualizar_turma_professor(turmas, professores)
                    elif opcao_professor == 6:
                        visualizar_turma_alunos(turmas, alunos, professores)
                    elif opcao_professor == 0:
                        break
                    else:
                        print("Opção inválida")
            elif opcao == 3:
                while True:
                    menu_aluno()
                    opcao_aluno = int(input("Digite a opção desejada: "))
                    print(" ")
                    if opcao_aluno == 1:
                        cadastrar_aluno(alunos)
                    elif opcao_aluno == 2:
                        editar_aluno(alunos)
                    elif opcao_aluno == 3:
                        visualizar_alunos(alunos)
                    elif opcao_aluno == 4:
                        apagar_aluno(alunos)
                    elif opcao_aluno == 0:
                        break
                    else:
                        print("Opção inválida")
            elif opcao == 0:
                break
            else:
                print("Opção inválida")

interacao()
