# -*- coding: utf-8 -*-
import os
import re
import json
import pypdfium2 as pdfium

BASE_DIR = r"C:\antigravity\1151101AI做影片\downloads\AI平台對話"

def parse_gemini(fname):
    p = os.path.join(BASE_DIR, fname)
    pdf = pdfium.PdfDocument(p)
    text = '\n'.join([pdf[i].get_textpage().get_text_range() for i in range(len(pdf))])
    
    turn_matches = list(re.finditer(r'Turn\s+(\d+)', text))
    turns = []
    for i, m in enumerate(turn_matches):
        turn_num = int(m.group(1))
        start = m.end()
        end = turn_matches[i+1].start() if i+1 < len(turn_matches) else len(text)
        turn_text = text[start:end].strip()
        
        user_match = re.search(r'👤\s*使用者', turn_text)
        bot_match = re.search(r'🤖\s*助理', turn_text)
        
        user_content = ''
        bot_content = ''
        if user_match and bot_match:
            user_content = turn_text[user_match.end():bot_match.start()].strip()
            bot_content = turn_text[bot_match.end():].strip()
        elif user_match:
            user_content = turn_text[user_match.end():].strip()
        else:
            bot_content = turn_text
            
        # Clean up header/footer artifacts like URLs and timestamps
        clean_user = re.sub(r'https://gemini\.google\.com/app/\S+', '', user_content)
        clean_user = re.sub(r'\d{4}/\d{1,2}/\d{1,2}\s+(?:上午|下午)\d+:\d+', '', clean_user)
        clean_user = re.sub(r'\d+/\d+', '', clean_user).strip()

        clean_bot = re.sub(r'https://gemini\.google\.com/app/\S+', '', bot_content)
        clean_bot = re.sub(r'\d{4}/\d{1,2}/\d{1,2}\s+(?:上午|下午)\d+:\d+', '', clean_bot)
        clean_bot = re.sub(r'\d+/\d+', '', clean_bot).strip()

        turns.append({
            'turn': turn_num,
            'user': clean_user,
            'assistant': clean_bot
        })
    return turns

def parse_chatgpt(fname):
    p = os.path.join(BASE_DIR, fname)
    pdf = pdfium.PdfDocument(p)
    text = '\n'.join([pdf[i].get_textpage().get_text_range() for i in range(len(pdf))])

    # In this PDF, the format has '你說：' and 'ChatGPT 說：'
    # Let's split by these tokens
    pattern = re.compile(r'(你說：|ChatGPT 說：)')
    parts = pattern.split(text)
    
    turns = []
    current_user = ''
    current_bot = ''
    turn_counter = 1
    
    i = 1
    while i < len(parts):
        role = parts[i].strip()
        content = parts[i+1].strip() if i+1 < len(parts) else ''
        content = re.sub(r'https://chatgpt\.com/\S+', '', content)
        content = re.sub(r'\d{4}/\d{1,2}/\d{1,2}\s+(?:上午|下午)\d+:\d+', '', content)
        content = re.sub(r'\d+/\d+', '', content).strip()
        
        if role == '你說：':
            if current_user and current_bot:
                turns.append({
                    'turn': turn_counter,
                    'user': current_user,
                    'assistant': current_bot
                })
                turn_counter += 1
                current_user = ''
                current_bot = ''
            current_user = (current_user + '\n' + content).strip()
        elif role == 'ChatGPT 說：':
            current_bot = (current_bot + '\n' + content).strip()
        i += 2
        
    if current_user or current_bot:
        turns.append({
            'turn': turn_counter,
            'user': current_user,
            'assistant': current_bot
        })
    return turns

husky_gemini = parse_gemini('哈士奇動畫企劃方案建議 - Gemini-劇本-照片-影片提示詞.pdf')
shepherd_gemini = parse_gemini('邊際牧羊犬動畫企劃方案建議 - Gemini-劇本-照片-影片提示詞.pdf')
shepherd_chatgpt = parse_chatgpt('邊際牧羊犬動畫企劃方案建議 - ChatGPT-劇本-照片-影片提示詞.pdf')

data = {
    'gemini_husky': {
        'title': 'Google Gemini 實戰對話：哈士奇動畫企劃《四季的足跡》',
        'model': 'Google Gemini',
        'badge': 'Gemini 2.0 / Advanced',
        'color': '#38bdf8',
        'turns': husky_gemini
    },
    'chatgpt_shepherd': {
        'title': 'ChatGPT 實戰對話：邊境牧羊犬企劃《明天，也要一起散步》',
        'model': 'OpenAI ChatGPT-4o',
        'badge': 'ChatGPT Plus / 4o',
        'color': '#10b981',
        'turns': shepherd_chatgpt
    },
    'gemini_shepherd': {
        'title': 'Google Gemini 實戰對話：邊境牧羊犬企劃《雨中的牧羊人》',
        'model': 'Google Gemini',
        'badge': 'Gemini 2.0 / Advanced',
        'color': '#818cf8',
        'turns': shepherd_gemini
    }
}

out_path = r'C:\antigravity\1151101AI做影片\ai_dialogues.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully parsed AI dialogues:")
print(f"  Gemini Husky: {len(husky_gemini)} turns")
print(f"  ChatGPT Shepherd: {len(shepherd_chatgpt)} turns")
print(f"  Gemini Shepherd: {len(shepherd_gemini)} turns")
print(f"Saved to {out_path} ({os.path.getsize(out_path)} bytes)")
