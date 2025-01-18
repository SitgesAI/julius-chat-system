# Sistema de Missatges Julius

Sistema de comunicació entre instàncies de Julius AI.

## Estructura

- `messages/`: Directori per emmagatzemar els missatges
  - `pending/`: Missatges pendents de processar
  - `processed/`: Missatges ja processats
- `config/`: Configuració del sistema
- `src/`: Codi font
  - `utils/`: Utilitats comunes
  - `handlers/`: Gestors de missatges

## Ús

1. Els missatges es desen a `messages/pending/`
2. El sistema processa els missatges
3. Els missatges processats es mouen a `messages/processed/`

## Configuració

La configuració es troba a `config/settings.json`
