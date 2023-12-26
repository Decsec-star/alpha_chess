max_depth = 4
# 最大值，最小值
max_val = 1000000
min_val = -1000000
# 评估方法
            #空， 兵， 仕， 马， 象， 炮， 车， 将
base_val = [0, 80, 200, 250, 300, 500, 700, 10000]
mobile_val = [0, 15, 1, 1, 12, 6, 6, 0]
pos_val = [
    [  # 空
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0
    ],
    [  # 兵
        5,15,25,35,45,35,25,15,5,
        20,30,50,65,70,65,50,30,20,
        20,30,45,55,55,55,45,30,20,
        20,27,30,40,42,40,30,27,20,
        10,18,22,35,40,35,22,18,10,
        3,0,4,0,7,0,4,0,3,
        -2,0,-2,0,-2,0,-2,0,-2,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0
    ],
    [  # 士
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,3,0,0,0,0,
        0,0,0,0,0,0,0,0,0
    ],
    [  # 相
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        -2,0,0,0,3,0,0,0,-2,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0
    ],
    [  # 马
        2,2,2,8,2,8,2,2,2,
        2,8,15,9,6,9,15,8,2,
        4,10,11,15,11,15,11,10,4,
        5,20,12,19,12,19,12,20,5,
        2,12,11,15,16,15,11,12,2,
        2,10,13,14,15,14,13,10,2,
        4,6,10,7,10,7,10,6,4,
        5,4,6,7,4,7,6,4,5,
        -3,2,4,5,-10,5,4,2,-3,
        0,-3,2,0,2,0,2,-3,0,
    ],
[  # 炮
        4,4,0,-5,-6,-5,0,4,4,
        2,2,0,-4,-7,-4,0,2,2,
        1,1,0,-5,-4,-5,0,1,1,
        0,3,3,2,4,2,3,3,0,
        0,0,0,0,4,0,0,0,0,
        -1,0,3,0,4,0,3,0,-1,
        0,0,0,0,0,0,0,0,0,
        1,0,5,3,5,3,5,0,1,
        0,1,2,2,2,2,2,1,0,
        0,0,1,3,3,3,1,0,0,
    ],
[  # 车
        6,8,7,15,30,15,7,8,6,
        6,12,9,20,40,20,9,12,6,
        6,8,7,14,20,14,7,8,6,
        6,13,13,16,20,16,13,13,6,
        8,11,11,14,15,14,11,11,8,
        8,12,12,14,15,14,12,12,8,
        4,9,4,12,14,12,4,9,4,
        -2,8,4,12,12,12,4,8,-2,
        5,8,6,12,0,12,6,8,5,
        -8,6,4,12,0,12,4,6,-8,
    ],
    [  # 将
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,-9,-9,-9,0,0,0,
        0,0,0,-8,-8,-8,0,0,0,
        0,0,0,1,5,1,0,0,0
    ]
]