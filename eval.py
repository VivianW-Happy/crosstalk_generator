# -*- coding: utf-8 -*-

import tensorflow as tf
from dataset import tokenizer
import settings
import utils
# tf.enable_eager_execution()
# 加载训练好的模型
model = tf.keras.models.load_model(settings.BEST_MODEL_PATH)
# 随机生成一首三句半

for i in range(1,10):
    print(utils.generate_random_sanjuban(tokenizer, model))
