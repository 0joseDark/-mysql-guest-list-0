#  mysql-guest-list-0
  **lista de convidados com mysql**
 - Aplicação de gestão de convidados com interface gráfica, utilizando MySQL para armazenar e gerir os dados.
### Explicações:
1. **Banco de Dados MySQL**:
   - O script cria uma base de dados chamada `convidados_db` e uma tabela `convidados`.
   - Armazena os campos: `nome`, `palavra_passe`, `email`, e `telefone`.

2. **Interface Gráfica**:
   - Usa `tkinter` para criar a janela, campos de entrada e botões.
   - Exibe os convidados numa caixa de listagem (`Listbox`).

3. **Funcionalidades**:
   - **Adicionar**: Salva um convidado na base de dados.
   - **Remover**: Remove o convidado selecionado.
   - **Listar**: Atualiza a lista de convidados automaticamente após alterações.

4. **Módulos Necessários**:
   - `mysql-connector-python`: Para comunicação com o MySQL.
    ```bash
     pip install mysql-connector-python
     ```
   - `tkinter`: Para a interface gráfica.

5. **Instruções**:
   - Execute o script com o Python 3 instalado no Windows 10.
   - Certifique-se de que o MySQL está em execução e a senha está corretamente configurada no código.
