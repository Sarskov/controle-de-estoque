import PySimpleGUI as sg
import sqlite3

conn = sqlite3.connect("C:\TkinterVenda\Database\store.db")
c = conn.cursor()

result = c.execute("SELECT MAX(id) from inventory")
for r in result:
    id = r[0]


class TelaPython:
    def __init__(self):
        # layout
        layout = [
            [sg.Text('Cadastro De Produtos', font=('arial 20 bold') )],

            [sg.Text('Nome do produto', font=('david 12 '))],
            [sg.Input((' '), key='name')],  # key configura uma variavel

            [sg.Text('Estoque', font=('david 12 '))],
            [sg.Input((''), key='stock_1')],  # DICIPLINA DO PROFESSOR

            [sg.Text('Preço de custo', font=('david 12'))],
            [sg.Input((''), key='cp_1')],
            # [sg.Text('ABAIXO DA MEDIA')],
            # [sg.Radio('nao','medias',key='abaixo')],

            [sg.Text('Preço de venda', font=('david 12'))],
            [sg.Input((''), key='sp_1')],

            [sg.Text('Nome do fornecedor', font=('david 12'))],
            [sg.Input((''), key='vendor_1')],

            [sg.Text('Telefone do fornecedor', font=('david 12'))],
            [sg.Input((''), key='vendor_phoneno')],

            [sg.Text('ID', font=('david 12'))],
            [sg.Input((''), key='id_1')],

            [sg.Button('enviar_dados')],

            #[sg.Output(size=(40, 20))]
        ]
        # janela
        self.janela = sg.Window("FORMULARIO DE CADASTRO").layout(layout)

        # extrair dados da tela

    def Iniciar(self):

        self.button, self.values = self.janela.Read()
        name = self.values['name']
        stock = self.values['stock_1']
        cp = self.values['cp_1']
        sp= self.values['sp_1']
        vendor = self.values['vendor_1']
        vendor_phoneno = self.values['vendor_phoneno']
        #id = self.values = ['id_1']
        totalcp = float(cp) * float(stock)
        totalsp = float(sp) * float(stock)
        assumed_profit = float(totalsp - totalcp)


        print(f'{name}')
        print(f'{stock}')
        print(f'{cp}')
        print(f'{sp}')
        print(f'{vendor}')
        print(f'{vendor_phoneno}')
        #print(f'{id}')


        if name =='' or stock =='' or cp =='' or sp =='':
            sg.Popup("FAVOR PREECHER TODOS OS CAMPOS")
        else:
            sql = "INSERT INTO inventory(name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phoneno) VALUES (?,?,?,?,?,?,?,?,?)"
            c.execute(sql,(name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phoneno))
            conn.commit()
            sg.Popup("CADASTRO REALIZADO COM SUCESSO")



            # print(f'{abaixo}')


tela = TelaPython()
tela.Iniciar()