# Common Objects in Context (COCO) Labels

## List of object labels / categories

The labels are divided into three sections:

1. Original COCO paper
2. COCO dataset release in 2014
3. COCO dataset release in 2017

Since the labels for COCO datasets released in 2014 and 2017 were the same, they were merged into a single file.
The file name should be self-explanatory in determining the publication type of the labels.

More elaboration about COCO dataset labels can be found in [this article](http://tech.amikelive.com/node-718/what-object-categories-labels-are-in-coco-dataset/)

## How to obtain the COCO labels

A Python script is provided to dump the labels for each COCO dataset release. It works by performing one-time download 
for the annotations archive file, which is then saved to a local directory (default to `/tmp`). Subsequently, the 
archive file is inflated as a preparation for the label dump request.

When the script is executed, it will find the correct JSON file and then parse the JSON as stream. Each label is 
displayed on `stdout` as sequences of id, name, and super category.

Prior to running the Python script, install the dependencies from the script directory as follows:
    
    pip install -r requirements.txt

To obtain the labels for each COCO dataset release, provide `-y` option when executing the Python script.

For listing the labels in 2014 release: 

    python dump_coco_labels.py -y 2014
    
And for the labels in 2017 release:

    python dump_coco_labels.py -y 2017

