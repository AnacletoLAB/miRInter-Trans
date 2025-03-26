# miRInter-Trans
miRInter-Trans is a miRNA-ncRNA interaction classifier, based on a Transformer architecture.

# Requirements
A CUDA environment, and a minimum VRAM of 8GB is required.
### Dependencies
```
miRInter-Trans/RNA-FM/environment.yml
```

# Usage
Firstly, download the checkpoint of the foundational RNA Language model (RNA-FM) in the directory: "RNA-FM/redevelop/pretrained/"
#### Directory tree
```
.
├── LICENSE
├── README.md
├── classification_dataset_creation.py # python module for dataset files generation starting from only positive interactive couples
├── classification_miRNA-miRNA-example-notebook.ipynb # Example usage of miRInter-Trans for training on a set of miRNA-miRNA interaction sequences
├── RNA-FM/ # Foundational ncRNA language model, with custom scripts for embeddings extraction
```