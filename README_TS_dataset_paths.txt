To make the model refer to the right dataset paths and in coco17 dataset structure the following changes were made:

1. In the yolox_base.py file, the function get_eval_loader took name="val2017' and test name = "test2017".
   These were changed to "train_1.0.1" and "test_1.0.1"

2. In the /exp/examples/custom/yolox_s.py file was given the data dir of dataset folder (whose child folders include annotations, train_1.0.1(train images folder) and test_1.0.1(test images folder))

3. In /yolox/data/datasets/coco.py search for the function which has the assert error prompt (probably the load_img_annotation fuction)
   Here the self.name has not been used and is changed to a prefixed name

4. in the same file above, in the init function for Dataset class, specify name = dev or test dataset folder name 
(for some reason the get_eval_loader function in yolox/exp/yolox_base.py does not pass correct name to coco.py)
