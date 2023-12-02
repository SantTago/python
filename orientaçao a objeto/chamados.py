desenheCirculo(tess)
#Isso sugere que a função é um agente ativo, que
#diz algo como, “Ei, função desenheCirculo! Aqui está um objeto tartaruga para você desenhar. “

tess.forward(100) # que pede para a tartaruga se mover um certo número de passos para a frente.

tess.circle() # quer dizer “Ei tess! Por favor use seu método circle!”

from PySide.QtGui import QApplication
from PySide.QtCore import QUrl
from PySide.QtWebKit import QWebView
import sys

__autor__= 'Rodrigo Gomes'

app = QApplication(sys.argv)
b = QWebView()
b.load(QUrl('https://youtu.be/QXG-Rsmrt4A?list=PLe1Buo9ERpeVkq-3aqxBSeriyV-didkwW'))
b.show()
app.exec_()