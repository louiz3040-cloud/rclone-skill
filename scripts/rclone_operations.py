import subprocess

def run_rclone_command(command, source, destination, dry_run=True, progress=False, extra_args=None):
    """Executa um comando rclone com opções de dry-run e progresso."""
    cmd = ["rclone", command, source, destination]
    if dry_run:
        cmd.append("--dry-run")
    if progress:
        cmd.append("-P")
    if extra_args:
        cmd.extend(extra_args)

    print(f"Executando comando: {" ".join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"Comando rclone '{command}' executado com sucesso.\n{result.stdout}")
        if result.stderr:
            print(f"Erros/Warnings: {result.stderr}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar comando rclone '{command}':\n{e.stderr}")
        raise

def sync_data(source, destination, dry_run=True, progress=False, extra_args=None):
    """Sincroniza dados de source para destination (cuidado: pode deletar no destino)."""
    print(f"Iniciando sincronização de {source} para {destination} (dry_run={dry_run})")
    return run_rclone_command("sync", source, destination, dry_run, progress, extra_args)

def copy_data(source, destination, dry_run=False, progress=False, extra_args=None):
    """Copia dados de source para destination."""
    print(f"Iniciando cópia de {source} para {destination}")
    return run_rclone_command("copy", source, destination, dry_run, progress, extra_args)

def move_data(source, destination, dry_run=True, progress=False, extra_args=None):
    """Move dados de source para destination (dry_run padrão para segurança)."""
    print(f"Iniciando movimentação de {source} para {destination} (dry_run={dry_run})")
    return run_rclone_command("move", source, destination, dry_run, progress, extra_args)

if __name__ == "__main__":
    # Exemplo de uso:
    # sync_data("/home/ubuntu/local_data", "myremote:backup", dry_run=True, progress=True)
    # copy_data("myremote:photos", "/home/ubuntu/local_photos", progress=True)
    pass
