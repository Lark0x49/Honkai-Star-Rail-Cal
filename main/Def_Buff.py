# 怪物抗性计算类

class Def_Buff:
    def __init__(self, Q_DEF_broken: bool, ATK_Level: int, Enemy_Level: int, Dec_DEF: float):
        self.Dec_DEF = Dec_DEF  #减防
        self.Q_DEF_broken = Q_DEF_broken  #韧性条
        self.ATK_Level = ATK_Level  #我方等级
        self.Enemy_Level = Enemy_Level  #敌方等级

    def calculate_Q_DEF_effect(self):
        # 计算韧性区的影响
        return 0.9 if not self.Q_DEF_broken else 1.0

    def calculate_D_DEF_effect(self):
        # 计算防御效果区的影响
        attacker_def = (self.ATK_Level * 10 + 200)
        enemy_def = ((self.Enemy_Level * 10 + 200) * (1.0 - self.Dec_DEF))
        return attacker_def / (attacker_def + enemy_def)

    def calculate_total_defense_effect(self):
        # 计算所有防御效果乘区的总影响
        return self.calculate_Q_DEF_effect() * self.calculate_D_DEF_effect()
