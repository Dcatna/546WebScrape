from bs4 import BeautifulSoup
import csv

with open("courses.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

course_blocks = soup.find_all("li", {"data-automation-id": "compositeContainer"})

courses = []

for block in course_blocks:
    title_div = block.find("div", role="button")
    aria_label = title_div.get("aria-label", "") if title_div else ""
    course_title = (
        aria_label.replace("More ", "")
                .replace("Related Actions ", "")
                .strip()
        if aria_label else ""
    )

    meta_tag = block.find("span", {"data-automation-id": "compositeSubHeaderOne"})
    meta_text = meta_tag.get_text(strip=True) if meta_tag else ""
    status = instructor = ""
    if "|" in meta_text:
        parts = [part.strip() for part in meta_text.split("|")]
        if len(parts) >= 2:
            status, instructor = parts[0], parts[1]
    elif meta_text:
        status = meta_text

    details_tag = block.find("span", {"data-automation-id": "compositeSubHeaderTwo"})
    section_details = details_tag.get_text(strip=True) if details_tag else ""

    courses.append({
        "Course": course_title,
        "Status": status,
        "Instructor": instructor,
        "Section Details": section_details
    })

with open("parsed_courses.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Course", "Status", "Instructor", "Section Details"])
    writer.writeheader()
    writer.writerows(courses)

print(f"saved {len(courses)} coruses to parsed_courses.csv")
