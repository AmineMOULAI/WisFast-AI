import streamlit as st

TRANSLATIONS = {
    'en': {
        'nav_home': "Home", 'nav_about': "About", 'stats': "5 books, 1289 pages indexed", 'uploaded_books': "Uploaded Books", 'main_title': "Smart search in your books", 'upload_label': "Drag & drop your PDFs here or", 'indexed': "pages indexed", 'search_placeholder': "advice patience hardships...", 'search_results': "Search results", 'page': "Page", 'read_btn': "Read page", 'about_title': "WisFast AI", 'about_subtitle': "Your smart research assistant", 'about_btn': "✨ Discover WisFast AI",
        'badges': ["🚀 WisFast AI", "🎯 Our Mission", "⚙️ How it works", "🎓 Created At"],
        'texts_about': [
            "Transforms your PDF documents into a smart research assistant.",
            "Tired of Ctrl+F searches that bury you under 50 irrelevant pages?",
            "Simply upload your PDF (up to 200 pages), type your question, and watch the magic.",
            "Developed for the L3 Computer Science Software Engineering course at Université de Perpignan Via Domitia (UPVD)."
        ],
        'mock_results': [
            "Patience is cultivated by repetition...",
            "Mental endurance in the face of hardship...",
            "To achieve serenity, one must accept...",
            "True happiness lies not in the possession..."
        ],
        # NOUVEAU : Footer traduit
        'footer_text': "⚡ WisFast AI - Semantic search in your PDFs | <a href='https://github.com/AmineMOULAI' target='_blank' style='color: #046e5c; font-weight: bold;'>Amine Moulai</a> | Made with ❤️ for UPVD L3 GL"
    },
    'fr': {
        'nav_home': "Accueil", 'nav_about': "À propos", 'stats': "5 livres, 1289 pages indexées", 'uploaded_books': "Livres Uploadés", 'main_title': "Recherche intelligente dans tes livres", 'upload_label': "Glissez & déposez vos PDF ici ou", 'indexed': "pages indexées", 'search_placeholder': "conseils patience épreuves...", 'search_results': "Résultats de la recherche", 'page': "Page", 'read_btn': "Lire la page", 'about_title': "WisFast AI", 'about_subtitle': "Votre assistant de recherche intelligent", 'about_btn': "✨ Découvrir WisFast AI",
        'badges': ["🚀 WisFast AI", "🎯 Notre Mission", "⚙️ Comment ça marche", "🎓 Créé à"],
        'texts_about': [
            "Transforme vos documents PDF en un assistant de recherche intelligent.",
            "Fatigué des recherches Ctrl+F qui vous noient sous 50 pages non pertinentes ?",
            "Téléchargez simplement votre PDF, tapez votre question et admirez le résultat.",
            "Développé pour le cours de Génie Logiciel L3 Informatique à l'Université de Perpignan Via Domitia (UPVD)."
        ],
        'mock_results': [
            "La patience se cultive par répétition...",
            "L'endurance mentale face aux épreuves...",
            "Pour atteindre la sérénité, il faut accepter...",
            "Le véritable bonheur ne réside pas dans la possession..."
        ],
        # NOUVEAU : Footer traduit
        'footer_text': "⚡ WisFast AI - Recherche sémantique dans vos PDF | <a href='https://github.com/AmineMOULAI' target='_blank' style='color: #046e5c; font-weight: bold;'>Amine Moulai</a> | Fait avec ❤️"
    },
    'ar': {
        'nav_home': "الرئيسية", 'nav_about': "حول التطبيق", 'stats': "5 كتب، 1289 صفحة مفهرسة", 'uploaded_books': "الكتب المرفوعة", 'main_title': "بحث ذكي في كتبك", 'upload_label': "اسحب وأفلت ملفات PDF هنا أو", 'indexed': "صفحة مفهرسة", 'search_placeholder': "نصائح الصبر المحن...", 'search_results': "نتائج البحث", 'page': "صفحة", 'read_btn': "اقرأ الصفحة", 'about_title': "WisFast AI", 'about_subtitle': "مساعد البحث الذكي الخاص بك", 'about_btn': "✨ اكتشف WisFast AI",
        'badges': ["🚀 WisFast AI", "🎯 مهمتنا", "⚙️ كيف يعمل", "🎓 أنشئ في"],
        'texts_about': ["يحول مستندات PDF الخاصة بك...", "هل تعبت من عمليات البحث...", "ما عليك سوى تحميل ملف PDF...", "تم تطويره لدورة هندسة البرمجيات..."],
        'mock_results': ["يُزرع الصبر بالتكرار...", "التحمل العقلي في مواجهة المحن...", "لتحقيق الطمأنينة، يجب على المرء...", "السعادة الحقيقية لا تكمن في امتلاك..."],
        # NOUVEAU : Footer traduit
        'footer_text': "⚡ WisFast AI - بحث دلالي في ملفات PDF | <a href='https://github.com/AmineMOULAI' target='_blank' style='color: #046e5c; font-weight: bold;'>أمين مولاي</a> | صُنع بـ ❤️ لـ UPVD L3 GL"
    }
}

def init_language():
    if 'lang' not in st.session_state:
        st.session_state.lang = 'fr' 
    return TRANSLATIONS[st.session_state.lang]

def cycle_language():
    langs = ['fr', 'en', 'ar']
    current_index = langs.index(st.session_state.lang)
    next_index = (current_index + 1) % len(langs)
    st.session_state.lang = langs[next_index]

def language_selector():
    # On remet le bouton rond à droite
    col1, col2 = st.columns([18, 1])
    with col2:
        st.button("🌍", on_click=cycle_language, key="global_lang_btn")