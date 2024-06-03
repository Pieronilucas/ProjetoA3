import re

class VerificadorCPF:
    def __init__(self):
        pass
        
    def verificar_cpf(self, cpf):
        cpf = cpf.replace('.','').replace('-','')
        if not re.match(r'^\d{11}$', cpf):
            return False
        if cpf == cpf[0] * 11:
            return False
        
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        primeiro_digito = soma % 11
        if primeiro_digito <= 1:
            primeiro_digito = 0
        else:
            primeiro_digito = 11 - primeiro_digito

        if int(cpf[9]) != primeiro_digito:
            return False
        
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        segundo_digito = soma % 11
        if segundo_digito <= 1:
            segundo_digito = 0
        else:
            segundo_digito = 11 - segundo_digito

        if int(cpf[10]) != segundo_digito:
            return False
        
        return True
    
