install:
	./install.sh

run:
	./Anews "$(topic)"

logs:
	tail -n 50 logs/agent_news.log

update:
	unzip -o Agent_News_Patch.zip

bot:
	bash bot/startup.sh

clean-logs:
	rm -f logs/agent_news.log
