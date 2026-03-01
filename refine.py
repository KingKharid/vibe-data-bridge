import json

def load_data(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Raw data file not found.")
        return []

def refine_data(raw_list):
    refined_list = []
    seen_titles = set()

    for item in raw_list:
        title = item.get("title", "").strip()
        
        # 1. Basic Cleaning: Remove empty entries
        if not title:
            continue
            
        # 2. De-duplication: Only keep unique titles
        if title not in seen_titles:
            # 3. Standardization: e.g., making titles title-case
            item["title"] = title.title()
            
            refined_list.append(item)
            seen_titles.add(title)

    return refined_list

def save_refined_data(data, filename="refined_data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Refinement complete. {len(data)} unique items saved to {filename}")

if __name__ == "__main__":
    raw_data = load_data("raw_data.json")
    if raw_data:
        clean_data = refine_data(raw_data)
        save_refined_data(clean_data)
