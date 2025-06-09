

def main():
    usuario = {
        'nome': '',
        'cpf': '',
        'data_nascimento': '',
        'telefone': '',
        'email': '',
        'senha': ''
    }

    usuario['nome'] = input("Digite seu nome completo: ")
    usuario['cpf'] = input("Digite seu CPF: ")
    usuario['data_nascimento'] = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    usuario['telefone'] = input("Digite seu número de telefone com DDD (ex: (11)91234-5678): ")

    while True:
        email = input("Digite seu email: ")
        confirma_email = input("Confirme seu email: ")
        if email == confirma_email:
            usuario['email'] = email
            break
        else:
            print("Os emails não coincidem. Por favor, digite novamente.")

    usuario['senha'] = input("Crie uma senha: ")

    print("\nInformações do usuário:")
    print(f"Nome: {usuario['nome']}")
    print(f"CPF: {usuario['cpf']}")
    print(f"Data de Nascimento: {usuario['data_nascimento']}")
    print(f"Telefone: {usuario['telefone']}")
    print(f"Email: {usuario['email']}")

    # Opção de alterar senha
    mudar_senha = input("\nDeseja mudar sua senha? (sim/não): ")
    if mudar_senha.lower() == 'sim':
        senha_atual = input("Digite sua senha atual: ")
        if senha_atual == usuario['senha']:
            nova_senha = input("Digite sua nova senha: ")
            confirma_nova_senha = input("Confirme sua nova senha: ")
            if nova_senha == confirma_nova_senha:
                usuario['senha'] = nova_senha
                print("Senha alterada com sucesso!")
            else:
                print("As novas senhas não coincidem. A senha não foi alterada.")
        else:
            print("Senha atual incorreta. A senha não foi alterada.")

 
    mudar_telefone = input("\nDeseja alterar seu telefone? (sim/não): ")
    if mudar_telefone.lower() == 'sim':
        novo_telefone = input("Digite seu novo número de telefone com DDD: ")
        usuario['telefone'] = novo_telefone
        print("Telefone alterado com sucesso!")

    print("\nInformações atualizadas:")
    print(f"Nome: {usuario['nome']}")
    print(f"CPF: {usuario['cpf']}")
    print(f"Data de Nascimento: {usuario['data_nascimento']}")
    print(f"Telefone: {usuario['telefone']}")
    print(f"Email: {usuario['email']}")
    print(f"Senha: {usuario['senha']}")

if __name__ == "__main__":
    main()



