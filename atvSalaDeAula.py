
#valida cpfs

def va_cpfl(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido!"
    
    cpf_mascarado = ['X'] * 3 + list(cpf[3:9]) + ['X'] * 2
    return ''.join(cpf_mascarado)

# Testes
print(valida_cpf("70468293493"))  # Saída: XXX682934XX
print(valida_cpf("12345678901"))  # Saída: XXX456789XX
print(valida_cpf("00000000000"))  # Saída: XXX000000XX
print(valida_cpf("01234567890"))  # Saída: XXX456789XX
print(valida_cpf("12345678abc"))  # Saída: CPF inválido! (não numérico)
print(valida_cpf("123456789"))    # Saída: CPF inválido! (tamanho errado)


#valida placa mercosul 

def valida_merco(placa, texto):
    paises = ['Argentina', 'Brasil', 'Venezuela', 'Paraguai', 'Uruguai']
    
    
    if len(placa) == 7 and placa[:3].isalpha() and placa[3].isdigit() and placa[4].isalpha() and placa[5:].isdigit():
        if texto in paises:
            return "Mercosul"
        else:
            return "Modelo Antigo"
    else:
        return "Placa está com caracteres fora do padrão!"


print(valida_merco("ABC1D23", "Brasil"))  # Saída esperada: "Mercosul"
print(valida_merco("A2C1D23", "Joao Pessoa - Paraíba"))  # Saída esperada: "Placa está com caracteres fora do padrão!"
print(valida_merco("A4C1D23", "Brasil"))  # Saída esperada: "Placa está com caracteres fora do padrão!"
print(valida_merco("ABC1D23", "Joao Pessoa - Paraíba"))  # Saída esperada: "Modelo Antigo"


#reconhece placa antiga 

def reconhece_placAntiga(string):
    if len(string) == 8 and string[:3].isalpha() and string[3] == '-' and string[4:].isdigit():
        return string + " placa correta."
    else:
        return string + " placa fora do padrão."


print(reconhece_placAntiga('ABC-DEFG'))  # Saída: ABC-DEFG placa fora do padrão
print(reconhece_placAntiga('ABC-1234'))  # Saída: ABC-1234 placa correta.
