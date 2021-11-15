#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.
import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define yourself dataset path
        self.data_dir = "/mnt/ts-cvml-datastore/ts_data/datasets/cotton/yolo_x"
        self.train_ann = "train_1.0.1.json"
        self.val_ann = "dev_1.0.1.json"

        self.num_classes = 1
        self.input_size = (640, 640)
        self.multiscale_range = 0

        self.max_epoch = 500
        self.data_num_workers = 12
        self.eval_interval = 1
