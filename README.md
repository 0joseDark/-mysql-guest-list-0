### Guia para Configurar o Ambiente e Executar o Script
- English [English](https://www.python.org/downloads/) 
Aqui está um guia detalhado para configurar o ambiente no Windows 10 e executar o script de gestão de convidados:

---

#### 1. **Instalar o Python**
   - Faça o download do Python a partir do site oficial: [python.org/downloads](https://www.python.org/downloads/).
   - Durante a instalação, **marque a opção "Add Python to PATH"** para facilitar o uso do Python no terminal.
   - Verifique a instalação abrindo o terminal (ou `cmd`) e digitando:
     ```bash
     python --version
     ```

---

#### 2. **Instalar o MySQL**
   - Faça o download e instale o MySQL Community Server a partir do site oficial: [dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/).
   - Durante a instalação:
     1. Configure uma senha para o usuário `root` (anote essa senha, pois será usada no script).
     2. Escolha a configuração padrão para ativar o MySQL como um serviço no Windows.
   - Após a instalação, abra o **MySQL Workbench** (se incluído) ou conecte-se ao MySQL pelo terminal usando:
     ```bash
     mysql -u root -p
     ```
   - Insira a senha configurada.
=======
  **lista de convidados com mysql**
 - Aplicação de gestão de convidados com interface gráfica, utilizando MySQL para armazenar e gerir os dados.
### Explicações:
1. **Banco de Dados MySQL**:
   - O script cria uma base de dados chamada `convidados_db` e uma tabela `convidados`.
   - Armazena os campos: `nome`, `palavra_passe`, `email`, e `telefone`.

---

#### 3. **Instalar os Módulos Necessários**
   - Abra o terminal ou `cmd` e instale o módulo `mysql-connector-python` com o comando:
     ```bash
     pip install mysql-connector-python
     ```

---

#### 4. **Configurar o Banco de Dados**
   - O script automaticamente cria a base de dados e a tabela necessárias. Certifique-se de que as credenciais do MySQL no script (host, usuário, senha) estão corretas:
     ```python
     conexao = mysql.connector.connect(
         host="localhost",
         user="root",
         password="sua_senha"  # Substitua 'sua_senha' pela senha configurada no MySQL
     )
     ```
   - Se necessário, pode testar a conexão com o MySQL antes de executar o script:
     ```python
     import mysql.connector

     try:
         conexao = mysql.connector.connect(
             host="localhost",
             user="root",
             password="sua_senha"
         )
         print("Conexão bem-sucedida!")
         conexao.close()
     except mysql.connector.Error as err:
         print(f"Erro: {err}")
     ```

---

#### 5. **Executar o Script**
   - Salve o script Python num ficheiro com extensão `.py` (por exemplo, `gestao_convidados.py`).
   - Execute o script no terminal digitando:
     ```bash
     python gestao_convidados.py
     ```
   - A janela da aplicação abrirá com os campos e botões para gerir os convidados.

---

#### 6. **Utilizar a Aplicação**
   - **Adicionar Convidados**:
     1. Preencha os campos `Nome`, `Palavra-passe`, `E-mail`, e `Telefone`.
     2. Clique no botão "Adicionar".
   - **Listar Convidados**:
     - Os convidados adicionados aparecem na lista automaticamente.
   - **Remover Convidados**:
     1. Selecione um convidado na lista.
     2. Clique no botão "Remover".

---

#### 7. **Erros Comuns e Soluções**
   - **Erro de conexão ao MySQL**:
     - Verifique se o serviço MySQL está em execução no Windows. Pode iniciar o serviço manualmente:
       ```bash
       net start MySQL
       ```
   - **Erro "ModuleNotFoundError"**:
     - Verifique se o módulo `mysql-connector-python` foi instalado corretamente:
       ```bash
       pip install mysql-connector-python
       ```
   - **Credenciais Inválidas**:
     - Confirme que o usuário, senha e host no script correspondem à configuração do MySQL.
