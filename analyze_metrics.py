import json, argparse, csv, glob

def analyze(results_dir, out_file):
    rows = []
    for file in glob.glob(f"{results_dir}/*.jsonl"):
        with open(file) as f:
            data = json.load(f)
        rows.append({"file": file, "count": len(data)})
    with open(out_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["file","count"])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    analyze(args.results, args.out)
