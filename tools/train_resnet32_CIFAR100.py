import sys
sys.path.append('.')

from Data.CIFAR100data import *
from layers.residual_attention_network import *
from modelling.ResNet32 import *

n_layers = 100

bar = LitProgressBar()
data_module_100 = CIFAR100DataModule()
data_module_100.prepare_data()
test_data_100 = data_module_100.test_dataloader()
train_data_100 = data_module_100.train_dataloader()

model = ResidualAttentionModel(n_layers)
trainer = pl.Trainer(max_epochs=10, gpus=-1, callbacks=[bar], accelerator='ddp')

trainer.fit(model, train_data_100)
trainer.test(test_dataloaders=test_data_100, verbose=True)