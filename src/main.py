import torchvision.datasets as datasets
import torchvision.transforms as transforms

# Define the transform to preprocess the images
transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# Load the CelebA dataset
celeba_dataset = datasets.CelebA(
    root='../data/img_align_celeba',
    split='train',
    transform=transform,
    download=True
)

# Access the images and attributes
images = celeba_dataset.data
attributes = celeba_dataset.attr

# Print the number of images and attributes
print(f"Number of images: {len(images)}")
print(f"Number of attributes: {attributes.shape[1]}")
