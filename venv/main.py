"""
Created on Mon Jan 22 00:55:42 2018

@author: kyle
node.py 里面含有算法里需要用到的所有滤波器
node_visitor.py 里面导入了node.py,然后完成了非递归访问者模式的实现
tree.py 里面包含了由字符串到表达式树的实现过程
"""
from node_visitor import Evaluator
from tree import Tree

if __name__ == "__main__":
    test_string = "*-+1/111+11111111111111"
    test_tree = Tree(test_string)

    e = Evaluator()
    print(e.visit(test_tree.root))
