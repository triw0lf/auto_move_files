import os
import shutil

# Change this to change the source directory
root_src_dir = '/home/lproehl/source'
# Change this to change the destination directory
root_dst_dir = '/home/lproehl/destination'

# Checks if files in source location are in destination location
for src_dir, dirs, files in os.walk(root_src_dir): 
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
# If the files are not in the location, move the files from the source to the destination
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
# If the files are in the location, overwrite the files 
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        shutil.move(src_file, dst_dir)
