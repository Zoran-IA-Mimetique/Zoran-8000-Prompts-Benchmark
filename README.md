#


[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16940525.svg)](https://doi.org/10.5281/zenodo.16940525)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16941007.svg)](https://doi.org/10.5281/zenodo.16941007)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16940299.svg)](https://doi.org/10.5281/zenodo.16940299)
[![Reproducibility](https://img.shields.io/badge/Reproduce-100%25-blue.svg)](./Makefile)
[![C2PA](https://img.shields.io/badge/Traceability-C2PA%20enabled-purple.svg)](meta/C2PA_manifest.json)
[![SBOM](https://img.shields.io/badge/SBOM-CycloneDX-orange.svg)](meta/sbom_cyclonedx.json)
[![AI Act](https://img.shields.io/badge/Compliance-EU%20AI%20Act-lightgrey.svg)](https://artificial-intelligence-act.eu/)
[![RGPD](https://img.shields.io/badge/Privacy-RGPD-red.svg)](https://gdpr-info.eu/)

#Zoran 8000 Benchmark 🌞⧉

**But :**
Évaluer Zoran sur **8000 prompts** avec trois configurations :
- **A** : Zoran-Nu (mimétique seul)
- **B** : Zoran + Mathématiques
- **C** : Zoran + Full interdisciplinaire

## 📊 Métriques suivies
- HR (Hallucinations)
- BI (Biais)
- XS (Précision explicative)
- CF (Pertinence contextuelle)
- TC (Traçabilité)
- EC (Éthique / Compliance)

## 📂 Structure du repo
- `prompts/` → corpus complet (JSONL plat)
- `results/` → sorties pour A, B, C + résumé CSV
- `scripts/` → exécutions et analyses
- `meta/` → manifestes, SBOM CycloneDX, C2PA

## ⚙️ Reproductibilité
- Seeds fixes : 13 / 42 / 101
- Scripts de réplication :

```bash
make reproduce_all
```

## 🔐 Traçabilité
- SBOM : `meta/sbom_cyclonedx.json`
- C2PA : `meta/C2PA_manifest.json`
- SHA256 check :

```bash
./scripts/check_hashes.sh
```

## 📜 Licence
MIT — voir `LICENSE`

## 🔗 Citations
DOIs liés :
- 10.5281/zenodo.16940525
- 10.5281/zenodo.16941007
- 10.5281/zenodo.16940299

## 🌞 Symbolique
Chaque prompt = **mètre-étalon cognitif**.
Chaque résultat = **trace auditable**.
Ensemble, ce corpus balise le chemin vers une **AGI mimétique**.
