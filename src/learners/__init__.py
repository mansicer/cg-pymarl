from .q_learner import QLearner
from .coma_learner import COMALearner
from .qtran_learner import QLearner as QTranLearner
from .casec_learner import CASECLearner


REGISTRY = {}

REGISTRY["q_learner"] = QLearner
REGISTRY["coma_learner"] = COMALearner
REGISTRY["qtran_learner"] = QTranLearner
REGISTRY["casec_learner"] = CASECLearner

from .dcg_learner import DCGLearner
REGISTRY["dcg_learner"] = DCGLearner
