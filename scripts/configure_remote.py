import subprocess
import json

def configure_remote(name, type, options=None):
    """Configura um novo remote rclone de forma programática."""
    cmd = ["rclone", "config", "create", name, type]
    if options:
        for key, value in options.items():
            cmd.append(f"{key}={value}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"Remote '{name}' configurado com sucesso.\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao configurar remote '{name}':\n{e.stderr}")
        raise

def list_remotes():
    """Lista todos os remotes configurados."""
    cmd = ["rclone", "listremotes"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"Remotes configurados:\n{result.stdout}")
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"Erro ao listar remotes:\n{e.stderr}")
        raise

if __name__ == "__main__":
    # Exemplo de uso:
    # configure_remote("meu_drive", "drive", {"scope": "drive", "client_id": "...", "client_secret": "..."})
    # list_remotes()
    pass
