from view import View
from model import Model
import flet as ft

class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()
        self._sign = None
        self._temporaneo = ''
        
    def saveNumber(self, event):
        num = event.control.text
        self._view._display.value = self._temporaneo
        self._view._display.value += num
        self._temporaneo = self._view._display.value
        self._model.numero = self._temporaneo
        self._view.update()

    def saveSign(self, event):
        self._temporaneo = ''
        if event.control.text == "+":
            self._sign = event.control.text
            self._model.addizione()
            self.disableButtons()
        elif event.control.text == "-":
            self._sign = event.control.text
            self._model.sottrazione()
            self.disableButtons()
        elif event.control.text == "*":
            self._sign = event.control.text
            self._model.moltiplicazione()
            self.disableButtons()
        elif event.control.text == "÷":
            self._sign = event.control.text
            self._model.divisione()
            self.disableButtons()
        
    def result(self, event):
        try:
            if self._sign == "+":
                self._model.addizione()
            elif self._sign == "-":
                self._model.sottrazione()
            elif self._sign == "*":
                self._model.moltiplicazione()
            elif self._sign == "÷":
                self._model.divisione()
            result = self._model.result()
            self._view._display.value = result
            self.enableButtons()
            self._view.update()
        except ZeroDivisionError:
            self._view._display.value = 'Errore'
            print("Non puoi dividere per 0")
            self._view.update()
    
    def clear(self, event):
        self._view._display.value = "0"
        self._temporaneo = ''
        self._view.update()
        self.enableButtons()
        self._model.clear()

    def disableButtons(self):
        self._view._btnAdd.disabled = True
        self._view._btnSott.disabled = True
        self._view._btnMolt.disabled = True
        self._view._btnDiv.disabled = True
        self._view.update()
    
    def enableButtons(self):
        self._view._btnAdd.disabled = False
        self._view._btnSott.disabled = False
        self._view._btnMolt.disabled = False
        self._view._btnDiv.disabled = False
        self._view.update()