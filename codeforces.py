import os
import re
import cloudscraper
from bs4 import BeautifulSoup

def slugify(text):
    return re.sub(r'\W+', '_', text.strip().replace(' ', '_'))

def fetch_problem(contest_id, problem_index):
    url = f"https://codeforces.com/contest/{contest_id}/problem/{problem_index}"
    scraper = cloudscraper.create_scraper()
    res = scraper.get(url)
    if res.status_code != 200:
        raise Exception("Failed to fetch problem page.")
    soup = BeautifulSoup(res.text, 'html.parser')
    problem_div = soup.select_one('.problem-statement')
    if not problem_div:
        raise Exception("Problem HTML not found.")
    title = problem_div.select_one('.title').text.strip()
    return title, str(problem_div), soup

def extract_samples(soup):
    inputs = [pre.text.strip() for pre in soup.select('.input pre')]
    outputs = [pre.text.strip() for pre in soup.select('.output pre')]
    return list(zip(inputs, outputs))

def create_files(contest_id, problem_index, title, html, samples):
    folder = f"{contest_id}{problem_index}_{slugify(title)}"
    os.makedirs(folder, exist_ok=True)

    # Save problem.html
    with open(os.path.join(folder, "problem.html"), "w", encoding="utf-8") as f:
        f.write(html)

    # Save README.md
    with open(os.path.join(folder, "README.md"), "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n[Original problem](https://codeforces.com/contest/{contest_id}/problem/{problem_index})\n\n")
        f.write("See `problem.html` for the full problem statement.\n")

    # Save main.py
    with open(os.path.join(folder, "main.py"), "w", encoding="utf-8") as f:
        f.write("# Write your solution here\n")

    # Save test.py
    with open(os.path.join(folder, "test.py"), "w", encoding="utf-8") as f:
        f.write(f"""import subprocess

def run_test(input_path, output_path):
    with open(input_path) as f_in, open(output_path) as f_out:
        expected = f_out.read().strip()
        result = subprocess.run(['python3', 'main.py'], input=f_in.read(), text=True, capture_output=True)
        output = result.stdout.strip()
        assert output == expected, f"Failed: Expected {{expected}}, Got {{output}}"

if __name__ == '__main__':
    run_test('input1.txt', 'output1.txt')
""")

    # Save samples
    for i, (inp, outp) in enumerate(samples, 1):
        with open(os.path.join(folder, f"input{i}.txt"), "w", encoding="utf-8") as f:
            f.write(inp)
        with open(os.path.join(folder, f"output{i}.txt"), "w", encoding="utf-8") as f:
            f.write(outp)

    print(f"✅ Folder created: {folder}")

# === Entry ===
if __name__ == "__main__":
    contest_id = input("Enter contest ID (e.g. 1700): ").strip()
    problem_index = input("Enter problem index (e.g. A): ").strip().upper()

    title, html, soup = fetch_problem(contest_id, problem_index)
    samples = extract_samples(soup)
    create_files(contest_id, problem_index, title, html, samples)