# 📜 Changelog – Agent_News

## [0.1.0] – 2025-06-09

### Ajouté
- Structure complète modulaire
- Collecte RSS dynamique + personnalisée (`feeds.txt`)
- Analyse IA via 1min.ai avec fallback DeepSeek
- Journalisation complète dans `logs/agent_news.log`
- Script CLI `Anews` global
- Support Discord et Telegram avec gestion des erreurs

### Corrigé
- Tronquage des messages trop longs pour Discord
- Filtrage des actualités sensibles (violence, guerre...)
- Relance automatique sur erreur 423 (content policy)

