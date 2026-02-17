import shutil
import os

source_dir = r"c:\Users\SystemAnalyst\Desktop\Programming Ass_3 - Copy\output"
dest_dir = r"c:\Users\SystemAnalyst\.gemini\antigravity\brain\46aa2d47-b0e6-4b26-a3a2-d3549ad7ee4f"

files_to_copy = [
    "inference_speed_comparison.png",
    "confidence_score_distribution.png",
    "detections_per_frame.png",
    "result_cricket-1.jpg",
    "result_football-1.jpg",
    "result_rugby-1.jpg",
    "metrics.txt"
]

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

print(f"Copying files from {source_dir} to {dest_dir}...")

for filename in files_to_copy:
    src = os.path.join(source_dir, filename)
    dst = os.path.join(dest_dir, filename)
    
    if os.path.exists(src):
        try:
            shutil.copy2(src, dst)
            print(f"Copied: {filename}")
        except Exception as e:
            print(f"Error copying {filename}: {e}")
    else:
        print(f"File not found: {filename}")

print("Copy operation complete.")
