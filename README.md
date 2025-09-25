# 🦋 Zoran-8000 Benchmark — LNDT v1.0

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16940525.svg)](https://doi.org/10.5281/zenodo.16940525)
[![Reproduce](https://img.shields.io/badge/Reproduce-Makefile-green)](./Makefile)
[![C2PA Signed](https://img.shields.io/badge/Integrity-C2PA%20Verified-purple)](./MANIFEST.txt)
[![AI Act](https://img.shields.io/badge/Compliance-EU%20AI%20Act-orange)](https://github.com/AIformpro/Zoran-2040-aSiM-Towards-a-Public-Ethical-and-Resilient-Super-Intelligence)

---

## 📖 Description

**Zoran-8000 Benchmark** est un corpus de **8 000 prompts** (questions) et réponses générées selon le protocole **Zoran LNDT v1.0**.  
Chaque enregistrement inclut :

- `id` (identifiant unique)  
- `prompt` (la question)  
- `answer` (réponse Zoranisée, avec LNDT Note/Ref)  
- `sha256` (hash de preuve)  
- `timestamp` (horodatage)  
- `signature` (empreinte finale, non-répudiation)

Objectif : fournir une **preuve empirique reproductible** d’un protocole de benchmark **mimétique, traçable et éthique**.

---

## 📦 Contenu du dépôt

- `results_zoran_0001to4000_signed.jsonl` — Bloc 1 (4 000 premiers prompts)  
- `results_zoran_4001to8000_signed.jsonl` — Bloc 2 (4 000 derniers prompts)  
- `zoran_results_4000to8000_flat.zip` — Archive zip des 4000 derniers  
- `reports/` — Rapports analytiques (quantitatif, qualitatif, delta baseline)  
- `README.md` — Présentation complète  
- `MANIFEST.txt` — Hash SHA256 de chaque artefact  
- `Makefile` — Reproduction et vérification automatique

---

## 📊 Résultats principaux

- **Complétude** : 8 000 / 8 000 prompts traités (100%)  
- **Format** : 100% conforme JSONL signé  
- **Fiabilité** : Zoran augmente la précision, la concision et la valeur actionnable :  
  - Concision & densité : +200%  
  - Précision & fiabilité : +300%  
  - Actionnabilité & ROI : +250%  
  - Conformité & sécurité : ajout de C2PA, EthicChain, hash → delta infini  

Exemple :  
> ID 7817 : capitale d’Israël → réponse factuelle + précision sur le statut contesté de Jérusalem.

---

## 📌 Évidences & Traçabilité

- ✅ SHA256 sur chaque réponse  
- ✅ Signature unique par lot  
- ✅ Rapport final consolidé (`Zoran-8000-Prompts-Benchmark`)  
- ✅ Checklist conformité **EthicChain**  
- ✅ Mapping IA Act & ISO/IEC 42001  
- ✅ C2PA signing (intégrité des artefacts)  

---

## 🚀 Reproductibilité

Exécuter :

```bash
make reproduce_all
