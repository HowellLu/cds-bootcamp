import dataclasses

@dataclasses.dataclass
class BertFineTuningConfig:
    precision: int = 16
    max_epochs: int = 20
    batch_size: int = 16
    gpus: int = 2
