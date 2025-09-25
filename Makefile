.PHONY: reproduce_all run analyze check

run:
	python3 scripts/run_benchmark.py --prompts prompts/prompts_8000.jsonl --out results/

analyze:
	python3 scripts/analyze_metrics.py --results results/ --out results/metrics_summary.csv

check:
	bash scripts/check_hashes.sh

reproduce_all: run analyze check
