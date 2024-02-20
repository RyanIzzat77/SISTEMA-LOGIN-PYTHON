from getpass import getpass

print('='*30)
print('Bem-vindo ao sistema de login')
print('='*30)

while True:
    try:
        print('-'*30)
        print('[1] Criar conta')
        print('[2] Fazer login')
        print('[3] Encerrar o programa') 
        print('')
        escolha = int(input('Digite a opção que deseja: '))

        #cria o arquivo texto e armazena a variável nome e senha
        if escolha == 1:
            print('')
            nome = str(input('Nome de usuário: '))
            senha = getpass('Digite a senha: ')

            with open('usuarios.txt', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'{nome},')
                arquivo.write(f'{senha}\n')

        elif escolha == 2:
            #função que verifica se em cada linha possui o nome e senha
            def verifica_login(login_nome, login_senha):
                login_sucesso = False
                with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
                    for linha in arquivo:
                        if login_nome in linha and login_senha in linha:
                            login_sucesso = True
                            break
            
                    if login_sucesso:
                        print('Login feito com sucesso :)')
                    else:
                        print('Usuário ou senha incorreto, não foi possível fazer login')
            print('')
            login_nome = str(input('Digite seu nome de usuário: '))
            login_senha = getpass('Digite sua senha: ')
            verifica_login(login_nome, login_senha)
            
        elif escolha == 3:
            print('Encerrando...')
            break

        else:
            print('Opção inválida')

    except ValueError:
        print('Opção inválida')

