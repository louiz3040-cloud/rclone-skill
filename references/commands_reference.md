# Referência de Comandos Rclone

Este documento lista os comandos rclone mais utilizados e suas principais funcionalidades.

## Comandos de Configuração

- `rclone config`: Inicia o assistente interativo para criar, editar ou excluir remotes. Essencial para a configuração inicial de qualquer serviço de nuvem.
- `rclone config create <name> <type> [key=value]...`: Cria um novo remote de forma não interativa, útil para automação. Exemplo: `rclone config create gdrive drive client_id=xxx client_secret=yyy scope=drive`.
- `rclone listremotes`: Lista todos os remotes configurados no arquivo `rclone.conf`.
- `rclone about remote:`: Exibe informações de cota e uso para um remote específico. Exemplo: `rclone about gdrive:`.

## Comandos de Transferência de Dados

- `rclone copy source:path dest:path`: Copia arquivos e diretórios da origem para o destino. Arquivos idênticos (mesmo tamanho e data de modificação, ou hash se disponível) são ignorados. Não deleta arquivos no destino.
- `rclone sync source:path dest:path`: Sincroniza a origem com o destino, tornando o destino idêntico à origem. **CUIDADO**: Este comando pode deletar arquivos no destino que não existem na origem.
- `rclone move source:path dest:path`: Move arquivos e diretórios da origem para o destino. Após a transferência bem-sucedida, os arquivos são deletados na origem.
- `rclone copyto source:path dest:path`: Copia um único arquivo da origem para o destino, renomeando-o se necessário.
- `rclone moveto source:path dest:path`: Move um único arquivo da origem para o destino, renomeando-o se necessário.

## Comandos de Gerenciamento de Arquivos e Diretórios

- `rclone delete remote:path`: Deleta arquivos no `remote:path` que correspondem aos filtros especificados. Não deleta diretórios vazios.
- `rclone purge remote:path`: Deleta o diretório `remote:path` e todo o seu conteúdo, incluindo subdiretórios e arquivos. **CUIDADO**: Operação destrutiva e irreversível.
- `rclone mkdir remote:path`: Cria um novo diretório no remote.
- `rclone rmdir remote:path`: Remove um diretório vazio no remote.
- `rclone rmdirs remote:path`: Remove diretórios vazios recursivamente no remote.

## Comandos de Listagem e Verificação

- `rclone ls remote:path`: Lista os arquivos no `remote:path` com seus tamanhos e caminhos.
- `rclone lsd remote:path`: Lista apenas os diretórios no `remote:path`.
- `rclone lsf remote:path`: Lista arquivos e diretórios em um formato mais fácil de parsear.
- `rclone lsjson remote:path`: Lista arquivos e diretórios em formato JSON, útil para processamento programático.
- `rclone size remote:path`: Exibe o tamanho total e o número de objetos no `remote:path`.
- `rclone tree remote:path`: Exibe a estrutura de diretórios do `remote:path` em formato de árvore.
- `rclone check source:path dest:path`: Verifica se os arquivos na origem e no destino correspondem (tamanho e hash). Útil para verificar a integridade de transferências.
- `rclone cryptcheck remote:path`: Verifica a integridade de um remote criptografado.

## Comandos Avançados

- `rclone mount remote:path /local/mountpoint`: Monta um remote como um sistema de arquivos local. Requer FUSE (Linux/macOS) ou WinFsp (Windows).
- `rclone serve <protocol> remote:path`: Serve o conteúdo de um remote através de um protocolo específico (HTTP, FTP, WebDAV, S3, etc.).
- `rclone obscure "password"`: Obscurece uma senha para ser usada no arquivo de configuração do rclone, aumentando a segurança.

## Opções Globais Comuns

- `--dry-run`: Realiza uma simulação da operação sem fazer alterações reais. **Altamente recomendado para comandos destrutivos.**
- `-P` ou `--progress`: Exibe o progresso da transferência em tempo real.
- `-v` ou `--verbose`: Aumenta o nível de verbosidade do log.
- `--bwlimit <rate>`: Limita a largura de banda de upload/download (ex: `--bwlimit 10M` para 10 Megabytes/s).
- `--transfers <num>`: Define o número de arquivos sendo transferidos simultaneamente (padrão: 4).
- `--checkers <num>`: Define o número de verificações de hash sendo realizadas simultaneamente (padrão: 8).
- `--exclude "pattern"`: Exclui arquivos que correspondem ao padrão (glob ou regex).
- `--include "pattern"`: Inclui apenas arquivos que correspondem ao padrão.
- `--min-size <size>`: Inclui apenas arquivos maiores que o tamanho especificado (ex: `100M`, `1G`).
- `--max-size <size>`: Inclui apenas arquivos menores que o tamanho especificado.
- `--min-age <duration>`: Inclui apenas arquivos mais antigos que a duração especificada (ex: `1d`, `2w`).
- `--max-age <duration>`: Inclui apenas arquivos mais novos que a duração especificada.
