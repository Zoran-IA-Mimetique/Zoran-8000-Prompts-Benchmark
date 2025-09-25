import json, argparse, random

SEEDS = [13, 42, 101]

def run_experiment(prompts, mode, seed, out_file):
    random.seed(seed)
    results = []
    for p in prompts:
        # Placeholder : remplacer par appel modèle Zoran
        results.append({"id": p.get("id"), "prompt": p.get("text"), "output": f"Fake-{mode}-{seed}"})
    with open(out_file, "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompts", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    prompts = [json.loads(l) for l in open(args.prompts)]
    for mode in ["A", "B", "C"]:
        for seed in SEEDS:
            out_file = f"{args.out}/results_{mode}_seed{seed}.jsonl"
            run_experiment(prompts, mode, seed, out_file)
