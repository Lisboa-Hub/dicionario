import os

# Criar dicionário
usuario = {
    "Nome": input("Informe o seu nome: "),
    "CPF": input("Informe o seu CPF: "),
    "RG": input("Informe o seu RG: "),
    "Data de Nascimento": input("Informe a sua data de nascimento: "),
    "SEXO": input("Informe o seu sexo: "),
    "Signo": input("Informe o seu signo: "),
    "Nome da mãe": input("Informe o nome da sua mãe: "),
    "Nome do pai": input("Informe o nome do seu pai: "),
    "E-mail": input("Informe o seu e-mail: "),
    "Senha": input("Informe a sua senha: "),
    "CEP": input("Informe o seu CEP: "),
    "Endereço": input("Informe o seu endereço: "),
    "Número": input("Informe o seu número: "),
    "Bairo": input("Informe o nome do bairro: "),
    "Cidade": input("Informe o nome da cidade: "),
    "Estado": input("Informe o nome do Estado: "),
    "Telefone": input("Informe o seu número de telefone fixo: "),
    "Celular": input("Informe o seu número de celular: "),
    "Altura": input("Informe a sua altura: "),
    "Peso": input("Informe o seu peso: "),
    "Tipo sanguíneo": input("Informe o seu tipo sanguíneo: "),
    "Cor Favorita": input("Informe a sua cor favorita: "),
}

os.system("cls")

print(f"{"-"*10} INFORMAÇÕES DO USUÁRIO {"-"*10}\n")

for chave in usuario:
    print(f"{chave}: {usuario.get(chave)}")
