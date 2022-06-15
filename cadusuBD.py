import pyodbc
import retornar_conexao_sql
import PySimpleGUI as sg


def jl_cadastroUSU():
    sg.theme('Reddit')
    layout = [
        [sg.Text('id Usuario')],
        [sg.Input(0, key='-IDU-')],
        [sg.Text('Nome')],
        [sg.Input(key='-NU-')],
        [sg.Text('Senha')],
        [sg.Input('A', key='-SU-')],
        [sg.Button('Cadastrar Usuario'), sg.Button(
            'Excluir Usuario'), sg.Button('Pequisar Usuario')],


    ]

    return sg.Window('Cadastro de Usuario', layout=layout, finalize=True)


janela = jl_cadastroUSU()

while True:
    window, event, values = sg.read_all_windows()
    if window == janela and event == sg.WIN_CLOSED:
        break
    if window == janela and event == 'Cadastrar Usuario':
        retornar_conexao_sql
        id_USU = values['-IDU-']
        nomeUSU = values['-NU-']
        senhaUSU = values['-SU-']

        cursor = retornar_conexao_sql()

        inserirUSU = f"""insert into Usuarios (id, Nome, senha)
        values ({id_USU}, '{nomeUSU}', '{senhaUSU}')"""
        cursor.execute(inserirUSU)
        cursor.commit()
        cursor.close()

    if window == janela and event == 'Excluir Usuario':
        retornar_conexao_sql

        id_USU = values['-IDU-']

        cursor = retornar_conexao_sql()

        excluirUSU = f"""delete from Usuarios where id = ({id_USU})"""
        cursor.execute(excluirUSU)
        cursor.commit()
        cursor.close()
    if window == janela and event == 'Pequisar Usuario':
        retornar_conexao_sql
        nomeUSU = values['-NU-']

        cursor = retornar_conexao_sql()

        pesqUSU = f"""select id, Nome from Usuarios where nome = ('{nomeUSU}')"""
        cursor.execute(pesqUSU)
        row = cursor.fetchall()
        cursor.commit()
        cursor.close()
        sg.popup(row)
