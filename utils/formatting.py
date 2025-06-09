import re

def markdown_to_html(text):
    # Convertir **gras** en <b>
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)

    # Convertir titres type "### Titre" en <b>Titre</b>
    text = re.sub(r"^#+\s*(.+)$", r"<b>\1</b>", text, flags=re.MULTILINE)

    # Convertir "- texte" en puces Telegram
    text = re.sub(r"^- (.+)$", r"• \1", text, flags=re.MULTILINE)

    # Convertir [texte](url) en liens HTML cliquables
    text = re.sub(r"\[(.+?)\]\((https?://[^\s]+)\)", r'<a href="\2">\1</a>', text)

    # Retirer les balises interdites et remplacer <br> par \n
    text = text.replace("<br>", "\n").replace("<br/>", "\n").replace("<br />", "\n")

    # Nettoyage final pour éviter les erreurs HTML
    return text
