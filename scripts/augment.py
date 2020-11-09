import torch
import torchvision.transforms as transforms
# from torchvision.utils import save_image
# from customDataset import wordDataset
import os
import random
import sys
from PIL import Image


def main(dataset):
    random.seed(311420)
    torch.manual_seed(311420)
    root = os.getcwd()
    # print(root)
    root = os.path.join(root, "data_augmented/{}".format(dataset))

    NUM_IMAGES_AUGMENTED = 5  # Number of images per character augmented
    NUM_AUGMENTATIONS = 5  # Number of times each image is augmented

    transform = transforms.Compose([
        transforms.RandomAffine(degrees=180,
                                translate=(0.15, 0.15),
                                fillcolor=255,
                                shear=60)
    ])

    for language in os.listdir(root):
        language_path = os.path.join(root, language)
        for character in os.listdir(language_path):
            character_path = os.path.join(language_path, character)
            images = os.listdir(character_path)
            sampled_images = random.sample(images, NUM_IMAGES_AUGMENTED)
            for _, sampled_image in enumerate(sampled_images):
                image_name = sampled_image[:-4]
                image = Image.open(os.path.join(character_path, sampled_image))
                # print(character_path)
                for j in range(1, NUM_AUGMENTATIONS + 1):
                    transformed_image = transform(image)
                    # print("{}/{}_aug{}.png".format(os.path.join(character_path, sampled_image), image_name, j))
                    transformed_image.save("{}/{}_aug{}.png".format(
                        character_path, image_name, j))


if __name__ == "__main__":
    main(sys.argv[1])
