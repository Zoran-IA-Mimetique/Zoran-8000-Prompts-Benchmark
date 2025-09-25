#!/bin/bash
echo "🔐 Vérification SHA256..."
for f in prompts/*.jsonl results/*.jsonl results/*.csv; do
    [ -f "$f" ] && sha256sum "$f"
done
