# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
# Original code is licensed under BSD-3-Clause.
#
# Copyright (c) 2025-2026, The RoboLab Project Developers.
# All rights reserved.
# Modifications are licensed under BSD-3-Clause.
#
# This file contains code derived from Isaac Lab Project (BSD-3-Clause license)
# with modifications by RoboLab Project (BSD-3-Clause license).

import gymnasium as gym

from . import agents

gym.register(
    id="Atom01-Interrupt",
    entry_point=f"{__name__}.interrupt_env:InterruptEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.atom01_interrupt_env_cfg:ATOM01InterruptEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.atom01_interrupt_agent_cfg:ATOM01InterruptAgentCfg",
    },
)