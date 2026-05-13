# Rclone Skill

Uma skill potente para gerenciamento avançado de armazenamento em nuvem usando [rclone](https://rclone.org/). Ideal para automação de transferências, backups criptografados, sincronização de dados e gerenciamento de múltiplos provedores de armazenamento.

## 🚀 Características

- **Suporte a 150+ provedores** de armazenamento em nuvem (Google Drive, S3, Dropbox, OneDrive, Box, etc.)
- **Operações avançadas**: sincronização, cópia, movimentação e backup de dados
- **Criptografia integrada** com backend `crypt` do rclone
- **Scripts Python** para automação e integração programática
- **Documentação completa** com referências de comandos e guias de configuração
- **Dry-run e progresso** para operações seguras

## 📋 Conteúdo

```
rclone-skill/
├── README.md                          # Este arquivo
├── SKILL.md                           # Documentação detalhada da skill
├── scripts/
│   ├── configure_remote.py            # Script para configurar remotes programaticamente
│   └── rclone_operations.py           # Funções Python para operações comuns
├── references/
│   ├── commands_reference.md          # Referência completa de comandos rclone
│   └── supported_providers.md         # Lista de provedores suportados
└── templates/
    └── rclone.conf.template           # Template de arquivo de configuração
```

## 🔧 Pré-requisitos

- **rclone** instalado ([guia de instalação](https://rclone.org/install/))
- **Python 3.6+** (para usar os scripts)
- Credenciais configuradas para os provedores de nuvem desejados

Verifique a instalação:
```bash
rclone version
rclone listremotes
```

## 🚀 Quick Start

### 1. Configurar um Remote

Usando o assistente interativo:
```bash
rclone config
```

Ou programaticamente via script Python:
```python
from scripts.configure_remote import configure_remote
configure_remote("mygdrive", "drive", client_id="...", client_secret="...")
```

### 2. Verificar Espaço em Disco

```bash
rclone about mygdrive:
```

### 3. Sincronizar Dados

Com simulação (recomendado para primeira execução):
```bash
rclone sync /caminho/local mygdrive:backup --dry-run -P
```

Execução real:
```bash
rclone sync /caminho/local mygdrive:backup -P
```

### 4. Usar Scripts Python

```python
from scripts.rclone_operations import sync_data, copy_data

# Sincronizar com dry-run
sync_data("/dados/local", "mygdrive:backup", dry_run=True, progress=True)

# Copiar dados
copy_data("mygdrive:fotos", "/dados/local/fotos", progress=True)
```

## 📚 Documentação

- **[SKILL.md](SKILL.md)** - Guia completo de uso, fluxos de trabalho, padrões de comando e dicas de performance
- **[references/commands_reference.md](references/commands_reference.md)** - Referência detalhada de todos os comandos rclone
- **[references/supported_providers.md](references/supported_providers.md)** - Lista de provedores suportados com exemplos de configuração

## 🔐 Segurança

- Use `--dry-run` antes de executar operações destrutivas
- Para dados sensíveis, utilize o backend `crypt` do rclone
- Nunca armazene senhas em texto claro em scripts
- Use variáveis de ambiente ou o sistema `obscure` do rclone

## 📊 Padrões Comuns

### Backup de Dados
```bash
rclone copy /home/usuario/documentos mygdrive:backups --update --use-server-modtime
```

### Sincronizar Múltiplos Diretórios
```bash
rclone sync /dados/fotos myremote:fotos -P
rclone sync /dados/videos myremote:videos -P
```

### Limitar Banda
```bash
rclone copy /dados myremote:backup --bwlimit 5M
```

### Listar Arquivos
```bash
rclone ls mygdrive:backup
rclone tree mygdrive:backup
```

## 💡 Dicas de Performance

- **Muitos arquivos pequenos**: Aumente `--transfers` e `--checkers`
- **S3/Object Storage**: Use `--fast-list` para reduzir custos de API
- **Limitação de banda**: Use `--bwlimit` para não saturar a rede
- **Verificação de hash**: Use `--checksum` para validar integridade

## 🤝 Contribuindo

Sinta-se à vontade para enviar issues e pull requests com melhorias, correções e novos recursos.

## 📄 Licença

Este projeto está licenciado sob a MIT License.

## 🔗 Recursos Úteis

- [Documentação oficial do rclone](https://rclone.org/docs/)
- [Guia de configuração por provedor](https://rclone.org/#providers)
- [Fórum comunitário rclone](https://forum.rclone.org/)