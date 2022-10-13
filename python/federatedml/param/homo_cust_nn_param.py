from federatedml.param.base_param import BaseParam


class TrainerParam(BaseParam):

    def __init__(self, trainer_name='', **kwargs):
        super(TrainerParam, self).__init__()
        self.trainer_name = trainer_name
        self.param = kwargs

    def check(self):
        self.check_string(self.trainer_name, 'trainer_name')

    def to_dict(self):
        ret = {'trainer_name': self.trainer_name, 'param': self.param}
        return ret


class DatasetParam(BaseParam):

    def __init__(self, dataset_name='', **kwargs):
        super(DatasetParam, self).__init__()
        self.dataset_name = dataset_name
        self.param = kwargs

    def check(self):
        self.check_string(self.dataset_name, 'dataset_name')

    def to_dict(self):
        ret = {'dataset_name': self.dataset_name, 'param': self.param}
        return ret


class HomoCustNNParam(BaseParam):

    def __init__(self,
                 trainer: TrainerParam = TrainerParam(),
                 dataset: DatasetParam = DatasetParam(),
                 torch_seed: int = 100,
                 validation_freq: int = None,
                 nn_define: dict = None,
                 loss: dict = None,
                 optimizer: dict = None
                 ):

        super(HomoCustNNParam, self).__init__()
        self.trainer = trainer
        self.dataset = dataset
        self.torch_seed = torch_seed
        self.validation_freq = validation_freq
        self.nn_define = nn_define
        self.loss = loss
        self.optimizer = optimizer

    def check(self):

        self.trainer.check()
        self.dataset.check()
        self.check_positive_integer(self.torch_seed, 'torch seed')
        if self.validation_freq is not None:
            self.check_positive_integer(self.validation_freq, 'validation freq')
        assert isinstance(self.nn_define, dict), 'nn define should be a dict defining model structures'
        assert isinstance(self.loss, dict), 'loss parameter should be a loss config dict'
        assert isinstance(self.optimizer, dict), 'optimizer parameter should be a config dict'
