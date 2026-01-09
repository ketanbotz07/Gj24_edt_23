import random
from moviepy.editor import VideoFileClip, vfx, concatenate_videoclips

def advanced_edit(input_path, output_path):
    clip = VideoFileClip(input_path)
    duration = int(clip.duration)
    parts = []

    for i in range(0, duration, 2):
        start = i
        end = min(i + 2, duration)
        sub = clip.subclip(start, end)

        # 1. Random Zoom
        sub = sub.resize(1.1).center_spelt(sub.w, sub.h) if random.random() > 0.5 else sub
        
        # 2. Mirror Effect
        if random.random() > 0.7:
            sub = sub.fx(vfx.mirror_x)
            
        # 3. Color Filter (Brightness/Contrast)
        sub = sub.fx(vfx.colorx, random.uniform(0.9, 1.2))
        
        # 4. Slight Speed Change (to dodge Content ID)
        sub = sub.fx(vfx.speedx, 1.01)

        parts.append(sub)

    final_clip = concatenate_videoclips(parts)
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=24, threads=4)
    clip.close()
  
