# -*-coding: utf-8 -*-
#@Author: 'ljd'
#@Time：2016/9/10 11:13

import logging
logger = logging.getLogger('simple_logging.log')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.debug('debug message')