#基础倍率计算

class Base_Skill_Hit:
    def __init__(self, ATK: float, CRIT_Rate: float, CRIT_DMG: float,
                 attack_multiplier_Main_R: float, attack_sequences_Main_R: int,
                 spread_multiplier_Obj_R: float, attack_sequences_Obj_R: int, targets_hit_Main_R: int,
                 attack_multiplier_Main_E: float, attack_sequences_Main_E: int,
                 spread_multiplier_Obj_E: float, attack_sequences_Obj_E: int, targets_hit_Main_E: int,
                 attack_multiplier_Main_Q: float, attack_sequences_Main_Q: int,
                 spread_multiplier_Obj_Q: float, attack_sequences_Obj_Q: int, targets_hit_Main_Q: int):

        # 初始化技能倍率参数
        self.attack_multiplier_Main_R = attack_multiplier_Main_R  # 主目标终结技倍率
        self.attack_sequences_Main_R = attack_sequences_Main_R  # 主目标终结技攻击段数
        self.spread_multiplier_Obj_R = spread_multiplier_Obj_R  # 副目标终结技攻击倍率
        self.attack_sequences_Obj_R = attack_sequences_Obj_R  # 副目标终结技攻击段数
        self.targets_hit_Main_R = targets_hit_Main_R  # 副目标终结技数量

        self.attack_multiplier_Main_E = attack_multiplier_Main_E  # 主目标战技倍率
        self.attack_sequences_Main_E = attack_sequences_Main_E  # 主目标战攻击段数
        self.spread_multiplier_Obj_E = spread_multiplier_Obj_E  # 副目标战攻击倍率
        self.attack_sequences_Obj_E = attack_sequences_Obj_E  # 副目标战攻击段数
        self.targets_hit_Main_E = targets_hit_Main_E  # 副目标战数量

        self.attack_multiplier_Main_Q = attack_multiplier_Main_Q  # 主目标普通攻击倍率
        self.attack_sequences_Main_Q = attack_sequences_Main_Q  # 主目标普通攻击段数
        self.spread_multiplier_Obj_Q = spread_multiplier_Obj_Q  # 副目标普通攻击倍率
        self.attack_sequences_Obj_Q = attack_sequences_Obj_Q  # 副目标普通攻击段数
        self.targets_hit_Main_Q = targets_hit_Main_Q  # 副目标普通攻击数量

        # 计算 Base_DMG
        self.Base_DMG = self.calculate_base_dmg()

        # 初始化基础攻击参数
        self.ATK = ATK
        self.CRIT_Rate = CRIT_Rate
        self.CRIT_DMG = CRIT_DMG

    def calculate_base_dmg(self):
        # 计算 Base_DMG
        return (self.attack_multiplier_Main_R * self.attack_sequences_Main_R) + \
            (self.spread_multiplier_Obj_R * self.attack_sequences_Obj_R * self.targets_hit_Main_R) + \
            (self.attack_multiplier_Main_E * self.attack_sequences_Main_E) + \
            (self.spread_multiplier_Obj_E * self.attack_sequences_Obj_E * self.targets_hit_Main_E) + \
            (self.attack_multiplier_Main_Q * self.attack_sequences_Main_Q) + \
            (self.spread_multiplier_Obj_Q * self.attack_sequences_Obj_Q * self.targets_hit_Main_Q)

    def calculate_crit_damage(self):
        # 计算暴击伤害
        return self.ATK * self.Base_DMG * (self.CRIT_DMG + 1)

    def calculate_non_crit_damage(self):
        # 计算非暴击伤害
        return self.ATK * self.Base_DMG

    def calculate_expected_damage(self):
        # 计算期望伤害
        crit_damage = self.calculate_crit_damage()
        non_crit_damage = self.calculate_non_crit_damage()
        expected_damage = (self.CRIT_Rate * crit_damage) + ((1.0 - self.CRIT_Rate) * non_crit_damage)
        return expected_damage
