# Content Studio

**Un pack de skills Claude qui gère le flux de contenu d'une petite marque : se configurer une fois, trouver des sujets, créer, suivre, apprendre des chiffres.**

[English](README.md) · Licence MIT · fonctionne avec Claude Code et les skills Claude.ai

Les petites marques, créateurs, musées, écoles et projets perso publient seuls. Le plus dur n'est pas un post : c'est de rester dans son sujet, exact, cohérent, et d'apprendre de ce qui marche. Content Studio donne à Claude un **profil de qui vous êtes** et des skills ciblés qui le lisent tous : le même pack sert une chaîne d'histoire, une boulangerie, un SaaS ou une association.

## Les skills

| Skill | Rôle |
|---|---|
| `studio` | Point d'entrée : vérifie le profil, puis aiguille vers le bon skill. |
| `studio-setup` | Petit entretien → `studio/profile.yml` : identité, audience, **sujets autorisés**, voix, charte, réseaux, outil de suivi, règles. |
| `studio-ideas` | Cherche et classe des sujets **uniquement dans vos domaines**, vérifie les faits (2 sources), évite les doublons, enregistre les idées. |
| `studio-create` | Transforme une idée en accroche, script ou slides, légende, hashtags, texte alternatif, brief visuel ; contrôle qualité ; enregistrement. |
| `studio-video` *(optionnel)* | Génère une vidéo verticale (texte, fondus, musique) avec Python + ffmpeg, aux couleurs et à la police de votre charte. |
| `studio-analytics` | Lit les stats (Metricool, exports, chiffres collés), compare les formats équitablement, propose **3 changements maximum** avec un plan de test. |
| `studio-planner` | Calendrier éditorial selon votre cadence et vos dates clés ; comptes à rebours de lancement ; export `.ics`. |
| `studio-engage` | Prépare des réponses et idées d'engagement **que vous postez à la main**. N'automatise jamais likes, abonnements ni commentaires. |

## Principes

- **Un profil, plusieurs skills.** Rien n'est codé en dur pour une marque : changez le profil, le pack suit.
- **Le périmètre est une règle stricte** : les idées et contenus restent dans vos domaines.
- **Rien d'inventé.** Chiffres, partenariats, témoignages, prix et dates sont dans une liste `never_invent` : Claude demande au lieu de deviner. Un fait doit avoir deux sources indépendantes.
- **L'humain valide.** Rien n'est publié ni envoyé sans votre accord. Aucune automatisation des likes, abonnements ou commentaires (le validateur de profil la refuse).
- **Analyse honnête.** On compare des groupes de posts, pas des anecdotes ; « pas assez de données » quand c'est vrai ; trois changements maximum par bilan.
- **Vos outils.** Le suivi passe par des adaptateurs (`adapters/`) ; la vidéo est optionnelle.

## Installation

**Claude Code**
```bash
git clone https://github.com/PRochotte/content-studio.git
cd content-studio
scripts/install.sh            # pour tout l'utilisateur (~/.claude/skills)
scripts/install.sh --project  # ou seulement pour le projet courant
```
Puis, dans votre dossier de projet : *« Configure Content Studio. »*

**Claude.ai** : lancez `scripts/package_skills.sh` et importez les zips de `dist/` (commencez par `studio` et `studio-setup`).

**Module vidéo (optionnel)** : Python 3.9+ et [ffmpeg](https://ffmpeg.org).

## Démarrage rapide

1. `Configure Content Studio` → quatre courtes séries de questions → profil enregistré et validé.
2. `Donne-moi 8 idées pour la semaine prochaine` → tableau classé avec sources et risques ; vous validez.
3. `Fais l'idée 3 en reel` → accroches, script, légende, contrôle qualité ; enregistré dans votre outil de suivi.
4. Deux semaines plus tard : `Comment ont marché mes 10 derniers posts ?` → constats, hypothèses, trois tests.

## Démo

Une vidéo de démonstration (configuration → idées → création → vidéo → analyse) : **[vidéo de démo (français)](https://youtu.be/OJ_CTXQ1vuw)** · [English version](https://youtu.be/U0UuWZV3FqM). Elle montre un vrai run, dont les fichiers sont dans [`examples/temporia/demo-run/`](examples/temporia/demo-run/).

## Exemple

`examples/temporia/` est le profil d'un vrai projet (une appli de quiz d'histoire et de patrimoine) : vidéo activée, suivi Notion, stats Metricool. Il montre un périmètre étroit, des règles `never_invent` strictes et une voix de marque précise. C'est un exemple, pas une partie du pack.

## Limites

- Les skills guident Claude, ils ne garantissent pas le résultat : vérifiez toujours les faits et les droits (images, musiques).
- Une petite audience donne des chiffres bruités : le pack le dit plutôt que de conclure.
- Les plateformes et connecteurs changent : les noms d'outils Metricool ou autres peuvent différer.
- Le rendu vidéo est volontairement simple ; les montages complexes restent dans votre éditeur.

## Contribuer, licence

Voir [CONTRIBUTING.md](CONTRIBUTING.md). Licence [MIT](LICENSE).
