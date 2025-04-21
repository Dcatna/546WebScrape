from bs4 import BeautifulSoup
import csv

with open("courses.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

course_blocks = soup.find_all("li", {"data-automation-id": "compositeContainer"})

courses = []

for block in course_blocks:
    title_div = block.find("div", role="button")
    aria_label = title_div.get("aria-label", "") if title_div else ""
    course_section = ( # changed from title to section
        aria_label.replace("More ", "")
                .replace("Related Actions ", "")
                .strip()
        if aria_label else ""
    )

    meta_tag = block.find("span", {"data-automation-id": "compositeSubHeaderOne"})
    meta_text = meta_tag.get_text(strip=True) if meta_tag else ""
    status = instructor = ""
    # if "|" in meta_text:
    #     parts = [part.strip() for part in meta_text.split("|")]
    #     if len(parts) >= 2:
    #         status, instructor = parts[0], parts[1]
    # elif meta_text:
    #     status = meta_text
    
    course_details = meta_text.split('|')
    match len(course_details):
        case 0:
            course_title = status = instructor = ""
        case 1:
            course_title = course_details[0].strip()
            status = instructor = ""
        case 2:
            course_title = course_details[0].strip()
            status = course_details[1].strip()
            instructor = ""
        case 3:
            course_title = course_details[0].strip()
            status = course_details[1].strip()
            instructor = course_details[2].strip()
        case _:
            course_title = status = instructor = ""
            break


    details_tag = block.find("span", {"data-automation-id": "compositeDetailPreview"}).find("div", {"data-automation-id": "promptOption"})
    # print(f"{details_tag.get_text()}\n")
    section_details = details_tag.get_text(strip=True) if details_tag else ""
    
    
    # print(f"{section_details}\n")
    section_details = section_details.split("|")
    match len(section_details):
        case 0:
            location = days = time = ""
        case 1:
            location = section_details[0].strip()
            days = time = ""
        case 2:
            location = section_details[0].strip()
            days = section_details[1].strip()
            time = ""
        case 3:
            location = section_details[0].strip()
            days = section_details[1].strip()
            time = section_details[2].strip()
        case _:
            location = days = time = ""

    # if (section_details == "") :
    #     # print(f"{course_section}\n")
    #     location = days = time = ""

    courses.append({
        "Course Section": course_section,
        "Course": course_title,
        "Status": status,
        "Instructor": instructor,
        # "Section Details": section_details
        "Location": location,
        "Days": days,
        "Time": time
    })

with open("parsed_courses.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Course Section", "Course", "Status", "Instructor", "Location", "Days", "Time"])
    writer.writeheader()
    writer.writerows(courses)

print(f"saved {len(courses)} coruses to parsed_courses.csv")

