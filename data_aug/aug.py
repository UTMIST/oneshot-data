import torch
import torchvision.transforms as transforms
from torchvision.utils import save_image
from customDataset import wordDataset


my_transforms = transforms.Compose([
    transforms.ToPILImage(),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(degrees=45),
    # transforms.RandomCrop((224, 224)) , #size?
    transforms.RandomVerticalFlip(p=0.05),
    transforms.ToTensor()
])

dataset = wordDataset(csv_file = './csv/Angelic.csv', root_dir = 'images_evaluation/Angelic', transform=my_transforms)

n = 1
for i in range(10):
    for img, label in dataset:
        save_image(img, 'tf_'+str(n)+'.png')
        n += 1
        