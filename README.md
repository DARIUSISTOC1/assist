# BYBO ASSISTANT

> Offline Voice Assistant to control your PC with your voice <br>
> "Bybo" is the name of my PC, you can change it if you want

---

## Structure du projet / Structure of the project

```bash
assist/
├── assistant.py        # Code principal de l'assistant / main assistant code
├── apps.json           # Configuration des applications / apps configuration
├── model/              # Modèle vocal Vosk (à télécharger) / Vosk model (to download)
│   └── ...
├── README.md           # Documentation
```

---

<details>
<summary>🇫🇷 Version Française (cliquer pour ouvrir)</summary>

---

## Fonctionnalités

* Reconnaissance vocale **offline**
* Commandes naturelles ("ouvre steam", "lance discord")
* Wake word : **bybo** (tolérant : bibo, bibeau, vivo…)
* Lancement de jeux Steam
* Ouverture d'applications
* 100% local (aucune API)
* Prend peu de place (~70Mo)

---

## Exemple

```text
Toi: bybo
IA : Oui ?

Toi: lance steam
IA : J'ouvre steam
```

---

## Installation

```bash
pip install vosk pyttsx3 sounddevice
```

Télécharger le modèle :
https://alphacephei.com/vosk/models

→ `vosk-model-small-fr-0.22`
→ Renommer en `model`

---

## Lancer

```bash
python assistant.py
```

---

## Configuration (`apps.json`)

```json
{
  "steam": {
    "type": "shortcut",
    "path": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Steam.lnk",
    "keywords": ["steam", "ssteam", "stim"]
  }
}
```

---

## 🔧 Changer le nom de l'assistant (wake word)

Par défaut, l’assistant écoute le mot :

```text
bybo
```

### Étapes :

1. Ouvre le fichier `assistant.py`
2. Trouve cette ligne :

```python
WAKE_WORDS = ["bybo", "bibo", "bibeau", "vivo"]
```

3. Remplace par ton nom :

```python
WAKE_WORDS = ["jarvis", "jarvi", "jarviss"]
```

👉 Conseil :

* ajoute plusieurs variantes pour éviter les erreurs micro
* évite les mots trop courts (ex: "ok")

---

## Limitations

* pas une vraie IA
* dépend du micro
* erreurs possibles

---

</details>

---

<details>
<summary>🇬🇧 English Version (click to open)</summary>

---

## Features

* Offline voice recognition
* Natural commands ("open steam", "launch discord")
* Wake word: **bybo** (tolerant: bibo, bibeau, vivo…)
* Launch Steam games
* Open applications
* 100% local (no API)
* lightweight (~70MB)

---

## Example

```text
You: bybo
AI : Yes?

You: launch steam
AI : Opening steam
```

---

## Installation

```bash
pip install vosk pyttsx3 sounddevice
```

Download model:
https://alphacephei.com/vosk/models

→ `vosk-model-small-en-us-0.15`
→ Rename to `model`

---

## Run

```bash
python assistant.py
```

---

## Configuration (`apps.json`)

```json
{
  "steam": {
    "type": "shortcut",
    "path": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Steam.lnk",
    "keywords": ["steam", "steaam"]
  }
}
```

---

## 🔧 Change the assistant name (wake word)

By default, the assistant listens to:

```text
bybo
```

### Steps:

1. Open `assistant.py`
2. Find this line:

```python
WAKE_WORDS = ["bybo", "bibo", "bibeau", "vivo"]
```

3. Replace it with your own name:

```python
WAKE_WORDS = ["jarvis", "jarvi", "jarviss"]
```

👉 Tip:

* add variations to improve recognition
* avoid very short words

---

## Limitations

* not a real AI
* depends on microphone quality
* recognition errors possible

---

</details>

---

## ⭐ Support

If you like the project, leave a ⭐ on GitHub!
