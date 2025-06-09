# Makefile pour Agent_News

install:
	./install.sh

update:
	unzip -o Agent_News_Final_Patch.zip

run:
	Anews "$(topic)"

test:
	Anews "IA"

logs:
	tail -n 50 logs/agent_news.log

clean-logs:
	rm -f logs/agent_news.log

help:
	@echo "📘 Commandes disponibles :"
	@echo "  make install       → Installation complète du projet"
	@echo "  make update        → Appliquer les derniers correctifs (patch)"
	@echo "  make run topic=IA  → Lancer une analyse sur un sujet"
	@echo "  make test          → Test rapide sur le sujet 'IA'"
	@echo "  make logs          → Voir les 50 dernières lignes du log"
	@echo "  make clean-logs    → Supprimer les logs"
