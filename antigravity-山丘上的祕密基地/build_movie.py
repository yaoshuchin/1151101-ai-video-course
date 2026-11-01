# -*- coding: utf-8 -*-
"""
Full Video Production Script for:
《風吹過的山丘 (The Whispering Hill)》 - 山丘上的祕密基地
Based on the Antigravity Storyboard & 10-Shot Breakdown.
Constraint: NO SUBTITLES (不需要配字幕)
Format: 9:16 Vertical HD (1080x1920), 30 FPS, H.264 / AAC
Audio: Microsoft Hanhan Voiceover + Gentle Piano BGM
"""

import os
import sys
import math
import subprocess
import numpy as np
import cv2
from PIL import Image

BASE_DIR = r"C:\antigravity\1151101AI做影片\antigravity-山丘上的祕密基地"
OUT_VIDEO = os.path.join(BASE_DIR, "風吹過的山丘_完整影片.mp4")
AUDIO_DIR = os.path.join(BASE_DIR, "audio_clips")
BGM_PATH = os.path.join(BASE_DIR, "bgm_shepherd.mp3")

FPS = 30
W, H = 1080, 1920

# 10 Shots Configuration:
# 9 shots x 6.5s (overlaps 0.5s -> net 6.0s each) + Shot 10 6.0s (ends at 60.0s)
# Total timeline duration = 9 * 6.0 + 6.0 = 60.0s (1800 frames at 30 fps)
SHOTS_CONFIG = [
    {
        "id": "shot_01", # 【夏日山丘】 慢速航拍、俯瞰海灣
        "file": "1151101-PP1.png",
        "duration": 6.5,
        "z_start": 1.00,
        "z_end": 1.08,
        "c_start": (0.50, 0.44),
        "c_end": (0.50, 0.52),
    },
    {
        "id": "shot_02", # 【樹下休憩】 大樹下靜思、緩慢推近
        "file": "1151101-PP2.png",
        "duration": 6.5,
        "z_start": 1.00,
        "z_end": 1.10,
        "c_start": (0.50, 0.48),
        "c_end": (0.50, 0.52),
    },
    {
        "id": "shot_03", # 【夥伴靠近】 穿梭花草、低角跟隨
        "file": "1151101-PP3.png",
        "duration": 6.5,
        "z_start": 1.04,
        "z_end": 1.04,
        "c_start": (0.47, 0.50),
        "c_end": (0.53, 0.50),
    },
    {
        "id": "shot_04", # 【溫柔輕觸】 濕熱鼻尖觸碰手背
        "file": "1151101-PP4.png",
        "duration": 6.5,
        "z_start": 1.02,
        "z_end": 1.12,
        "c_start": (0.50, 0.52),
        "c_end": (0.50, 0.48),
    },
    {
        "id": "shot_05", # 【轉身探尋】 花叢嗅聞、轉身探尋
        "file": "1151101-PP5.png",
        "duration": 6.5,
        "z_start": 1.05,
        "z_end": 1.05,
        "c_start": (0.53, 0.50),
        "c_end": (0.47, 0.50),
    },
    {
        "id": "shot_06", # 【神奇信物】 彩繪紙風車靜立草地
        "file": "1151101-PP6.png",
        "duration": 6.5,
        "z_start": 1.02,
        "z_end": 1.10,
        "c_start": (0.50, 0.46),
        "c_end": (0.50, 0.54),
    },
    {
        "id": "shot_07", # 【靜默依偎】 側臥身旁、撫摸後頸
        "file": "1151101-PP7.png",
        "duration": 6.5,
        "z_start": 1.02,
        "z_end": 1.12,
        "c_start": (0.50, 0.50),
        "c_end": (0.50, 0.48),
    },
    {
        "id": "shot_08", # 【起風之時】 清風吹拂、風車飛旋
        "file": "1151101-PP8.png",
        "duration": 6.5,
        "z_start": 1.10,
        "z_end": 1.02,
        "c_start": (0.50, 0.50),
        "c_end": (0.50, 0.50),
    },
    {
        "id": "shot_09", # 【重現笑容】 釋懷展顏、溫暖相擁
        "file": "1151101-Q1.png",
        "duration": 6.5,
        "z_start": 1.02,
        "z_end": 1.12,
        "c_start": (0.50, 0.50),
        "c_end": (0.50, 0.48),
    },
    {
        "id": "shot_10", # 【並肩遠眺】 夕陽晚霞、老樹遠眺
        "file": "1151101-Q2.png",
        "duration": 6.0,
        "z_start": 1.10,
        "z_end": 1.00,
        "c_start": (0.50, 0.50),
        "c_end": (0.50, 0.48),
    }
]

def render_ken_burns_frame(img_np, progress, cfg):
    """
    Renders a single frame with smooth Ken Burns camera motion.
    progress: float 0.0 to 1.0
    """
    if progress < 0.5:
        ease = 2 * progress * progress
    else:
        ease = 1 - math.pow(-2 * progress + 2, 2) / 2

    z = cfg["z_start"] + (cfg["z_end"] - cfg["z_start"]) * ease
    cx_norm = cfg["c_start"][0] + (cfg["c_end"][0] - cfg["c_start"][0]) * ease
    cy_norm = cfg["c_start"][1] + (cfg["c_end"][1] - cfg["c_start"][1]) * ease

    ih, iw = img_np.shape[:2]
    target_ratio = float(W) / float(H) # 1080 / 1920 = 0.5625

    if iw / ih > target_ratio:
        base_w = ih * target_ratio
        base_h = ih
    else:
        base_w = iw
        base_h = iw / target_ratio

    crop_w = base_w / z
    crop_h = base_h / z

    cx = cx_norm * iw
    cy = cy_norm * ih

    x1 = int(round(cx - crop_w / 2.0))
    y1 = int(round(cy - crop_h / 2.0))
    x2 = int(round(x1 + crop_w))
    y2 = int(round(y1 + crop_h))

    # Clamp bounds safely
    if x1 < 0:
        x2 -= x1
        x1 = 0
    if y1 < 0:
        y2 -= y1
        y1 = 0
    if x2 > iw:
        x1 -= (x2 - iw)
        x2 = iw
    if y2 > ih:
        y1 -= (y2 - ih)
        y2 = ih

    x1 = max(0, x1)
    y1 = max(0, y1)
    x2 = min(iw, x2)
    y2 = min(ih, y2)

    cropped = img_np[y1:y2, x1:x2]
    frame = cv2.resize(cropped, (W, H), interpolation=cv2.INTER_LANCZOS4)
    return frame

def generate_video_frames(pipe):
    """
    Renders all frames shot-by-shot, applies 0.5s crossfade between shots,
    and streams directly into the ffmpeg rawvideo stdin pipe.
    """
    crossfade_sec = 0.5
    crossfade_frames = int(round(crossfade_sec * FPS)) # 15 frames

    num_shots = len(SHOTS_CONFIG)
    prev_tail_frames = []
    total_frames_written = 0

    for i, cfg in enumerate(SHOTS_CONFIG):
        img_path = os.path.join(BASE_DIR, cfg["file"])
        print(f"[{i+1}/{num_shots}] Rendering shot '{cfg['id']}' ({cfg['file']})...")
        
        with Image.open(img_path) as pil_img:
            img_rgb = pil_img.convert("RGB")
            img_np = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2BGR)

        num_frames = int(round(cfg["duration"] * FPS))
        shot_frames = []

        is_last_shot = (i == num_shots - 1)
        for f in range(num_frames):
            progress = float(f) / float(max(1, num_frames - 1))
            frame = render_ken_burns_frame(img_np, progress, cfg)

            # For the last shot, apply gentle fade to black over the last 1.0 second
            if is_last_shot and f >= (num_frames - 30):
                fade_alpha = max(0.0, float(num_frames - 1 - f) / 30.0)
                frame = (frame.astype(np.float32) * fade_alpha).astype(np.uint8)

            shot_frames.append(frame)

        if i > 0:
            # Apply crossfade between prev_tail_frames and first frames of current shot
            cf_len = min(len(prev_tail_frames), crossfade_frames, len(shot_frames))
            for k in range(cf_len):
                alpha = float(k + 1) / float(cf_len + 1)
                blended = cv2.addWeighted(prev_tail_frames[k], 1.0 - alpha, shot_frames[k], alpha, 0)
                pipe.stdin.write(blended.tobytes())
                total_frames_written += 1
            
            # Write remaining frames of current shot (excluding the tail if not last shot)
            if i < num_shots - 1:
                mid_frames = shot_frames[cf_len : -crossfade_frames]
                for mf in mid_frames:
                    pipe.stdin.write(mf.tobytes())
                    total_frames_written += 1
                prev_tail_frames = shot_frames[-crossfade_frames:]
            else:
                # Last shot: write all remaining frames to the very end
                for mf in shot_frames[cf_len:]:
                    pipe.stdin.write(mf.tobytes())
                    total_frames_written += 1
        else:
            # First shot: write up to `num_frames - crossfade_frames`
            for mf in shot_frames[:-crossfade_frames]:
                pipe.stdin.write(mf.tobytes())
                total_frames_written += 1
            prev_tail_frames = shot_frames[-crossfade_frames:]

    print(f"Total video frames generated: {total_frames_written} ({total_frames_written/FPS:.2f}s)")

def build_audio_track(output_wav_path):
    """
    Builds the combined audio track:
    - BGM at volume 0.18 with fade out
    - 10 VO tracks positioned precisely at each scene
    """
    total_dur = 60.0 # exactly 60 seconds

    vo_offsets = [
        (1, 1.0),   # Shot 01: 0.0s - 6.0s
        (2, 7.0),   # Shot 02: 6.0s - 12.0s
        (3, 13.0),  # Shot 03: 12.0s - 18.0s
        (4, 19.0),  # Shot 04: 18.0s - 24.0s
        (5, 25.0),  # Shot 05: 24.0s - 30.0s
        (6, 31.0),  # Shot 06: 30.0s - 36.0s
        (7, 37.0),  # Shot 07: 36.0s - 42.0s
        (8, 43.0),  # Shot 08: 42.0s - 48.0s
        (9, 49.0),  # Shot 09: 48.0s - 54.0s
        (10, 54.8)  # Shot 10: 54.0s - 60.0s
    ]

    inputs = ["-i", BGM_PATH]
    for idx, offset in vo_offsets:
        vo_file = os.path.join(AUDIO_DIR, f"vo_{idx:02d}.wav")
        inputs.extend(["-i", vo_file])

    filter_complex = []
    # 1. BGM: trim to 60s, adjust volume to 0.18, fade in 1s, fade out last 3s
    filter_complex.append(
        f"[0:a]atrim=0:{total_dur},asetpts=PTS-STARTPTS,volume=0.18,afade=t=in:st=0:d=1.0,afade=t=out:st={total_dur-3.0}:d=3.0[bgm];"
    )

    # 2. Delayed VO tracks
    amix_inputs = "[bgm]"
    for i, (idx, offset_sec) in enumerate(vo_offsets):
        ms = int(round(offset_sec * 1000))
        inp_idx = i + 1
        filter_complex.append(
            f"[{inp_idx}:a]adelay={ms}|{ms},volume=1.35[vo{inp_idx}];"
        )
        amix_inputs += f"[vo{inp_idx}]"

    # 3. Mix everything together
    filter_complex.append(
        f"{amix_inputs}amix=inputs=11:duration=first:dropout_transition=2[aout]"
    )

    full_filter = "".join(filter_complex)

    cmd = [
        "ffmpeg", "-y",
        *inputs,
        "-filter_complex", full_filter,
        "-map", "[aout]",
        "-t", str(total_dur),
        "-c:a", "pcm_s16le",
        output_wav_path
    ]

    print("Synthesizing audio track...")
    subprocess.check_call(cmd)
    print(f"Generated combined audio track: {output_wav_path}")

def main():
    temp_raw_video = os.path.join(BASE_DIR, "temp_video_no_audio.mp4")
    temp_audio = os.path.join(BASE_DIR, "temp_full_audio.wav")

    # Step 1: Render Audio Track
    build_audio_track(temp_audio)

    # Step 2: Render Video Track via pipe to ffmpeg
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{W}x{H}",
        "-pix_fmt", "bgr24",
        "-r", str(FPS),
        "-i", "-", # read from stdin pipe
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        temp_raw_video
    ]

    pipe = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)
    generate_video_frames(pipe)
    pipe.stdin.close()
    pipe.wait()
    print("Video track render finished!")

    # Step 3: Mux Video + Audio together into final MP4
    print("Muxing final video and audio...")
    mux_cmd = [
        "ffmpeg", "-y",
        "-i", temp_raw_video,
        "-i", temp_audio,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "256k",
        "-shortest",
        OUT_VIDEO
    ]
    subprocess.check_call(mux_cmd)

    # Cleanup temporary files
    for tmp in [temp_raw_video, temp_audio]:
        if os.path.exists(tmp):
            try: os.remove(tmp)
            except: pass

    print(f"\n==========================================")
    print(f"MOVIE GENERATION COMPLETE!")
    print(f"Output File: {OUT_VIDEO}")
    print(f"Resolution: {W}x{H} (9:16 Vertical HD)")
    print(f"Duration: 60.0 seconds")
    print(f"Subtitles: None (pure picture, motion & voiceover)")
    print(f"==========================================")

if __name__ == "__main__":
    main()
