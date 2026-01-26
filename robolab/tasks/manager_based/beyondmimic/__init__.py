
import gymnasium as gym
from . import agents

##
# Register Gym environments.
##

gym.register(
    id="Atom01-BeyondMimic",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.atom01_beyondmimic_env_cfg:Atom01BeyondMimicEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.atom01_beyondmimic_agent_cfg:Atom01BeyondMimicPPORunnerCfg",
    },
)
