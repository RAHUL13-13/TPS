from PIL import Image
import os

vids = os.listdir("/shared/home/v_rahul_pratap_singh/local_scratch/action_recognition/TPS/data/diving48/rawframes/")
if not os.path.exists("/shared/home/v_rahul_pratap_singh/local_scratch/action_recognition/TPS/data/diving48/frame_resize256/"):
    os.makedirs("/shared/home/v_rahul_pratap_singh/local_scratch/action_recognition/TPS/data/diving48/frame_resize256/")

for vid in vids:
    vid_add = "/shared/home/v_rahul_pratap_singh/local_scratch/action_recognition/TPS/data/diving48/rawframes/"+vid
    frames = os.listdir(vid_add)

    new_vid_add = "/shared/home/v_rahul_pratap_singh/local_scratch/action_recognition/TPS/data/diving48/frame_resize256/" + vid+"/"
    if not os.path.exists(new_vid_add):
        os.makedirs(new_vid_add)

    for frame in frames:
        frame_add = vid_add + "/"+ frame
        image = Image.open(frame_add)
        
        frame_h, frame_w = image.size 
        if frame_h < frame_w:
            resized = image.resize((256, frame_w))
        else:
            resized = image.resize((frame_h, 256))
        
        new_frame_add = new_vid_add + "/"+frame
        resized.save(new_frame_add)
