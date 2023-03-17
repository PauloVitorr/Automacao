import pyautogui
import pyperclip
import time
# import pandas

pyautogui.PAUSE = 1.5

#Passo 1: Entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("microsoft edge")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(2)

#Passo 2: Navegar até o local do relatório
    #temos que pegar a coordenada de onde temos que clicar com o mouse usando o pyautogui.position() que vai falar aonde o seu mouse tá em cima, a posição exata(x e y) farei e depois comentarei
    #time.sleep(6) Aqui eu dei um tempo pra conseguir colocar a seta em cima do botão que preciso apertar
    #print(pyautogui.position())
pyautogui.click(x=408, y=267, clicks=2)
time.sleep(2)

#Passo 3: Exportar o relatório
    #vamos pegar DE NOVO a localização para conseguir baixar o arquivi que precisamos
pyautogui.click(x=410, y=344)
pyautogui.click(x=1721, y=163)
pyautogui.click(x=1493, y=552)
time.sleep(4)

#time.sleep(6)
#print(pyautogui.position())

#Passo 4: Calcular os indicadores
# tabela = pandas.read_excel(r"C:\Users\paulo\Downloads\Vendas - Dez.xlsx")

# print(tabela)