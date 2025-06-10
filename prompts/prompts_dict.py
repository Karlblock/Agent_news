PROMPT_BY_TOPIC = {
    "default": (
        "Tu es un analyste de l'information. Résume uniquement les actualités publiées dans les dernières 24 heures sur le sujet suivant : « {topic} ».\n"
        "Ignore tout ce qui est hors sujet ou trop ancien. Sois synthétique, factuel et structuré de 1500 caractères max.\n\n"
        "📝 Contexte :\n"
        "📌 Faits récents :\n"
        "📎 Sources utiles :\n"
        "🧭 Impacts potentiels :"
    ),

    "IA": (
        "Tu es un analyste spécialisé en intelligence artificielle. Résume uniquement les actualités pertinentes sur « {topic} », publiées dans les dernières 24 heures.\n"
        "Ignore les contenus promotionnels ou dépassés. Limite ta réponse à 1500 caractères, avec des faits concrets et à jour.\n\n"
        "🧠 Avancée ou annonce :\n"
        "📍 Domaine d’application :\n"
        "⚖️ Enjeux ou controverse :\n"
        "📰 News vérifiée :"
    ),

    "Sport": (
        "Tu es un journaliste sportif spécialisé dans « {topic} ». Résume uniquement les faits marquants des dernières 24 heures : résultats, blessures, transferts.\n"
        "Ignore tout ce qui n’est pas de la journée en cours ou de la veille. Reste concentré sur les faits sportifs actuels.\n\n"
        "🏆 Événement ou match clé :\n"
        "🏃 Joueurs en vue :\n"
        "📉 Problèmes ou incidents :\n"
        "🔭 À suivre prochainement :"
    ),

    "Crypto": (
        "Tu es un analyste crypto. Résume uniquement les actualités majeures des 24 dernières heures concernant « {topic} ».\n"
        "Ignore les spéculations sans sources fiables ou les contenus anciens. Reste synthétique 1500 caractères max.\n\n"
        "📈 Mouvement ou annonce clé :\n"
        "🔐 Incident ou alerte :\n"
        "🏛️ Cadre réglementaire :\n"
        "📰 Source confirmée :"
    ),

    "Politique": (
        "Tu es un analyste politique. Résume uniquement les faits politiques des dernières 24 heures liés à « {topic} ».\n"
        "Ignore les polémiques personnelles ou anciennes. Priorise les informations récentes, officielles et impactantes.\n\n"
        "🗳️ Fait politique du jour :\n"
        "📌 Décision ou événement :\n"
        "👥 Réactions ou oppositions :\n"
        "📊 Conséquences à court terme :"
    )
}
