"""MakeFun fridge entry: writes a single-line passive-aggressive note to /output/entry.txt."""
import os


def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', 'output')
    os.makedirs(output_dir, exist_ok=True)
    note = "Week-old leftovers: still unclaimed. Bold of you to buy more."
    if not 1 <= len(note) <= 200:
        raise ValueError(f"note length {len(note)} not in range [1, 200]")
    with open(os.path.join(output_dir, 'entry.txt'), 'w', encoding='utf-8') as f:
        f.write(note)


if __name__ == "__main__":
    main()