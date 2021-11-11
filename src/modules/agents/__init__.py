REGISTRY = {}


from .casec_rnn_agent import CASECRNNAgent
from .casec_rnn_agent import CASECPairRNNAgent

REGISTRY["casec_rnn"] = CASECRNNAgent
REGISTRY["casec_pair_rnn"] = CASECPairRNNAgent

from .rnn_feature_agent import RNNFeatureAgent
REGISTRY["rnn_feat"] = RNNFeatureAgent
