import flet as ft


class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "Calcolatrice FLET" 
        self._page.horizontal_alignment = 'CENTER'
        self._page.vertical_alignment = 'CENTER'
        self._page.window_height = 300
        self._page.window_width = 300
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        # Riga 1
        self._display = ft.TextField(value='0', text_size=24, text_align='right', width=188, disabled=True)
        self._btnResult = ft.ElevatedButton(text='=', color='white', bgcolor='#FF8C00', on_click=self._controller.result)
        row1 = ft.Row(controls=[self._display, self._btnResult])

        # Riga 2
        self._btn7 = ft.ElevatedButton(text='7', color='white', bgcolor='#808080', on_click=self._controller.saveNumber)
        self._btn8 = ft.ElevatedButton(text='8', color='white', bgcolor='#808080', on_click=self._controller.saveNumber)
        self._btn9 = ft.ElevatedButton(text='9', color='white', bgcolor='#808080', on_click=self._controller.saveNumber)
        self._btnDiv = ft.ElevatedButton(text='÷', color='white', bgcolor='#FF8C00', on_click=self._controller.saveSign)
        row2 = ft.Row(controls=[self._btn7, self._btn8, self._btn9, self._btnDiv])

        # Riga 3
        self._btn4 = ft.ElevatedButton(text='4', color='white', bgcolor='#808080', on_click=self._controller.saveNumber)
        self._btn5 = ft.ElevatedButton(text='5', color='white', bgcolor='#808080', on_click=self._controller.saveNumber)
        self._btn6 = ft.ElevatedButton(text='6', color='white', bgcolor='#808080', on_click=self._controller.saveNumber)
        self._btnMolt = ft.ElevatedButton(text='x', color='white', bgcolor='#FF8C00', on_click=self._controller.saveSign)
        row3 = ft.Row(controls=[self._btn4, self._btn5, self._btn6, self._btnMolt])

        # Riga 4
        self._btn1 = ft.ElevatedButton(text='1', color='white', bgcolor='#808080', on_click=self._controller.saveNumber)
        self._btn2 = ft.ElevatedButton(text='2', color='white', bgcolor='#808080', on_click=self._controller.saveNumber)
        self._btn3 = ft.ElevatedButton(text='3', color='white', bgcolor='#808080', on_click=self._controller.saveNumber)
        self._btnSott = ft.ElevatedButton(text='-', color='white', bgcolor='#FF8C00', on_click=self._controller.saveSign)
        row4 = ft.Row(controls=[self._btn1, self._btn2, self._btn3, self._btnSott])

        # Riga 5
        self._btn0 = ft.ElevatedButton(text='0', color='white', bgcolor='#808080', on_click=self._controller.saveNumber)
        self._btnVirgola = ft.ElevatedButton(text='.', color='white', bgcolor='#808080', on_click=self._controller.saveNumber)
        self._btnC = ft.ElevatedButton(text='C', color='white', bgcolor='#00CED1', on_click=self._controller.clear)
        self._btnAdd = ft.ElevatedButton(text='+', color='white', bgcolor='#FF8C00', on_click=self._controller.saveSign)
        row5 = ft.Row(controls=[self._btn0, self._btnVirgola, self._btnC, self._btnAdd])

        self._page.add(row1, row2, row3, row4, row5)

    def setController(self, controller):
        self._controller = controller

    def update(self):
        self._page.update()
