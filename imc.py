import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class IMCApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora de IMC")
        
        # Layout da aplicação
        layout = QVBoxLayout()

        # Campo de entrada de peso
        self.label_peso = QLabel("Peso (kg):")
        layout.addWidget(self.label_peso)
        self.entry_peso = QLineEdit(self)
        layout.addWidget(self.entry_peso)

        # Campo de entrada de altura
        self.label_altura = QLabel("Altura (cm):")
        layout.addWidget(self.label_altura)
        self.entry_altura = QLineEdit(self)
        layout.addWidget(self.entry_altura)

        # Botão para calcular o IMC
        self.botao_calcular = QPushButton("Calcular IMC", self)
        self.botao_calcular.clicked.connect(self.calcular_imc)
        layout.addWidget(self.botao_calcular)

        # Botão para limpar os campos
        self.botao_limpar = QPushButton("Limpar", self)
        self.botao_limpar.clicked.connect(self.limpar_campos)
        layout.addWidget(self.botao_limpar)

        # Definir o layout da janela
        self.setLayout(layout)

    def calcular_imc(self):
        try:
            # Verifica se os campos não estão vazios
            peso_text = self.entry_peso.text().strip()
            altura_text = self.entry_altura.text().strip()

            if not peso_text or not altura_text:
                raise ValueError("Campos de peso e altura não podem estar vazios.")

            peso = float(peso_text)
            altura = float(altura_text)

            # Verifica se os valores são positivos
            if peso <= 0 or altura <= 0:
                raise ValueError("Peso e altura devem ser valores positivos.")

            # Converter altura de cm para metros
            altura_metros = altura / 100
            imc = peso / (altura_metros ** 2)

            # Classificação do IMC
            if imc < 18.5:
                classificacao = (
                    "Baixo peso: Seu IMC está abaixo do recomendado. "
                    "É importante consultar um nutricionista para ajustar sua alimentação."
                )
            elif 18.5 <= imc < 25:
                classificacao = (
                    "Peso normal: Parabéns! Seu IMC está dentro da faixa saudável. "
                    "Continue mantendo uma alimentação equilibrada e um estilo de vida ativo."
                )
            elif 25 <= imc < 30:
                classificacao = (
                    "Sobrepeso: Atenção! Seu IMC indica sobrepeso. "
                    "Tente adotar hábitos saudáveis para melhorar sua qualidade de vida."
                )
            elif 30 <= imc < 35:
                classificacao = (
                    "Obesidade grau 1: Cuidado! Seu IMC está em um nível de risco. "
                    "Recomenda-se buscar acompanhamento médico para evitar problemas de saúde."
                )
            elif 35 <= imc < 40:
                classificacao = (
                    "Obesidade grau 2: Seu IMC está em um nível elevado de risco. "
                    "É muito importante procurar um médico para orientação profissional."
                )
            else:
                classificacao = (
                    "Obesidade grau 3 (mórbida): Alerta! Seu IMC está em um nível crítico. "
                    "Procure ajuda médica com urgência para melhorar sua saúde e qualidade de vida."
                )

            resultado_texto = f"O seu IMC é: {imc:.2f}\nClassificação: {classificacao}"
            QMessageBox.information(self, "Resultado IMC", resultado_texto)

        except ValueError as e:
            # Exibe uma mensagem de erro apropriada
            QMessageBox.warning(self, "Erro", str(e))

    def limpar_campos(self):
        self.entry_peso.clear()
        self.entry_altura.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    janela = IMCApp()
    janela.show()

    sys.exit(app.exec())
