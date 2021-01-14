# -*- coding: utf-8 -*-

# 禁用词，包含如下字符的将被忽略
DISALLOWED_WORDS = ['（', '）', '(', ')', '__', '《', '》', '【', '】', '[', ']']
# 句子最大长度
MAX_LEN = 64
# 最小词频
MIN_WORD_FREQUENCY = 2
# 训练的batch size
BATCH_SIZE = 16
# 数据集路径
DATASET_PATH = './sanjuban.txt'
# 每个epoch训练完成后，随机生成SHOW_NUM首三句半作为展示
SHOW_NUM = 5
# 共训练多少个epoch
TRAIN_EPOCHS = 80
# 最佳权重保存路径
BEST_MODEL_PATH = './best_model.h5'