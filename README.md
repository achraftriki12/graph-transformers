# A graph-transformer architecture for embryo images classification
This work is based on the paper "A graph-transformer for whole slide image classification"


# Usage
## 1. Graph Construction

### (a) Tiling Patch 
```
python src/tile.py  <full_patch_to_output_folder> "full_path_to_input_slides/*/*.svs"
```
Non-mandatory parameters:
parser.add_argument("input_image", help="Path to the input image")
    parser.add_argument("--tile_size", type=int, default=256, help="Size of each tile (default is 256 pixels)")
    parser.add_argument("--variance_threshold", type=float, default=20.0, help="Variance threshold below which tiles will not be saved (default is 10.0)")
<li>--tile_size : Size of each tile (default is 256 pixels)</li>
<li>--variance_threshold : Variance threshold below which tiles will not be saved (default is 20.0)</li>

### (b) Training Patch Feature Extractor
Go to './feature_extractor' and config 'config.yaml' before training. The trained feature extractor based on contrastive learning is saved in folder './feature_extractor/runs'. Before training, put paths to all pathces in 'all_patches.csv' file.
```
python run.py
```
You could use pretrained feature extractor: feature_extractor/model.pth.

### (c) Constructing Graph
Go to './feature_extractor' and build graphs from patches:
```
python build_graphs.py --weights "path_to_pretrained_feature_extractor" --dataset "path_to_patches" --output "../graphs"
```

## 2. Training Graph-Transformer
Run the following script to train and store the model and logging files under "graph_transformer/saved_models" and "graph_transformer/runs".
```
bash scripts/train.sh
```
To evaluate the model. run
```bash scripts/test.sh```

Split training, validation, and testing dataset and store them in text files as:
```
sample1 \t label1
sample2 \t label2
...
```


# Requirements
Major dependencies are:
<li> python </li>
<li> pytorch </li>
