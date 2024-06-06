import streamlit as st
from datetime import datetime
from user_management import UserManagement
from streamlit_option_menu import option_menu
from verificar_cpf import VerificadorCPF
import random

controlador = UserManagement()
verificador = VerificadorCPF()

st.set_page_config(layout='wide')

with st.sidebar:
    st.sidebar.image("https://i.imgur.com/FWvPyTW.png")
    escolha = option_menu(
        menu_title = 'Serviços',
        menu_icon = "https://i.imgur.com/FWvPyTW.png",
        options = ['Agendar visita','Atualizar usuário','Realizar denuncia','Consultar sintomas', 'Área do fiscal'],
        icons = ['https://i.imgur.com/FWvPyTW.png', 'https://i.imgur.com/FWvPyTW.png', 'https://i.imgur.com/FWvPyTW.png', 'https://i.imgur.com/FWvPyTW.png', 'https://i.imgur.com/FWvPyTW.png'],
    )

css = r'''
    <style>
        [data-testid="stForm"] {border: 0px}
    </style>
'''

st.markdown(css, unsafe_allow_html=True)
''
if escolha == 'Agendar visita':
    st.image("https://i.imgur.com/2x5L8Gb.png")
    st.title('Agendar visita do fiscal')
    st.write('Agende uma visita do fiscal para garantir que sua residência ou estabelecimento esteja livre de focos do mosquito da dengue. Nossa equipe realizará uma inspeção detalhada, aplicará medidas preventivas e fornecerá orientações essenciais para manter o ambiente seguro e saudável. Preencha o formulário abaixo para marcar uma data e hora conveniente para a visita.')
    baseboard_html = """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            color: #000;
            text-align: center;
            padding: 2px 0;
            font-size: 12px;
            box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.2);
            z-index: 1000; /* Ensure footer stays on top */
        }
    </style>
    <div class="footer">
        <p>&copy; Lucas Pieroni, Rafael Fonseca, Kenner Henrique, Pedro Santos, Bruno Santana e Lucas Augusto</p>
    </div>
    """
    st.markdown(baseboard_html, unsafe_allow_html=True)
    
    st.divider()
    with st.form(key='agendar_visita'):
        st.subheader('Dados de usuário')
        c1, c2 = st.columns(2)
        with c1:
            cpf = st.text_input('CPF', placeholder= 'Digite seu CPF')
        with c2:
            nome = st.text_input('Nome', placeholder= 'Seu nome completo')
        c3, c4 = st.columns(2)
        with c3: 
            celular = st.text_input('Celular', placeholder= 'Seu número de celular')
        with c4:
            email = st.text_input('Email', placeholder= 'Seu e-mail')
        st.divider()
        st.subheader('Endereço da visita')
        c5, c6, c67 = st.columns(3)
        with c5:
            cep = st.text_input('CEP', placeholder= 'CEP da sua rua sem pontos ou hífens')
        with c6:
            rua = st.text_input('Rua', placeholder= 'Logradouro')
        with c67:
            bairro = st.text_input('Bairro', placeholder= 'Bairro')
        c7, c8 = st.columns(2)
        with c7:
            numero = st.text_input('Número')
        with c8:
             complemento = st.text_input('Complemento', placeholder = 'Digite aqui um ponto de referência, complemento, etc')
        st.divider()
        st.subheader('Data da visita')
        c9, c10 = st.columns(2)
        with c9:
            data = st.date_input(label='Data', min_value=datetime.today().date(), format='DD/MM/YYYY',)
        with c10:
            hora = st.time_input('Hora', step=3600)  
        st.divider()
        st.subheader('Razão da visita')      
        servico = st.selectbox('Serviço', ['1 - Agendar limpeza', '2 - Aplicação de inseticida'])
        st.divider()
        st.subheader('Informações extras')
        info_extra = st.text_input('Observações', placeholder = 'Adicione qualquer observação relevante')

        submit_button = st.form_submit_button(label='Agendar')

        if submit_button:
            # verifica se o cpf é valido e adiciona dados a tabela do bd
            if verificador.verificar_cpf(cpf):
                data_str = data.strftime('%d-%m-%Y')
                hora_str = hora.strftime('%H:%M')
                # print('\tCADASTREI: ')
                # print('CPF: ', cpf)
                # print('NOME: ', nome)
                # print('EMAIL: ', email)
                # servico_code = servico.split(' ')[0]
                resultado = controlador.add_user(cpf, nome, celular, email, cep, rua, bairro, numero, complemento, data, hora, servico, info_extra)
                # print('\t', resultado)
                # print(controlador.user_dados)
                st.success(f'Sua visita foi agendada para o dia {data_str} às {hora_str} horas. Agradecemos por colaborar no combate à dengue. '
                        'Você receberá uma ligação de confirmação no dia anterior à visita. Caso precise reagendar, entre em contato conosco. Juntos, podemos manter nossa comunidade saudável e segura.')
                st.success(resultado)
            else:
                st.error('CPF inválido')

elif escolha == 'Atualizar usuário':
    st.title(':red[ATUALIZAR USUÁRIO]')
    baseboard_html = """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            color: #000;
            text-align: center;
            padding: 2px 0;
            font-size: 12px;
            box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.2);
            z-index: 1000; /* Ensure footer stays on top */
        }
    </style>
    <div class="footer">
        <p>&copy; Lucas Pieroni, Rafael Fonseca, Kenner Henrique, Pedro Santos, Bruno Santana e Lucas Augusto</p>
    </div>
    """
    st.markdown(baseboard_html, unsafe_allow_html=True)

    cpf = st.text_input('Insira o CPF do usuário a ser atualizado')
    if len(cpf) != 0:
        # chama a função de buscar os dados do úsuario através de seu cpf
        user = controlador.usuario_por_cpf(cpf)
        if user:
            # caso encontrado, abre novamente os dados básicos para serem redefinidos
            with st.form(key='update_user_form'):
                c1, c2, c3 = st.columns(3)
                with c1:
                    nome = st.text_input('Novo nome', user[1])
                with c2:
                    celular = st.text_input('Novo celular', user[2])
                with c3:
                    email = st.text_input('Novo e-mail', user[3])
                st.divider()
                c4, c5, c6 = st.columns(3)
                with c4:
                    cep = st.text_input('Novo CEP', user[4])
                with c5:
                    rua = st.text_input('Novo Logradouro', user[5])
                with c6:
                    bairro = st.text_input('Novo Bairro', user[6])
                c7, c8 = st.columns(2)
                with c7:
                    numero = st.text_input('Novo número', user[7])
                with c8:
                    complemento = st.text_input('Complemento', user[8])
                submit_button = st.form_submit_button(label='Atualizar')

                # adiciona novamente ao bd
                if submit_button:
                    resultado = controlador.atualizar_user(cpf, nome, celular, email, cep, rua, bairro, numero, complemento)
                    st.success(resultado)
        else:
            st.error('Usuário não encontrado')


elif escolha == 'Realizar denuncia':
    st.image("https://i.imgur.com/2x5L8Gb.png")
    st.title('Agendar visita do fiscal')
    st.write('Agende uma visita do fiscal para garantir que sua residência ou estabelecimento esteja livre de focos do mosquito da dengue. Nossa equipe realizará uma inspeção detalhada, aplicará medidas preventivas e fornecerá orientações essenciais para manter o ambiente seguro e saudável. Preencha o formulário abaixo para marcar uma data e hora conveniente para a visita.')
    baseboard_html = """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            color: #000;
            text-align: center;
            padding: 2px 0;
            font-size: 12px;
            box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.2);
            z-index: 1000; /* Ensure footer stays on top */
        }
    </style>
    <div class="footer">
        <p>&copy; Lucas Pieroni, Rafael Fonseca, Kenner Henrique, Pedro Santos, Bruno Santana e Lucas Augusto</p>
    </div>
    """
    st.markdown(baseboard_html, unsafe_allow_html=True)

    st.divider()
    with st.form(key='add_user_form'):
        st.subheader('Dados de usuário')
        c1, c2 = st.columns(2)
        with c1:
            cpf_denuncia = st.text_input('CPF', placeholder = 'Digite seu CPF')
        with c2:
            nome_denuncia = st.text_input('Nome', placeholder = 'Digite seu nome completo')
        c3, c4 = st.columns(2)
        with c3:
            celular_denuncia = st.text_input('Celular', placeholder = 'Digite seu telefone')
        with c4:
            email_denuncia = st.text_input('E-mail', placeholder = 'Digite seu email')
        st.divider()
        st.subheader('Endereço da visita')
        c5, c6 = st.columns(2)
        with c5:
            cep_denuncia = st.text_input('CEP', placeholder = 'Digite o CEP para denúncia')
        with c6:
            rua_denuncia = st.text_input('Rua', placeholder = 'Digite o nome da rua')
        c7, c8, c87 = st.columns(3)
        with c7:
            bairro_denuncia = st.text_input('Bairro', placeholder = 'Digite o nome do bairro')
        with c8:
            numero_denuncia = st.text_input('Número', placeholder='Digite o número do local (caso seja lote ou não possua número, deixe em branco)')
        with c87:
            complemento_denuncia = st.text_input('Tipo de ambiente', placeholder = 'Digite aqui qual o tipo de ambiente (lote, casa, apartamento, etc) e, caso seja apartamento, seu complemento.')
        st.divider()
        st.subheader('Data da visita')
        c9, c10 = st.columns(2)
        with c9:
            data = st.date_input(label='Data', min_value=datetime.today().date(), format='DD/MM/YYYY',)
        with c10:
            hora = st.time_input('Hora', step=3600)
        st.divider()
        st.subheader('Informações extras')
        info_extra_denuncia = st.text_input('Observações', placeholder = 'Adicione qualquer observação relevante')

        submit_button_complaint = st.form_submit_button(label='DENUNCIAR')

        if submit_button_complaint:
            # verifica se o cpf é valido e adiciona dados a tabela do bd
            if verificador.verificar_cpf(cpf_denuncia):
                protocolo = random.randint(1, 9999)
                data_str = data.strftime('%d-%m-%Y')
                hora_str = hora.strftime('%H:%M')
                # print('\tCADASTREI: ')
                # print('CPF: ', cpf)
                # print('NOME: ', nome)
                # print('EMAIL: ', email)
                # servico_code = servico.split(' ')[0]
                resultado_denuncia = controlador.add_complainer(cpf_denuncia, nome_denuncia, celular_denuncia, email_denuncia, cep_denuncia, rua_denuncia, bairro_denuncia, numero_denuncia, complemento_denuncia, data, hora, info_extra_denuncia)
                # print('\t', resultado)
                # print(controlador.user_dados)
                st.success(f'Sua denúncia foi procoloda seguindo o protocolo de número {protocolo}. Agradecemos por colaborar no combate à dengue. ')
                st.success(resultado_denuncia)
            else:
                st.error('CPF inválido')

elif escolha == 'Consultar sintomas':
    sintomas_dengue = [
        "Febre alta",
        "Dor de cabeça intensa",
        "Dor atrás dos olhos",
        "Dores musculares e articulares",
        "Náuseas e vômitos",
        "Fadiga",
        "Erupção cutânea",
        "Sangramento leve"
    ]
    
    sintomas_graves = [
        "Sangramento severo",
        "Dificuldade respiratória",
        "Dor abdominal severa",
        "Vômitos persistentes",
        "Acúmulo de líquidos",
        "Queda de pressão arterial"
    ]

    contagem_dengue = []
    contagem_grave = []

    st.title('Consulta Simples de Sintomas de Dengue')
    st.write('Marque os sintomas que você está sentindo. Não se esqueça que esse teste não substitui a avalição médica e deve ser considerado apenas como um parâmetro, não um diagnóstico')
    baseboard_html = """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            color: #000;
            text-align: center;
            padding: 2px 0;
            font-size: 12px;
            box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.2);
            z-index: 1000; /* Ensure footer stays on top */
        }
    </style>
    <div class="footer">
        <p>&copy; Lucas Pieroni, Rafael Fonseca, Kenner Henrique, Pedro Santos, Bruno Santana e Lucas Augusto</p>
    </div>
    """
    st.markdown(baseboard_html, unsafe_allow_html=True)
    
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.header('Sintomas Comuns')
        for sintoma in sintomas_dengue:
            if st.checkbox(sintoma):
                contagem_dengue.append(sintoma)
    with c2:
        st.header('Sintomas Graves')
        for sintoma_grave in sintomas_graves:
            if st.checkbox(sintoma_grave):
                contagem_grave.append(sintoma_grave)
    
    if st.button('Ver Resultado'):
        # valores definidos como base para retornar as possibilidades
        if len(contagem_dengue) < 3:
            resultado = 'Provavelmente não é dengue. Procure auxílio médico para confirmação de qual a doença.'
        elif len(contagem_dengue) >= 3 and len(contagem_grave) == 0:
            resultado = 'Possível caso de dengue. Procure o posto mais próximo para mais instruções.'
        elif len(contagem_dengue) >= 3 and len(contagem_grave) >= 1:
            resultado = 'Possível caso de dengue hemorrágica! Procure ajuda médica o mais breve possível.'
        else:
            resultado = 'Caso indeterminado. Favor procurar auxílio médico para maiores investigações.'
        
        st.subheader('Resultado da Consulta:')
        st.info(resultado)

elif escolha == 'Área do fiscal':
    st.subheader('INSIRA A SENHA DE ADMINISTRADOR PARA PROSSEGUIR.')
    senha_forte = 'loudeco'
    senha_usuario = st.text_input('Senha agendamentos', type='password')
    if senha_forte == senha_usuario:
        tipo_servico = st.selectbox('Tipo de serviço', ['0 - Selecione o serviço','1 - Visitas', '2 - Denuncias'])
        if tipo_servico.startswith('0'):
            pass
        elif tipo_servico.startswith('1'):
                st.title(':red[CONSULTA AGENDAMENTOS EM ABERTO]')         
                st.write('Agendamentos em aberto')
                # acessar a função de listagem de úsuarios 
                usuarios = controlador.listar_usuarios()
                if usuarios:
                    for user in usuarios:
                        # print('Listar usuários: ')
                        # print(user)
                        st.info(user)
                        
                else:
                    st.info('Nenhum agendamento cadastrado.')
        elif tipo_servico.startswith('2'):
                st.title(':red[CONSULTA DENUNCIAS EM ABERTO]')
                st.write('Denúncias em aberto')
                # acessar a função de listagem de denúncias
                denuncias = controlador.listar_denuncias()
                if denuncias:
                    for denuncia in denuncias:
                        # print('Listar usuários: ')
                        # print(user)
                        st.info(denuncia)
                else:
                    st.info('Nenhuma denúncia cadastrada.')
        else:
            st.info('')
    elif senha_usuario:
        st.error('SENHA INCORRETA!')
