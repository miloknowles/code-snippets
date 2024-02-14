import torch


def count_parameters(model) -> int:
  """Returns the number of parameters in a model.
  
  References
  ----------
  https://discuss.pytorch.org/t/how-do-i-check-the-number-of-parameters-of-a-model/4325/8
  """
  return sum(p.numel() for p in model.parameters() if p.requires_grad)


def get_best_system_device() -> str:
  """Detect the best available device on this machine."""
  device = "cpu"
  if torch.cuda.is_available():
    device = "cuda"
  elif torch.backends.mps.is_available():
    device = "mps"
  return device