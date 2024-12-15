


# CodeBot - Your Bilingual Programming Learning Assistant

---

## Table of Contents / Table des matières

- [Overview / Vue d'ensemble](#overview)
- [Installation](#installation)
- [Usage / Utilisation](#usage)
  - [English](#english)
  - [Français](#français)
- [Features / Fonctionnalités](#features)
- [Contributing / Contribution](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview / Vue d'ensemble

**CodeBot** est une application Streamlit conçue pour aider les étudiants et les professionnels à apprendre la programmation dans les langages Python, Java ou C++, adaptée à leur domaine d'étude ou de travail. Elle offre une expérience utilisateur bilingue, permettant d'interagir en anglais ou en français.

**CodeBot** is a Streamlit application designed to assist students and professionals in learning programming in Python, Java, or C++, tailored to their field of study or work. It provides a bilingual user experience, allowing interaction in either English or French.

---

## Installation

### Prerequisites / Prérequis

- Python 3.10 or higher / Python 3.10 ou supérieur
- Streamlit
- OpenAI or XAI API Key / Clé API d'OpenAI ou XAI

### Steps / Étapes

1. **Clone this repository** / Clonez ce dépôt:
   ```bash
   git clone https://github.com/your-username/CodeBot.git
   cd CodeBot
   ```

2. **Install dependencies** / Installez les dépendances:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API Key** / Configurez votre clé API:
   - For OpenAI, get your API key from [here](https://platform.openai.com/account/api-keys).
   - For XAI, get your API key from [here](https://developer.x.ai/).

   Add your API key in the `streamlit.toml` file or as an environment variable:
   ```toml
   [openai]
   api_key = "your-api-key-here"
   ```

   Or:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

4. **Run the app** / Exécutez l'application:
   ```bash
   streamlit run chatbot.py
   ```

---

## Usage / Utilisation

### English

- **Start the app**: Open your terminal or command prompt, navigate to the project directory, and run `streamlit run chatbot.py`.
- **Choose your API**: Select between OpenAI or XAI for the backend AI service.
- **Enter API Key**: Provide your API key in the sidebar.
- **Select Field and Language**: Choose your field of study or work and your preferred programming language.
- **Interact**: Type your questions or commands in the chat input box.

### Français

- **Lancer l'application** : Ouvrez votre terminal ou invite de commande, naviguez jusqu'au répertoire du projet et exécutez `streamlit run chatbot.py`.
- **Choisir l'API** : Sélectionnez entre OpenAI ou XAI pour le service d'IA backend.
- **Entrer la Clé API** : Fournissez votre clé API dans la barre latérale.
- **Sélectionnez le domaine et la langue** : Choisissez votre domaine d'étude ou de travail ainsi que votre langage de programmation préféré.
- **Interagir** : Tapez vos questions ou commandes dans la boîte de chat.

---

## Features / Fonctionnalités

- **Bilingual Support** / **Support bilingue**: English and French.
- **Field-specific Learning** / **Apprentissage spécifique au domaine**: Tailored content based on the user's field of study or work.
- **API Integration** / **Intégration d'API**: Uses OpenAI or XAI for AI responses.
- **Error Handling** / **Gestion des erreurs**: Provides user-friendly error messages for API key issues or other unexpected errors.
- **Mobile Friendly** / **Adapté aux mobiles**: Ensures a good experience on smaller screens.

---

## Contributing / Contribution

We welcome contributions! Here's how you can help:

- **Fork the repo** and create your branch from `main`.
- **Make your changes** or improvements.
- **Test** your changes to ensure they work as expected.
- **Submit a pull request**.

Pour contribuer:

- **Fork ce dépôt** et créez votre branche à partir de `main`.
- **Apportez vos modifications** ou améliorations.
- **Testez** vos changements pour vous assurer qu'ils fonctionnent comme prévu.
- **Soumettez une pull request**.

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

Ce projet est sous licence MIT - voir le fichier [LICENSE.md](LICENSE.md) pour plus de détails.

---

## Contact

For any questions, comments or feedback, please contact:

Pour toute question, commentaire ou retour, veuillez contacter :

- **Christ ND** / **Christ ND** - [christ@ndsec24.tech](mailto:christ@ndsec24.tech)

---

Feel free to contribute or report any issues you encounter!

N'hésitez pas à contribuer ou à signaler tout problème que vous rencontrez !
