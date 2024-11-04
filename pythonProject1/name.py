import numpy as np
import pandas as pd
from pymoo.core.problem import ElementwiseProblem
from pymoo.termination import get_termination
from pymoo.optimize import minimize
from pymoo.core.variable import Integer, Real
from pymoo.core.mixed import MixedVariableGA
from pymoo.core.evaluator import Evaluator
from pymoo.core.population import Population
from copy import deepcopy

data1 = pd.read_csv("2024C附件/i1-乡村现有耕地.csv")
data2 = pd.read_csv("2024C附件/i2-乡村种植的农作物.csv")
data3 = pd.read_csv("2024C附件/i3-2023年的农作物种植情况.csv")
data4 = pd.read_csv("2024C附件/i4-2023年统计的相关数据.csv")
data5 = pd.read_csv("2024C附件/o5-2023作物产量统计.csv")
data6 = pd.read_csv("2024C附件/o6-2023作物销售单价统计.csv")


class MyProblem(ElementwiseProblem):

    def __init__(self, **kwargs):

        # 定义变量 Note!
        # 考虑到整型变量的运算效率高于浮点型变量
        # 将自变量定义为整型变量

        vars = {}

        # A、B、C 类地块种植 CT1 的面积 Areaij
        for i in range(1, 26 + 1):
            for j in range(1, 15 + 1):
                vars[f"Area{i}_{j}"] = Integer(
                    bounds=(0, data1.iloc[i - 1]['地块面积/亩']))

        # D 类地块种植类型 DTypei
        for i in range(27, 34 + 1):
            vars[f"DType{i}"] = Integer(
                bounds=(0, 1))

        # D 类地块种植 水稻 的面积 Areai16
        for i in range(27, 34 + 1):
            vars[f"Area{i}_16"] = Integer(
                bounds=(0, data1.iloc[i - 1]['地块面积/亩']))

        # D、E、F 类地块第一季种植各类作物的面积 AreaOneij
        for i in range(27, 54 + 1):
            for j in range(17, 34 + 1):
                vars[f"AreaOne{i}_{j}"] = Integer(
                    bounds=(0, data1.iloc[i - 1]['地块面积/亩']))

        # D 类地块第二季种植各类作物的面积 AreaTwoij
        for i in range(27, 34 + 1):
            for j in range(35, 37 + 1):
                vars[f"AreaTwo{i}_{j}"] = Integer(
                    bounds=(0, data1.iloc[i - 1]['地块面积/亩']))

        # E 类地块第二季种植各类作物的面积 AreaTwoij
        for i in range(35, 50 + 1):
            for j in range(38, 41 + 1):
                vars[f"AreaTwo{i}_{j}"] = Real(
                    bounds=(0, data1.iloc[i - 1]['地块面积/亩']))

        # F 类地块第二季种植各类作物的面积 AreaTwoij
        for i in range(51, 54 + 1):
            for j in range(17, 34 + 1):
                vars[f"AreaTwo{i}_{j}"] = Real(
                    bounds=(0, data1.iloc[i - 1]['地块面积/亩']))

        # 输出变量的数量
        print(f'变量的数量: {len(vars)}')

        super().__init__(
            vars=vars,
            n_obj=1,  # 优化目标数量
            n_ieq_constr=54 * 3,  # 不等式约束条件数量
            **kwargs,
        )

    def _evaluate(self, x, out, *args, **kwargs):

        # 定义目标函数（售价）
        W = 0

        ## 首先统计各类作物的产量（共41种）
        total_yield_1 = [0] * 41  # 各类作物第一季的总产量
        total_yield_2 = [0] * 41  # 各类作物第二季的总产量
        total_yield_3 = [0] * 41  # 各类作物单季的总产量
        crop_area_1 = [0] * 54  # 第一季各类地块种植的总面积
        crop_area_2 = [0] * 54  # 第二季各类地块种植的总面积
        crop_area_3 = [0] * 54  # 单季各类地块种植的总面积

        # 统计 A、B、C 类地块的产量
        # A、B、C 类地块的只种植单季 CT1（除水稻）
        for i in range(1, 26 + 1):
            for j in range(1, 15 + 1):
                # 按照地块序号 i，在 data1 中匹配到地块类型
                area_type = data1.iloc[i - 1]['地块类型']
                # 按照地块类型area_type和作物编号j，在 data4 中匹配到亩产量/斤
                yield_per_area = data4.loc[
                    (data4['地块类型'] == area_type) & (data4['作物编号'] == j), '亩产量/斤'].values[0]
                # 累计产量
                total_yield_3[j - 1] += yield_per_area * x[f"Area{i}_{j}"]
                # 累计地块种植面积
                crop_area_3[i - 1] += x[f"Area{i}_{j}"]

        # 统计 D 类地块的产量
        # D 类地块有两种种植方式，使用变量 DType 表示种植方式：
        #      0.种植两季 CT2
        #      1.种植一季水稻
        for i in range(27, 34 + 1):
            dtype = x[f"DType{i}"]  # D 类地块的种植类型
            if dtype == 1:  # 种植水稻
                # 地块类型
                area_type = "水浇地"
                # 按照地块类型area_type和作物编号16，在 data4 中匹配到亩产量
                yield_per_area = data4.loc[
                    (data4['地块类型'] == area_type) &
                    (data4['作物编号'] == 16),
                    '亩产量/斤'].values[0]
                # 累计产量
                total_yield_3[16 - 1] += yield_per_area * x[f"Area{i}_16"]
                # 累计地块种植面积
                crop_area_3[i - 1] += x[f"Area{i}_16"]
            else:  # 种植 两季CT2
                for j in range(17, 34 + 1):
                    # 地块类型
                    area_type = "水浇地"
                    # 按照地块类型area_type和作物编号，在 data4 中匹配到亩产量
                    yield_per_area = data4.loc[
                        (data4['地块类型'] == area_type) &
                        (data4['种植季次'] == '第一季') &
                        (data4['作物编号'] == j),
                        '亩产量/斤'].values[0]
                    # 累计产量
                    total_yield_1[j - 1] += yield_per_area * x[f"AreaOne{i}_{j}"]
                    # 累计地块种植面积
                    crop_area_1[i - 1] += x[f"AreaOne{i}_{j}"]
                for j in range(35, 37 + 1):
                    # 地块类型
                    area_type = "水浇地"
                    # 按照地块类型area_type和作物编号，在 data4 中匹配到亩产量
                    yield_per_area = data4.loc[
                        (data4['地块类型'] == area_type) &
                        (data4['种植季次'] == '第二季') &
                        (data4['作物编号'] == j),
                        '亩产量/斤'].values[0]
                    # 累计产量
                    total_yield_2[j - 1] += yield_per_area * x[f"AreaTwo{i}_{j}"]
                    # 累计地块种植面积
                    crop_area_2[i - 1] += x[f"AreaTwo{i}_{j}"]

        # 统计 E 类地块的产量
        # E 类地块种植一季 CT2 和 一季 CT3
        for i in range(35, 50 + 1):
            for j in range(17, 34 + 1):
                # 地块类型
                area_type = "普通大棚"
                # 按照地块类型area_type和作物编号，在 data4 中匹配到亩产量
                yield_per_area = data4.loc[
                    (data4['地块类型'] == area_type) &
                    (data4['种植季次'] == '第一季') &
                    (data4['作物编号'] == j),
                    '亩产量/斤'].values[0]
                # 累计产量
                total_yield_1[j - 1] += yield_per_area * x[f"AreaOne{i}_{j}"]
                # 累计地块种植面积
                crop_area_1[i - 1] += x[f"AreaOne{i}_{j}"]
            for j in range(38, 41 + 1):
                # 地块类型
                area_type = "普通大棚"
                # 按照地块类型area_type和作物编号，在 data4 中匹配到亩产量
                yield_per_area = data4.loc[
                    (data4['地块类型'] == area_type) &
                    (data4['种植季次'] == '第二季') &
                    (data4['作物编号'] == j),
                    '亩产量/斤'].values[0]
                # 累计产量
                total_yield_2[j - 1] += yield_per_area * x[f"AreaTwo{i}_{j}"]
                # 累计地块种植面积
                crop_area_2[i - 1] += x[f"AreaTwo{i}_{j}"]

        # 统计 F 类地块的产量
        # F 类地块种植两季 CT2
        for i in range(51, 54 + 1):
            for j in range(17, 34 + 1):
                # 地块类型，数据中说明：第一季智慧大棚同普通大棚
                area_type = "普通大棚"
                # 按照地块类型area_type和作物编号，在 data4 中匹配到亩产量
                yield_per_area = data4.loc[
                    (data4['地块类型'] == area_type) &
                    (data4['种植季次'] == '第一季') &
                    (data4['作物编号'] == j),
                    '亩产量/斤'].values[0]
                # 累计产量
                total_yield_1[j - 1] += yield_per_area * x[f"AreaOne{i}_{j}"]
                # 累计地块种植面积
                crop_area_1[i - 1] += x[f"AreaOne{i}_{j}"]

                # 地块类型
                area_type = "智慧大棚"
                # 按照地块类型area_type和作物编号，在 data4 中匹配到亩产量
                yield_per_area = data4.loc[
                    (data4['地块类型'] == area_type) &
                    (data4['种植季次'] == '第二季') &
                    (data4['作物编号'] == j),
                    '亩产量/斤'].values[0]
                # 累计产量
                total_yield_2[j - 1] += yield_per_area * x[f"AreaTwo{i}_{j}"]
                # 累计地块种植面积
                crop_area_2[i - 1] += x[f"AreaTwo{i}_{j}"]

        total_yield = pd.DataFrame({
            "第一季": total_yield_1,
            "第二季": total_yield_2,
            "单季": total_yield_3})

        crop_area = pd.DataFrame({
            "第一季": crop_area_1,
            "第二季": crop_area_2,
            "单季": crop_area_3})

        ## 获取需求量
        demand = data5[['第一季', '第二季', '单季']]

        ## 获取销售单价
        price = data6[['第一季', '第二季', '单季']]

        ## 计算产量超出部分，将小于 0 的值置为 0
        over_yield = total_yield - demand
        over_yield[over_yield < 0] = 0

        ## 将 total_yield 超出 demand 的部分转为 demand
        sale_yield = total_yield - over_yield

        ## 计算总收益
        # 情况一：超出部分全部浪费，卖不出去
        # income = sale_yield * price
        # 情况二：超出部分半价卖
        income = sale_yield * price + over_yield * price * 0.5

        ## 定义约束条件，种植面积 - 地块面积 < 0
        # 获取地块面积
        plot_area = data1['地块面积/亩'].to_list()
        # 每个地块的种植面积
        crop_area
        # 生成不等式约束
        g = [0] * 54 * 3
        for i in range(54):
            for j in range(3):
                g[i * 3 + j] = crop_area.iloc[i, j] - plot_area[i]
        # 输出结果
        out["F"] = -income.sum(axis=1).sum()
        out["G"] = g


if __name__ == "__main__":
    # 实例化问题
    problem = MyProblem()
    # 初始化种群，并将 init_pop 中的值改为 0
    init_pop: dict = deepcopy(problem.vars)
    for i in init_pop.keys():
        init_pop[i] = 0
    # 实例化算法
    algorithm = MixedVariableGA(pop_size=5)
    # 实例化算法终止条件
    termination = get_termination("n_gen", 10)
    # 启动优化
    res = minimize(
        problem,
        algorithm,
        termination,
        seed=1,
        save_history=False,
        verbose=True
    )
    # 获取优化结果
    X = res.X
    F = res.F
    print(F)
