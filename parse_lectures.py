# -*- coding: utf-8 -*-
import os
import json
import docx

BASE_DIR = r"C:\antigravity\1151101AI做影片\downloads\講義"

def docx_to_structure(fname):
    p = os.path.join(BASE_DIR, fname)
    doc = docx.Document(p)
    
    sections = []
    current_sec = {"title": fname.replace(".docx", ""), "items": []}
    
    for p_elem in doc.paragraphs:
        text = p_elem.text.strip()
        if not text:
            continue
        style = p_elem.style.name
        if style.startswith("Heading 1") or text.startswith(("一、", "二、", "三、", "四、", "五、", "六、", "七、", "八、", "九、")):
            if current_sec["items"]:
                sections.append(current_sec)
            current_sec = {"title": text, "items": []}
        else:
            current_sec["items"].append({"style": style, "text": text})
            
    if current_sec["items"]:
        sections.append(current_sec)
        
    # Also extract tables
    tables_data = []
    for t_idx, table in enumerate(doc.tables):
        rows = []
        for row in table.rows:
            rows.append([cell.text.strip().replace("\n", "<br>") for cell in row.cells])
        tables_data.append(rows)
        
    return {"title": fname, "sections": sections, "tables": tables_data}

doc1 = docx_to_structure("1151101-呂聰賢-AI 短影音創作全流程：課後複習講義與實作檢核表.docx")
doc2 = docx_to_structure("1151101-呂聰賢-AI影音創作教學講義.docx")

out_path = r"C:\antigravity\1151101AI做影片\lectures_data.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({"review_guide": doc1, "teaching_guide": doc2}, f, ensure_ascii=False, indent=2)

print(f"Saved lectures data to {out_path} ({os.path.getsize(out_path)} bytes)")
