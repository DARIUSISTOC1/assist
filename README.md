# BYBO ASSISTANT

> 🎤 Offline Voice Assistant to control your PC with your voice

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
* Prend pas beaucoup de place (seulement 70Mo)

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

-> `vosk-model-small-fr-0.22`
-> Renommer en `model`

---

## Lancer

```bash
python assistant.py
```

ou lancer directement le fichier python

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
* don't take a lot of place (only 70 Mo)

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

👉 Download model:
https://alphacephei.com/vosk/models

➡️ `vosk-model-small-en-us-0.15`
➡️ Rename to `model`

---

## Run

```bash
python assistant.py
```

or open directly the python file

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

## Limitations

* not a true AI
* depends on microphone quality
* recognition errors possible

---

</details>

---

## ⭐ Support

If you like the project, leave a ⭐ on GitHub!
