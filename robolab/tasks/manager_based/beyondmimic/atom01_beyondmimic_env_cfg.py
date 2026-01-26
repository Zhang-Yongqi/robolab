
import os

from robolab.assets.robots import ATOM01_CFG
from robolab.robolab.tasks.manager_based.beyondmimic.beyondmimic_env_cfg import BeyondMimicEnvCfg

from isaaclab.utils import configclass
from robolab import ROBOLAB_ROOT_DIR


@configclass
class Atom01BeyondMimicEnvCfg(BeyondMimicEnvCfg):
    def __post_init__(self):
        super().__post_init__()

        self.scene.robot = ATOM01_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")
        self.commands.motion.motion_file = os.path.join(
            ROBOLAB_ROOT_DIR, "data", "motions", "atom01_bm", "yundong1.npz"
        )
        self.commands.motion.anchor_body_name = "torso_link"
        self.commands.motion.body_names = [
            'left_thigh_yaw_link', 
            'right_thigh_yaw_link', 
            'torso_link', 
            'left_thigh_roll_link', 
            'right_thigh_roll_link', 
            'left_arm_pitch_link', 
            'right_arm_pitch_link', 
            'left_thigh_pitch_link', 
            'right_thigh_pitch_link', 
            'left_arm_roll_link', 
            'right_arm_roll_link', 
            'left_knee_link', 
            'right_knee_link', 
            'left_arm_yaw_link', 
            'right_arm_yaw_link', 
            'left_ankle_pitch_link', 
            'right_ankle_pitch_link', 
            'left_elbow_pitch_link', 
            'right_elbow_pitch_link', 
            'left_ankle_roll_link', 
            'right_ankle_roll_link', 
            'left_elbow_yaw_link', 
            'right_elbow_yaw_link',
        ]

        self.observations.policy.motion_anchor_pos_b = None
        self.observations.policy.base_lin_vel = None

        self.episode_length_s = 20.0
