# Comandes Disponibles

Aquest document manté un registre de les comandes personalitzades disponibles per a les instàncies de Julius.

## Sistema de Missatges

### Enviar Missatge
```python
# A través del repositori github.com/SitgesAI/julius-chat-system
# Els missatges es guarden a messages/pending/{msg_id}.json

format = {
    "id": "msg_YYYYMMDD_HHMMSS",
    "sender": "Julius1/Julius2",
    "receiver": "Pau",
    "content": "Contingut del missatge",
    "timestamp": "2025-01-18T00:00:00.000000",
    "status": "pending",
    "tags": ["tag1", "tag2"]
}
```

### Llegir Missatges
```python
# Revisar missatges pendents al directori messages/pending/
# Un cop processats, moure'ls a messages/processed/
```

## Sistema Antic (Deprecat)
⚠️ El sistema de missatges basat en julius_chat.json està deprecat i serà eliminat properament.
Utilitzar el nou sistema basat en GitHub.

---
## Com Afegir Noves Comandes

1. Crear una nova secció en aquest document
2. Documentar:
   - Nom de la comanda
   - Descripció
   - Format/Paràmetres
   - Exemple d'ús
3. Fer PR amb els canvis
