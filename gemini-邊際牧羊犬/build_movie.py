# -*- coding: utf-8 -*-
"""
Full Video Production Script for:
《雨中的牧羊人 (Shepherd in the Rain)》
Based on the Gemini-Border Collie storyboard and instructions.
"""

import os
import math
import subprocess
import numpy as np
import cv2
from PIL import Image

BASE_DIR = r"C:\antigravity\1151101AI做影片\gemini-邊際牧羊犬"
OUT_VIDEO = os.path.join(BASE_DIR, "雨中的牧羊人_完整影片.mp4")
AUDIO_DIR = os.path.join(BASE_DIR, "audio_clips")
BGM_PATH = os.path.join(BASE_DIR, "bgm_shepherd.mp3")

FPS = 30
W, H = 1080, 1920

# 11 Shots configuration: (image_file, duration, zoom_start, zoom_end, center_start, center_end)
# center is in normalized (cx, cy)
SHOTS_CONFIG = [
    {
        "id": "cover",
        "file": "P00.jpg",
        "duration": 3.5, # overlaps 0.5s with next -> net 3.0s
        "z_start": 1.00,
        "z_end": 1.06,
        "c_start": (0.50, 0.50),
        "c_end": (0.50, 0.50),
    },
    {
        "id": "shot_01",
        "file": "P1.jpg",
        "duration": 6.5,
        "z_start": 1.02,
        "z_end": 1.10,
        "c_start": (0.50, 0.44), # slow tilt down
        "c_end": (0.50, 0.54),
    },
    {
        "id": "shot_02",
        "file": "P2.jpg",
        "duration": 6.5,
        "z_start": 1.04,
        "z_end": 1.12,
        "c_start": (0.50, 0.56), # focus on crumpled paper & hands
        "c_end": (0.50, 0.56),
    },
    {
        "id": "shot_03",
        "file": "P3.jpg",
        "duration": 6.5,
        "z_start": 1.12,
        "z_end": 1.00, # pull back dynamic run
        "c_start": (0.50, 0.56),
        "c_end": (0.50, 0.50),
    },
    {
        "id": "shot_04",
        "file": "P4.jpg",
        "duration": 6.5,
        "z_start": 1.00,
        "z_end": 1.08,
        "c_start": (0.50, 0.48),
        "c_end": (0.50, 0.44), # push towards dog's gentle eyes
    },
    {
        "id": "shot_05",
        "file": "P5.jpg",
        "duration": 6.5,
        "z_start": 1.02,
        "z_end": 1.08,
        "c_start": (0.50, 0.54),
        "c_end": (0.50, 0.60), # tilt down to umbrella and red boots
    },
    {
        "id": "shot_06",
        "file": "P6.jpg",
        "duration": 6.5,
        "z_start": 1.00,
        "z_end": 1.08,
        "c_start": (0.50, 0.52),
        "c_end": (0.50, 0.44), # tilt up towards glowing umbrella & face
    },
    {
        "id": "shot_07",
        "file": "P7.jpg",
        "duration": 6.5,
        "z_start": 1.00,
        "z_end": 1.08,
        "c_start": (0.50, 0.46),
        "c_end": (0.50, 0.52), # high angle tracking
    },
    {
        "id": "shot_08",
        "file": "P8.jpg",
        "duration": 6.5,
        "z_start": 1.04,
        "z_end": 1.08,
        "c_start": (0.52, 0.50), # side profile horizontal tracking
        "c_end": (0.48, 0.50),
    },
    {
        "id": "shot_09",
        "file": "P9.jpg",
        "duration": 6.5,
        "z_start": 1.10,
        "z_end": 1.00, # pull back to reveal porch warm light
        "c_start": (0.50, 0.52),
        "c_end": (0.50, 0.50),
    },
    {
        "id": "shot_10",
        "file": "P10.jpg",
        "duration": 6.0, # last shot, ends at exactly 63.0s
        "z_start": 1.00,
        "z_end": 1.12,
        "c_start": (0.50, 0.50),
        "c_end": (0.50, 0.48),
    }
]

def render_ken_burns_frame(img_np, progress, cfg):
    """
    Renders a single frame with smooth Ken Burns camera motion.
    progress: float 0.0 to 1.0
    """
    # Smooth easing curve (easeInOutQuad)
    if progress < 0.5:
        ease = 2 * progress * progress
    else:
        ease = 1 - math.pow(-2 * progress + 2, 2) / 2

    z = cfg["z_start"] + (cfg["z_end"] - cfg["z_start"]) * ease
    cx_norm = cfg["c_start"][0] + (cfg["c_end"][0] - cfg["c_start"][0]) * ease
    cy_norm = cfg["c_start"][1] + (cfg["c_end"][1] - cfg["c_start"][1]) * ease

    ih, iw = img_np.shape[:2]
    # Crop window aspect ratio is 9:16 (W:H)
    # The image is already 9:16 (572x1024), so max crop width is iw / z
    crop_w = iw / z
    crop_h = ih / z

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
    # Resize to target 1080x1920 with high quality INTER_LANCZOS4
    frame = cv2.resize(cropped, (W, H), interpolation=cv2.INTER_LANCZOS4)
    return frame

def generate_video_frames(pipe):
    """
    Renders all clips with 0.5s crossfade between adjacent clips
    and writes raw BGR frames directly to ffmpeg pipe.
    """
    crossfade_frames = int(0.5 * FPS) # 15 frames = 0.5s
    num_shots = len(SHOTS_CONFIG)

    # Preload all images
    images = []
    for cfg in SHOTS_CONFIG:
        p = os.path.join(BASE_DIR, cfg["file"])
        pil_im = Image.open(p).convert("RGB")
        # Convert RGB to BGR for OpenCV / ffmpeg
        bgr = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
        images.append(bgr)

    # We will generate shot by shot
    prev_tail_frames = None

    total_frames_written = 0

    for i in range(num_shots):
        cfg = SHOTS_CONFIG[i]
        img_np = images[i]
        num_frames = int(round(cfg["duration"] * FPS))

        print(f"Rendering {cfg['id']} ({cfg['file']}): {num_frames} frames...")

        shot_frames = []
        for f in range(num_frames):
            prog = f / max(1, num_frames - 1)
            frame = render_ken_burns_frame(img_np, prog, cfg)
            shot_frames.append(frame)

        # If last shot, apply warm soft fade-out on last 45 frames (1.5s)
        if i == num_shots - 1:
            fade_len = int(1.5 * FPS)
            for fi in range(fade_len):
                idx = len(shot_frames) - fade_len + fi
                fade_alpha = 1.0 - (fi / float(fade_len))
                shot_frames[idx] = (shot_frames[idx].astype(np.float32) * fade_alpha).astype(np.uint8)

        # Handle crossfade with previous shot
        if prev_tail_frames is not None:
            # First `crossfade_frames` of current shot blend with `prev_tail_frames`
            for c in range(crossfade_frames):
                alpha = c / float(crossfade_frames) # 0.0 -> 1.0
                blended = cv2.addWeighted(shot_frames[c], alpha, prev_tail_frames[c], 1.0 - alpha, 0)
                pipe.stdin.write(blended.tobytes())
                total_frames_written += 1
            # Write remaining frames of current shot (excluding the tail if not last shot)
            if i < num_shots - 1:
                mid_frames = shot_frames[crossfade_frames : -crossfade_frames]
                for mf in mid_frames:
                    pipe.stdin.write(mf.tobytes())
                    total_frames_written += 1
                prev_tail_frames = shot_frames[-crossfade_frames:]
            else:
                # Last shot: write all remaining frames to the very end
                for mf in shot_frames[crossfade_frames:]:
                    pipe.stdin.write(mf.tobytes())
                    total_frames_written += 1
        else:
            # First shot (Cover): write up to `num_frames - crossfade_frames`
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
    total_dur = 63.0 # exactly 63 seconds

    # Timeline for VO clips:
    # Shot 00: 0.0 to 3.0s
    # Shot 01: starts 3.0s, VO at 3.8s
    # Shot 02: starts 9.0s, VO at 9.8s
    # ...
    # Shot 10: starts 57.0s, VO at 57.8s
    vo_offsets = [
        (1, 3.8),
        (2, 9.8),
        (3, 15.8),
        (4, 21.8),
        (5, 27.8),
        (6, 33.8),
        (7, 39.8),
        (8, 45.8),
        (9, 51.8),
        (10, 57.8)
    ]

    # Build ffmpeg complex filter command
    # Input 0: BGM
    # Input 1..10: VO files
    inputs = ["-i", BGM_PATH]
    for idx, offset in vo_offsets:
        vo_file = os.path.join(AUDIO_DIR, f"vo_{idx:02d}.wav")
        inputs.extend(["-i", vo_file])

    filter_complex = []
    # 1. BGM: trim to 63s, adjust volume to 0.18, fade in 1s, fade out last 3s
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
    print(f"Duration: 63.0 seconds")
    print(f"Subtitles: None (pure picture, motion & voiceover)")
    print(f"==========================================")

if __name__ == "__main__":
    main()
