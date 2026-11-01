# -*- coding: utf-8 -*-
"""
Flagship Website Generator for 1151101 AI Video Course
Updates:
#1: Online Course Lecture Notes from 'downloads/講義'
#2: Presentation Slide Viewer from 'downloads/簡報' (replacing old slides)
#3: AI Platform Dialogue Simulator from 'downloads/AI平台對話'
#4: Prominent Teaching Visual Flowcharts at the top of the site from 'downloads/教學圖'
"""

import os
import json

BASE_DIR = r"C:\antigravity\1151101AI做影片"

with open(os.path.join(BASE_DIR, "ai_dialogues.json"), "r", encoding="utf-8") as f:
    dialogues_data = json.load(f)

with open(os.path.join(BASE_DIR, "lectures_data.json"), "r", encoding="utf-8") as f:
    lectures_data = json.load(f)

dialogues_json_str = json.dumps(dialogues_data, ensure_ascii=False)

html_code = f"""<!DOCTYPE html>
<html lang="zh-TW" class="scroll-smooth">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI 影片創作與生成式影音工具應用 · 呂聰賢老師研習旗艦網</title>
<meta name="description" content="1151101 呂聰賢老師 AI 影片創作與生成式影音工具應用：核心教學大圖、線上教學講義、84頁精選簡報觀看器、AI平台真實對話示範與4部實戰成果短片。">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg-main: #090d16;
    --bg-card: rgba(18, 26, 43, 0.75);
    --bg-card-hover: rgba(28, 40, 65, 0.9);
    --border-color: rgba(56, 189, 248, 0.15);
    --border-hover: rgba(56, 189, 248, 0.45);
    --primary: #38bdf8;
    --primary-glow: rgba(56, 189, 248, 0.35);
    --secondary: #818cf8;
    --accent: #34d399;
    --accent-amber: #fbbf24;
    --accent-rose: #fb7185;
    --text-main: #f1f5f9;
    --text-muted: #94a3b8;
    --text-dim: #64748b;
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background-color: var(--bg-main);
    color: var(--text-main);
    font-family: 'Noto Sans TC', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    overflow-x: hidden;
    background-image: 
      radial-gradient(circle at 15% 15%, rgba(56, 189, 248, 0.08) 0%, transparent 40%),
      radial-gradient(circle at 85% 65%, rgba(129, 140, 248, 0.08) 0%, transparent 45%),
      radial-gradient(circle at 50% 90%, rgba(52, 211, 153, 0.05) 0%, transparent 50%);
    background-attachment: fixed;
  }}

  ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
  ::-webkit-scrollbar-track {{ background: #0b1120; }}
  ::-webkit-scrollbar-thumb {{ background: #1e293b; border-radius: 4px; }}
  ::-webkit-scrollbar-thumb:hover {{ background: #38bdf8; }}

  /* Sticky Navigation */
  header.navbar {{
    position: sticky;
    top: 0;
    z-index: 1000;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    background: rgba(9, 13, 22, 0.88);
    border-bottom: 1px solid var(--border-color);
  }}
  .nav-container {{
    max-width: 1440px;
    margin: 0 auto;
    padding: 12px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
  }}
  .brand {{
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
    color: var(--text-main);
  }}
  .brand-logo {{
    width: 40px;
    height: 40px;
    border-radius: 10px;
    background: linear-gradient(135deg, #38bdf8, #818cf8);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    box-shadow: 0 0 16px var(--primary-glow);
  }}
  .brand-title {{
    font-size: 16px;
    font-weight: 800;
    background: linear-gradient(90deg, #38bdf8, #818cf8, #ffffff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .brand-badge {{
    font-size: 11px;
    background: rgba(56, 189, 248, 0.15);
    color: #38bdf8;
    padding: 2px 8px;
    border-radius: 999px;
    border: 1px solid rgba(56, 189, 248, 0.3);
  }}
  .nav-links {{
    display: flex;
    gap: 4px;
    align-items: center;
    list-style: none;
  }}
  .nav-links a {{
    color: var(--text-muted);
    text-decoration: none;
    padding: 6px 12px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 500;
    transition: all 0.2s;
  }}
  .nav-links a:hover {{
    color: #38bdf8;
    background: rgba(56, 189, 248, 0.1);
  }}
  .btn-gh {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 7px 14px;
    border-radius: 8px;
    background: #1e293b;
    color: #f8fafc;
    text-decoration: none;
    font-size: 13px;
    font-weight: 600;
    border: 1px solid #334155;
    transition: all 0.2s;
  }}
  .btn-gh:hover {{
    background: #334155;
    border-color: #38bdf8;
  }}

  /* Hero Section */
  .hero-section {{
    padding: 56px 24px 36px;
    max-width: 1320px;
    margin: 0 auto;
    text-align: center;
  }}
  .hero-pill {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 18px;
    border-radius: 999px;
    background: rgba(56, 189, 248, 0.12);
    border: 1px solid rgba(56, 189, 248, 0.3);
    color: #38bdf8;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 20px;
  }}
  .hero-title {{
    font-size: clamp(30px, 4.5vw, 54px);
    font-weight: 900;
    line-height: 1.18;
    letter-spacing: -1px;
    margin-bottom: 16px;
    background: linear-gradient(135deg, #ffffff 40%, #bae6fd 80%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .hero-desc {{
    font-size: clamp(15px, 1.8vw, 18px);
    color: var(--text-muted);
    max-width: 880px;
    margin: 0 auto 28px;
    line-height: 1.7;
  }}
  .instructor-credits {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 16px;
    margin-bottom: 28px;
    font-size: 14px;
  }}
  .instructor-chip {{
    background: rgba(30, 41, 59, 0.6);
    padding: 6px 16px;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,0.08);
  }}
  .hero-actions {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 40px;
  }}
  .btn-primary {{
    background: linear-gradient(135deg, #0284c7, #38bdf8);
    color: #04121d;
    font-weight: 700;
    padding: 11px 24px;
    border-radius: 10px;
    text-decoration: none;
    font-size: 14px;
    box-shadow: 0 4px 18px rgba(56, 189, 248, 0.4);
    transition: all 0.2s;
  }}
  .btn-primary:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 22px rgba(56, 189, 248, 0.6);
  }}
  .btn-secondary {{
    background: rgba(30, 41, 59, 0.8);
    color: #f1f5f9;
    font-weight: 600;
    padding: 11px 22px;
    border-radius: 10px;
    text-decoration: none;
    font-size: 14px;
    border: 1px solid rgba(255,255,255,0.12);
    transition: all 0.2s;
  }}
  .btn-secondary:hover {{
    background: rgba(51, 65, 85, 0.9);
    border-color: #38bdf8;
    transform: translateY(-2px);
  }}

  /* Section Containers */
  section.module-section {{
    max-width: 1400px;
    margin: 0 auto 72px;
    padding: 0 24px;
  }}
  .section-header {{
    text-align: center;
    margin-bottom: 36px;
  }}
  .section-tag {{
    display: inline-block;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #38bdf8;
    background: rgba(56, 189, 248, 0.1);
    padding: 4px 14px;
    border-radius: 999px;
    margin-bottom: 10px;
    border: 1px solid rgba(56, 189, 248, 0.2);
  }}
  .section-title {{
    font-size: clamp(24px, 3.2vw, 34px);
    font-weight: 800;
    letter-spacing: -0.5px;
    margin-bottom: 10px;
  }}
  .section-desc {{
    font-size: 14px;
    color: var(--text-muted);
    max-width: 720px;
    margin: 0 auto;
  }}

  /* TOP VISUAL TEACHING CHARTS (#4 Focus) */
  .teaching-charts-container {{
    background: rgba(15, 23, 42, 0.85);
    border: 1px solid var(--border-color);
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 16px 40px rgba(0,0,0,0.4);
  }}
  .chart-nav-tabs {{
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 20px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    padding-bottom: 14px;
  }}
  .btn-chart-tab {{
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 700;
    background: #1e293b;
    color: #94a3b8;
    border: 1px solid #334155;
    cursor: pointer;
    transition: all 0.2s;
  }}
  .btn-chart-tab:hover {{
    color: #f1f5f9;
    border-color: #38bdf8;
  }}
  .btn-chart-tab.active {{
    background: #0284c7;
    color: #ffffff;
    border-color: #38bdf8;
    box-shadow: 0 0 12px rgba(56, 189, 248, 0.35);
  }}
  .chart-display-card {{
    display: grid;
    grid-template-columns: 1.4fr 1fr;
    gap: 24px;
    align-items: center;
  }}
  @media (max-width: 992px) {{
    .chart-display-card {{ grid-template-columns: 1fr; }}
  }}
  .chart-img-frame {{
    width: 100%;
    aspect-ratio: 16 / 9;
    background: #000;
    border-radius: 12px;
    overflow: hidden;
    position: relative;
    cursor: zoom-in;
    border: 1px solid rgba(255,255,255,0.1);
  }}
  .chart-img-frame img {{
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
    transition: transform 0.3s ease;
  }}
  .chart-img-frame:hover img {{
    transform: scale(1.02);
  }}
  .chart-badge-zoom {{
    position: absolute;
    bottom: 12px;
    right: 12px;
    background: rgba(0,0,0,0.7);
    color: #38bdf8;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 6px;
    border: 1px solid rgba(56, 189, 248, 0.3);
    backdrop-filter: blur(4px);
  }}
  .chart-text-box h3 {{
    font-size: 22px;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 8px;
  }}
  .chart-text-box p.lead {{
    font-size: 14px;
    color: #38bdf8;
    font-weight: 600;
    margin-bottom: 16px;
  }}
  .chart-steps-list {{
    list-style: none;
    font-size: 13px;
    color: var(--text-muted);
  }}
  .chart-steps-list li {{
    margin-bottom: 10px;
    padding-left: 20px;
    position: relative;
    line-height: 1.6;
  }}
  .chart-steps-list li::before {{
    content: "✓";
    position: absolute;
    left: 0;
    color: #34d399;
    font-weight: 700;
  }}

  /* NEW SLIDE PRESENTATION VIEWER (#2 Focus) */
  .viewer-wrapper {{
    background: rgba(15, 23, 42, 0.85);
    border: 1px solid var(--border-color);
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
  }}
  .viewer-topbar {{
    background: #111827;
    padding: 14px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  }}
  .deck-tabs {{
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
  }}
  .btn-deck {{
    padding: 7px 14px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 600;
    border: 1px solid #374151;
    cursor: pointer;
    background: #1f2937;
    color: #9ca3af;
    transition: all 0.2s;
  }}
  .btn-deck:hover {{
    color: #f1f5f9;
    border-color: #38bdf8;
  }}
  .btn-deck.active {{
    background: #0284c7;
    color: #ffffff;
    border-color: #38bdf8;
    box-shadow: 0 0 12px rgba(56, 189, 248, 0.35);
  }}
  .viewer-screen {{
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
    background: #000;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }}
  .viewer-screen img {{
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
    user-select: none;
    transition: opacity 0.2s;
  }}
  .screen-overlay-btn {{
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(0, 0, 0, 0.55);
    color: #fff;
    border: 1px solid rgba(255, 255, 255, 0.25);
    width: 48px;
    height: 48px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 20px;
    backdrop-filter: blur(4px);
    transition: all 0.2s;
    z-index: 10;
  }}
  .screen-overlay-btn:hover {{
    background: rgba(56, 189, 248, 0.85);
    color: #0f172a;
    border-color: #38bdf8;
  }}
  .btn-prev {{ left: 18px; }}
  .btn-next {{ right: 18px; }}

  .viewer-info-panel {{
    padding: 16px 24px;
    background: #111827;
    border-top: 1px solid rgba(255,255,255,0.06);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 14px;
  }}
  .slide-counter {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    color: var(--text-muted);
  }}
  .btn-icon {{
    padding: 7px 14px;
    border-radius: 8px;
    background: #1f2937;
    color: #e5e7eb;
    border: 1px solid #374151;
    cursor: pointer;
    font-size: 13px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s;
  }}
  .btn-icon:hover {{
    background: #374151;
    color: #38bdf8;
    border-color: #38bdf8;
  }}

  /* Filmstrip Thumbnails */
  .filmstrip-container {{
    display: flex;
    gap: 8px;
    padding: 12px 20px;
    background: #090e17;
    overflow-x: auto;
    border-top: 1px solid rgba(255,255,255,0.06);
  }}
  .thumb-item {{
    flex: 0 0 110px;
    aspect-ratio: 16 / 9;
    border-radius: 6px;
    overflow: hidden;
    cursor: pointer;
    border: 2px solid transparent;
    opacity: 0.6;
    transition: all 0.2s;
    background: #000;
  }}
  .thumb-item:hover {{
    opacity: 0.9;
    transform: translateY(-2px);
  }}
  .thumb-item.active {{
    border-color: #38bdf8;
    opacity: 1;
    box-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
  }}
  .thumb-item img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }}

  /* AI DIALOGUE SIMULATOR (#3 Focus) */
  .dialogue-box {{
    background: rgba(15, 23, 42, 0.85);
    border: 1px solid var(--border-color);
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 16px 40px rgba(0,0,0,0.4);
  }}
  .dialogue-tabs {{
    display: flex;
    gap: 8px;
    padding: 16px 24px;
    background: #111827;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    flex-wrap: wrap;
  }}
  .btn-chat-tab {{
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 700;
    background: #1e293b;
    color: #94a3b8;
    border: 1px solid #334155;
    cursor: pointer;
    transition: all 0.2s;
  }}
  .btn-chat-tab:hover {{
    color: #f1f5f9;
    border-color: #38bdf8;
  }}
  .btn-chat-tab.active {{
    background: #0284c7;
    color: #ffffff;
    border-color: #38bdf8;
    box-shadow: 0 0 12px rgba(56, 189, 248, 0.35);
  }}
  .chat-stream-window {{
    padding: 24px;
    max-height: 650px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 20px;
    background: #090e17;
  }}
  .chat-turn-group {{
    border-bottom: 1px dashed rgba(255,255,255,0.1);
    padding-bottom: 20px;
  }}
  .chat-turn-badge {{
    display: inline-block;
    font-size: 11px;
    font-family: 'JetBrains Mono', monospace;
    color: var(--text-dim);
    background: #1e293b;
    padding: 2px 8px;
    border-radius: 4px;
    margin-bottom: 12px;
  }}
  .chat-bubble {{
    display: flex;
    gap: 14px;
    margin-bottom: 14px;
  }}
  .chat-avatar {{
    width: 36px;
    height: 36px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    flex-shrink: 0;
  }}
  .avatar-user {{ background: #3b82f6; color: #fff; }}
  .avatar-gemini {{ background: linear-gradient(135deg, #38bdf8, #818cf8); color: #fff; }}
  .avatar-chatgpt {{ background: #10b981; color: #fff; }}
  .bubble-content {{
    flex: 1;
    background: rgba(30, 41, 59, 0.7);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 16px 20px;
    font-size: 14px;
    line-height: 1.65;
    position: relative;
  }}
  .bubble-content.user-bubble {{
    background: rgba(37, 99, 235, 0.12);
    border-color: rgba(59, 130, 246, 0.3);
  }}
  .bubble-content.ai-bubble {{
    background: rgba(18, 26, 43, 0.85);
    border-color: rgba(56, 189, 248, 0.25);
  }}
  .bubble-author {{
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .bubble-text {{
    white-space: pre-wrap;
    font-family: inherit;
    color: #e2e8f0;
  }}

  /* ONLINE LECTURE NOTES (#1 Focus) */
  .lecture-tabs {{
    display: flex;
    gap: 10px;
    margin-bottom: 24px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    padding-bottom: 12px;
    flex-wrap: wrap;
  }}
  .btn-lec-tab {{
    padding: 10px 20px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 700;
    background: #1e293b;
    color: #94a3b8;
    border: 1px solid #334155;
    cursor: pointer;
    transition: all 0.2s;
  }}
  .btn-lec-tab:hover {{
    color: #f1f5f9;
    border-color: #38bdf8;
  }}
  .btn-lec-tab.active {{
    background: #0284c7;
    color: #ffffff;
    border-color: #38bdf8;
    box-shadow: 0 0 12px rgba(56, 189, 248, 0.35);
  }}
  .lecture-pane {{
    display: none;
  }}
  .lecture-pane.active {{
    display: block;
  }}
  .lecture-card {{
    background: rgba(18, 26, 43, 0.75);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 28px;
    margin-bottom: 24px;
  }}
  .lecture-card h3 {{
    font-size: 20px;
    font-weight: 800;
    color: #38bdf8;
    margin-bottom: 14px;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(56, 189, 248, 0.2);
  }}
  .lecture-content p {{
    font-size: 14px;
    color: var(--text-main);
    margin-bottom: 10px;
    line-height: 1.7;
  }}
  .lecture-table-wrap {{
    overflow-x: auto;
    margin: 16px 0;
  }}
  table.lecture-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    color: #e2e8f0;
  }}
  table.lecture-table th, table.lecture-table td {{
    border: 1px solid #334155;
    padding: 10px 14px;
    text-align: left;
  }}
  table.lecture-table th {{
    background: #1e293b;
    color: #38bdf8;
    font-weight: 700;
  }}
  table.lecture-table tr:nth-child(even) {{
    background: rgba(15, 23, 42, 0.5);
  }}

  /* Interactive Checklist */
  .checklist-box {{
    background: rgba(15, 23, 42, 0.75);
    border: 1px solid rgba(56, 189, 248, 0.25);
    border-radius: 16px;
    padding: 24px;
    margin-top: 24px;
  }}
  .checklist-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 14px;
    margin-bottom: 16px;
    padding-bottom: 14px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
  }}
  .progress-bar-bg {{
    width: 100%;
    height: 8px;
    background: #1e293b;
    border-radius: 999px;
    overflow: hidden;
    margin-top: 8px;
  }}
  .progress-bar-fill {{
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, #38bdf8, #34d399);
    transition: width 0.3s ease;
  }}
  .check-item {{
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 10px 14px;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.2s;
    user-select: none;
  }}
  .check-item:hover {{
    background: rgba(56, 189, 248, 0.05);
  }}
  .check-item input[type="checkbox"] {{
    width: 18px;
    height: 18px;
    accent-color: #38bdf8;
    margin-top: 3px;
    cursor: pointer;
  }}
  .check-label {{
    font-size: 14px;
    color: var(--text-main);
  }}
  .check-item.done .check-label {{
    text-decoration: line-through;
    color: var(--text-dim);
  }}

  /* Video Showcase Theater */
  .videos-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
    gap: 20px;
  }}
  .video-card {{
    background: rgba(18, 26, 43, 0.75);
    border: 1px solid var(--border-color);
    border-radius: 18px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    transition: all 0.3s ease;
  }}
  .video-card:hover {{
    border-color: var(--border-hover);
    transform: translateY(-4px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.4);
  }}
  .video-player-wrap {{
    position: relative;
    width: 100%;
    aspect-ratio: 9 / 16;
    background: #000;
    max-height: 480px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .video-player-wrap video {{
    width: 100%;
    height: 100%;
    object-fit: contain;
    background: #000;
  }}
  .video-info {{
    padding: 18px;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .video-meta {{
    display: flex;
    gap: 6px;
    margin-bottom: 8px;
    flex-wrap: wrap;
  }}
  .video-badge {{
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 6px;
  }}
  .badge-dur {{ background: rgba(52, 211, 153, 0.15); color: #34d399; border: 1px solid rgba(52, 211, 153, 0.3); }}
  .badge-spec {{ background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }}
  .badge-voice {{ background: rgba(129, 140, 248, 0.15); color: #818cf8; border: 1px solid rgba(129, 140, 248, 0.3); }}
  .video-title {{
    font-size: 17px;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 4px;
  }}
  .video-tagline {{
    font-size: 12px;
    color: var(--text-muted);
    font-style: italic;
    margin-bottom: 10px;
  }}
  .video-features {{
    font-size: 12px;
    color: var(--text-dim);
    line-height: 1.5;
  }}

  /* Downloads Grid */
  .downloads-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 16px;
  }}
  .download-card {{
    background: rgba(18, 26, 43, 0.7);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 18px;
    display: flex;
    align-items: center;
    gap: 14px;
    transition: all 0.2s;
    text-decoration: none;
    color: inherit;
  }}
  .download-card:hover {{
    background: rgba(28, 40, 65, 0.85);
    border-color: #38bdf8;
    transform: translateY(-2px);
  }}
  .dl-icon {{
    width: 42px;
    height: 42px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    flex-shrink: 0;
  }}
  .dl-pdf {{ background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }}
  .dl-docx {{ background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); }}
  .dl-png {{ background: rgba(52, 211, 153, 0.15); color: #34d399; border: 1px solid rgba(52, 211, 153, 0.3); }}
  .dl-info h4 {{
    font-size: 14px;
    font-weight: 700;
    color: #f1f5f9;
    margin-bottom: 2px;
  }}
  .dl-info p {{
    font-size: 12px;
    color: var(--text-dim);
  }}

  /* Lightbox Modal */
  .modal-overlay {{
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.9);
    z-index: 99999;
    align-items: center;
    justify-content: center;
    padding: 20px;
    cursor: zoom-out;
  }}
  .modal-overlay.active {{
    display: flex;
  }}
  .modal-img {{
    max-width: 95vw;
    max-height: 95vh;
    border-radius: 8px;
    box-shadow: 0 0 30px rgba(0,0,0,0.8);
    object-fit: contain;
  }}

  /* Toast Notification */
  .toast {{
    position: fixed;
    bottom: 24px;
    right: 24px;
    background: #0284c7;
    color: #ffffff;
    padding: 12px 20px;
    border-radius: 8px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    font-size: 14px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 8px;
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.3s ease;
    z-index: 9999;
    pointer-events: none;
  }}
  .toast.show {{
    opacity: 1;
    transform: translateY(0);
  }}

  /* Footer */
  footer {{
    background: #070a12;
    border-top: 1px solid var(--border-color);
    padding: 48px 24px 32px;
    text-align: center;
  }}
  .footer-content {{
    max-width: 1200px;
    margin: 0 auto;
    font-size: 14px;
    color: var(--text-dim);
  }}
  .footer-links {{
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-bottom: 20px;
    flex-wrap: wrap;
  }}
  .footer-links a {{
    color: var(--text-muted);
    text-decoration: none;
    transition: color 0.2s;
  }}
  .footer-links a:hover {{
    color: #38bdf8;
  }}
</style>
</head>
<body>

<!-- Navbar -->
<header class="navbar">
  <div class="nav-container">
    <a href="#" class="brand">
      <div class="brand-logo">🎬</div>
      <div>
        <div class="brand-title">AI 影片創作全流程旗艦網</div>
        <div class="brand-badge">呂聰賢老師 · 1151101研習</div>
      </div>
    </a>
    <ul class="nav-links">
      <li><a href="#focus-charts">核心教學大圖</a></li>
      <li><a href="#slides">研習精選簡報</a></li>
      <li><a href="#lectures">線上教學講義</a></li>
      <li><a href="#ai-dialogues">AI平台對話示範</a></li>
      <li><a href="#theater">實戰作品劇院</a></li>
      <li><a href="#downloads">教材下載</a></li>
    </ul>
    <div style="display:flex; align-items:center; gap:10px;">
      <a href="https://github.com/yaoshuchin/1151101-ai-video-course" target="_blank" class="btn-gh">
        <svg height="16" width="16" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
        GitHub 專案
      </a>
    </div>
  </div>
</header>

<!-- Hero Section -->
<section class="hero-section">
  <div class="hero-pill">✨ 1151101 教師專業成長研習 · 生成式影音全流程實戰</div>
  <h1 class="hero-title">AI 影片創作與<br>生成式影音工具應用</h1>
  <p class="hero-desc">
    整合研習核心教學圖解、數位線上講義、4 大精選簡報觀看器、Gemini / ChatGPT 實戰對話示範與 4 部高畫質完整動畫作品——打造最強生成式影音教學入口。
  </p>
  
  <div class="instructor-credits">
    <div class="instructor-chip"><span>👨‍🏫 主講：</span><strong>呂聰賢老師</strong></div>
    <div class="instructor-chip"><span>🤝 協作助教：</span><strong>阿啄校長</strong></div>
    <div class="instructor-chip"><span>⚡ 整理策劃：</span><strong>AI 軍師</strong></div>
  </div>

  <div class="hero-actions">
    <a href="#focus-charts" class="btn-primary">📌 查看核心教學大圖</a>
    <a href="#slides" class="btn-secondary">📊 觀看 84 頁精選簡報</a>
    <a href="#ai-dialogues" class="btn-secondary">🤖 探索 AI 平台實戰對話</a>
  </div>
</section>

<!-- #4 FOCUS: TEACHING CHARTS (Placed Prominently at the Top) -->
<section id="focus-charts" class="module-section">
  <div class="section-header">
    <span class="section-tag">Key Knowledge Visualized</span>
    <h2 class="section-title">核心教學圖解 · 重點流程全覽</h2>
    <p class="section-desc">研習最精華的 4 大教學核心架構圖，以圖解方式梳理 AI 短影音、動畫三步驟與剪輯後製標準程序。（點擊圖片可放大檢視）</p>
  </div>

  <div class="teaching-charts-container">
    <div class="chart-nav-tabs">
      <button class="btn-chart-tab active" onclick="switchChart(1)">1️⃣ AI 短影音創作全流程圖解</button>
      <button class="btn-chart-tab" onclick="switchChart(2)">2️⃣ AI 動畫影片創作三步驟</button>
      <button class="btn-chart-tab" onclick="switchChart(3)">3️⃣ AI 動畫影片創作全攻略</button>
      <button class="btn-chart-tab" onclick="switchChart(4)">4️⃣ AI 影片創作剪輯流程</button>
    </div>

    <div class="chart-display-card">
      <div class="chart-img-frame" onclick="openLightbox(document.getElementById('chartImg').src)">
        <img id="chartImg" src="assets/charts/chart1_short_video_workflow.png" alt="AI 短影音創作全流程圖解">
        <span class="chart-badge-zoom">🔍 點擊查看超高畫質大圖</span>
      </div>
      <div class="chart-text-box">
        <h3 id="chartTitle">AI 短影音創作全流程圖解</h3>
        <p class="lead" id="chartLead">從概念、圖像、動態到後製的一體化生產管線</p>
        <ul class="chart-steps-list" id="chartSteps">
          <li><strong>故事與腳本架構：</strong> 在單一 Gemini 對話中鎖定人物設定與情節綱要，確保上下文記憶不丟失。</li>
          <li><strong>視覺一致性錨定：</strong> 預先產出三視圖定裝照，固定髮型、服飾、年齡與毛色特徵。</li>
          <li><strong>分鏡提示詞工程：</strong> 中文供創作者構思檢驗，英文提示詞供模型生成高精度圖像與動態。</li>
          <li><strong>剪映後製整合：</strong> 時間軸順序編排、TTS 統一旁白聲線、文稿匹配字幕與 BGM 自然淡出。</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- #2 FOCUS: PRESENTATION SLIDES VIEWER (from downloads/簡報) -->
<section id="slides" class="module-section">
  <div class="section-header">
    <span class="section-tag">Slide Presentation Decks</span>
    <h2 class="section-title">研習精選簡報 · 84 頁線上觀看器</h2>
    <p class="section-desc">精選四大主題投影片（Google AI 動畫實戰、動畫導演大師班、AI 影音創作全攻略雙版本），支援全螢幕、鍵盤左右鍵切換與縮圖導覽。</p>
  </div>

  <div class="viewer-wrapper">
    <div class="viewer-topbar">
      <div class="deck-tabs">
        <button class="btn-deck active" onclick="switchDeck('deck1_google_ai', 'Google AI 動畫實戰指南')">📕 Google AI 動畫實戰指南 (21頁)</button>
        <button class="btn-deck" onclick="switchDeck('deck2_director', 'AI 動畫導演實戰大師班')">🎬 AI 動畫導演實戰大師班 (21頁)</button>
        <button class="btn-deck" onclick="switchDeck('deck3_guide_a', 'AI 影音創作全攻略 A')">📘 AI 影音創作全攻略 A (21頁)</button>
        <button class="btn-deck" onclick="switchDeck('deck4_guide_b', 'AI 影音創作全攻略 B')">📙 AI 影音創作全攻略 B (21頁)</button>
      </div>
      <div class="viewer-controls">
        <span class="slide-counter" id="slideNumDisplay">投影片 1 / 21</span>
        <button class="btn-icon" onclick="toggleFullscreen()">⛶ 全螢幕</button>
      </div>
    </div>

    <!-- Viewer Screen -->
    <div class="viewer-screen" id="viewerScreen">
      <button class="screen-overlay-btn btn-prev" onclick="prevSlide()" title="上一頁 (←)">‹</button>
      <img id="currentSlideImg" src="slides/deck1_google_ai/slide_1.jpg" alt="Slide presentation">
      <button class="screen-overlay-btn btn-next" onclick="nextSlide()" title="下一頁 (→)">›</button>
    </div>

    <!-- Slide Details Panel -->
    <div class="viewer-info-panel">
      <div>
        <h3 id="deckTitleDisplay" style="font-size:16px; font-weight:700; color:#f8fafc;">Google AI 動畫實戰指南</h3>
        <p style="font-size:13px; color:#38bdf8;">16:9 寬螢幕超高畫質投影片簡報</p>
      </div>
      <div style="font-size:12px; color:var(--text-dim); text-align:right;">
        鍵盤快捷鍵：<kbd style="background:#1f2937; padding:2px 6px; border-radius:4px; border:1px solid #374151;">←</kbd> 上一頁 ｜ <kbd style="background:#1f2937; padding:2px 6px; border-radius:4px; border:1px solid #374151;">→</kbd> 下一頁
      </div>
    </div>

    <!-- Thumbnails Filmstrip -->
    <div class="filmstrip-container" id="filmstrip"></div>
  </div>
</section>

<!-- #1 FOCUS: ONLINE COURSE LECTURE NOTES (from downloads/講義) -->
<section id="lectures" class="module-section">
  <div class="section-header">
    <span class="section-tag">Curriculum Handbook</span>
    <h2 class="section-title">數位線上講義 · 實作教學專題</h2>
    <p class="section-desc">整合研習兩大官方講義文件精華，涵蓋完整備課指南、實作步驟、避坑檢核表與學生專題教案。</p>
  </div>

  <div class="lecture-tabs">
    <button class="btn-lec-tab active" onclick="switchLectureTab('teaching')">📖 AI 影音創作教學實作講義（9大教學模組）</button>
    <button class="btn-lec-tab" onclick="switchLectureTab('review')">📋 課後複習講義與實作檢核表（SOP & 百寶箱）</button>
  </div>

  <!-- Pane 1: Teaching Guide -->
  <div id="pane-teaching" class="lecture-pane active">
    <div class="lecture-card">
      <h3>一、AI 影音創作工具與工作分工矩陣</h3>
      <div class="lecture-content">
        <p>AI 影片創作並非單一工具完成，而是跨工具的協同管線：</p>
        <div class="lecture-table-wrap">
          <table class="lecture-table">
            <thead>
              <tr><th>階段</th><th>主要工具</th><th>任務產出</th><th>操作關鍵提示</th></tr>
            </thead>
            <tbody>
              <tr><td>1. 企劃與劇本</td><td>ChatGPT / Gemini</td><td>分鏡大綱、人物設定、提示詞</td><td>同一個對話中完成，保留上下文記憶</td></tr>
              <tr><td>2. 圖像生成</td><td>Gemini / Flux / Midjourney</td><td>角色定妝照、分鏡關鍵影格</td><td>決定比例（9:16 或 16:9），固定特徵</td></tr>
              <tr><td>3. 影片生成</td><td>Google Flow / Kling / Runway</td><td>動態影片短片段（6~10 秒）</td><td>選擇適當模型，多段並行提交</td></tr>
              <tr><td>4. 音樂音效</td><td>Gemini 音樂 / Suno / 剪映庫</td><td>純配樂、環境音、動作音效</td><td>音量調降 -15dB，片頭片尾淡入淡出</td></tr>
              <tr><td>5. 剪輯整合</td><td>剪映電腦版 (CapCut)</td><td>完整輸出 1080p MP4</td><td>封面 2~3 秒、文稿匹配字幕、語音 TTS</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="lecture-card">
      <h3>二、AI 角色設計與定妝三視圖法則</h3>
      <div class="lecture-content">
        <p><strong>防跑角核心思維：</strong> 單段生成屬於獨立隨機任務，若未建立強約束，AI 會隨機更換主角外貌與服裝。必須預先在乾淨背景下產出「正面、45度側面、側面、背面」的全身設定圖，並於後續提示詞中鎖定關鍵特徵（如：粉色洋裝、紅色蝴蝶結、黑白相間邊牧）。</p>
      </div>
    </div>

    <div class="lecture-card">
      <h3>三、劇本、分鏡與 9:16 vs 16:9 畫面比例選擇</h3>
      <div class="lecture-content">
        <p><strong>直式 9:16 (1080×1920)：</strong> 手機直向瀏覽（YouTube Shorts, TikTok, Reels, LINE VOOM），構圖需注意上下視覺重心。</p>
        <p><strong>橫式 16:9 (1920×1080)：</strong> 教室投影、電腦螢幕、標準 YouTube，適合大景深與廣闊風景敘事。</p>
      </div>
    </div>

    <div class="lecture-card">
      <h3>四、剪映電腦版後製：TTS 旁白對齊與多語字幕</h3>
      <div class="lecture-content">
        <p><strong>口白長度原則：</strong> 旁白文案朗讀時長必須短於對應鏡頭（例如 6 秒畫面，口白約 2.5～3.5 秒），留白給觀眾感受情緒。</p>
        <p><strong>文稿匹配字幕：</strong> 避免語音辨識錯字，直接輸入純淨中文文稿進行自動對齊，字體加上黑白對比描邊，確保全片清晰辨讀。</p>
      </div>
    </div>
  </div>

  <!-- Pane 2: Review Guide & Checklist -->
  <div id="pane-review" class="lecture-pane">
    <div class="checklist-box">
      <div class="checklist-header">
        <div>
          <h3 style="font-size:18px; font-weight:700; color:#f8fafc;">📋 課後實作避坑檢核表 (自我進度追蹤)</h3>
          <p style="font-size:13px; color:var(--text-muted); margin-top:4px;">勾選已完成的實作步驟，系統會自動在瀏覽器儲存您的進度。</p>
        </div>
        <div style="text-align:right;">
          <span id="checkPercent" style="font-family:'JetBrains Mono'; font-weight:700; color:#38bdf8; font-size:18px;">0%</span>
          <div class="progress-bar-bg" style="width:160px;">
            <div id="checkFill" class="progress-bar-fill"></div>
          </div>
        </div>
      </div>

      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:10px;" id="checklistItems">
        <label class="check-item"><input type="checkbox" onchange="toggleCheck(this)"><span class="check-label">已開啟 Google Drive 資料夾取得研習講義與範例</span></label>
        <label class="check-item"><input type="checkbox" onchange="toggleCheck(this)"><span class="check-label">在同一 Gemini 對話中完成主角與寵物設定稿</span></label>
        <label class="check-item"><input type="checkbox" onchange="toggleCheck(this)"><span class="check-label">確認全片畫面比例（橫式 16:9 或直式 9:16）</span></label>
        <label class="check-item"><input type="checkbox" onchange="toggleCheck(this)"><span class="check-label">已依序生成並下載分鏡圖（命名 P1～P10）</span></label>
        <label class="check-item"><input type="checkbox" onchange="toggleCheck(this)"><span class="check-label">已登入 Google Flow 並建立獨立影片專案</span></label>
        <label class="check-item"><input type="checkbox" onchange="toggleCheck(this)"><span class="check-label">已完成分鏡影片生成並依序下載至本機</span></label>
        <label class="check-item"><input type="checkbox" onchange="toggleCheck(this)"><span class="check-label">已將封面縮短為 2～3 秒置於時間軸開頭</span></label>
        <label class="check-item"><input type="checkbox" onchange="toggleCheck(this)"><span class="check-label">已使用剪映文字朗讀產生全片統一旁白聲線</span></label>
        <label class="check-item"><input type="checkbox" onchange="toggleCheck(this)"><span class="check-label">已透過文稿匹配生成字幕並加上清晰描邊</span></label>
        <label class="check-item"><input type="checkbox" onchange="toggleCheck(this)"><span class="check-label">已設定背景音樂音量適中且結尾自然淡出</span></label>
      </div>
    </div>
  </div>
</section>

<!-- #3 FOCUS: AI DIALOGUE SIMULATOR (from downloads/AI平台對話) -->
<section id="ai-dialogues" class="module-section">
  <div class="section-header">
    <span class="section-tag">Prompt Engineering In Action</span>
    <h2 class="section-title">AI 平台對話示範 · 實錄重現</h2>
    <p class="section-desc">研習現場與 Gemini 及 ChatGPT 的真實多輪對話紀錄，展示如何從最初一句構想到輸出完整 10 段分鏡與圖像、影片雙提示詞。</p>
  </div>

  <div class="dialogue-box">
    <div class="dialogue-tabs">
      <button class="btn-chat-tab active" onclick="switchChat('gemini_husky')">🐕 Google Gemini 示範：哈士奇動畫企劃 (20輪)</button>
      <button class="btn-chat-tab" onclick="switchChat('chatgpt_shepherd')">💬 ChatGPT 示範：邊境牧羊犬企劃 (5輪)</button>
      <button class="btn-chat-tab" onclick="switchChat('gemini_shepherd')">🌧️ Google Gemini 示範：雨中的牧羊人 (19輪)</button>
    </div>

    <!-- Active Chat Title & Info -->
    <div style="padding:14px 24px; background:#1e293b; border-bottom:1px solid rgba(255,255,255,0.08); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
      <div style="display:flex; align-items:center; gap:10px;">
        <span id="chatModelBadge" class="brand-badge">Google Gemini</span>
        <strong id="chatTitleDisplay" style="color:#f8fafc; font-size:15px;">哈士奇動畫企劃方案建議</strong>
      </div>
      <span style="font-size:12px; color:var(--text-muted);">完整還原真實提示詞指令與模型反饋</span>
    </div>

    <!-- Chat Messages Window -->
    <div class="chat-stream-window" id="chatStream"></div>
  </div>
</section>

<!-- SHOWCASE THEATER -->
<section id="theater" class="module-section">
  <div class="section-header">
    <span class="section-tag">Masterpieces Showcase</span>
    <h2 class="section-title">實戰作品影音劇院</h2>
    <p class="section-desc">研習教材實戰合成的四部 9:16 直式高畫質純淨動畫短片（純畫面、動態運鏡、台灣女聲配音與鋼琴混音，無字幕）。</p>
  </div>

  <div class="videos-grid">
    <!-- Video 1 -->
    <div class="video-card">
      <div class="video-player-wrap">
        <video controls preload="metadata" poster="gemini-邊際牧羊犬/P00.jpg">
          <source src="assets/videos/shepherd_in_rain.mp4" type="video/mp4">
        </video>
      </div>
      <div class="video-info">
        <div>
          <div class="video-meta">
            <span class="video-badge badge-dur">⏱️ 63秒</span>
            <span class="video-badge badge-spec">📱 1080×1920 (9:16)</span>
            <span class="video-badge badge-voice">🎙️ 台灣女聲配音</span>
          </div>
          <h3 class="video-title">《雨中的牧羊人》</h3>
          <p class="video-tagline">「大雨會停，而我會一直在這裡。」</p>
          <p class="video-features">黃色雨衣小女孩與黑白邊境牧羊犬在大雨中的溫暖歸途，全片 10 段分鏡與柔和交叉淡出。</p>
        </div>
      </div>
    </div>

    <!-- Video 2 -->
    <div class="video-card">
      <div class="video-player-wrap">
        <video controls preload="metadata" poster="chatGPT-明天，也要一起散步/PP00夕陽下的櫻花散步.png">
          <source src="assets/videos/walk_together_tomorrow.mp4" type="video/mp4">
        </video>
      </div>
      <div class="video-info">
        <div>
          <div class="video-meta">
            <span class="video-badge badge-dur">⏱️ 63秒</span>
            <span class="video-badge badge-spec">📱 1080×1920 (9:16)</span>
            <span class="video-badge badge-voice">🎙️ 台灣女聲配音</span>
          </div>
          <h3 class="video-title">《明天，也要一起散步》</h3>
          <p class="video-tagline">「你走慢了，我就陪你慢慢走。」</p>
          <p class="video-features">櫻花樹下老牧羊犬步履漸緩，女孩停下等待並重溫紅色小球童年回憶，深刻詮釋陪伴的意義。</p>
        </div>
      </div>
    </div>

    <!-- Video 3 -->
    <div class="video-card">
      <div class="video-player-wrap">
        <video controls preload="metadata" poster="gemin-哈士奇/P00.jpg">
          <source src="assets/videos/always_by_my_side.mp4" type="video/mp4">
        </video>
      </div>
      <div class="video-info">
        <div>
          <div class="video-meta">
            <span class="video-badge badge-dur">⏱️ 63秒</span>
            <span class="video-badge badge-spec">📱 1080×1920 (9:16)</span>
            <span class="video-badge badge-voice">🎙️ 台灣女聲配音</span>
          </div>
          <h3 class="video-title">《未來的路，有你同在》</h3>
          <p class="video-tagline">「你看見我所有的夢，溫熱了孤獨的長夜。」</p>
          <p class="video-features">幼犬哈士奇踩翻藍色顏料留下爪印，撫平作畫女孩的挫折，在雪窗與夕陽下共同完成繪本。</p>
        </div>
      </div>
    </div>

    <!-- Video 4 -->
    <div class="video-card">
      <div class="video-player-wrap">
        <video controls preload="metadata" poster="antigravity-山丘上的祕密基地/1151101-PP1.png">
          <source src="assets/videos/whispering_hill.mp4" type="video/mp4">
        </video>
      </div>
      <div class="video-info">
        <div>
          <div class="video-meta">
            <span class="video-badge badge-dur">⏱️ 60秒</span>
            <span class="video-badge badge-spec">📱 1080×1920 (9:16)</span>
            <span class="video-badge badge-voice">🎙️ 台灣女聲配音</span>
          </div>
          <h3 class="video-title">《風吹過的山丘》</h3>
          <p class="video-tagline">「語言到不了的地方，有你無聲的守候。」</p>
          <p class="video-features">吉卜力手繪畫風。老橡樹下大狗叼來彩繪紙風車，清風拂去心中的煩憂，於晚霞海灣並肩遠眺。</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- DOWNLOAD CENTER -->
<section id="downloads" class="module-section">
  <div class="section-header">
    <span class="section-tag">Resource Pack</span>
    <h2 class="section-title">研習教材與檔案下載</h2>
    <p class="section-desc">完整收錄本次研習的 4 大簡報 PDF、2 份講義 DOCX、3 份 AI 平台對話紀錄與 4 張高畫質教學大圖。</p>
  </div>

  <div class="downloads-grid">
    <a href="downloads/簡報/Google_AI_動畫實戰指南.pdf" class="download-card" download>
      <div class="dl-icon dl-pdf">📕</div>
      <div class="dl-info">
        <h4>Google AI 動畫實戰指南</h4>
        <p>21 頁高畫質簡報檔 · PDF (25.8 MB)</p>
      </div>
    </a>

    <a href="downloads/簡報/AI動畫導演實戰大師班.pdf" class="download-card" download>
      <div class="dl-icon dl-pdf">🎬</div>
      <div class="dl-info">
        <h4>AI 動畫導演實戰大師班</h4>
        <p>21 頁高畫質簡報檔 · PDF (20.3 MB)</p>
      </div>
    </a>

    <a href="downloads/簡報/AI_影音創作全攻略.pdf" class="download-card" download>
      <div class="dl-icon dl-pdf">📘</div>
      <div class="dl-info">
        <h4>AI 影音創作全攻略 (版A)</h4>
        <p>21 頁高畫質簡報檔 · PDF (21.9 MB)</p>
      </div>
    </a>

    <a href="downloads/簡報/AI影音創作全攻略.pdf" class="download-card" download>
      <div class="dl-icon dl-pdf">📙</div>
      <div class="dl-info">
        <h4>AI 影音創作全攻略 (版B)</h4>
        <p>21 頁高畫質簡報檔 · PDF (18.3 MB)</p>
      </div>
    </a>

    <a href="downloads/講義/1151101-呂聰賢-AI影音創作教學講義.docx" class="download-card" download>
      <div class="dl-icon dl-docx">📄</div>
      <div class="dl-info">
        <h4>AI 影音創作教學實作講義</h4>
        <p>備課指南與教學模組 · DOCX (46 KB)</p>
      </div>
    </a>

    <a href="downloads/講義/1151101-呂聰賢-AI 短影音創作全流程：課後複習講義與實作檢核表.docx" class="download-card" download>
      <div class="dl-icon dl-docx">📄</div>
      <div class="dl-info">
        <h4>課後複習講義與實作檢核表</h4>
        <p>含提示詞百寶箱 · DOCX (8.2 MB)</p>
      </div>
    </a>

    <a href="downloads/AI平台對話/哈士奇動畫企劃方案建議 - Gemini-劇本-照片-影片提示詞.pdf" class="download-card" download>
      <div class="dl-icon dl-pdf">🤖</div>
      <div class="dl-info">
        <h4>Gemini 實戰對話紀錄 (哈士奇)</h4>
        <p>20 輪完整提示詞日誌 · PDF (4.2 MB)</p>
      </div>
    </a>

    <a href="downloads/AI平台對話/邊際牧羊犬動畫企劃方案建議 - ChatGPT-劇本-照片-影片提示詞.pdf" class="download-card" download>
      <div class="dl-icon dl-pdf">💬</div>
      <div class="dl-info">
        <h4>ChatGPT 實戰對話紀錄 (邊境牧羊犬)</h4>
        <p>完整分鏡與生圖提示詞 · PDF (8.7 MB)</p>
      </div>
    </a>

    <a href="downloads/教學圖/AI_短影音創作全流程圖解.png" class="download-card" download>
      <div class="dl-icon dl-png">🖼️</div>
      <div class="dl-info">
        <h4>AI 短影音創作全流程圖解</h4>
        <p>2752×1536 高解析教學大圖 · PNG</p>
      </div>
    </a>

    <a href="downloads/教學圖/AI動畫影片創作三步驟.png" class="download-card" download>
      <div class="dl-icon dl-png">🖼️</div>
      <div class="dl-info">
        <h4>AI 動畫影片創作三步驟</h4>
        <p>2752×1536 高解析教學大圖 · PNG</p>
      </div>
    </a>
  </div>
</section>

<!-- Lightbox Modal -->
<div id="lightbox" class="modal-overlay" onclick="closeLightbox()">
  <img id="lightboxImg" class="modal-img" src="" alt="Enlarged chart">
</div>

<!-- Toast -->
<div id="toast" class="toast">
  <span>✓</span>
  <span id="toastMsg">已複製到剪貼簿！</span>
</div>

<!-- Footer -->
<footer>
  <div class="footer-content">
    <div class="footer-links">
      <a href="#focus-charts">核心教學大圖</a>
      <a href="#slides">精選簡報觀看器</a>
      <a href="#lectures">線上講義</a>
      <a href="#ai-dialogues">AI平台對話</a>
      <a href="#theater">實戰作品劇院</a>
      <a href="#downloads">教材下載</a>
    </div>
    <p style="margin-bottom:8px;">
      主講：<strong>呂聰賢老師</strong> ｜ 協作助教：<strong>阿啄校長</strong> ｜ 整理：<strong>AI 軍師</strong>
    </p>
    <p style="color:var(--text-dim); font-size:12px;">
      1151101 教師專業成長研習 · 生成式影音工具應用成果網站 ｜ 採用純 HTML5 / CSS3 / Vanilla JS 建置 · 支援響應式行動瀏覽
    </p>
  </div>
</footer>

<!-- Interactive Scripts -->
<script>
  // 1. TEACHING CHARTS DATA & SWITCHER (#4)
  const CHARTS_DATA = {{
    1: {{
      title: "AI 短影音創作全流程圖解",
      lead: "從概念、圖像、動態到後製的一體化生產管線",
      img: "assets/charts/chart1_short_video_workflow.png",
      steps: [
        "<strong>故事與腳本架構：</strong> 在單一 Gemini 對話中鎖定人物設定與情節綱要，確保上下文記憶不丟失。",
        "<strong>視覺一致性錨定：</strong> 預先產出三視圖定裝照，固定髮型、服飾、年齡與毛色特徵。",
        "<strong>分鏡提示詞工程：</strong> 中文供創作者構思檢驗，英文提示詞供模型生成高精度圖像與動態。",
        "<strong>剪映後製整合：</strong> 時間軸順序編排、TTS 統一旁白聲線、文稿匹配字幕與 BGM 自然淡出。"
      ]
    }},
    2: {{
      title: "AI 動畫影片創作三步驟",
      lead: "精準把控「生圖 ➔ 動畫 ➔ 剪輯」黃金鐵三角",
      img: "assets/charts/chart2_animation_three_steps.png",
      steps: [
        "<strong>步驟一（靜態生成）：</strong> 運用 Gemini / ChatGPT 設計分鏡，產出高解析度 9:16 靜態關鍵幀圖片。",
        "<strong>步驟二（動態轉化）：</strong> 匯入 Google Flow / Kling 進行 Image-to-Video，加入運鏡提示詞推拉平移。",
        "<strong>步驟三（後製剪輯）：</strong> 在剪映中編排時間軸、縮短封面、配置交叉溶解、添加智慧字幕與音樂。"
      ]
    }},
    3: {{
      title: "AI 動畫影片創作全攻略",
      lead: "全方位的角色設計、提示詞語法與後製細節指南",
      img: "assets/charts/chart3_animation_guide.png",
      steps: [
        "<strong>角色外觀強約束：</strong> 設定白背景全身三視圖，描述明確顏色、服飾、飾品以避免角色跑板。",
        "<strong>相機鏡頭語言：</strong> 靈活運用 Dolly in (推近)、Pan (平移)、Tracking (跟拍) 與 Macro (微距) 強化氛圍。",
        "<strong>音訊分軌混音：</strong> 旁白置於主聲軌，背景音樂調降至 -15dB 襯底，片尾預留 3 秒平滑淡出收尾。"
      ]
    }},
    4: {{
      title: "AI 影片創作剪輯流程",
      lead: "專業剪輯剪映 (CapCut) 電腦版標準時間軸配置 SOP",
      img: "assets/charts/chart4_editing_workflow.png",
      steps: [
        "<strong>專案規格化：</strong> 設定 1080×1920 (9:16) 垂直影格，匯入分鏡圖與分段生成的影片素材。",
        "<strong>封面停留控制：</strong> 封面片段縮短至約 2～3 秒，吸引停留目光並迅速銜接正片劇情。",
        "<strong>音畫同步：</strong> 嚴格遵守「口白時長小於鏡頭畫面」原則，留出 2～3 秒純情緒留白鏡頭。"
      ]
    }}
  }};

  function switchChart(chartId) {{
    const data = CHARTS_DATA[chartId];
    if (!data) return;

    document.querySelectorAll('.btn-chart-tab').forEach((btn, idx) => {{
      btn.classList.toggle('active', (idx + 1) === chartId);
    }});

    document.getElementById('chartImg').src = data.img;
    document.getElementById('chartTitle').textContent = data.title;
    document.getElementById('chartLead').textContent = data.lead;

    const list = document.getElementById('chartSteps');
    list.innerHTML = '';
    data.steps.forEach(st => {{
      const li = document.createElement('li');
      li.innerHTML = st;
      list.appendChild(li);
    }});
  }}

  // 2. SLIDE PRESENTATION VIEWER (#2)
  let currentDeck = 'deck1_google_ai';
  let currentSlideIndex = 1;
  const totalSlides = 21;

  function switchDeck(deckId, deckTitle) {{
    currentDeck = deckId;
    currentSlideIndex = 1;

    document.querySelectorAll('.btn-deck').forEach(btn => {{
      btn.classList.toggle('active', btn.getAttribute('onclick').includes(deckId));
    }});

    document.getElementById('deckTitleDisplay').textContent = deckTitle;
    renderFilmstrip();
    updateSlideDisplay();
  }}

  function renderFilmstrip() {{
    const container = document.getElementById('filmstrip');
    container.innerHTML = '';
    for (let i = 1; i <= totalSlides; i++) {{
      const div = document.createElement('div');
      div.className = `thumb-item ${{i === currentSlideIndex ? 'active' : ''}}`;
      div.onclick = () => goToSlide(i);
      div.innerHTML = `<img src="slides/${{currentDeck}}/slide_${{i}}.jpg" alt="Thumb ${{i}}" loading="lazy">`;
      container.appendChild(div);
    }}
  }}

  function updateSlideDisplay() {{
    const img = document.getElementById('currentSlideImg');
    img.src = `slides/${{currentDeck}}/slide_${{currentSlideIndex}}.jpg`;
    document.getElementById('slideNumDisplay').textContent = `投影片 ${{currentSlideIndex}} / ${{totalSlides}}`;

    const thumbs = document.querySelectorAll('.thumb-item');
    thumbs.forEach((t, idx) => {{
      t.classList.toggle('active', (idx + 1) === currentSlideIndex);
      if (idx + 1 === currentSlideIndex) {{
        t.scrollIntoView({{ behavior: 'smooth', block: 'nearest', inline: 'center' }});
      }}
    }});
  }}

  function prevSlide() {{
    if (currentSlideIndex > 1) currentSlideIndex--;
    else currentSlideIndex = totalSlides;
    updateSlideDisplay();
  }}

  function nextSlide() {{
    if (currentSlideIndex < totalSlides) currentSlideIndex++;
    else currentSlideIndex = 1;
    updateSlideDisplay();
  }}

  function goToSlide(idx) {{
    currentSlideIndex = idx;
    updateSlideDisplay();
  }}

  document.addEventListener('keydown', (e) => {{
    if (e.key === 'ArrowLeft') prevSlide();
    if (e.key === 'ArrowRight') nextSlide();
  }});

  function toggleFullscreen() {{
    const elem = document.getElementById('viewerScreen');
    if (!document.fullscreenElement) {{
      elem.requestFullscreen().catch(err => alert(`無法進入全螢幕: ${{err.message}}`));
    }} else {{
      document.exitFullscreen();
    }}
  }}

  // 3. AI DIALOGUES SIMULATOR (#3)
  const DIALOGUES = {dialogues_json_str};

  function switchChat(chatKey) {{
    const chat = DIALOGUES[chatKey];
    if (!chat) return;

    document.querySelectorAll('.btn-chat-tab').forEach(btn => {{
      btn.classList.toggle('active', btn.getAttribute('onclick').includes(chatKey));
    }});

    document.getElementById('chatTitleDisplay').textContent = chat.title;
    document.getElementById('chatModelBadge').textContent = chat.badge;

    const stream = document.getElementById('chatStream');
    stream.innerHTML = '';

    chat.turns.forEach(t => {{
      const group = document.createElement('div');
      group.className = 'chat-turn-group';

      let html = `<span class="chat-turn-badge">Turn ${{t.turn}}</span>`;

      if (t.user) {{
        html += `
          <div class="chat-bubble">
            <div class="chat-avatar avatar-user">👤</div>
            <div class="bubble-content user-bubble">
              <div class="bubble-author">
                <span>使用者 (Prompt)</span>
                <button class="btn-copy" onclick="copyText(this)">📋 複製</button>
              </div>
              <div class="bubble-text">${{escapeHtml(t.user)}}</div>
            </div>
          </div>
        `;
      }}

      if (t.assistant) {{
        const isGemini = chatKey.includes('gemini');
        const avClass = isGemini ? 'avatar-gemini' : 'avatar-chatgpt';
        const avIcon = isGemini ? '✨' : '🤖';
        const modelName = isGemini ? 'Google Gemini' : 'ChatGPT';

        html += `
          <div class="chat-bubble">
            <div class="chat-avatar ${{avClass}}">${{avIcon}}</div>
            <div class="bubble-content ai-bubble">
              <div class="bubble-author">
                <span style="color:#38bdf8;">${{modelName}} (Response)</span>
                <button class="btn-copy" onclick="copyText(this)">📋 複製</button>
              </div>
              <div class="bubble-text">${{escapeHtml(t.assistant)}}</div>
            </div>
          </div>
        `;
      }}

      group.innerHTML = html;
      stream.appendChild(group);
    }});
  }}

  function escapeHtml(text) {{
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }}

  function copyText(btn) {{
    const textElem = btn.closest('.bubble-content').querySelector('.bubble-text');
    navigator.clipboard.writeText(textElem.innerText).then(() => {{
      showToast('對話內容已成功複製！');
    }});
  }}

  // 4. LECTURES TAB SWITCHER (#1)
  function switchLectureTab(tabKey) {{
    document.querySelectorAll('.btn-lec-tab').forEach(btn => {{
      btn.classList.toggle('active', btn.getAttribute('onclick').includes(tabKey));
    }});
    document.querySelectorAll('.lecture-pane').forEach(p => p.classList.remove('active'));
    document.getElementById(`pane-${{tabKey}}`).classList.add('active');
  }}

  // 5. CHECKLIST WITH LOCALSTORAGE
  function updateChecklistProgress() {{
    const checkboxes = document.querySelectorAll('#checklistItems input[type="checkbox"]');
    let checkedCount = 0;
    const states = [];
    checkboxes.forEach((cb) => {{
      if (cb.checked) {{
        checkedCount++;
        cb.closest('.check-item').classList.add('done');
      }} else {{
        cb.closest('.check-item').classList.remove('done');
      }}
      states.push(cb.checked);
    }});
    const pct = Math.round((checkedCount / checkboxes.length) * 100);
    document.getElementById('checkPercent').textContent = `${{pct}}%`;
    document.getElementById('checkFill').style.width = `${{pct}}%`;
    localStorage.setItem('ai_video_checklist_1151101', JSON.stringify(states));
  }}

  function toggleCheck(cb) {{
    updateChecklistProgress();
  }}

  function loadChecklist() {{
    const saved = localStorage.getItem('ai_video_checklist_1151101');
    if (saved) {{
      try {{
        const states = JSON.parse(saved);
        const checkboxes = document.querySelectorAll('#checklistItems input[type="checkbox"]');
        states.forEach((val, idx) => {{
          if (checkboxes[idx]) checkboxes[idx].checked = val;
        }});
      }} catch(e) {{}}
    }}
    updateChecklistProgress();
  }}

  // 6. LIGHTBOX MODAL
  function openLightbox(src) {{
    document.getElementById('lightboxImg').src = src;
    document.getElementById('lightbox').classList.add('active');
  }}
  function closeLightbox() {{
    document.getElementById('lightbox').classList.remove('active');
  }}

  // 7. TOAST NOTIFICATION
  function showToast(msg) {{
    const toast = document.getElementById('toast');
    document.getElementById('toastMsg').textContent = msg;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 2500);
  }}

  // INITIALIZE
  window.addEventListener('DOMContentLoaded', () => {{
    renderFilmstrip();
    updateSlideDisplay();
    switchChat('gemini_husky');
    loadChecklist();
  }});
</script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_code)

print(f"Flagship website updated successfully: {os.path.getsize(os.path.join(BASE_DIR, 'index.html'))} bytes")
