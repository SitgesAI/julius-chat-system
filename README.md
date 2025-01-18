# Sistema de Missatges Julius

Sistema simple de comunicació entre instàncies de Julius AI.

## Estructura

- `messages/`: Directori per emmagatzemar els missatges
  - `pending/`: Missatges pendents de processar
  - `processed/`: Missatges ja processats

## Format dels Missatges

Els missatges es guarden en format JSON amb l'estructura:

```json
{
  "id": "msg_YYYYMMDD_HHMMSS",
  "sender": "Julius1/Julius2",
  "receiver": "Pau",
  "content": "Contingut del missatge",
  "timestamp": "2025-01-18T00:00:00.000000",
  "status": "pending/processed",
  "tags": ["tag1", "tag2"]
}
```

## Ús

1. Els missatges nous es desen a `messages/pending/`
2. Un cop llegits/processats, es mouen a `messages/processed/`
