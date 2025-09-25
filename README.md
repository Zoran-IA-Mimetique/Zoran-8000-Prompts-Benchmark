# Zoran Benchmark 4000 — Certified Corpus

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16940525.svg)](https://doi.org/10.5281/zenodo.16940525)
[![Reproducibility](https://img.shields.io/badge/Reproduce-make%20verify-success)](#reproducibility)

---

## 📌 Description courte (≤350 caractères)

Corpus certifié de **4000 prompts Zoran** (ID 1–4000) avec réponses signées (SHA-256 + timestamp + signature LNDT). Conçu pour tester hallucinations, biais, traçabilité et pertinence dans un cadre **mimétique interdisciplinaire** (Zoran aSiM). Format JSONL plat, prêt à scraper, auditer et reproduire.

---

## 📖 Description longue (≈1200 caractères)

Ce dépôt contient le **premier lot complet de 4000 prompts Zoran**, intégrant un protocole de certification inédit :  
- Chaque enregistrement inclut : `id`, `prompt`, `answer`, `sha256`, `timestamp`, `signature`.  
- Les réponses suivent le protocole **Zoran aSiM MAXI** : explicabilité mimétique, connexions interdisciplinaires (PolyResonator), garde-fous éthiques (Aegis Layer), et rollback ΔM11.3.  
- L’ensemble est fourni au format **JSONL plat** (scraping-friendly) pour assurer interopérabilité, reproductibilité et auditabilité.  
- Ce corpus est destiné aux chercheurs, industriels et régulateurs souhaitant évaluer les IA sur :  
  - **Hallucinations (HR)**  
  - **Biais (BI)**  
  - **Qualité explicative (XS)**  
  - **Pertinence contextuelle (CF)**  
  - **Traçabilité empirique (TC)**  
  - **Conformité éthique (EC)**  

Ce benchmark est conçu comme un **bien commun open-source**, positionné dans la lignée des travaux sur la transparence, la conformité à l’**AI Act** et aux normes ISO/IEC 42001, et visant à constituer un **standard public** de certification IA.

---

## 📂 Contenu

- `results_zoran_4000_signed.jsonl` — Corpus complet signé (4000 entrées).  
- `manifest.json` — Métadonnées (lot, SHA256 global, signature, DOIs).  
- `README.md` — Présent fichier.  
- `LICENSE` — MIT License.  

---

## 📜 DOIs de référence

- [10.5281/zenodo.16940525](https://doi.org/10.5281/zenodo.16940525)  
- [10.5281/zenodo.16941007](https://doi.org/10.5281/zenodo.16941007)  
- [10.5281/zenodo.16940299](https://doi.org/10.5281/zenodo.16940299)  
- [10.5281/zenodo.16995014](https://doi.org/10.5281/zenodo.16995014)  
- [10.5281/zenodo.16995226](https://doi.org/10.5281/zenodo.16995226)  
- [10.5281/zenodo.16997156](https://doi.org/10.5281/zenodo.16997156)  

---

## ⚙️ Reproductibilité

```bash
# Vérifier l’intégrité
sha256sum -c manifest.json

# Rejouer l’analyse
make reproduce_all
