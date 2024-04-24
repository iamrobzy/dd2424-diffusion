# Description

The problem we are aiming to tackle is that of semantic segmentation, which can be used to put different objects into categories or regions in an image, aiding in scene understanding. For this project, we will complete one of the custom projects, and add some extensions/modifications to it. The project that we aim to replicate is *Label-Efficient Semantic Segmentation with Diffusion Models* [1]. Recently, diffusion models have proven to be exceptional generative performance. The authors show that using the diffusion models can be a useful tool for semantic segmentation, especially when the labeled data is somewhat scarce. To ensure novelty, we will use the code provided by the authors as an inspiration and implement the architecture ourselves, using the common Machine Learning library PyTorch. Thus, none of our code will be copied from open-source resources.

Some of the modifications which we aim to explore in this project are:

- E grade:
  - Creating our own implementation of the architecture proposed in the original paper.

- D-C grade:
  - Experimenting with different U-NET architectures, by changing upsampling and downsampling.
  - Modifying the hyperparameters of the network and pre-processing the data with augmentations.

- B-A grade:
  - Upgrading the pixel classifier layer with different forward layers; for instance making the network deeper/wider, or using residual blocks akin to ResNet architecture.
  - Updating the objective function by using the *Improved Denoising Diffusion* objective function - leading to better results - as proposed in [2].

The original paper used their datasets for most of the training and testing, however, one they put into publically available use is the Large-scale CelebFaces Attributes (CelebA) Dataset [3]. We consider using the ADE-Bedroom dataset as well, but that would require getting a subset of the ADE20 dataset [4]. Both of the datasets are annotated. The performance will be computed in terms of the mean Intersection over Union (IoU) measure.

# Member backgrounds

All team members are enrolled in the MSc. Machine Learning program and have prior experience with machine learning theory for first-semester courses. Machine learning practice varies on an individual basis

- Robert - experience with Tensorflow and exposure to Pytorch. Aims to gain more experience in developing deep architectures by hand.
- Jacques - I wish to improve my general knowledge about the interchangeability of different deep-learning architectures and their implementation in Pytorch.
- Michal - experience in PyTorch. Aspires to learn more about diffusion and semantic segmentation.

# Project Expectations
Through the implementation of all these modifications on top of the implementation based on the paper, we aim for an **A grade** for this project.

[1]: baranchuk2021label
[2]: nichol2021improved
[3]: liu2015faceattributes
[4]: zhou2017scene
