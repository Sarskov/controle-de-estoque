import PySimpleGUI as sg
import sqlite3
import datetime

date = datetime.datetime.now().date()

conn = sqlite3.connect("C:\TkinterVenda\Database\store.db")
c = conn.cursor()

result = c.execute("SELECT MAX(id) from inventory")
for r in result:
    id = r[0]


class TelaPython:
    def __init__(self):
        # layout
        layout = [

            [sg.Text('Atualizar Produtos', font=('arial 20 bold') )],

            [sg.Text('dia de hoje: '+ str (date),key='dia', font=('david 15 bold'), text_color='black')], #''' background_color='green')'''

            [sg.Text('Digite o id', font=('david 12'))],
            [sg.Input((''), key='id_le')],

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


            [sg.Button(('enviar dados'))],

            #[sg.Output(size=(40, 8))]
        ]
        # janela
        self.janela = sg.Window("FORMULARIO DE CADASTRO").layout(layout)

        # extrair dados da tela

    def Iniciar(self):
        while True:

            self.button, self.values = self.janela.Read()
            name = self.values['name']
            stock = self.values['stock_1']
            cp = self.values['cp_1']
            sp = self.values['sp_1']
            vendor = self.values['vendor_1']
            vendor_phoneno = self.values['vendor_phoneno']
            #id = self.values = ['id_le']
            totalcp = float(cp) * float(stock)
            totalsp = float(sp) * float(stock)
            assumed_profit = float(totalsp - totalcp)
            #dia=self.values['dia']


            #print(f'{dia}')
            print(f'{name}')
            print(f'{stock}')
            print(f'{cp}')
            print(f'{sp}')
            print(f'{vendor}')
            print(f'{vendor_phoneno}')
            #print(f'{id}')


            if name =='' or stock =='' or cp =='' or sp =='':
                sg.Popup("FAVOR PREENCHER TODOS OS CAMPOS")
            else:
                sql = "INSERT INTO inventory(name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phoneno) VALUES (?,?,?,?,?,?,?,?,?)"
                c.execute(sql,(name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phoneno))
                conn.commit()
                sg.Popup("CADASTRO REALIZADO COM SUCESSO")






            # abaixo = self.values['abaixo']


            # print(f'{abaixo}')


tela = TelaPython()
tela.Iniciar()