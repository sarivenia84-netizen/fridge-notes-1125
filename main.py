import os
output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', 'output')
os.makedirs(output_dir, exist_ok=True)
note = "Week-old leftovers: still unclaimed. Bold of you to buy more."
with open(os.path.join(output_dir, 'entry.txt'), 'w') as f:
    f.write(note)