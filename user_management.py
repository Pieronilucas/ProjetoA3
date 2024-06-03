import sqlite3

class UserManagement:
    def __init__(self):
        # self.user_dados = [{'cpf': '70227461681'}]
        # self.user_dados = []
        db_name = 'users.db'
        self.conn = sqlite3.connect(db_name)
        self.create_users_table()
        self.create_complaint_table()


    def create_users_table(self):
        new_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            cpf INTEGER PRIMARY KEY NOT NULL,
            nome VARCHAR(100) NOT NULL,
            celular VARCHAR(20) NOT NULL,
            email VARCHAR(20) NOT NULL,
            cep VARCHAR(20) NOT NULL,
            rua VARCHAR(20) NOT NULL,
            bairro VARCHAR(20) NOT NULL,
            numero VARCHAR(20) NOT NULL,
            complemento VARCHAR(20),
            data TEXT NOT NULL,
            hora TEXT NOT NULL,
            servico VARCHAR(100) NOT NULL,
            observacao VARCHAR(100)
        );
        '''
        self.conn.execute(new_table_query)
        self.conn.commit()
    
    def create_complaint_table(self):
        new_table_query = '''
        CREATE TABLE IF NOT EXISTS complaint (
            cpfDenunciante INTEGER PRIMARY KEY NOT NULL,
            nomeDenunciante VARCHAR(100) NOT NULL,
            celularDenunciante VARCHAR(20) NOT NULL,
            emailDenunciante VARCHAR(20) NOT NULL,
            cepDenuncia VARCHAR(20) NOT NULL,
            ruaDenuncia VARCHAR(20) NOT NULL,
            bairroDenuncia VARCHAR(20) NOT NULL,
            numeroDenuncia VARCHAR(20),
            complementoDenuncia VARCHAR(20),
            data TEXT NOT NULL,
            hora TEXT NOT NULL,
            observacao VARCHAR(100)
        );
        '''
        self.conn.execute(new_table_query)
        self.conn.commit()
    
    def add_complainer(self, cpfDenunciante, nomeDenunciante, celularDenunciante, emailDenunciante, cepDenuncia, ruaDenuncia, BairroDenuncia, NumeroDenuncia, complementoDenuncia, data, hora, observacao):
        data_str = data.strftime('%d-%m-%Y')
        hora_str = hora.strftime('%H:%M:%S')
        add_complaint_query = f'''
        INSERT INTO complaint (cpfDenunciante, nomeDenunciante, celularDenunciante, emailDenunciante, cepDenuncia, ruaDenuncia, BairroDenuncia, NumeroDenuncia, complementoDenuncia, data, hora, observacao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        self. conn.execute(add_complaint_query, (int(cpfDenunciante), nomeDenunciante, celularDenunciante, emailDenunciante, cepDenuncia, ruaDenuncia, BairroDenuncia, NumeroDenuncia, complementoDenuncia, data_str, hora_str, observacao))
        self.conn.commit()
        return 'Denúncia feita com sucesso!'

    def add_user(self, cpf, nome, celular, email, cep, rua, bairro, numero, complemento, data, hora, servico, observacao):
        # cpf = input('Por favor, insira seu cpf: \n')
        data_str = data.strftime('%d-%m-%Y')
        hora_str = hora.strftime('%H:%M:%S')


        # print('USER_DADOS -> ', self.listar_usuarios())
        # validador = VerificadorCPF(cpf)
        # if validador.verificar_cpf():
            # if not any(user['cpf'] == cpf for user in self.user_dados):
        if self.cpf_exists(cpf):
                return 'CPF já cadastrado!'
            #     user = {
            #         'cpf': cpf,
            #         'nome': nome,
            #         'celular': celular,
            #         'email': email,
            #         'cep': cep,
            #         'rua': rua,
            #         'bairro': bairro,
            #         'numero': numero
            #     }
                # self.user_dados.append(user)
        else:
            add_user_query = f'''
            INSERT INTO users (cpf, nome, celular, email, cep, rua, bairro, numero, complemento, data, hora, servico, observacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); 
            '''
            self.conn.execute(add_user_query, (int(cpf), nome, celular, email, cep, rua, bairro, numero, complemento, data_str, hora_str, servico, observacao))
            self.conn.commit()
            return 'Usuário adicionado com sucesso!'


    def cpf_exists(self, cpf):
        check_cpf_exists_query = '''
        SELECT * FROM users WHERE cpf = ?;
        '''
        cursor = self.conn.execute(check_cpf_exists_query, (cpf,))
        result = cursor.fetchone()
        return result

    def atualizar_user(self, cpf, nome=None, celular=None, email=None, cep=None, rua=None, bairro=None, numero=None, complemento=None):
        # print('new name -> ', nome)
        # print('new celular -> ', celular)

        update_user_query = '''
        UPDATE users
        SET nome = ?, celular = ?, email = ?, cep = ?, rua = ?, bairro = ?, numero = ?, complemento = ?
        WHERE cpf = ?;
        '''
        self.conn.execute(update_user_query, (nome, celular, email, cep, rua, bairro, numero, complemento, cpf))
        self.conn.commit()
        return "Dados de usuário atualizados"

        # for user in self.user_dados:
        # for user in self.listar_usuarios():
        # user = self.usuario_por_cpf
        #     if user[0] == cpf:
        #         print('EDITAR USER -> ', cpf)
        #         print(nome)
        #             if user['cpf'] == cpf:
        #                 if nome:
        #                     user['nome'] = nome
        #             if celular:
        #                 user['celular'] = celular
        #             if email:
        #                 user['email'] = email
        #             if cep:
        #                 user['cep'] = cep
        #                 user['rua'] = rua
        #                 user['bairro'] = bairro
        #                 user['numero'] = numero
        #             return "Dados de usuário atualizados"
        #     return "Usuário não encontrado"

    
    def usuario_por_cpf(self, cpf):
        user = self.cpf_exists(cpf)
        # print(user)
        return user
    
    def listar_usuarios(self):
        get_users_query = '''
        SELECT * FROM users;
        '''
        cursor = self.conn.execute(get_users_query)
        # print("\nlistar_usuarios:")
        users = [row for row in cursor.fetchall()]
        # print(users)
        return users
    
    def listar_denuncias(self):
        get_denuncia_query = '''
        SELECT * FROM complaint;
        '''
        cursor = self.conn.execute(get_denuncia_query)
        complaint = [row for row in cursor.fetchall()]
        return complaint

# class Horariomarcado:
#     def __init__(self, data, hora, servico):
#         self.data = data
#         self.hora = hora
#         self.servico = servico

#     def marcarhorario(self):
#         try:
#             data_hora_str = f'{self.data} {self.hora}'
#             marcandohorario = datetime.strptime(data_hora_str, '%d-%m-%Y %H:%M')
#             nome_servico = self.bananadepijama()
#             return f'O serviço "{nome_servico}" foi marcado para: {marcandohorario.strftime("%d-%m-%Y %H:%M")}'

#         except ValueError:
#             print('Formato inválido, por favor entre com dia, mês, ano. Seguido com as horas e minutos')
#             return None
        
#     def bananadepijama(self):
#         if self.servico == '1':
#             return 'agendar limpeza'
#         elif self.servico == '2':
#             return 'aplicação de inseticida'
#         else:
#             return 'Opção inválida'          