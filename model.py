class Model(object):
    def __init__(self):
        self._numero = 0
        self._temporaneo = 0
        self._risultato = None
        self._firstTime = True
        self._flagRisultato = False
        
    @property
    def numero(self):
        return self._numero  
    @numero.setter
    def numero(self, value):
        try:
            if '.' in value:
                self._numero = float(value)
            else:
                self._numero = int(value)
        except ValueError:
            raise ValueError('Inserisci un numero')
    
    def addizione(self):
        if not self._flagRisultato and not self._firstTime:
            self._temporaneo += self._numero
            self._risultato = self._temporaneo
        elif self._firstTime:
            self._temporaneo = self._numero
            self._firstTime = False
        else:
            self._temporaneo = self._risultato
            self._flagRisultato = False

    def sottrazione(self): 
        if not self._flagRisultato and not self._firstTime:
            self._temporaneo -= self._numero
            self._risultato = self._temporaneo
        elif self._firstTime:
            self._temporaneo = self._numero
            self._firstTime = False
        else:
            self._temporaneo = self._risultato
            self._flagRisultato = False
    
    def moltiplicazione(self):
        if not self._flagRisultato and not self._firstTime:
            self._temporaneo *= self._numero
            self._risultato = self._temporaneo
            if self._risultato == 0.0:
                self._risultato = int(self._risultato)
        elif self._firstTime:
            self._temporaneo = self._numero
            self._firstTime = False
        else:
            self._temporaneo = self._risultato
            self._flagRisultato = False
    
    def divisione(self):
        try:
            if not self._flagRisultato and not self._firstTime:
                if self._temporaneo % self._numero == 0:
                    isINT = True
                else:
                    isINT = False
                self._temporaneo /= self._numero
                self._risultato = self._temporaneo
                if isINT:
                    self._risultato = int(self._risultato)
            elif self._firstTime:
                self._temporaneo = self._numero
                self._firstTime = False
            else:
                self._temporaneo = self._risultato
                self._flagRisultato = False
        except ZeroDivisionError:
            raise ZeroDivisionError
    
    def result(self):
        self._flagRisultato = True
        return self._risultato
    
    def clear(self):
        self._numero = None
        self._risultato = None
        self._temporaneo = 0
        self._flagRisultato = False
        self._firstTime = True
    
if __name__ == "__main__":
    pass