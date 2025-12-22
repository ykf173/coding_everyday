# 给你一个长度为 n 的字符串数组 names 。你将会在文件系统中创建 n 个文件夹：在第 i 分钟，新建名为 names[i] 的文件夹。
#
# 由于两个文件 不能 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，系统会以 (k) 的形式为新文件夹的文件名添加后缀，其中 k 是能保证文件名唯一的 最小正整数 。
#
# 返回长度为 n 的字符串数组，其中 ans[i] 是创建第 i 个文件夹时系统分配给该文件夹的实际名称。
# 
# 示例 1：
# 
# 输入：names = ["pes","fifa","gta","pes(2019)"]
# 输出：["pes","fifa","gta","pes(2019)"]
# 解释：文件系统将会这样创建文件名：
# "pes" --> 之前未分配，仍为 "pes"
# "fifa" --> 之前未分配，仍为 "fifa"
# "gta" --> 之前未分配，仍为 "gta"
# "pes(2019)" --> 之前未分配，仍为 "pes(2019)"
# 示例 2：
# 
# 输入：names = ["gta","gta(1)","gta","avalon"]
# 输出：["gta","gta(1)","gta(2)","avalon"]
# 解释：文件系统将会这样创建文件名：
# "gta" --> 之前未分配，仍为 "gta"
# "gta(1)" --> 之前未分配，仍为 "gta(1)"
# "gta" --> 文件名被占用，系统为该名称添加后缀 (k)，由于 "gta(1)" 也被占用，所以 k = 2 。实际创建的文件名为 "gta(2)" 。
# "avalon" --> 之前未分配，仍为 "avalon"
# 示例 3：
# 
# 输入：names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
# 输出：["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
# 解释：当创建最后一个文件夹时，最小的正有效 k 为 4 ，文件名变为 "onepiece(4)"。
# 示例 4：
# 
# 输入：names = ["wano","wano","wano","wano"]
# 输出：["wano","wano(1)","wano(2)","wano(3)"]
# 解释：每次创建文件夹 "wano" 时，只需增加后缀中 k 的值即可。
# 示例 5：
# 
# 输入：names = ["kaido","kaido(1)","kaido","kaido(1)"]
# 输出：["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
# 解释：注意，如果含后缀文件名被占用，那么系统也会按规则在名称后添加新的后缀 (k) 。
#  
# 
# 提示：
# 
# 1 <= names.length <= 5 * 10^4
# 1 <= names[i].length <= 20
# names[i] 由小写英文字母、数字和/或圆括号组成。
import re
from collections import defaultdict
from typing import List


class treeNode:
    def __init__(self, val, folders=None):
        self.val = val
        self.children = folders


class Solution:
    pattern = r'(\d{1})'

    def update(self, dir, children):
        di = dir[-3:]
        isexobj = re.search(self.pattern, di)
        if isexobj and int(dir[-2]):
            children[dir[:-3]].add(int(dir[-2]))
        return children

    def writeFolderPath(self, dir, cur_node, all_path):
        new_node = treeNode(dir, defaultdict(set))
        if dir not in set(cur_node.children):
            cur_node.children[dir].add(-1)
            all_path.append(dir)
        else:
            max_v = max(cur_node.children[dir])
            if max_v != len(cur_node.children[dir]) - 1:
                v = min(set(list(range(-1, max_v))) - set(cur_node.children[dir]) - {0}) if max_v not in [0, -1] else 1
            else:
                v = max_v + 1
            value = f"{dir}({v})" if v not in [-1, 0] else dir
            all_path.append(value)
            new_node.val = value
            cur_node.children[dir].add(v)
            cur_node.children[value].add(-1)
        if len(dir) > 3:
            cur_node.children = self.update(dir, cur_node.children)

    def getFolderNames2(self, names: List[str]) -> List[str]:
        all_folders = []
        root = treeNode(None, defaultdict(set))
        for name in names:
            self.writeFolderPath(name, root, all_folders)

        return all_folders

    def getFolderNames(self, names: List[str]) -> List[str]:
        all_folders = []
        index = {}
        for name in names:
            index_set = set(index.keys())
            if name not in index_set:
                all_folders.append(name)
                index[name] = 1
            else:
                k = index[name]
                while f'{name}({k})' in index_set:
                    k += 1

                index[name] = k
                all_folders.append(f'{name}({k})')
                index[f'{name}({k})'] = 1

        return all_folders


if __name__ == '__main__':
    namess = [
        # ["pes", "fifa", "gta", "pes(2019)"],
        ["gta", "gta(1)", "gta", "avalon"],
        ["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"],
        ["wano", "wano", "wano", "wano"],
        ["kaido", "kaido(1)", "kaido", "kaido(1)"],
        ["kaido(4)", "kaido(3)", "kaido", "kaido(1)", "kaido"],
        ["kaido", "kaido(1)", "kaido", "kaido(1)", "kaido(2)"],
        ["kingston(0)", "kingston", "kingston"],
        ["kaido(4)/kaido", "kaido(3)/kaido", "kaido/kaido(2)", "kaido(1)/kaido(3)", "kaido/kaido", 'kaido(3)/kaido'],
        ["e", "g", "s(4)(2)", "a", "u", "b(2)", "s(2)", "h(2)", "g", "s", "h", "d", "v", "a(2)", "a", "s(4)", "y", "c",
         "l(1)(4)", "q", "m", "z", "j", "u", "b", "x", "n", "e", "m(1)(3)", "b", "n(1)(3)", "f", "n", "j", "e", "v",
         "d(1)", "e", "v(2)(4)", "c", "f", "v", "i", "p", "i(4)", "f", "k", "n", "c", "u"]
    ]

    s = Solution()
    for names in namess:
        print(names)
        print(s.getFolderNames(names))
        print('*' * 80)
