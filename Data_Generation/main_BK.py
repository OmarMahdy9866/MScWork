import itertools
import math
import os.path
import re
import subprocess

import pandas as pd
from tqdm import tqdm


def main_loop(H, B, q, R_int, gamma, Su, base_, i):
    base_folder = os.path.join(os.getcwd(), 'ParametricStudy', f'run_{i}_{base_}')
    os.makedirs(base_folder, exist_ok=True)

    input_file = os.path.join(base_folder, 'Input.g2x')
    output_file = os.path.join(base_folder, 'Output_Results.g2x')
    log_file = os.path.join(base_folder, 'Run_log.txt')

    with open(base_, 'r') as fd:
        file_lines = fd.read()
        file_lines = file_lines.replace("$H$", str(-H))
        file_lines = file_lines.replace("$B$", str(-B))
        file_lines = file_lines.replace("$q$", str(-q))
        file_lines = file_lines.replace("$Rint$", str(R_int))
        file_lines = file_lines.replace("$gamma$", str(gamma))
        file_lines = file_lines.replace("$Su$", str(Su))

    with open(input_file, 'w+') as fd:
        fd.write(file_lines)

    command = ['optumg2cmd', input_file, f'/output:{output_file}', f'/log:{log_file}']
    p = subprocess.Popen(command, shell=True)
    p.wait()

    with open(log_file, 'r') as fd:
        lines = fd.read()
        rx1 = re.compile(r'BEST STRENGTH REDUCTION FACTOR = \d+\.\d+', re.IGNORECASE)
        rx2 = re.compile(r'\d+\.\d+', re.IGNORECASE)
        return rx2.findall(rx1.findall(lines)[0])[0]


if __name__ == '__main__':
    base_file_lower = 'Base_Model_Param_LowerFELA.g2x'
    base_file_upper = 'Base_Model_Param_UperFELA.g2x'
    output_csv_file = 'output_results.csv'

    H = range(2, 11, 2)
    B = range(2, 21, 2)
    q = range(0, 21, 10)
    R_int = [0.6, 0.8, 1.0]
    gamma = range(14, 19, 2)
    s_u = [25, 50, 75, 100]

    p = [H, B, q, R_int, gamma, s_u]
    possible_combinations = list(itertools.product(*p))

    result = pd.DataFrame(columns=['H', 'B', 'q', 'R_int', 'gamma', 'Su', 'sf_lower', 'sf_upper'])
    with tqdm(total=len(possible_combinations)) as bar:
        for i, combination in enumerate(possible_combinations):
            sf_l = main_loop(*combination, base_file_lower, i)
            sf_u = main_loop(*combination, base_file_upper, i)

            result.loc[-1] = [*combination, sf_l, sf_u]
            result.index = result.index + 1
            result = result.sort_index()

            result.to_csv(output_csv_file)
            bar.update(1)
            print(f"########### Combination No. {i} ###########")
            print(
                f"B = {combination[0]}, H = {combination[1]}, q = {combination[2]}, R_int = {combination[3]},"
                f" Unit Weight = {combination[4]}, Su = {combination[5]}")
            print(f"SF_L:{sf_l} & SF_U:{sf_u}")
            print("_______________________________________________")

    print(result)
