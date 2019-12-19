import os
import json
# import requests
from PIL import Image
from torchvision import models
import torch
from torchvision import transforms


def classify(path):
    # define transform for preprocess
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )])

    # get labels
    with open('./labels.json') as f:
        labels = json.load(f)
    labels = {int(key): value for key, value in labels.items()}

    with open('./food.json') as f:
        food_labels = json.load(f)
    food_labels = {int(key): value for key, value in food_labels.items()}

    # resnet and set as evaluate mode
    resnet = models.resnet50(pretrained=True)
    resnet.eval()
    # resnet.cuda()
    csv = open(path + '/classify.csv', 'w')

    for root, dirs, files in os.walk(path):
        for f in files:
            if not f.lower().endswith('jpg') and not f.lower().endswith('png'):
                continue
            # print(root+'/'+f)
            img = Image.open(root + '/' + f)
            # preprocess
            img_t = transform(img)
            batch_t = torch.unsqueeze(img_t, 0)
            # batch_t = batch_t.cuda(non_blocking=True)

            # get answer
            out = resnet(batch_t)
            _, indices = torch.sort(out, descending=True)
            percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100

            have_food = False
            csv.write(root + '/' + f + ',')

            for idx in indices[0][:5]:
                print()
                csv.write(labels.get(int(idx)).replace(',', ' ') + ',')
                if food_labels.get(int(idx)) is not None:
                    have_food = True

            if have_food:
                csv.write('1\n')
            else:
                csv.write('0\n')
    csv.close()
