#!/usr/bin/env python3
import json, os

def simplify_outline(input_json_path, output_json_path):
    with open(input_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # The data is already in the correct format from main.py
    # Just ensure the structure is clean
    simple = {
      "title": data.get("title", ""),
      "outline": data.get("outline", [])
    }
    
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(simple, f, ensure_ascii=False, indent=2)

def main():
    in_dir  = "output"
    out_dir = "output"
    os.makedirs(out_dir, exist_ok=True)
    for fn in os.listdir(in_dir):
        if fn.lower().endswith(".json"):
            simplify_outline(
                os.path.join(in_dir, fn),
                os.path.join(out_dir, fn)
            )
            print("→ Simplified", fn)

if __name__ == "__main__":
    main()
