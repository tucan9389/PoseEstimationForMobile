# -*- coding: utf-8 -*-
# @Time    : 18-3-6 3:20 PM
# @Author  : edvard_hua@live.com
# @FileName: data_filter.py
# @Software: PyCharm

import training.src.network_mv2_cpm
import training.src.network_mv2_hourglass

def get_network(type, input, trainable=True):
    if type == 'mv2_cpm':
        net, loss = training.src.network_mv2_cpm.build_network(input, trainable)
    elif type == "mv2_hourglass":
        net, loss = training.src.network_mv2_hourglass.build_network(input, trainable)
    return net, loss
