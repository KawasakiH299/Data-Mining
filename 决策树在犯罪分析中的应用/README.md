#### 本项目用于实现并绘制决策树
##### 项目逻辑并不复杂，但为了将函数式编程和面向对象编程的一些知识实例化，并为了积累一些简单的开发经验，而将代码实现倾向于项目
- 在函数式中：yield *args **kwargs cls try
- 面向对象中主要是测试包和模块，以及一些简单的接口的实现

##### 该项目通过两个包实现，create_data包主要功能时利用自动化将数据写入excel，create_tree包主要是训练并绘制决策树
- create_data包
  - wirteda模块
    - xlsxwriter写入excel
  - test_yield模块
    - 用于xlsxwriter写入测试，对项目实现不具有实际贡献


- create_tree包 
  - decision_onehot模块
    - 简单决策树的实现
  - become_onehot模块
    - decision_onehot模块的接口化
    - sk_tree()方法用与训练决策树模型
    - clf_plot()用于绘出完全决策树
  - Onehot 模块
    - 采用onehot方法，将特征变换为热编码数据
  - main模块
    - 对总个项目接口的调用
  - onedata模块 
    - 读入数据并转化为热编码测试模块，对项目实现不具有实际贡献
