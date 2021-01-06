from PyQt5 import QtWidgets, QtCore, QtGui
from login import Ui_MainWindow
from playsound import playsound
from random import randint
from about import about

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # variavel de modo:
        # 1. para saber em que modo esta o programa: "login"; "cadastro" 1,2; "recuperação_de_conta" e outros.
        # para cada modo os botões mudam de funcionallidades.
        self.mode = "login"
        # 2. para saber em modo está a line edit da senha do usuário: "lock" e "no-lock".
        self.password_mode = "lock"
        # variaveis para verificar se as lines edits foram preemchidas.
        self.name_user = None
        self.password = None
        self.password2 = None
        # Lista de pregunta de recuperação da conta, que seram exibidas no cadasto do usuário.
        self.list_of_question = ["Qual é o seu esporto\nfavorito?",
                                  "Qual é o seu nome que\nninguem mais conheça?",
                                  "Qual foi melhor momento\nda sua vida?",
                                  "Quem foi o(a) seu(sua) melhor\namigo(a) na escola primaria?",
                                  "Qual é o nome do ator que o\nseu amigo(a) mais gosta?",
                                  "Qual é a sua cor\nfavorita?",
                                  "Qual é o nome do seu programa\nfavorito?", "Qual é a sua comida\nfavorita?"]
        # Está variavel sera utilizado para saber em que pergunta de recuperação da conta está o 
        # programa.
        self.question_number = None
        # ------------
        self.setupUi(self)
        # escondendo o frame de notificações e de erros.
        self.frame_notification.hide()
        # criando conexões des cliques de botões com funções e lines edits.
        self.pushButton_close_notification.clicked.connect(lambda: self.click(event="hide_notification"))
        self.pushButton_enter.clicked.connect(lambda: self.click(event="validate"))
        self.lineEdit_name_user.textEdited.connect(lambda: self.frame_notification.hide())
        self.pushButton_add.clicked.connect(lambda: self.click(event="add"))
        self.pushButton_password.clicked.connect(lambda: self.click(event="password"))
        self.pushButton_recover_account.clicked.connect(lambda: self.click(event="recover_account"))
        self.pushButton_about.clicked.connect(lambda : self.click(event="about"))

    # Esta função serve para dar uma utilidades aos botões dependendo do modo em que está o programa.
    def click(self, event: str = ""):
        # Ocultando a frame de notificação.
        self.frame_notification.hide()
        # Função para adiçionar son no programa.
        # Mandando tocar o son "Click".
        playsound("sons/click.wav")
        # -----
        if self.mode == "login" and event == "add":
            self.form()
        # -------
        elif event == "about":
            about(self)
        
        # -----
        elif event == "add":
            # Adicionando uma imagem. 
            try:
                self.image_path, filte = QtWidgets.QFileDialog.getOpenFileName(self, "Escolha uma imagem", filter="Arquivos de imagem (*.png; *jpg)")
                self.user_image = QtGui.QPixmap(self.image_path)
                # Modificando o tamanho da imagem para 120x120
                self.user_image = self.user_image.scaled(QtCore.QSize(120, 120), transformMode=QtCore.Qt.SmoothTransformation)
                self.frame_user_image.setPixmap(self.user_image)
            except:
               self.notification("Não foi possivel carrega essa imagem. Tente mais tarde!")
            
        # ---------
        elif event == "hide_notification":
            self.frame_notification.hide()
        # ------
        elif event == "recover_account":
            self.recover_account()
        # -------
        elif event == "password":
            self.password_lock()
        # ------
        elif event == "validate":
            self.validate()
        # ------
        elif event == "cancel":
            self.back_login(event="cancel")
        # -------
        elif event == "next_question":
            self.change_question()
        else:
            pass

    # Função para mostrar notificações e mensagens para o usuário.
    def notification(self, message: str = ""):
        # Mostrando a frame de notificação ou de mensagem para o usuário.
        self.frame_notification.show()
        self.label_notification_message.setText(message)
        playsound("sons/notification.wav")

    # Funcão para recuperação de contas.
    def recover_account(self):
        # Ocultando a frame de notificação.
        self.frame_notification.hide()

        if self.mode == "login":
            # Definindo o modo do programa de "login" para "recuperar_conta"
            self.mode = "recuperar_conta"
            # Mudando o Titulo de "Login" para "Conta".
            self.title_text(text="conta")
            # Modificando os posicionamentos e os tamanhos das lines edits e pusbuttons.
            self.label_title_text.setGeometry(QtCore.QRect(130, 0, 191, 131))
            self.pushButton_enter.setGeometry(QtCore.QRect(100, 335, 250, 51))
            self.lineEdit_name_user.setGeometry(QtCore.QRect(100, 270, 250, 51))
            self.frame_user_image.setGeometry(QtCore.QRect(159, 130, 131, 131))
            #  Mudando o texto do botão "Avancar" para "Entrar".
            self.pushButton_enter.setText("Avançar")
            # Ocultando elementos do layoput.
            # 1. Ocultando o botão para ver a senha.
            self.pushButton_password.hide()
            # 2. Ocultanad a line edit da senha.
            self.lineEdit_password.hide()
            # 3. Ocultando o botão para adicionar.
            self.pushButton_add.hide()
            # 4. Ocultando o botão esquici a minha senha.
            self.pushButton_recover_account.hide()
            # 5. Adicionando uma pusbutton "Cancelar" para sair do modo "recuperar_conta".
            self.pushButton_cancel = QtWidgets.QPushButton(self.layout_main)
            self.pushButton_cancel.setGeometry(QtCore.QRect(100, 400, 250, 51))
            font = QtGui.QFont()
            font.setFamily("Microsoft YaHei UI")
            font.setPointSize(11)
            self.pushButton_cancel.setFont(font)
            self.pushButton_cancel.setStyleSheet("QPushButton{\n"
                                                 "    background-color: rgb(161, 97, 79);\n"
                                                 "    border-radius: 10px;\n"
                                                 "    padding: 10px;\n"
                                                 "    color: rgb(230, 230, 231);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover{\n"
                                                 "    border: 2px solid rgb(212, 127, 104);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:pressed{\n"
                                                 "    background-color: rgb(212, 127, 104);\n"
                                                 "}")
            self.pushButton_cancel.setObjectName("pushButton_cancel")
            self.pushButton_cancel.show()
            self.pushButton_cancel.setText('Cancelar')

            # Dando um função ao botão "cancelar" quando ele for cliquado.
            self.pushButton_cancel.clicked.connect(lambda: self.click(event="cancel"))

        elif self.mode == "recuperar_conta":
            # Chamando a função de formulario. 
            self.form()
            # Mudando a geometrica e o posicionamento dos elementos no layout.
            self.pushButton_enter.setGeometry(QtCore.QRect(100, 445, 120, 41))
            self.pushButton_cancel.setGeometry(QtCore.QRect(230, 445, 120, 41))
            # Modificando o posicionamento da frame "imagen_perfil".
            self.frame_user_image.setGeometry(QtCore.QRect(159, 80, 131, 131))
            # Modificando o posicionamento  da label de titulo.
            self.label_title_text.setGeometry(QtCore.QRect(95, -30, 250, 131))
            # Dando um texto no botão.
            self.pushButton_enter.setText("Avançar")
            # Ocultando elementos do layout.
            self.pushButton_next_question.hide()

        elif self.mode == "recuperar_conta2":
            self.form()
            # Mostrando elemento escondidos.
            self.lineEdit_password.show()
            self.pushButton_password.show()
            # Deletando elementos do layout.
            self.line_title1.deleteLater()
            self.line_title2.deleteLater()
            self.label_title_question.deleteLater()
            self.label_question.deleteLater()
            self.lineEdit_answer.deleteLater()
            # Mudado o titulo de "login" para "conta"
            self.title_text(text="Conta")
            # Mudando o posicionamento dos elementos no layout.
            self.label_title_text.setGeometry(QtCore.QRect(130, 0, 191, 131))
            self.frame_user_image.setGeometry(QtCore.QRect(159, 130, 131, 131))
            # pondo uma mensegem para o usuário.
            self.lineEdit_password.setPlaceholderText("Nova senha.")
            # Mundando texto do pushButton_conect para "concluir"
            self.pushButton_enter.setText("Concluir")

    # Esta função serve para trocar de pergunta de recuperação da conta caso o usuário queria, 
    # clicando no botão proximo ⇨.
    def change_question(self):
        # Verificando se o numero da pergunta é inferior ao da lista de pergunta. 
        # E se o número for inferior, ele é associado a uma pergunta da lista de pergunta.
        if self.question_number < len(self.list_of_question) - 1:
            self.question_number += 1
            self.label_question.setText(self.list_of_question[self.question_number])
        else:
            # Verificando se o numero da pergunta é superior ao da lista de pergunta. 
            # E se o número for superior, ele não é associado a uma pergunta da lista e o numero da pergunta volta a zero!
            # E so depois de voltar a zero ele pode ser associado a uma pergunta da lista de pergunta.
            self.question_number = 0
            self.label_question.setText(self.list_of_question[self.question_number])

    # Função para ver a password.
    def password_lock(self):
        # Escondendo a frame de notificação.
        self.frame_notification.hide()
        if self.mode == "login":
            # Verificando o modo da variavel password mode.
            if self.password_mode == "lock":
                # Trocando de estilo "imagem" com CSS do botão para ver a password.
                self.pushButton_password.setStyleSheet(u"QPushButton{\n"
                                                       "	background-image: url(:/image/Images/open_lock1.png);\n"
                                                       "	background-position: center;\n"
                                                       "	background-repeat: none;\n"
                                                       "	background-color: rgb(161, 97, 79, 0);\n"
                                                       "	border-radius: 20px;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QPushButton:hover{\n"
                                                       "	border: 2px solid rgb(212, 127, 104);\n"
                                                       "}\n"
                                                       "\n"
                                                       "QPushButton:pressed{\n"
                                                       "	background-color: rgb(212, 127, 104);\n"
                                                       "}\n"
                                                       "")
                # Trocando de echomode para que a senha fique legível.
                self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Normal)
                # Trocando de modo na variavel, do modo "lock" para "not-lock".
                self.password_mode = "not-lock"

            elif self.password_mode == "not-lock":
                # Trocando de estilo "imagem" com CSS do botão para ver a password.
                self.pushButton_password.setStyleSheet(u"QPushButton{\n"
                                                       "	background-image: url(:/image/Images/closed_lock1.png);\n"
                                                       "	background-position: center;\n"
                                                       "	background-repeat: none;\n"
                                                       "	background-color: rgb(161, 97, 79, 0);\n"
                                                       "	border-radius: 20px;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QPushButton:hover{\n"
                                                       "	border: 2px solid rgb(212, 127, 104);\n"
                                                       "}\n"
                                                       "\n"
                                                       "QPushButton:pressed{\n"
                                                       "	background-color: rgb(212, 127, 104);\n"
                                                       "}\n"
                                                       "")
                # Trocando de echomode da line edit para que a senha fique ilegível.
                self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
                # Trocando de modo na variavel, do modo "not-lock" para "lock".
                self.password_mode = "lock"

            else:
                pass

        elif self.mode == "cadastro1" or self.mode == "recuperar_conta3":
            if self.password_mode == "lock":
                # Trocando de estilo "imagem" com CSS do botão para ver a password.
                self.pushButton_password.setStyleSheet(u"QPushButton{\n"
                                                       "	background-image: url(:/image/Images/open_lock1.png);\n"
                                                       "	background-position: center;\n"
                                                       "	background-repeat: none;\n"
                                                       "	background-color: rgb(161, 97, 79, 0);\n"
                                                       "	border-radius: 20px;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QPushButton:hover{\n"
                                                       "	border: 2px solid rgb(212, 127, 104);\n"
                                                       "}\n"
                                                       "\n"
                                                       "QPushButton:pressed{\n"
                                                       "	background-color: rgb(212, 127, 104);\n"
                                                       "}\n"
                                                       "")
                # Trocando de echomode para que a senha fique legível.
                self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.lineEdit_password2.setEchoMode(QtWidgets.QLineEdit.Normal)
                # Trocando de modo na variavel, do modo "lock" para "not-lock".
                self.password_mode = "not-lock"

            elif self.password_mode == "not-lock":
                # Trocando o estilo e a "imagem" com CSS do botão para ver a password.
                self.pushButton_password.setStyleSheet(u"QPushButton{\n"
                                                       "	background-image: url(:/image/Images/closed_lock1.png);\n"
                                                       "	background-position: center;\n"
                                                       "	background-repeat: none;\n"
                                                       "	background-color: rgb(161, 97, 79, 0);\n"
                                                       "	border-radius: 20px;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QPushButton:hover{\n"
                                                       "	border: 2px solid rgb(212, 127, 104);\n"
                                                       "}\n"
                                                       "\n"
                                                       "QPushButton:pressed{\n"
                                                       "	background-color: rgb(212, 127, 104);\n"
                                                       "}\n"
                                                       "")
                # Trocando de echomode para que a senha fique ilegível.
                self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
                self.lineEdit_password2.setEchoMode(QtWidgets.QLineEdit.Password)
                # Trocando de modo na variavel, do modo "not-lock" para "lock".
                self.password_mode = "lock"

    # Funcão para mostrar formularios que vão servir para cadastrar novos usuários e recuperar conta.
    def form(self):
        # Escondendo a frame de notificação.
        self.frame_notification.hide()
        if self.mode == "login" or self.mode == "recuperar_conta2":
            # Tratando da formatação do text do "login" para "cadastrar".
            self.title_text(text='Cadastro', size=40)
            # Modificando o posicionamento  da label de titulo.
            self.label_title_text.setGeometry(QtCore.QRect(95, -20, 250, 131))
            # Modificando o posicionamento da frame "imagen_perfil".
            self.frame_user_image.setGeometry(QtCore.QRect(159, 80, 131, 131))
            # Modificando o posicionamento das lines edits e pusbuttons.
            self.lineEdit_name_user.setGeometry(QtCore.QRect(100, 220, 250, 51))
            self.lineEdit_password.setGeometry(QtCore.QRect(100, 280, 250, 51))
            self.pushButton_password.setGeometry(QtCore.QRect(305, 285, 41, 41))
            self.pushButton_enter.setGeometry(QtCore.QRect(100, 445, 120, 41))
            self.pushButton_add.setGeometry(QtCore.QRect(248, 170, 41, 41))
            # Mudando o estilo e a "imagem" com CSS do botão cadastrar novo usuário.
            self.pushButton_add.setStyleSheet("QPushButton{\n"
                                              "    background-image: url(:/image/Images/camera1.png);\n"
                                              "    background-position: center;\n"
                                              "    background-repeat: none;\n"
                                              "    background-color: rgb(161, 97, 79);\n"
                                              "    border-radius: 20px;\n"
                                              "    border: 4px solid rgb(161, 97, 79);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "    border: 2px solid rgb(212, 127, 104);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed{\n"
                                              "    background-color: rgb(212, 127, 104);\n"
                                              "}\n"
                                              "")
            # Mudando o texto do botão "Entrar" para "Avançar".
            self.pushButton_enter.setText("Avançar")
            # Dando uma mensaggem para o usuário na line edit password
            self.lineEdit_password.setPlaceholderText("Insira a sua senha.")
            # Ocultando o botão "esqueci a minha senha"
            self.pushButton_recover_account.hide()
            # Adiçionando uma line edit "Insira novamente a senha".
            self.lineEdit_password2 = QtWidgets.QLineEdit(self.layout_main)
            self.lineEdit_password2.setGeometry(QtCore.QRect(100, 340, 250, 51))
            font = QtGui.QFont()
            font.setFamily("Microsoft YaHei UI")
            font.setPointSize(11)
            self.lineEdit_password2.setFont(font)
            # Definindo o estilo com CSS do elemento line edit.
            self.lineEdit_password2.setStyleSheet("QLineEdit{\n"
                                                  "    background-color: rgb(44, 34, 31, 160);\n"
                                                  "    border-radius: 10px;\n"
                                                  "    border: 2px solid rgb(161, 97, 79);\n"
                                                  "    padding: 10px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLineEdit:hover{\n"
                                                  "    border: 2px solid rgb(201, 131, 90);\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLineEdit:focus{\n"
                                                  "    border: 2px solid rgb(201, 131, 90);\n"
                                                  "}")
            self.lineEdit_password2.setInputMask("")
            self.lineEdit_password2.setText("")
            self.lineEdit_password2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            # Verificando o estado da line edit da senha para manter o estado de legibilidade da senha.
            if self.password_mode == "not-lock":
                # Estado na qual a senha sera legivel.
                self.lineEdit_password2.setEchoMode(QtWidgets.QLineEdit.Normal)
            else:
                # Estado na qual a senha sare ilegivel.
                self.lineEdit_password2.setEchoMode(QtWidgets.QLineEdit.Password)
            self.lineEdit_password2.setPlaceholderText("Insira novamente a senha.")
            self.lineEdit_password2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
            self.lineEdit_password2.setClearButtonEnabled(False)
            self.lineEdit_password2.setObjectName("lineEdit_password2")
            self.lineEdit_password2.show()
            if self.mode == "login":
                # Adicionando uma pusbutton "Cancelar" para sair do modo adiçionar usuário.
                self.pushButton_cancel = QtWidgets.QPushButton(self.layout_main)
                self.pushButton_cancel.setGeometry(QtCore.QRect(230, 445, 120, 41))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei UI")
                font.setPointSize(11)
                self.pushButton_cancel.setFont(font)
                self.pushButton_cancel.setStyleSheet("QPushButton{\n"
                                                     "    background-color: rgb(161, 97, 79);\n"
                                                     "    border-radius: 10px;\n"
                                                     "    padding: 10px;\n"
                                                     "    color: rgb(230, 230, 231);\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton:hover{\n"
                                                     "    border: 2px solid rgb(212, 127, 104);\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton:pressed{\n"
                                                     "    background-color: rgb(212, 127, 104);\n"
                                                     "}")
                self.pushButton_cancel.setObjectName("pushButton_cancel")
                self.pushButton_cancel.show()
                self.pushButton_cancel.setText('Cancelar')
            else:
                pass
            if self.mode == "login":
                # Mudando de modo "login" para modo "cadastrar1" que significa que as funções dos
                # botões vão mudar. 
                self.mode = "cadastro1"
            else:
                self.mode = "recuperar_conta3"
            # chamando a função back_login.
            self.pushButton_cancel.clicked.connect(lambda: self.click(event="cancel"))

        elif self.mode == "cadastro1" or self.mode == "recuperar_conta":
            # Escondendo as lines edits "Insira a sua senha", "Nome do usuário" e outros.
            self.lineEdit_password.hide()
            self.lineEdit_name_user.hide()
            self.pushButton_password.hide()
            # Deletando a line edit "Insira novamente a sua senha".
            if self.mode == "cadastro1":
                self.lineEdit_password2.deleteLater()
            else:
                pass
            # Mudar o texto botão "Avançar" para "cadastrar".
            self.pushButton_enter.setText("Cadastrar")
            # Introduzindo uma line edit "Sua resposta".
            self.lineEdit_answer = QtWidgets.QLineEdit(self.layout_main)
            self.lineEdit_answer.setGeometry(QtCore.QRect(100, 385, 250, 51))
            font = QtGui.QFont()
            font.setFamily("Microsoft YaHei UI")
            font.setPointSize(11)
            self.lineEdit_answer.setFont(font)
            self.lineEdit_answer.setStyleSheet("QLineEdit{\n"
                                               "    background-color: rgb(44, 34, 31, 160);\n"
                                               "    border-radius: 10px;\n"
                                               "    border: 2px solid rgb(161, 97, 79);\n"
                                               "    padding: 10px;\n"
                                               "}\n"
                                               "\n"
                                               "QLineEdit:hover{\n"
                                               "    border: 2px solid rgb(201, 131, 90);\n"
                                               "}\n"
                                               "\n"
                                               "QLineEdit:focus{\n"
                                               "    border: 2px solid rgb(201, 131, 90);\n"
                                               "}")
            self.lineEdit_answer.setInputMask("")
            self.lineEdit_answer.setText("")
            self.lineEdit_answer.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            self.lineEdit_answer.setPlaceholderText("Sua resposta.")
            self.lineEdit_answer.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
            self.lineEdit_answer.setClearButtonEnabled(False)
            self.lineEdit_answer.setObjectName("lineEdit_answer")
            self.lineEdit_answer.show()
            # Adicionando lines horizontais. -------  --------
            self.line_title1 = QtWidgets.QFrame(self.layout_main)
            self.line_title1.setObjectName(u"line_title1")
            self.line_title1.setGeometry(QtCore.QRect(60, 240, 118, 3))
            self.line_title1.setFrameShape(QtWidgets.QFrame.HLine)
            # Adicionando stilo com CSS na linha horizontal.
            self.line_title1.setStyleSheet("background-color: rgb(161, 97, 79);"
                                           "\n")
            self.line_title1.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_title1.show()
            self.line_title2 = QtWidgets.QFrame(self.layout_main)
            self.line_title2.setObjectName(u"line_pergunta2")
            self.line_title2.setGeometry(QtCore.QRect(275, 240, 118, 3))
            self.line_title2.setFrameShape(QtWidgets.QFrame.HLine)
            # Adicionando stilo com CSS na linha horizontal.
            self.line_title2.setStyleSheet("background-color: rgb(161, 97, 79);"
                                           "\n")
            self.line_title2.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_title2.show()

            # Adicionando uma label de sub-titulo com a seguinte frase "Pergunta de recuperação da conta" 
            self.label_title_question = QtWidgets.QLabel(self.layout_main)
            self.label_title_question.setGeometry(QtCore.QRect(100, 215, 249, 41))
            font = QtGui.QFont()
            font.setFamily("Microsoft JhengHei UI")
            font.setPointSize(12)
            self.label_title_question.setFont(font)
            self.label_title_question.setText("Pergunta de recuperação da\n conta")
            self.label_title_question.setAlignment(QtCore.Qt.AlignCenter)
            self.label_title_question.setStyleSheet("background-color: rgb(255, 170, 255, 0);\n"
                                                    "color: rgb(230, 230, 231);")
            self.label_title_question.setObjectName("label_pergunta")
            self.label_title_question.show()
            # Adiçionando uma label de Pergunta, onde serão visualizadas as perguntas de 
            # recuperação da conta.
            self.label_question = QtWidgets.QLabel(self.layout_main)
            self.label_question.setGeometry(QtCore.QRect(100, 270, 249, 80))
            font = QtGui.QFont()
            font.setFamily("Microsoft JhengHei UI")
            font.setPointSize(12)
            self.label_question.setFont(font)
            # Escolhendo uma pergunta de recuperação de conta.
            # Que esta na lista de perguntas e atribuindo o valor numerico na variavel 
            # numero da pergunta.
            self.question_number = randint(0, 7)
            self.label_question.setText(self.list_of_question[self.question_number])
            self.label_question.setAlignment(QtCore.Qt.AlignCenter)
            self.label_question.setStyleSheet("background-color: rgb(255, 170, 255, 0);\n"
                                              "color: rgb(230, 230, 231);")
            self.label_question.setObjectName("label_question")
            self.label_question.show()
            # Adicionando o botão "proximo", que vai servir ao usuário para troque de pergunta de recuperação da conta.
            self.pushButton_next_question = QtWidgets.QPushButton(self.layout_main)
            self.pushButton_next_question.setObjectName(u"pushButton_next_question")
            self.pushButton_next_question.setGeometry(QtCore.QRect(320, 330, 41, 41))
            self.pushButton_next_question.setStyleSheet(u"QPushButton{\n"
                                                        "	background-image: url(:/image/Images/next.png);\n"
                                                        "	background-position: center;\n"
                                                        "	background-repeat: none;\n"
                                                        "	background-color: rgb(161, 97, 79);\n"
                                                        "	border-radius: 20px;\n"
                                                        "	border: 4px solid rgb(161, 97, 79);\n"
                                                        "}\n"
                                                        "\n"
                                                        "QPushButton:hover{\n"
                                                        "	border: 2px solid rgb(212, 127, 104);\n"
                                                        "}\n"
                                                        "\n"
                                                        "QPushButton:pressed{\n"
                                                        "	background-color: rgb(212, 127, 104);\n"
                                                        "}\n"
                                                        "")
            self.pushButton_next_question.show()
            # Quando o usuário clicar nesse botão vai chamar a função "mudar de pergunta" que serve 
            # para trocar de pergunta de recuperação da conta caso o usuário queria.
            self.pushButton_next_question.clicked.connect(lambda: self.click(event="next_question"))
            self.pushButton_cancel.clicked.connect(lambda: self.back_login(event="cancel"))
            # mudando o modo do programa de "cadastro1" para "cadastro2".
            if self.mode == "cadastro1":
                self.mode = "cadastro2"
            else:
                # Mudando de modo do programa para para cadastro
                self.mode = "recuperar_conta2"
        else:
            pass

    # Função serve:
    # 1) para validar os dados que o usuário esta digitando. 
    # 2) para navegar entre as janela. 
    def validate(self):
        # Escondendo a frame de notificação.
        self.frame_notification.hide()
        # Verrificando o modo.
        if self.mode == "login":
            self.name_user = self.lineEdit_name_user.text()
            self.password = self.lineEdit_password.text()
            # Quando for inserido a senha e não o nome do usuário para o modo "login".
            if self.name_user == '' and self.password != '':
                # Mostrando uma notificação.
                self.notification(message="Por favor introduze o nome do usúario.")
                self.lineEdit_name_user.setFocus()
            # Quando for inserido o nome do usuário e não a senha para o modo "login".
            elif self.password == '' and self.name_user != '':
                # Mostrando uma notificação.
                self.notification(message="Por favor introduze a senha.")
                self.lineEdit_password.setFocus()
            # Quando for inserido o nome do usuário e a senha para o modo "login".
            elif self.name_user != '' and self.password != '':
                # Mostrando uma notificação.
                self.notification(message="Nemhum usúario com esse nome, cadastre-se.")
            # Quando não for inserido o nome do usuário e nem a senha para o modo "login".
            elif self.name_user == '' and self.password == '':
                # Mostrando uma notificação.
                self.notification(message="Por favor introduze a senha e o nome do usuário.")
            else:
                # Mostrando uma notificação.
                self.notification(message="Falhia desconhecida. Tente novamente.")

        elif self.mode == "cadastro1":
            self.form()

        elif self.mode == "cadastro2":
            # Quando o usuário clicar no botão cadastras.
            self.back_login(event='cadastro')

        elif self.mode == "recuperar_conta":
            self.recover_account()

        elif self.mode == "recuperar_conta2":
            self.recover_account()

        elif self.mode == "recuperar_conta3":
            self.back_login(event="concluido")
        else:
            pass

    # Esta função serve para dar um texto para label title.
    def title_text(self, text="Login", size: int = 48):
        font = QtGui.QFont()
        font.setFamily("Alba Super")
        font.setPointSize(size)
        self.label_title_text.setFont(font)
        self.label_title_text.setText(text)

    # Esta função serve para mudar o posicionamento de alguns elementos do layout.
    def posisition_of_element(self):
        # Mudando o posicionamento de dos elementos.
        self.frame_user_image.setGeometry(QtCore.QRect(159, 145, 131, 131))
        self.lineEdit_name_user.setGeometry(QtCore.QRect(100, 290, 250, 51))
        self.lineEdit_password.setGeometry(QtCore.QRect(100, 350, 250, 51))
        self.pushButton_enter.setGeometry(QtCore.QRect(100, 410, 250, 51))
        self.pushButton_password.setGeometry(QtCore.QRect(305, 355, 41, 41))
        self.pushButton_add.setGeometry(QtCore.QRect(400, 10, 41, 41))
        self.label_title_text.setGeometry(QtCore.QRect(130, 0, 191, 131))

    # Função que faz com que a tela volte ao login e ao modo "login".
    def back_login(self, event=""):
        # Escondendo a frame de notificação.
        self.frame_notification.hide()
        # Verrificando em que modo o programa está.
        if self.mode == "cadastro1" and event == "cancel":
            # Mostrando elementos escondidos(ocultos).
            self.pushButton_recover_account.show()
            # Apagando o elementos do layout.
            self.pushButton_cancel.deleteLater()
            self.lineEdit_password2.deleteLater()
            # Mudando o posicionamento de dos elementos.
            self.posisition_of_element()
            # Mudando o texto do botão "Avançar" para "Entrar".
            self.pushButton_enter.setText("Entrar")
            # Mudando o estilo "imagen" do botão adicio
            self.pushButton_add.setStyleSheet("QPushButton{\n"
                                              "    background-image: url(:/image/Images/add_user.png);\n"
                                              "    background-position: center;\n"
                                              "    background-repeat: none;\n"
                                              "    background-color: rgb(161, 97, 79);\n"
                                              "    border-radius: 20px;\n"
                                              "    border: 4px solid rgb(161, 97, 79);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "    border: 2px solid rgb(212, 127, 104);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed{\n"
                                              "    background-color: rgb(212, 127, 104);\n"
                                              "}\n"
                                              "")
            # Mudando o Titulo "cadastro" para "Login".
            self.title_text()
            # Definindo o modo do programa de "cadastro1" para "login"
            self.mode = "login"

        # Verrificando em que modo o programa está.
        elif self.mode == "cadastro2" and event == "cancel" or self.mode == "recuperar_conta2" and event == "cancel":
            # Apagando o elementos do layout.
            self.line_title1.deleteLater()
            self.line_title2.deleteLater()
            self.lineEdit_answer.deleteLater()
            self.label_title_question.deleteLater()
            self.label_question.deleteLater()
            self.pushButton_next_question.deleteLater()
            self.pushButton_cancel.deleteLater()
            # Mostrando elementos escondidos(ocultos).
            # Mostrando a line edit da senha.
            self.lineEdit_password.show()
            # Mosrando a line edit "nome do usuário".
            self.lineEdit_name_user.show()
            # Mostrando a botão "Esqueci a senha".
            self.pushButton_recover_account.show()
            # Mostrano o botão "password" para ver a senha.
            self.pushButton_password.show()
            # Mudando o posicionamento de dos elementos.
            self.posisition_of_element()
            # Mudando o texto do botão "Avançar" para "Entrar".
            self.pushButton_enter.setText("Entrar")
            # Mudando o estilo "imagen" com CSS do botão add.
            self.pushButton_add.setStyleSheet("QPushButton{\n"
                                              "    background-image: url(:/image/Images/add_user.png);\n"
                                              "    background-position: center;\n"
                                              "    background-repeat: none;\n"
                                              "    background-color: rgb(161, 97, 79);\n"
                                              "    border-radius: 20px;\n"
                                              "    border: 4px solid rgb(161, 97, 79);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "    border: 2px solid rgb(212, 127, 104);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed{\n"
                                              "    background-color: rgb(212, 127, 104);\n"
                                              "}\n"
                                              "")
            # Mudando o Titulo "cadastro" para "Login".
            self.title_text()
            # Verificando o modo do programa para mostrar o botão de cadastro que foi oculto no modo "recuperar_conta".
            if self.mode == "recuperar_conta2":
                self.pushButton_add.show()
            else:
                pass
            # Definindo o modo do programa de "cadastro1" para "login".
            self.mode = "login"

        # Esta parte da funcão só vai ser executada quando o botão "cadastrar" for clicado. 
        elif self.mode == "cadastro2" and event == "cadastro":
            # Voltando a tela de login.
            self.back_login(event="cancel")
            # Mostrando uma notificação.
            self.notification(message="Cadastro feito com sucesso.")
            # Mudando o modo do programa para "login".
            self.mode = "login"

        elif self.mode == "recuperar_conta":
            # Mudando o Titulo "conta" para "Login".
            self.title_text()
            # Mudando o posicionamento de dos elementos.
            self.posisition_of_element()
            # Mudando o texto do botão "Cancelar" para "Entrar".
            self.pushButton_enter.setText("Entrar")
            # Mostrando elementos escondidos(ocultos).
            # 1. Mostrando a line edit da senha.
            self.lineEdit_password.show()
            # 2. Mostrando a botão "Esqueci a senha".
            self.pushButton_recover_account.show()
            # 3. Mostrano o botão "password" para ver a senha.
            self.pushButton_password.show()
            # 4. Mostrando o botão para adicionar novos usuários
            self.pushButton_add.show()
            # Excluindo o botão cancelar.
            self.pushButton_cancel.deleteLater()
            # Definindo o modo do programa de "cadastro1" para "login"
            self.mode = "login"
        elif self.mode == "recuperar_conta3":
            # Deletando elementos do layout.
            self.pushButton_cancel.deleteLater()
            self.lineEdit_password2.deleteLater()
            # Mudando o Titulo "cadastro" para "Login".
            self.label_title_text.setText("Login")
            # ----------
            self.lineEdit_password.setPlaceholderText("Insira a sua senha.")
            # Mostrando elemento ocultos.
            self.lineEdit_name_user.show()
            self.pushButton_add.show()
            self.pushButton_recover_account.show()
            # Mudando o posicionamento de dos elementos.
            self.posisition_of_element()
            # Mudando o estilo "imagen" com CSS do botão add.
            self.pushButton_add.setStyleSheet("QPushButton{\n"
                                              "    background-image: url(:/image/Images/add_user.png);\n"
                                              "    background-position: center;\n"
                                              "    background-repeat: none;\n"
                                              "    background-color: rgb(161, 97, 79);\n"
                                              "    border-radius: 20px;\n"
                                              "    border: 4px solid rgb(161, 97, 79);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "    border: 2px solid rgb(212, 127, 104);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed{\n"
                                              "    background-color: rgb(212, 127, 104);\n"
                                              "}\n"
                                              "")
            # Mudando o texto do botão "Concluir" para "Entrar".
            self.pushButton_enter.setText("Entrar")
            if event == "concluido":
                self.notification(message="Nova senha salva. Faça o login agora!")
            else:
                pass
            # Mudando o modo do programa.
            self.mode = "login"


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
