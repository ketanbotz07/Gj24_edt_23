import random
from moviepy.editor import VideoFileClip, vfx, concatenate_videoclips

def advanced_edit(input_path, output_path):
    clip = VideoFileClip(input_path)
    duration = int(clip.duration)
    segments = []
    
    for i in range(0, duration, 2):
        start = i
        end = min(i + 2, duration)
        sub_clip = clip.subclip(start, end)
        
        # 1. Random Zoom (105% to 115%)
        sub_clip = sub_clip.resize(random.uniform(1.05, 1.15))
        
        # 2. Mirroring (Randomly flip segments)
        if random.choice([True, False]):
            sub_clip = sub_clip.fx(vfx.mirror_x)
            
        # 3. Filter/Color adjustment
        sub_clip = sub_clip.fx(vfx.colorx, random.uniform(0.9, 1.1))
        
        # 4. Minute Speed Change (Metadata change)
        sub_clip = sub_clip.fx(vfx.speedx, random.choice([0.99, 1.01]))

        segments.append(sub_clip)

    # Combine all segments
    final_clip = concatenate_videoclips(segments)
    
    # Save with YouTube friendly settings
    final_clip.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac", bitrate="3000k")
    clip.close()
    final_clip.close()
