
# Automação de Backup e Restauração do Banco de Dados PostgreSQL

Este projeto automatiza o processo de renomear um banco de dados PostgreSQL, criar um novo banco e restaurar um backup a partir de um arquivo `.backup`. O script foi desenvolvido em Python utilizando as bibliotecas `psycopg2` para interação com o PostgreSQL e `subprocess` para executar o utilitário `pg_restore`.

## Requisitos

- Python 3.10 ou superior
- PostgreSQL instalado e rodando
- PyInstaller (opcional, para criar executáveis)


## Instalação

### 1. Clonar o repositório
Clone este repositório no seu ambiente local:
```bash
git clone https://github.com/seu-repositorio.git
cd seu-repositorio
```

### 2. Instalar as dependências
Instale as dependências necessárias usando o `pip`:
```bash
pip install psycopg2
```

## Como Executar

1. Certifique-se de que o banco de dados PostgreSQL está rodando e acessível.
2. Execute o script Python:
   ```bash
   python automacao_pgadmin.py
   ```
3. O script irá:
   - Renomear o banco de dados `ERP` para `ERP_OLD`.
   - Criar um novo banco de dados `ERP`.
   - Restaurar o backup a partir de um arquivo `.backup` localizado na pasta `C:\linetech\baserestaurada`.

### Geração de Executável (Opcional)
Caso deseje gerar um executável para rodar o script sem depender do Python instalado, utilize o **PyInstaller**:

```bash
pyinstaller --onefile automacao_pgadmin.py
```

O executável será gerado na pasta `dist`.

## Estrutura do Projeto

```
.
├── automacao_pgadmin.py  # Script principal
├── README.md             # Este arquivo de documentação
└── dist/                 # Pasta gerada pelo PyInstaller contendo o executável
```

## Personalizações

Você pode ajustar o script conforme necessário:
- Alterar o nome do banco de dados ou a localização do backup.
- Adicionar novas funcionalidades, como notificações após a execução.

## Licença

Este projeto está licenciado sob a licença MIT. Sinta-se à vontade para usar e modificar conforme necessário.
