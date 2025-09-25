# Zoran 8000 Benchmark 🌞⧉

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
