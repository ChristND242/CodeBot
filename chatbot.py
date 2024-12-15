import os
from openai import OpenAI, APIError
import streamlit as st
import locale

# Configure locale for language support
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Configuration for Streamlit page - Must be called first
# st.set_page_config(
#     page_title="💬 Pona Ekolo CodeBot",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )
import streamlit as st



st.set_page_config(
    page_title="💬 Pona Ekolo CodeBot",
    page_icon=":material/computer:",
    layout="wide",
    initial_sidebar_state="expanded",
    
)

with st.sidebar.expander("About", expanded=False):
    st.markdown(
        """
        [Get help](https://forum.ponaekolo.me/)  
        [Report a Bug](mailto:admin@ponaekolo.me)  
        **About**:  
        **CodeBot** is a programming learning assistant designed to provide tailored guidance for various fields and programming languages. 
        - Created with ❤️ by [Christ ND](https://ndsec24.tech/)
        - Version: 1.2
        - Contact: [Christnd@congolaisdenanjing.com](mailto:Christnd@congolaisdenanjing.com)
                   [Christndzila400@gmail.com](mailto:Christndzila400@gmail.com)
        """
    )

# st.markdown("""
# <style>
#     body {
#         background-color: #A52A2A; 
#         color: #A52A2A; 
#     }
#     .st-cb {
#         background-color: #A52A2A !important; 
#         color: white !important;
#     }
#     .st-cb-message {
#         font-size: 16px; 
#     }
#     .st-cb-input {
#         background-color: #E0E0E0; 
#     }
#     .sidebar .sidebar-content {
#         background-color: #A52A2A; 
#         color: white; 
#     }
#     .sidebar .stSelectbox div {
#         background-color: #A52A2A; 
#     }
# </style>
# """, unsafe_allow_html=True)

# Dictionary for translations
translations = {
    'en': {
        'page_title': "💬 Pona Ekolo CodeBot",
        'page_caption': "🚀 A Programming Learning Assistant tailored to your field!",
        'api_choice': "Choose API Provider:",
        'api_key_placeholder': "API Key",
        'openai_api_key': "OpenAI API Key",
        'xai_api_key': "XAI API Key",
        'api_key_url': "Get an API Key",
        'field_select': "Select your field or major:",
        'other_field': "Please specify your field or major:",
        'language_select': "Choose your preferred programming language:",
        'welcome': "Welcome to CodeBot! I'm here to help you with {language} tailored for {field}. What would you like to learn today?",
        'input_placeholder': "Type your {language} question here...",
        'error_api_key': "Please add your API key to continue.",
        'error_system': "System Error: {error}",
        'error_unexpected': "System Error: An unexpected error occurred. Please check your API key or try again later.",
        'tips_header': "### Tips for Learning {language} in {field}:",
        'tips_1': "- **Understand the Basics:** Start with syntax, data structures, and basic operations in {language}.",
        'tips_2': "- **Real-World Applications:** Look for examples or projects that align with {field}.",
        'tips_3': "- **Documentation:** Familiarize yourself with the official {language} documentation and libraries commonly used in your field.",
        'tips_4': "- **Community:** Engage with online communities or forums where {field} professionals discuss programming challenges.",
        'tips_5': "- **Practice:** Use coding platforms tailored to {field} or general coding challenges to apply your learning."
    },
    'fr': {
        'page_title': "💬 Pona Ekolo CodeBot",
        'page_caption': "🚀 Un assistant d'apprentissage de la programmation adapté à votre domaine!",
        'api_choice': "Choisissez le fournisseur d'API :",
        'api_key_placeholder': "Clé API",
        'openai_api_key': "Clé API OpenAI",
        'xai_api_key': "Clé API XAI",
        'api_key_url': "Obtenir une clé API",
        'field_select': "Sélectionnez votre domaine ou votre spécialité :",
        'other_field': "Veuillez préciser votre domaine ou votre spécialité :",
        'language_select': "Choisissez votre langage de programmation préféré :",
        'welcome': "Bienvenue à CodeBot! Je suis ici pour vous aider avec {language} adapté à {field}. Que souhaitez-vous apprendre aujourd'hui?",
        'input_placeholder': "Entrez votre question sur {language} ici...",
        'error_api_key': "Veuillez ajouter votre clé API pour continuer.",
        'error_system': "Erreur Système : {error}",
        'error_unexpected': "Erreur Système : Une erreur inattendue s'est produite. Veuillez vérifier votre clé API ou réessayer plus tard.",
        'tips_header': "### Conseils pour apprendre {language} dans le domaine {field} :",
        'tips_1': "- **Comprendre les bases** : Commencez par la syntaxe, les structures de données et les opérations de base en {language}.",
        'tips_2': "- **Applications réelles** : Cherchez des exemples ou des projets alignés avec {field}.",
        'tips_3': "- **Documentation** : Familiarisez-vous avec la documentation officielle de {language} et les bibliothèques couramment utilisées dans votre domaine.",
        'tips_4': "- **Communauté** : Engagez-vous avec des communautés en ligne ou des forums où les professionnels de {field} discutent des défis de programmation.",
        'tips_5': "- **Pratique** : Utilisez des plateformes de codage adaptées à {field} ou des défis de codage généraux pour appliquer votre apprentissage."
    }
}


language = st.sidebar.selectbox("Choose Language / Choisissez la langue", ('English', 'Français'))
lang_dict = translations.get('en' if language == 'English' else 'fr')

with st.sidebar:
    api_choice = st.radio(lang_dict['api_choice'], ("OpenAI", "XAI"))
    if api_choice == "OpenAI":
        api_key = st.text_input(lang_dict['openai_api_key'], key="chatbot_api_key", type="password")
        f"[{lang_dict['api_key_url']}](https://platform.openai.com/account/api-keys)"
    else:
        api_key = st.text_input(lang_dict['xai_api_key'], key="xai_api_key", type="password")
        f"[{lang_dict['api_key_url']}](https://developer.x.ai/)"

    # User's Field or Major
    user_field = st.selectbox(lang_dict['field_select'], 
                              ["Computer Science", "Data Science", "Software Engineering", "Mechanical Engineering", "Biology", "Physics", "Other"])
    
    if user_field == "Other":
        custom_field = st.text_input(lang_dict['other_field'])
        user_field = custom_field if custom_field else "Computer Science"  

    # User's Preferred Language
    user_language = st.selectbox(lang_dict['language_select'], 
                                 ["Python", "Java", "C++"])

st.title(lang_dict['page_title'])
st.caption(lang_dict['page_caption'].format(field=user_field))

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": lang_dict['welcome'].format(language=user_language, field=user_field)}
    ]

# Display existing messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"], unsafe_allow_html=True)

# User input for chat
if prompt := st.chat_input(lang_dict['input_placeholder'].format(language=user_language)):
    if not api_key:
        st.info(lang_dict['error_api_key'])
    else:
        try:
            # API Client Setup
            if api_choice == "OpenAI":
                client = OpenAI(api_key=api_key)
                model = "gpt-3.5-turbo"
            else:
                client = OpenAI(
                    api_key=api_key,
                    base_url="https://api.x.ai/v1",
                )
                model = "grok-beta"

            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)

            # Generate response
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": f"You are Pona Ekolo CodeBot, an AI designed to teach {user_language} for {user_field}. Provide high-quality content, concise guidance, and deep explanations of technical terms in a beginner-friendly manner. Focus on real-world applications and examples relevant to {user_field}. If the user's field is not directly related to programming, explain how {user_language} can be applied in that context."},
                ] + st.session_state.messages
            )
            
            msg = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": msg})
            st.chat_message("assistant").markdown(msg, unsafe_allow_html=True)
        except APIError as e:
            st.error(lang_dict['error_system'].format(error=e))
        except Exception as e:
            st.error(lang_dict['error_unexpected'])

# Additional features for mobile friendliness
st.markdown("""
<style>
    .stChatMessageContent {
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
</style>
""", unsafe_allow_html=True)

# Tips for Learning Programming
st.markdown(lang_dict['tips_header'].format(language=user_language, field=user_field))
st.markdown(lang_dict['tips_1'].format(language=user_language))
st.markdown(lang_dict['tips_2'].format(field=user_field))
st.markdown(lang_dict['tips_3'].format(language=user_language))
st.markdown(lang_dict['tips_4'].format(field=user_field))
st.markdown(lang_dict['tips_5'].format(field=user_field))
"[![Visit Pona Ekolo](https://camo.githubusercontent.com/2d820d835b1d6c8a0c39d0acc2cf5e056ff822b425380e7d374039e843e4651c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f7769726567756172642d2532333838313731412e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d776972656775617264266c6f676f436f6c6f723d7768697465)](https://forum.ponaekolo.me/)"

