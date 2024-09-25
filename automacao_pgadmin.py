import psycopg2
import os
import subprocess

# Função para conectar ao banco de dados PostgreSQL
def conectar_postgres(database="postgres"):
    try:
        # Conecta ao banco postgres padrão (você pode modificar se necessário)
        conexao = psycopg2.connect(
            host="localhost",
            database=database,
            user="xxxxxxx",  # ajuste se seu usuário for diferente
            password="xxxxxxx", # ajuste se sua senha for diferente
            port="xxxx"
        )
        conexao.autocommit = True  # Habilitar autocommit para execução dos comandos
        return conexao
    except Exception as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None

# Função para renomear a base de dados ERP para ERP-OLD
def renomear_base(conexao):
    try:
        cursor = conexao.cursor()
        # Comando SQL usando aspas duplas para lidar com case-sensitive
        cursor.execute('ALTER DATABASE "ERP" RENAME TO "ERP_OLD";')
        print("Base de dados renomeada para ERP-OLD.")
    except Exception as erro:
        print(f"Erro ao renomear a base de dados: {erro}")

# Função para criar uma nova base de dados ERP
def criar_base(conexao):
    try:
        cursor = conexao.cursor()
        # Comando SQL usando aspas duplas para garantir o nome correto da base de dados
        cursor.execute('CREATE DATABASE "ERP";')
        print("Nova base de dados ERP criada.")
    except Exception as erro:
        print(f"Erro ao criar a base de dados: {erro}")

# Função para restaurar o backup usando pg_restore
def restaurar_backup():
    caminho_backup = "C:\\linetech\\baserestaurada"  # Caminho da pasta onde estão os backups
    arquivos = os.listdir(caminho_backup)  # Lista os arquivos disponíveis na pasta
    
    # Exibe os arquivos para o usuário escolher qual restaurar
    print("Arquivos disponíveis para restauração:")
    for i, arquivo in enumerate(arquivos):
        print(f"{i}: {arquivo}")
    
    escolha = int(input("Escolha o número do arquivo que deseja restaurar: "))
    arquivo_escolhido = arquivos[escolha]
    
    # Monta o caminho completo do arquivo escolhido
    caminho_arquivo = os.path.join(caminho_backup, arquivo_escolhido)
    
    # Caminho completo para pg_restore
    pg_restore_path = "C:\\Program Files\\PostgreSQL\\9.3\\bin\\pg_restore"
    
    # Comando para restaurar o backup usando pg_restore
    comando_restore = [
        pg_restore_path,  # Caminho completo para pg_restore
        "--host", "localhost",
        "--port", "xxxx",
        "--username", "xxxxxxx",
        "--dbname", "ERP",  # Nome da base de dados, com letras maiúsculas
        "--no-password",  # Se não quiser pedir senha
        "--verbose",  # Para mostrar os detalhes da restauração
        caminho_arquivo
    ]
    
    # Executa o comando no sistema
    try:
        subprocess.run(comando_restore, check=True)
        print("Restauração concluída com sucesso.")
    except Exception as erro:
        print(f"Erro ao restaurar o backup: {erro}")

# Função principal para rodar todas as etapas
def main():
    # Conectando ao banco
    conexao = conectar_postgres()
    
    if conexao:
        # Renomeia a base ERP para ERP-OLD
        renomear_base(conexao)
        
        # Cria nova base ERP
        criar_base(conexao)
        
        # Restaura o backup
        restaurar_backup()

# Executa o script
if __name__ == "__main__":
    main()
