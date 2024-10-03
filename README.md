# Calculadora de IMC

Esta é uma aplicação de **Calculadora de IMC (Índice de Massa Corporal)** desenvolvida com **PySide6** (Qt for Python). A interface gráfica permite que o usuário insira seu peso e altura para calcular o IMC e exibe uma classificação com base no resultado.

## Funcionalidades

- **Entrada de peso e altura**: O usuário pode inserir seu peso em kg e altura em cm.
- **Cálculo do IMC**: O IMC é calculado e exibido juntamente com uma classificação da condição física (Baixo peso, Peso normal, Sobrepeso, Obesidade grau 1, 2 ou 3).
- **Limpeza dos campos**: Opção de limpar os campos de entrada para realizar novos cálculos.
- **Tratamento de erros**: Verificação de entradas inválidas, como campos vazios ou valores não numéricos.

## Classificação do IMC

A classificação segue a seguinte tabela:

| IMC                | Classificação                                      |
|--------------------|---------------------------------------------------|
| Menor que 18.5     | Baixo peso: Consulte um nutricionista              |
| 18.5 a 24.9        | Peso normal: Parabéns, mantenha o estilo de vida!  |
| 25 a 29.9          | Sobrepeso: Atenção, adote hábitos mais saudáveis   |
| 30 a 34.9          | Obesidade grau 1: Procure acompanhamento médico    |
| 35 a 39.9          | Obesidade grau 2: Risco elevado, busque orientação |
| Maior que 40       | Obesidade grau 3 (mórbida): Alerta crítico!        |

## Tecnologias Utilizadas

- **Python 3.8+**
- **PySide6**: Biblioteca para criar a interface gráfica.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/calculadora-imc.git
Navegue até o diretório do projeto:

bash
Copiar código
cd calculadora-imc
Crie um ambiente virtual:

bash
Copiar código
python -m venv venv
Ative o ambiente virtual:

No Windows:
bash
Copiar código
venv\Scripts\activate
No Linux/MacOS:
bash
Copiar código
source venv/bin/activate
Instale as dependências:

bash
Copiar código
pip install PySide6
Como executar
Após instalar as dependências, execute o arquivo principal da aplicação:

bash
Copiar código
python main.py
Contribuição
Se você deseja contribuir para o projeto, siga estas etapas:

Fork o repositório.
Crie uma nova branch (git checkout -b feature/nova-funcionalidade).
Faça suas alterações e commit (git commit -m 'Adiciona nova funcionalidade').
Envie para sua branch (git push origin feature/nova-funcionalidade).
Abra um pull request.
