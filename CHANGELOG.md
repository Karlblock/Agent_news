
## [v0.4.0] - 2025-06-10
### Nouveautés
- ✅ Interface CLI enrichie : sélection interactive du modèle et de la catégorie via `prompt_toolkit` + `rich`
- ✅ Support complet du modèle `deepseek-chat` (par défaut)
- ✅ Intégration initiale de Mistral (`mistral-large-latest`) via API Mistral.ai (clé à configurer)
- ✅ Réécriture de `analyze_with_model()` pour simplification, suppression du support 1min.ai
- ✅ Ajout du tri des news récentes (moins de 24h) dans `news_fetcher.py`
- ✅ Sauvegarde automatique des prompts/réponses dans `data/training_examples/{topic}/...`
- ✅ Ajout de `feeds.txt` pour une personnalisation des flux par sujet (non bloquant)

### Améliorations
- 🔁 Refonte complète du fichier `main.py` (structure plus modulaire et lisible)
- 🧼 Meilleure gestion des erreurs RSS et nettoyage des titres obsolètes (ex : années passées)
- 🧪 Ajout d’un mode debug (`get_rss_news(topic, debug=True)`) pour inspecter les flux

### Suppressions
- ❌ Suppression de l’ancienne API 1min.ai
- ❌ Suppression de `migrate_structure.sh`

---

## Historique précédent
Consulte `CHANGELOG.md` ou les releases GitHub pour les versions antérieures.
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

