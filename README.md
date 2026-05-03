# ⚓ Pirate RPG

A text-based pirate RPG built in Python — sail the seas, loot enemies, and hunt down the Kraken.

> 🏆 Built in **3 hours 20 minutes** for [Skills Competition Wales](https://inspiringskills.gov.wales/results/skills-competition-wales-202526) — awarded **Highly Commended**

---

## 🎮 What is it?

You captain a pirate ship on the open ocean. Fight increasingly dangerous enemies, scavenge for supplies, upgrade your stats, and track down the legendary Kraken for the final showdown.

Every run starts fresh with a custom stat build — how you distribute your points between attack, defense, and speed shapes how you play.

---

## 🚀 Getting Started

**Requirements:** Python 3.x — no external libraries needed.

```bash
git clone https://github.com/tomTTFB/pirate-rpg
cd pirate-rpg
python main.py
```

On first launch you'll be asked to start a new game or load a save. Saves are stored in a local `saves/` folder automatically.

---

## 🕹️ How to Play

### Character Creation
You get **30 stat points** to distribute between:
- ⚔️ **Attack** — how much damage you deal
- 🛡️ **Defense** — reduces incoming damage
- 💨 **Speed** — determines who attacks first in battle

Choose wisely — you're stuck with your build (unless you find upgrades at sea).

### Main Actions
| Option | What it does |
|--------|-------------|
| Sail around | Random encounter — could be nothing, could be a fight |
| Scavenge for items | Your crew hunts for loot to buy |
| Use items | Buff your stats or repair your ship |
| Save Game | Saves to `saves/save.pkl` |
| Fight Kraken | The final boss — requires the Kraken Map |

### Items
| Item | Effect |
|------|--------|
| Unstable Gunpowder | +1 Attack |
| Reinforced Planks | +1 Defense |
| Rum | +1 Speed |
| Ship Repair Kit | +10–30 HP |

### Enemies
From scrappy Rafts to full Pirate Ships with different specialisations — and ultimately **💀 The Kraken** itself. Enemy stats are hidden until they're below 20% HP, so pay attention.

### Winning
Defeat enemies until you find the **Kraken Map** (rare drop), then challenge the Kraken. Beat it and you win — your save gets deleted as a reward. 🏴‍☠️

---

## 📁 Project Structure

```
├── main.py          # Game loop and main menu
├── battle.py        # Combat system
├── gameclasses.py   # Character class
├── enemies.py       # Enemy templates
└── utils.py         # Utility functions
```

---

*Made for Skills Competition Wales — Coding category*
