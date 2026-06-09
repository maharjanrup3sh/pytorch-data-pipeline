import os
from pathlib import Path
from PIL import Image
from torch.utils.data import Dataset


class FlowerDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = Path(root_dir)
        self.transform = transform
        self.image_paths = []
        self.labels = []
        
        self.classes = sorted([d.name for d in self.root_dir.iterdir() if d.is_dir()])
        
        for label, class_name in enumerate(self.classes):
            class_folder = self.root_dir / class_name
            for img_path in class_folder.glob("*.jpg"):
                self.image_paths.append(img_path)
                self.labels.append(label)
                
        print(f"Found {len(self.image_paths)} images in {len(self.classes)} classes")

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        label = self.labels[idx]
        image = Image.open(img_path).convert("RGB")
        if self.transform:
            image = self.transform(image)
        return image, label