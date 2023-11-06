# Buff加成计算类
class Buff_Enhance:
    def __init__(self, Feature_Enhance: float, IncreaseDMG: float):
        self.Feature_Enhance = Feature_Enhance  #属性增伤
        self.IncreaseDMG = IncreaseDMG  #其他增伤

    def calculate_total_enhance(self):
        # 计算总加成效果
        return self.Feature_Enhance + self.IncreaseDMG + 1.0
