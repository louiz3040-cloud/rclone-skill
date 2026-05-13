---
name: rclone-manager
description: "Gerenciamento avançado de armazenamento em nuvem usando rclone. Use para: configurar remotes, sincronizar arquivos, realizar backups criptografados, montar unidades de nuvem e gerenciar múltiplos provedores (Google Drive, S3, Dropbox, etc.)."
---

# Rclone Manager

Esta skill capacita o agente a gerenciar eficientemente diversos serviços de armazenamento em nuvem através da ferramenta `rclone`.

## Fluxo de Trabalho Principal

### 1. Verificação de Ambiente
Antes de iniciar operações, verifique se o rclone está instalado e quais remotes estão disponíveis:
- Execute `rclone version` para verificar a instalação.
- Execute `rclone listremotes` para ver os serviços configurados.

### 2. Operações de Transferência
Ao mover ou copiar dados, siga este padrão:
1. **Análise:** Verifique o tamanho dos dados com `rclone size source:path`.
2. **Simulação:** Sempre execute com `--dry-run` primeiro para operações destrutivas ou grandes volumes.
3. **Execução:** Use `-P` para monitorar o progresso em tempo real.

### 3. Gerenciamento de Configuração
- Para criar novos remotes programaticamente: `rclone config create <name> <type> [key=value]...`
- Para obter informações de cota: `rclone about remote:`

## Padrões de Comando

### Sincronização (Cuidado: Deleta no destino)
```bash
rclone sync /caminho/local remote:backup --dry-run
```

### Cópia de Segurança
```bash
rclone copy /caminho/local remote:backup --update --use-server-modtime
```

### Verificação de Integridade
```bash
rclone copy /caminho/local remote:backup --update --use-server-modtime
```

## Dicas de Performance
- **Muitos arquivos pequenos:** Aumente `--transfers` e `--checkers`.
- **Limitação de Banda:** Use `--bwlimit 5M` para não saturar a rede.
- **S3/Object Storage:** Use `--fast-list` para reduzir custos de API e acelerar a listagem.

## Segurança
- Ao lidar com dados sensíveis, recomende sempre o uso do backend `crypt`.
- Nunca armazene senhas em texto claro em scripts; use o sistema de `obscure` do rclone ou variáveis de ambiente.

## Recursos da Skill

Esta skill inclui os seguintes recursos para auxiliar nas operações com rclone:

### Scripts (`scripts/`)
- `configure_remote.py`: Script Python para configurar novos remotes rclone de forma programática. Útil para automação e integração.
- `rclone_operations.py`: Script Python com funções para executar operações comuns do rclone como `sync`, `copy` e `move`, com suporte a `dry-run` e `progress`.

### Referências (`references/`)
- `commands_reference.md`: Documento detalhado com os comandos rclone mais importantes, suas opções e exemplos de uso.
- `supported_providers.md`: Lista dos provedores de armazenamento em nuvem suportados pelo rclone, com descrições e exemplos de configuração.

### Templates (`templates/`)
- `rclone.conf.template`: Um template para o arquivo de configuração do rclone (`rclone.conf`), facilitando a criação de novas configurações.

Para utilizar esses recursos, o agente deve referenciar os arquivos conforme necessário durante a execução das tarefas.
