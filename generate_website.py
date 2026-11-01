# -*- coding: utf-8 -*-
"""
Website Generator for:
1151101 呂聰賢老師 - AI 影片創作與生成式影音工具應用
Online Course Portal, Interactive Mindmaps, Slide Viewer, Prompt Library & Film Showcase
"""

import os
import json

BASE_DIR = r"C:\antigravity\1151101AI做影片"

with open(os.path.join(BASE_DIR, "slides_data.json"), "r", encoding="utf-8") as f:
    slides_data = json.load(f)

# Convert slides_data to compact JSON for client JS
slides_json_str = json.dumps(slides_data, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="zh-TW" class="scroll-smooth">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI 影片創作與生成式影音工具應用 · 呂聰賢老師線上教學講義與成果旗艦網</title>
<meta name="description" content="1151101 呂聰賢老師 AI 影片創作與生成式影音工具應用線上教學講義、全流程心智圖、84頁雙風格簡報線上觀看器、實戰提示詞庫與4部完整動畫成果。">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg-main: #090d16;
    --bg-card: rgba(18, 26, 43, 0.75);
    --bg-card-hover: rgba(28, 40, 65, 0.85);
    --border-color: rgba(56, 189, 248, 0.15);
    --border-hover: rgba(56, 189, 248, 0.4);
    --primary: #38bdf8;
    --primary-glow: rgba(56, 189, 248, 0.35);
    --secondary: #818cf8;
    --accent: #34d399;
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

  /* Custom Scrollbar */
  ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
  ::-webkit-scrollbar-track {{ background: #0b1120; }}
  ::-webkit-scrollbar-thumb {{ background: #1e293b; border-radius: 4px; }}
  ::-webkit-scrollbar-thumb:hover {{ background: #38bdf8; }}

  /* Navigation Bar */
  header.navbar {{
    position: sticky;
    top: 0;
    z-index: 1000;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    background: rgba(9, 13, 22, 0.85);
    border-bottom: 1px solid var(--border-color);
  }}
  .nav-container {{
    max-width: 1440px;
    margin: 0 auto;
    padding: 14px 24px;
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
    width: 38px;
    height: 38px;
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
    letter-spacing: -0.3px;
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
    gap: 6px;
    align-items: center;
    list-style: none;
  }}
  .nav-links a {{
    color: var(--text-muted);
    text-decoration: none;
    padding: 8px 14px;
    border-radius: 8px;
    font-size: 14px;
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
    gap: 8px;
    padding: 8px 16px;
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
    box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
  }}

  /* Mobile menu button */
  .mobile-toggle {{
    display: none;
    background: none;
    border: none;
    color: #f1f5f9;
    font-size: 24px;
    cursor: pointer;
  }}
  @media (max-width: 992px) {{
    .nav-links {{ display: none; }}
    .mobile-toggle {{ display: block; }}
  }}

  /* Hero Section */
  .hero-section {{
    padding: 64px 24px 48px;
    max-width: 1320px;
    margin: 0 auto;
    text-align: center;
    position: relative;
  }}
  .hero-pill {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 16px;
    border-radius: 999px;
    background: rgba(56, 189, 248, 0.1);
    border: 1px solid rgba(56, 189, 248, 0.3);
    color: #38bdf8;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 24px;
  }}
  .hero-title {{
    font-size: clamp(32px, 5vw, 56px);
    font-weight: 900;
    line-height: 1.18;
    letter-spacing: -1px;
    margin-bottom: 18px;
    background: linear-gradient(135deg, #ffffff 40%, #bae6fd 80%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .hero-desc {{
    font-size: clamp(16px, 2vw, 19px);
    color: var(--text-muted);
    max-width: 860px;
    margin: 0 auto 32px;
    line-height: 1.7;
  }}
  .instructor-credits {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
    margin-bottom: 36px;
    font-size: 14px;
  }}
  .instructor-chip {{
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(30, 41, 59, 0.6);
    padding: 6px 16px;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,0.08);
  }}
  .hero-actions {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 14px;
    margin-bottom: 48px;
  }}
  .btn-primary {{
    background: linear-gradient(135deg, #0284c7, #38bdf8);
    color: #04121d;
    font-weight: 700;
    padding: 12px 28px;
    border-radius: 10px;
    text-decoration: none;
    font-size: 15px;
    box-shadow: 0 4px 20px rgba(56, 189, 248, 0.4);
    transition: all 0.2s;
  }}
  .btn-primary:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 24px rgba(56, 189, 248, 0.6);
  }}
  .btn-secondary {{
    background: rgba(30, 41, 59, 0.8);
    color: #f1f5f9;
    font-weight: 600;
    padding: 12px 26px;
    border-radius: 10px;
    text-decoration: none;
    font-size: 15px;
    border: 1px solid rgba(255,255,255,0.12);
    transition: all 0.2s;
  }}
  .btn-secondary:hover {{
    background: rgba(51, 65, 85, 0.9);
    border-color: #38bdf8;
    transform: translateY(-2px);
  }}

  /* Stats Grid */
  .stats-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    max-width: 1100px;
    margin: 0 auto 60px;
  }}
  .stat-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 20px 16px;
    text-align: center;
    backdrop-filter: blur(10px);
    transition: all 0.2s;
  }}
  .stat-card:hover {{
    border-color: var(--border-hover);
    transform: translateY(-3px);
  }}
  .stat-val {{
    font-size: 32px;
    font-weight: 800;
    color: #38bdf8;
    line-height: 1.1;
    margin-bottom: 6px;
    font-family: 'JetBrains Mono', monospace;
  }}
  .stat-lbl {{
    font-size: 13px;
    color: var(--text-muted);
  }}

  /* Section Containers */
  section.module-section {{
    max-width: 1380px;
    margin: 0 auto 80px;
    padding: 0 24px;
  }}
  .section-header {{
    text-align: center;
    margin-bottom: 40px;
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
    margin-bottom: 12px;
    border: 1px solid rgba(56, 189, 248, 0.2);
  }}
  .section-title {{
    font-size: clamp(26px, 3.5vw, 36px);
    font-weight: 800;
    letter-spacing: -0.5px;
    margin-bottom: 12px;
  }}
  .section-desc {{
    font-size: 15px;
    color: var(--text-muted);
    max-width: 720px;
    margin: 0 auto;
  }}

  /* Cards & Glassmorphism */
  .card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 28px;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    transition: all 0.25s;
  }}
  .card:hover {{
    background: var(--bg-card-hover);
    border-color: var(--border-hover);
  }}

  /* 5-Stage Workflow */
  .workflow-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 20px;
    margin-bottom: 40px;
  }}
  .workflow-card {{
    background: rgba(18, 26, 43, 0.7);
    border: 1px solid rgba(56, 189, 248, 0.15);
    border-radius: 16px;
    padding: 24px;
    position: relative;
    overflow: hidden;
  }}
  .workflow-step {{
    position: absolute;
    top: -8px;
    right: -8px;
    font-size: 64px;
    font-weight: 900;
    color: rgba(56, 189, 248, 0.05);
    font-family: 'JetBrains Mono', monospace;
    user-select: none;
  }}
  .workflow-badge {{
    display: inline-block;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 700;
    margin-bottom: 12px;
  }}
  .badge-p1 {{ background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }}
  .badge-p2 {{ background: rgba(129, 140, 248, 0.15); color: #818cf8; border: 1px solid rgba(129, 140, 248, 0.3); }}
  .badge-p3 {{ background: rgba(52, 211, 153, 0.15); color: #34d399; border: 1px solid rgba(52, 211, 153, 0.3); }}
  .badge-p4 {{ background: rgba(251, 113, 133, 0.15); color: #fb7185; border: 1px solid rgba(251, 113, 133, 0.3); }}
  .badge-p5 {{ background: rgba(251, 191, 36, 0.15); color: #fbbf24; border: 1px solid rgba(251, 191, 36, 0.3); }}

  .workflow-title {{
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 10px;
    color: #f8fafc;
  }}
  .workflow-list {{
    list-style: none;
    font-size: 13px;
    color: var(--text-muted);
  }}
  .workflow-list li {{
    margin-bottom: 6px;
    position: relative;
    padding-left: 18px;
  }}
  .workflow-list li::before {{
    content: "▹";
    position: absolute;
    left: 0;
    color: #38bdf8;
  }}

  /* Interactive Checklist */
  .checklist-box {{
    background: rgba(15, 23, 42, 0.7);
    border: 1px solid rgba(56, 189, 248, 0.2);
    border-radius: 16px;
    padding: 28px;
    margin-top: 24px;
  }}
  .checklist-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
    margin-bottom: 20px;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
  }}
  .progress-bar-bg {{
    width: 100%;
    height: 8px;
    background: #1e293b;
    border-radius: 999px;
    overflow: hidden;
    margin-top: 10px;
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

  /* Slide Presentation Viewer */
  .viewer-wrapper {{
    background: rgba(15, 23, 42, 0.85);
    border: 1px solid var(--border-color);
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
  }}
  .viewer-topbar {{
    background: #111827;
    padding: 16px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 14px;
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
    border: 1px solid transparent;
    cursor: pointer;
    background: #1f2937;
    color: #9ca3af;
    transition: all 0.2s;
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
    background: rgba(0, 0, 0, 0.5);
    color: #fff;
    border: 1px solid rgba(255, 255, 255, 0.2);
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
    background: rgba(56, 189, 248, 0.8);
    color: #0f172a;
    border-color: #38bdf8;
  }}
  .btn-prev {{ left: 20px; }}
  .btn-next {{ right: 20px; }}

  .viewer-info-panel {{
    padding: 20px 28px;
    background: #111827;
    border-top: 1px solid rgba(255,255,255,0.06);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
  }}
  .slide-info-left h3 {{
    font-size: 18px;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 4px;
  }}
  .slide-points-list {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 8px;
  }}
  .point-tag {{
    font-size: 12px;
    background: rgba(56, 189, 248, 0.12);
    color: #bae6fd;
    padding: 3px 10px;
    border-radius: 6px;
    border: 1px solid rgba(56, 189, 248, 0.2);
  }}
  .viewer-controls {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .slide-counter {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    color: var(--text-muted);
  }}
  .btn-icon {{
    padding: 8px 14px;
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
    padding: 14px 20px;
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

  /* Mindmap Section */
  .mindmap-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
    gap: 24px;
  }}
  @media (max-width: 768px) {{
    .mindmap-grid {{ grid-template-columns: 1fr; }}
  }}
  .mindmap-box {{
    background: rgba(18, 26, 43, 0.7);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 28px;
  }}
  .mindmap-tree {{
    list-style: none;
    margin-top: 16px;
  }}
  .tree-node {{
    margin-bottom: 14px;
  }}
  .tree-title {{
    font-size: 15px;
    font-weight: 700;
    color: #38bdf8;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 6px;
  }}
  .tree-sub {{
    list-style: none;
    padding-left: 20px;
    font-size: 13px;
    color: var(--text-muted);
  }}
  .tree-sub li {{
    margin-bottom: 4px;
    position: relative;
    padding-left: 14px;
  }}
  .tree-sub li::before {{
    content: "•";
    position: absolute;
    left: 0;
    color: #818cf8;
  }}

  /* Video Showcase Theater */
  .videos-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 24px;
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
    max-height: 520px;
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
    padding: 20px;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .video-meta {{
    display: flex;
    gap: 8px;
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
    font-size: 18px;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 6px;
  }}
  .video-tagline {{
    font-size: 13px;
    color: var(--text-muted);
    font-style: italic;
    margin-bottom: 12px;
  }}
  .video-features {{
    font-size: 12px;
    color: var(--text-dim);
    line-height: 1.5;
  }}

  /* Prompts Box */
  .prompt-card {{
    background: #0f172a;
    border: 1px solid rgba(56, 189, 248, 0.2);
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 16px;
    position: relative;
  }}
  .prompt-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
  }}
  .prompt-title {{
    font-size: 14px;
    font-weight: 700;
    color: #38bdf8;
  }}
  .btn-copy {{
    background: rgba(56, 189, 248, 0.15);
    color: #38bdf8;
    border: 1px solid rgba(56, 189, 248, 0.3);
    padding: 4px 12px;
    border-radius: 6px;
    font-size: 12px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    transition: all 0.2s;
  }}
  .btn-copy:hover {{
    background: #38bdf8;
    color: #0f172a;
  }}
  .prompt-content {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #cbd5e1;
    background: #090e17;
    padding: 12px;
    border-radius: 8px;
    white-space: pre-wrap;
    line-height: 1.5;
  }}

  /* Downloads Grid */
  .downloads-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
  }}
  .download-card {{
    background: rgba(18, 26, 43, 0.7);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 20px;
    display: flex;
    align-items: center;
    gap: 16px;
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
    width: 44px;
    height: 44px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    flex-shrink: 0;
  }}
  .dl-pptx {{ background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); }}
  .dl-pdf {{ background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }}
  .dl-docx {{ background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); }}
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
        <div class="brand-title">AI 影片創作全流程旗艦講義</div>
        <div class="brand-badge">呂聰賢老師 · 1151101研習</div>
      </div>
    </a>
    <ul class="nav-links">
      <li><a href="#workflow">五大實作階段</a></li>
      <li><a href="#slides">雙風格簡報</a></li>
      <li><a href="#mindmap">全景心智圖</a></li>
      <li><a href="#lectures">教學講義</a></li>
      <li><a href="#prompts">提示詞寶箱</a></li>
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
  <div class="hero-pill">✨ 1151101 教師專業成長研習 · 生成式影音完整實戰</div>
  <h1 class="hero-title">AI 影片創作與<br>生成式影音工具應用</h1>
  <p class="hero-desc">
    從故事構思、角色一致性設定、分鏡繪製、Google Flow 動畫生成，到剪映 (CapCut) 語音合成、智慧字幕與背景音樂混音——打造專業級 AI 短影音全流程教學門戶。
  </p>
  
  <div class="instructor-credits">
    <div class="instructor-chip"><span>👨‍🏫 主講：</span><strong>呂聰賢老師</strong></div>
    <div class="instructor-chip"><span>🤝 協作助教：</span><strong>阿啄校長</strong></div>
    <div class="instructor-chip"><span>⚡ 整理策劃：</span><strong>AI 軍師</strong></div>
  </div>

  <div class="hero-actions">
    <a href="#slides" class="btn-primary">📊 觀看 84 頁雙風格簡報</a>
    <a href="#theater" class="btn-secondary">🎬 觀賞 4 部實戰完整影片</a>
    <a href="#prompts" class="btn-secondary">🧰 複製實戰提示詞</a>
  </div>

  <!-- Stats Grid -->
  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-val">4 部</div>
      <div class="stat-lbl">9:16 高畫質完整實戰短片</div>
    </div>
    <div class="stat-card">
      <div class="stat-val">84 頁</div>
      <div class="stat-lbl">雙主題 (科技/手繪) 投影片</div>
    </div>
    <div class="stat-card">
      <div class="stat-val">2 大</div>
      <div class="stat-lbl">全景課程架構心智圖</div>
    </div>
    <div class="stat-card">
      <div class="stat-val">100%</div>
      <div class="stat-lbl">免下載工具 · 雲端實戰工作流</div>
    </div>
  </div>
</section>

<!-- Module 1: 5-Stage Core Workflow -->
<section id="workflow" class="module-section">
  <div class="section-header">
    <span class="section-tag">Methodology</span>
    <h2 class="section-title">五大實作核心階段與避坑法則</h2>
    <p class="section-desc">掌握 AI 動畫影片製作的標準化作業程序 (SOP)，步步推進，徹底解決角色走樣與生成卡關。</p>
  </div>

  <div class="workflow-grid">
    <div class="workflow-card">
      <div class="workflow-step">01</div>
      <span class="workflow-badge badge-p1">第一階段</span>
      <h3 class="workflow-title">腳本與角色設定</h3>
      <ul class="workflow-list">
        <li>同一 Gemini 對話框鎖定上下文記憶</li>
        <li>指定主題、角色年齡、服裝與特徵</li>
        <li>生成正面、側面、背部三視圖定裝照</li>
        <li>統一畫風（如 3D 皮克斯或日系手繪）</li>
      </ul>
    </div>

    <div class="workflow-card">
      <div class="workflow-step">02</div>
      <span class="workflow-badge badge-p2">第二階段</span>
      <h3 class="workflow-title">分鏡提示詞與生圖</h3>
      <ul class="workflow-list">
        <li>規劃 6～10 段分鏡（初學可先做 4 段）</li>
        <li>預先決定畫面比例（直式 9:16 / 橫式 16:9）</li>
        <li>中文文案創作者審閱，英文提示詞供 AI 繪製</li>
        <li>每幕嚴格依序下載命名 P1、P2 等序號</li>
      </ul>
    </div>

    <div class="workflow-card">
      <div class="workflow-step">03</div>
      <span class="workflow-badge badge-p3">第三階段</span>
      <h3 class="workflow-title">Google Flow 動畫生成</h3>
      <ul class="workflow-list">
        <li>建立獨立專案並統一命名</li>
        <li>上傳分鏡圖片並配置 Image-to-Video 運鏡詞</li>
        <li>掌握每日點數額度分配（每段約 6~10 秒）</li>
        <li>可並行提交多段任務，無需等待單段完成</li>
      </ul>
    </div>

    <div class="workflow-card">
      <div class="workflow-step">04</div>
      <span class="workflow-badge badge-p4">第四階段</span>
      <h3 class="workflow-title">剪映電腦版剪輯整合</h3>
      <ul class="workflow-list">
        <li>匯入封面 (縮短至 2-3 秒) 與各片段視頻</li>
        <li>依分鏡順序精準排列於時間軸</li>
        <li>相鄰片段配置 0.5 秒平滑交叉淡入淡出</li>
        <li>利用文字朗讀 (TTS) 產生全片一致聲線</li>
      </ul>
    </div>

    <div class="workflow-card">
      <div class="workflow-step">05</div>
      <span class="workflow-badge badge-p5">第五階段</span>
      <h3 class="workflow-title">字幕翻譯與混音發布</h3>
      <ul class="workflow-list">
        <li>文稿匹配自動對齊語音生成精準字幕</li>
        <li>加文字描邊提升各背景色辨識度</li>
        <li>BGM 音量調低 (-15dB) 避免掩蓋人聲旁白</li>
        <li>設定片頭漸入、片尾 3 秒自然淡出並匯出 MP4</li>
      </ul>
    </div>
  </div>

  <!-- Interactive Checklist -->
  <div class="checklist-box">
    <div class="checklist-header">
      <div>
        <h3 style="font-size:18px; font-weight:700; color:#f8fafc;">📋 課後實作檢核表 (自我進度追蹤)</h3>
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
      <label class="check-item"><input type="checkbox" onchange="toggleCheck(this)"><span class="check-label">已開啟 Google Drive 資料夾取得講義與範例</span></label>
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
</section>

<!-- Module 2: 84-Slide Presentation Viewer -->
<section id="slides" class="module-section">
  <div class="section-header">
    <span class="section-tag">Interactive Presentation</span>
    <h2 class="section-title">雙版本 84 頁研習簡報線上觀看器</h2>
    <p class="section-desc">包含 Part 1（動畫影片製作）與 Part 2（Flow 影片生成與剪映後製），提供「深色科技風」與「手繪筆記風」雙視覺版本，支援縮圖切換與全螢幕觀看。</p>
  </div>

  <div class="viewer-wrapper">
    <div class="viewer-topbar">
      <div class="deck-tabs">
        <button class="btn-deck active" onclick="switchDeck('p1_style1')">📘 Part 1 · 深色科技風 (21頁)</button>
        <button class="btn-deck" onclick="switchDeck('p1_style2')">📝 Part 1 · 手繪筆記風 (21頁)</button>
        <button class="btn-deck" onclick="switchDeck('p2_style1')">📗 Part 2 · 深色科技風 (21頁)</button>
        <button class="btn-deck" onclick="switchDeck('p2_style2')">📋 Part 2 · 手繪筆記風 (21頁)</button>
      </div>
      <div class="viewer-controls">
        <span class="slide-counter" id="slideNumDisplay">投影片 1 / 21</span>
        <button class="btn-icon" onclick="toggleFullscreen()">⛶ 全螢幕</button>
      </div>
    </div>

    <!-- Viewer Screen -->
    <div class="viewer-screen" id="viewerScreen">
      <button class="screen-overlay-btn btn-prev" onclick="prevSlide()" title="上一頁 (←)">‹</button>
      <img id="currentSlideImg" src="slides/p1_style1/slide_1.jpg" alt="Slide presentation">
      <button class="screen-overlay-btn btn-next" onclick="nextSlide()" title="下一頁 (→)">›</button>
    </div>

    <!-- Slide Details Panel -->
    <div class="viewer-info-panel">
      <div class="slide-info-left">
        <h3 id="slideTitle">AI影片創作與動畫生成實戰</h3>
        <p id="slideSubtitle" style="font-size:13px; color:#38bdf8; font-weight:600;">掌握Flow動畫製作流</p>
        <div class="slide-points-list" id="slidePoints"></div>
      </div>
      <div style="font-size:12px; color:var(--text-dim); text-align:right;">
        鍵盤快捷鍵：<kbd style="background:#1f2937; padding:2px 6px; border-radius:4px; border:1px solid #374151;">←</kbd> 上一頁 ｜ <kbd style="background:#1f2937; padding:2px 6px; border-radius:4px; border:1px solid #374151;">→</kbd> 下一頁
      </div>
    </div>

    <!-- Thumbnails Filmstrip -->
    <div class="filmstrip-container" id="filmstrip"></div>
  </div>
</section>

<!-- Module 3: Interactive Mindmaps -->
<section id="mindmap" class="module-section">
  <div class="section-header">
    <span class="section-tag">Structure & Architecture</span>
    <h2 class="section-title">研習全景心智圖架構</h2>
    <p class="section-desc">兩大單元核心思維導圖，完整梳理從概念、工具分工到實作細節的知識脈絡。</p>
  </div>

  <div class="mindmap-grid">
    <!-- Mindmap 1 -->
    <div class="mindmap-box">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
        <h3 style="font-size:18px; font-weight:800; color:#38bdf8;">🧠 Part 1 · Google Flow AI 動畫影片製作</h3>
        <span class="workflow-badge badge-p1">研習單元一</span>
      </div>
      <ul class="mindmap-tree">
        <li class="tree-node">
          <div class="tree-title">📌 課程資源與學習方式</div>
          <ul class="tree-sub">
            <li>雲端硬碟存放講義、範例與成果檔</li>
            <li>全程錄影與分段錄影，課後無限期複習</li>
            <li>課堂專注操作跟做，免抄筆記負擔</li>
          </ul>
        </li>
        <li class="tree-node">
          <div class="tree-title">💡 生成式影音核心概念</div>
          <ul class="tree-sub">
            <li>AI涵蓋腳本、圖像、影片與音樂四位一體</li>
            <li>短片段分段生成，再行主題剪輯串接</li>
            <li>視覺一致性策略：預先錨定角色三視圖與定裝照</li>
          </ul>
        </li>
        <li class="tree-node">
          <div class="tree-title">⚙️ 工具分工與協同作業</div>
          <ul class="tree-sub">
            <li><strong>Gemini / ChatGPT：</strong> 撰寫腳本故事、分鏡文案與中英文提示詞</li>
            <li><strong>Google Flow / Kling：</strong> 依分鏡圖生成動態影片片段</li>
            <li><strong>剪映 (CapCut)：</strong> 影音串接、TTS 配音、智慧字幕與混音</li>
          </ul>
        </li>
        <li class="tree-node">
          <div class="tree-title">⚡ Google Flow 實戰特性</div>
          <ul class="tree-sub">
            <li>單段最長約 10 秒；每日點數重置不累積</li>
            <li>免費版 720p 下載；可並行提交多個生成任務</li>
            <li>中文口型尚有限制，以旁白敘事最為自然</li>
          </ul>
        </li>
      </ul>
    </div>

    <!-- Mindmap 2 -->
    <div class="mindmap-box">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
        <h3 style="font-size:18px; font-weight:800; color:#34d399;">🧠 Part 2 · 影片生成與剪映後製實作</h3>
        <span class="workflow-badge badge-p3">研習單元二</span>
      </div>
      <ul class="mindmap-tree">
        <li class="tree-node">
          <div class="tree-title">🎞️ 剪映時間軸基本佈局</div>
          <ul class="tree-sub">
            <li>封面縮短至約 2～3 秒，吸引停留目光</li>
            <li>分鏡片段依序拖曳，相鄰片段加交叉溶解</li>
            <li>專案妥善命名，統一匯出 1080p MP4</li>
          </ul>
        </li>
        <li class="tree-node">
          <div class="tree-title">🎙️ 旁白語音與文字朗讀 (TTS)</div>
          <ul class="tree-sub">
            <li>旁白文案字數必須短於對應影片畫面時長</li>
            <li>全片鎖定單一音色，保持故事連貫性</li>
            <li>文字轉語音與語音轉字幕分步進行</li>
          </ul>
        </li>
        <li class="tree-node">
          <div class="tree-title">📝 智慧字幕與多語系翻譯</div>
          <ul class="tree-sub">
            <li>文稿匹配功能自動對齊旁白時間點</li>
            <li>添加深色描邊，適應各種亮暗背景變化</li>
            <li>可匯出 SRT 字幕檔，支援 AI 翻譯多語系</li>
          </ul>
        </li>
        <li class="tree-node">
          <div class="tree-title">🎵 背景音樂與混音法則</div>
          <ul class="tree-sub">
            <li>BGM 置於獨立音軌，音量調降至 -15dB ~ -18dB</li>
            <li>片頭 1 秒微幅淡入，片尾 3 秒自然淡出收尾</li>
            <li>檢查人聲旁白與原聲軌道，杜絕雜音衝突</li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</section>

<!-- Module 4: Online Lecture Notes -->
<section id="lectures" class="module-section">
  <div class="section-header">
    <span class="section-tag">Curriculum Handbook</span>
    <h2 class="section-title">數位線上講義精要</h2>
    <p class="section-desc">彙整自研習教學講義與課堂實錄精華，涵蓋關鍵技術規範與實戰技巧。</p>
  </div>

  <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:20px;">
    <div class="card">
      <h3 style="color:#38bdf8; font-size:18px; margin-bottom:12px;">📐 1. 畫面比例與應用情境</h3>
      <p style="font-size:14px; color:var(--text-muted); margin-bottom:10px;">
        製作前務必先確認發布平台，避免後製裁切破壞構圖：
      </p>
      <ul style="font-size:13px; color:var(--text-main); padding-left:18px; line-height:1.7;">
        <li><strong>直式 9:16 (1080×1920)：</strong> 適合 YouTube Shorts、TikTok、Instagram Reels、LINE VOOM 等手機短影音平台。</li>
        <li><strong>橫式 16:9 (1920×1080)：</strong> 適合一般電腦螢幕、教學投影機、智慧電視及標準 YouTube 橫向影片。</li>
      </ul>
    </div>

    <div class="card">
      <h3 style="color:#818cf8; font-size:18px; margin-bottom:12px;">🎨 2. 角色三視圖錨定法則</h3>
      <p style="font-size:14px; color:var(--text-muted); margin-bottom:10px;">
        解決 AI 生成不同鏡頭時「主角換人」的最有效對策：
      </p>
      <ul style="font-size:13px; color:var(--text-main); padding-left:18px; line-height:1.7;">
        <li>在同一對話中生成「正面、側面、背面」三視圖設定表。</li>
        <li>指定固定外觀特徵（如：粉色洋裝、紅色小髮夾、黑白相間毛色）。</li>
        <li>每段分鏡提示詞中，均重複關鍵特徵描述作為強約束。</li>
      </ul>
    </div>

    <div class="card">
      <h3 style="color:#34d399; font-size:18px; margin-bottom:12px;">🎬 3. 鏡頭語言與運鏡提示詞</h3>
      <p style="font-size:14px; color:var(--text-muted); margin-bottom:10px;">
        將靜態繪畫轉為靈動電影感鏡頭的關鍵指令：
      </p>
      <ul style="font-size:13px; color:var(--text-main); padding-left:18px; line-height:1.7;">
        <li><strong>Push-in / Zoom in：</strong> 鏡頭緩慢向前推進，營造情感凝聚與專注。</li>
        <li><strong>Pull-back / Zoom out：</strong> 緩慢向後拉遠，展現廣闊環境與落寞餘韻。</li>
        <li><strong>Tracking / Pan：</strong> 側面平移跟拍，呈現伴行或奔跑的動態流暢感。</li>
        <li><strong>Macro Close-up：</strong> 微距特寫（如爪印、小球、眼神），強化細節感動。</li>
      </ul>
    </div>
  </div>
</section>

<!-- Module 5: Prompts Library -->
<section id="prompts" class="module-section">
  <div class="section-header">
    <span class="section-tag">Prompt Toolbox</span>
    <h2 class="section-title">實戰提示詞百寶箱</h2>
    <p class="section-desc">精選課堂修正版提示詞模板，點擊「一鍵複製」即可直接套用至 Gemini、ChatGPT 或 Flow 中實作。</p>
  </div>

  <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(420px, 1fr)); gap:20px;">
    <!-- Prompt 1 -->
    <div class="prompt-card">
      <div class="prompt-header">
        <span class="prompt-title">🌟 3D 皮克斯風格角色四視圖提示詞（呂聰賢老師版）</span>
        <button class="btn-copy" onclick="copyPrompt('p1')">📋 一鍵複製</button>
      </div>
      <div class="prompt-content" id="p1">請以 3D 皮克斯精緻動畫風格，為我設計一個角色設定表：
角色：10 歲小女孩，綁著雙馬尾，佩戴紅色蝴蝶結髮夾，身穿淡粉色休閒連身洋裝，白色短襪與棕色皮鞋。
夥伴：一隻黑白相間、毛髮蓬鬆靈巧的邊境牧羊犬，眼神溫暖，嘴邊帶有些微灰白毛髮。
畫面規格：白色純淨背景，同張畫面包含正面、側面、背面三視圖及表情特寫。柔和攝影棚打光，高細節角色建模，不要文字、不要字幕。</div>
    </div>

    <!-- Prompt 2 -->
    <div class="prompt-card">
      <div class="prompt-header">
        <span class="prompt-title">🌅 新海誠日系手繪動漫光影風格提示詞</span>
        <button class="btn-copy" onclick="copyPrompt('p2')">📋 一鍵複製</button>
      </div>
      <div class="prompt-content" id="p2">Vertical 9:16, Makoto Shinkai anime aesthetic, breathtaking golden hour sunset, cinematic lighting, ethereal atmospheric perspective. An elderly black-and-white Border Collie and a young girl standing side by side overlooking the ocean town, wind blowing softly, dramatic lens flare, watercolor textures, 8k resolution, highly detailed background art. No text, no watermark.</div>
    </div>

    <!-- Prompt 3 -->
    <div class="prompt-card">
      <div class="prompt-header">
        <span class="prompt-title">🎥 AI 影片運鏡指令模板（Image-to-Video）</span>
        <button class="btn-copy" onclick="copyPrompt('p3')">📋 一鍵複製</button>
      </div>
      <div class="prompt-content" id="p3">9:16 vertical video, 6 seconds. Smooth cinematic camera motion. The camera slowly pushes forward (dolly in) while tilting slightly down toward the subject. Cherry blossom petals flutter gently in the soft spring breeze. Golden afternoon sunlight creates natural shimmering lens flare. Subtle, realistic character breathing movements. Maintain consistent character appearance and clothing, no sudden jumps, fluid motion.</div>
    </div>

    <!-- Prompt 4 -->
    <div class="prompt-card">
      <div class="prompt-header">
        <span class="prompt-title">🍃 吉卜力清新治癒草坡手繪風格提示詞</span>
        <button class="btn-copy" onclick="copyPrompt('p4')">📋 一鍵複製</button>
      </div>
      <div class="prompt-content" id="p4">吉卜力手繪水彩風格，9:16 豎屏構圖。夏日遼闊山丘頂端佇立著巨大古老橡樹，青翠草地隨風起伏如浪，遠處俯瞰蔚藍海灣與日式寧靜港口小鎮。陽光穿透薄雲灑下柔和光斑，微風拂動，清新自然，極致細膩的動漫背景美術，充滿希望與治癒氛圍。</div>
    </div>
  </div>
</section>

<!-- Module 6: Video Showcase Theater -->
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
          您的瀏覽器不支援播放此影片。
        </video>
      </div>
      <div class="video-info">
        <div>
          <div class="video-meta">
            <span class="video-badge badge-dur">⏱️ 63秒</span>
            <span class="video-badge badge-spec">📱 1080×1920 (9:16)</span>
            <span class="video-badge badge-voice">🎙️ 台灣女聲旁白</span>
          </div>
          <h3 class="video-title">《雨中的牧羊人》</h3>
          <p class="video-tagline">「大雨會停，而我會一直在這裡。」</p>
          <p class="video-features">
            以黃色雨衣與紅色雨靴小女孩為主角，黑白邊境牧羊犬在大雨滂沱中守護歸途。包含建立雨景、揉皺畫紙、打傘並行、玄關擦拭等 10 段分鏡。
          </p>
        </div>
      </div>
    </div>

    <!-- Video 2 -->
    <div class="video-card">
      <div class="video-player-wrap">
        <video controls preload="metadata" poster="chatGPT-明天，也要一起散步/PP00夕陽下的櫻花散步.png">
          <source src="assets/videos/walk_together_tomorrow.mp4" type="video/mp4">
          您的瀏覽器不支援播放此影片。
        </video>
      </div>
      <div class="video-info">
        <div>
          <div class="video-meta">
            <span class="video-badge badge-dur">⏱️ 63秒</span>
            <span class="video-badge badge-spec">📱 1080×1920 (9:16)</span>
            <span class="video-badge badge-voice">🎙️ 台灣女聲旁白</span>
          </div>
          <h3 class="video-title">《明天，也要一起散步》</h3>
          <p class="video-tagline">「你走慢了，我就陪你慢慢走。」</p>
          <p class="video-features">
            櫻花小徑上，老牧羊犬步履漸緩，女孩停下等待並拾起童年磨損的紅色網球。傳遞出愛不是催促，而是願意為彼此放慢腳步的動人深情。
          </p>
        </div>
      </div>
    </div>

    <!-- Video 3 -->
    <div class="video-card">
      <div class="video-player-wrap">
        <video controls preload="metadata" poster="gemin-哈士奇/P00.jpg">
          <source src="assets/videos/always_by_my_side.mp4" type="video/mp4">
          您的瀏覽器不支援播放此影片。
        </video>
      </div>
      <div class="video-info">
        <div>
          <div class="video-meta">
            <span class="video-badge badge-dur">⏱️ 63秒</span>
            <span class="video-badge badge-spec">📱 1080×1920 (9:16)</span>
            <span class="video-badge badge-voice">🎙️ 台灣女聲旁白</span>
          </div>
          <h3 class="video-title">《未來的路，有你同在》</h3>
          <p class="video-tagline">「你看見我所有的夢，溫熱了孤獨的長夜。」</p>
          <p class="video-features">
            插畫女孩與幼犬哈士奇相遇，從誤踩藍色爪印的驚慌、失意停筆的長夜依偎，到共同完成夕陽繪本，於天橋晚霞下邁向未來的成長歷程。
          </p>
        </div>
      </div>
    </div>

    <!-- Video 4 -->
    <div class="video-card">
      <div class="video-player-wrap">
        <video controls preload="metadata" poster="antigravity-山丘上的祕密基地/1151101-PP1.png">
          <source src="assets/videos/whispering_hill.mp4" type="video/mp4">
          您的瀏覽器不支援播放此影片。
        </video>
      </div>
      <div class="video-info">
        <div>
          <div class="video-meta">
            <span class="video-badge badge-dur">⏱️ 60秒</span>
            <span class="video-badge badge-spec">📱 1080×1920 (9:16)</span>
            <span class="video-badge badge-voice">🎙️ 台灣女聲旁白</span>
          </div>
          <h3 class="video-title">《風吹過的山丘》</h3>
          <p class="video-tagline">「語言到不了的地方，有你無聲的守候。」</p>
          <p class="video-features">
            吉卜力手繪畫風。老橡樹綠草坡上，大狗叼來彩繪手作紙風車，清風吹動五彩光芒拂散心中煩憂，重拾純真笑容，並肩遠眺金燦港灣。
          </p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Module 7: Download Center -->
<section id="downloads" class="module-section">
  <div class="section-header">
    <span class="section-tag">Resource Pack</span>
    <h2 class="section-title">研習講義與簡報教材下載</h2>
    <p class="section-desc">提供本次研習所有完整簡報檔 (PPTX)、全攻略電子書 (PDF) 與課後複習檢核講義 (DOCX)。</p>
  </div>

  <div class="downloads-grid">
    <a href="downloads/1151101呂聰賢1-AI_影片創作與生成式影音工具應用 1.pptx" class="download-card" download>
      <div class="dl-icon dl-pptx">📊</div>
      <div class="dl-info">
        <h4>Part 1 · 深色科技風簡報 (PPTX)</h4>
        <p>完整 21 頁投影片檔 · 4.1 MB</p>
      </div>
    </a>

    <a href="downloads/1151101呂聰賢1-AI_影片創作與生成式影音工具應用 2.pptx" class="download-card" download>
      <div class="dl-icon dl-pptx">📊</div>
      <div class="dl-info">
        <h4>Part 1 · 手繪筆記風簡報 (PPTX)</h4>
        <p>完整 21 頁投影片檔 · 3.6 MB</p>
      </div>
    </a>

    <a href="downloads/1151101呂聰賢2-AI_影片創作與生成式影音工具應用 1.pptx" class="download-card" download>
      <div class="dl-icon dl-pptx">📊</div>
      <div class="dl-info">
        <h4>Part 2 · 深色科技風簡報 (PPTX)</h4>
        <p>完整 21 頁投影片檔 · 4.2 MB</p>
      </div>
    </a>

    <a href="downloads/1151101呂聰賢2-AI_影片創作與生成式影音工具應用 2.pptx" class="download-card" download>
      <div class="dl-icon dl-pptx">📊</div>
      <div class="dl-info">
        <h4>Part 2 · 手繪筆記風簡報 (PPTX)</h4>
        <p>完整 21 頁投影片檔 · 3.6 MB</p>
      </div>
    </a>

    <a href="downloads/Google_AI_動畫實戰指南.pdf" class="download-card" download>
      <div class="dl-icon dl-pdf">📕</div>
      <div class="dl-info">
        <h4>Google AI 動畫實戰指南 (PDF)</h4>
        <p>高畫質全攻略電子書 · 25.8 MB</p>
      </div>
    </a>

    <a href="downloads/AI動畫導演實戰大師班.pdf" class="download-card" download>
      <div class="dl-icon dl-pdf">📕</div>
      <div class="dl-info">
        <h4>AI 動畫導演實戰大師班 (PDF)</h4>
        <p>高畫質全攻略電子書 · 20.3 MB</p>
      </div>
    </a>

    <a href="downloads/1151101-呂聰賢-AI 短影音創作全流程：課後複習講義與實作檢核表.docx" class="download-card" download>
      <div class="dl-icon dl-docx">📄</div>
      <div class="dl-info">
        <h4>課後複習講義與實作檢核表 (DOCX)</h4>
        <p>包含提示詞百寶箱 · 8.2 MB</p>
      </div>
    </a>

    <a href="downloads/1151101-呂聰賢-AI影音創作教學講義.docx" class="download-card" download>
      <div class="dl-icon dl-docx">📄</div>
      <div class="dl-info">
        <h4>AI 影音創作教學實作講義 (DOCX)</h4>
        <p>備課指南與學生專題教案 · 46 KB</p>
      </div>
    </a>
  </div>
</section>

<!-- Toast -->
<div id="toast" class="toast">
  <span>✓</span>
  <span id="toastMsg">提示詞已成功複製到剪貼簿！</span>
</div>

<!-- Footer -->
<footer>
  <div class="footer-content">
    <div class="footer-links">
      <a href="#workflow">五大實作階段</a>
      <a href="#slides">84頁雙風格簡報</a>
      <a href="#mindmap">全景心智圖</a>
      <a href="#lectures">教學講義</a>
      <a href="#prompts">提示詞寶箱</a>
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
  const SLIDES_DATA = {slides_json_str};

  let currentDeck = 'p1_style1';
  let currentSlideIndex = 1;
  const totalSlides = 21;

  function switchDeck(deckId) {{
    currentDeck = deckId;
    currentSlideIndex = 1;
    
    // Update button states
    document.querySelectorAll('.btn-deck').forEach(btn => {{
      btn.classList.toggle('active', btn.getAttribute('onclick').includes(deckId));
    }});

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

    // Update active thumb
    const thumbs = document.querySelectorAll('.thumb-item');
    thumbs.forEach((t, idx) => {{
      t.classList.toggle('active', (idx + 1) === currentSlideIndex);
      if (idx + 1 === currentSlideIndex) {{
        t.scrollIntoView({{ behavior: 'smooth', block: 'nearest', inline: 'center' }});
      }}
    }});

    // Extract slide metadata from JSON
    const partKey = currentDeck.startsWith('p1') ? 'part1' : 'part2';
    const slideInfo = SLIDES_DATA[partKey][currentSlideIndex - 1] || {{}};

    document.getElementById('slideTitle').textContent = slideInfo.title || `第 ${{currentSlideIndex}} 頁主題重點`;
    document.getElementById('slideSubtitle').textContent = slideInfo.subtitle || (slideInfo.category ? `分類：${{slideInfo.category}}` : '');

    const pointsList = document.getElementById('slidePoints');
    pointsList.innerHTML = '';
    if (slideInfo.points && slideInfo.points.length > 0) {{
      slideInfo.points.forEach(pt => {{
        const span = document.createElement('span');
        span.className = 'point-tag';
        span.textContent = pt;
        pointsList.appendChild(span);
      }});
    }}
  }}

  function prevSlide() {{
    if (currentSlideIndex > 1) {{
      currentSlideIndex--;
    }} else {{
      currentSlideIndex = totalSlides;
    }}
    updateSlideDisplay();
  }}

  function nextSlide() {{
    if (currentSlideIndex < totalSlides) {{
      currentSlideIndex++;
    }} else {{
      currentSlideIndex = 1;
    }}
    updateSlideDisplay();
  }}

  function goToSlide(idx) {{
    currentSlideIndex = idx;
    updateSlideDisplay();
  }}

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {{
    if (e.key === 'ArrowLeft') prevSlide();
    if (e.key === 'ArrowRight') nextSlide();
  }});

  // Fullscreen
  function toggleFullscreen() {{
    const elem = document.getElementById('viewerScreen');
    if (!document.fullscreenElement) {{
      elem.requestFullscreen().catch(err => alert(`無法進入全螢幕: ${{err.message}}`));
    }} else {{
      document.exitFullscreen();
    }}
  }}

  // Toast
  function showToast(msg) {{
    const toast = document.getElementById('toast');
    document.getElementById('toastMsg').textContent = msg;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 2500);
  }}

  // Copy Prompt
  function copyPrompt(elementId) {{
    const text = document.getElementById(elementId).innerText;
    navigator.clipboard.writeText(text).then(() => {{
      showToast('提示詞已成功複製到剪貼簿！');
    }}).catch(() => {{
      showToast('複製失敗，請手動複製文字。');
    }});
  }}

  // Checklist with localStorage
  function updateChecklistProgress() {{
    const checkboxes = document.querySelectorAll('#checklistItems input[type="checkbox"]');
    let checkedCount = 0;
    const states = [];
    checkboxes.forEach((cb, idx) => {{
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

  // Initialize
  window.addEventListener('DOMContentLoaded', () => {{
    renderFilmstrip();
    updateSlideDisplay();
    loadChecklist();
  }});
</script>
</body>
</html>
"""

out_html_path = os.path.join(BASE_DIR, "index.html")
with open(out_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated {out_html_path} ({os.path.getsize(out_html_path)} bytes)!")
