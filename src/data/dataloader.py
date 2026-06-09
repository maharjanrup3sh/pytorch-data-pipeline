from torch.utils.data import DataLoader
from torchvision import transforms
from src.data.dataset import FlowerDataset


def get_dataloader(root_dir, batch_size=32, shuffle=True, num_workers=0):
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
    ])

    dataset = FlowerDataset(root_dir=root_dir, transform=transform)

    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=num_workers
    )

    return dataloader, dataset