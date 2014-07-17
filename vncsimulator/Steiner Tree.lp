\* Minimum Cost Steiner Tree *\
Minimize
Sum_of_edge_costs: x_e(0,_1) + x_e(0,_2) + x_e(1,_2) + x_e(1,_3) + x_e(1,_4)
 + x_e(2,_5) + x_e(2,_6) + x_e(3,_4) + x_e(4,_5) + x_e(4,_8) + x_e(5,_6)
 + x_e(5,_7) + x_e(5,_8) + x_e(6,_7) + x_e(7,_8) + x_e(8,_9) + x_e(3,_9)
Subject To
No_Contraditory_Flows_from_n1_and_from_n2_over_e(0,_1): f_n1_e(0,_1)
 + f_n2_e(1,_0) - x_e(0,_1) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(0,_2): f_n1_e(0,_2)
 + f_n2_e(2,_0) - x_e(0,_2) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(1,_2): f_n1_e(1,_2)
 + f_n2_e(2,_1) - x_e(1,_2) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(1,_3): f_n1_e(1,_3)
 + f_n2_e(3,_1) - x_e(1,_3) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(1,_4): f_n1_e(1,_4)
 + f_n2_e(4,_1) - x_e(1,_4) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(2,_5): f_n1_e(2,_5)
 + f_n2_e(5,_2) - x_e(2,_5) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(2,_6): f_n1_e(2,_6)
 + f_n2_e(6,_2) - x_e(2,_6) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(3,_4): f_n1_e(3,_4)
 + f_n2_e(4,_3) - x_e(3,_4) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(3,_9): f_n1_e(3,_9)
 + f_n2_e(9,_3) - x_e(3,_9) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(4,_5): f_n1_e(4,_5)
 + f_n2_e(5,_4) - x_e(4,_5) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(4,_8): f_n1_e(4,_8)
 + f_n2_e(8,_4) - x_e(4,_8) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(5,_6): f_n1_e(5,_6)
 + f_n2_e(6,_5) - x_e(5,_6) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(5,_7): f_n1_e(5,_7)
 + f_n2_e(7,_5) - x_e(5,_7) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(5,_8): f_n1_e(5,_8)
 + f_n2_e(8,_5) - x_e(5,_8) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(6,_7): f_n1_e(6,_7)
 + f_n2_e(7,_6) - x_e(6,_7) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(7,_8): f_n1_e(7,_8)
 + f_n2_e(8,_7) - x_e(7,_8) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(8,_9): f_n1_e(8,_9)
 + f_n2_e(9,_8) - x_e(8,_9) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(0,_1): f_n2_e(0,_1)
 + f_n1_e(1,_0) - x_e(0,_1) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(0,_2): f_n2_e(0,_2)
 + f_n1_e(2,_0) - x_e(0,_2) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(1,_2): f_n2_e(1,_2)
 + f_n1_e(2,_1) - x_e(1,_2) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(1,_3): f_n2_e(1,_3)
 + f_n1_e(3,_1) - x_e(1,_3) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(1,_4): f_n2_e(1,_4)
 + f_n1_e(4,_1) - x_e(1,_4) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(2,_5): f_n2_e(2,_5)
 + f_n1_e(5,_2) - x_e(2,_5) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(2,_6): f_n2_e(2,_6)
 + f_n1_e(6,_2) - x_e(2,_6) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(3,_4): f_n2_e(3,_4)
 + f_n1_e(4,_3) - x_e(3,_4) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(3,_9): f_n2_e(3,_9)
 + f_n1_e(9,_3) - x_e(3,_9) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(4,_5): f_n2_e(4,_5)
 + f_n1_e(5,_4) - x_e(4,_5) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(4,_8): f_n2_e(4,_8)
 + f_n1_e(8,_4) - x_e(4,_8) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(5,_6): f_n2_e(5,_6)
 + f_n1_e(6,_5) - x_e(5,_6) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(5,_7): f_n2_e(5,_7)
 + f_n1_e(7,_5) - x_e(5,_7) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(5,_8): f_n2_e(5,_8)
 + f_n1_e(8,_5) - x_e(5,_8) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(6,_7): f_n2_e(6,_7)
 + f_n1_e(7,_6) - x_e(6,_7) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(7,_8): f_n2_e(7,_8)
 + f_n1_e(8,_7) - x_e(7,_8) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(8,_9): f_n2_e(8,_9)
 + f_n1_e(9,_8) - x_e(8,_9) <= 0
Sum_of_Flow_n1_on_node_n0: f_n1_e(0,_1) + f_n1_e(0,_2) - f_n1_e(1,_0)
 - f_n1_e(2,_0) = 0
Sum_of_Flow_n1_on_node_n1: f_n1_e(1,_0) + f_n1_e(1,_2) + f_n1_e(1,_3)
 + f_n1_e(1,_4) - f_n1_e(0,_1) - f_n1_e(2,_1) - f_n1_e(3,_1) - f_n1_e(4,_1)
 = 1
Sum_of_Flow_n1_on_node_n2: f_n1_e(2,_0) + f_n1_e(2,_1) + f_n1_e(2,_5)
 + f_n1_e(2,_6) - f_n1_e(0,_2) - f_n1_e(1,_2) - f_n1_e(5,_2) - f_n1_e(6,_2)
 = 0
Sum_of_Flow_n1_on_node_n3: f_n1_e(3,_1) + f_n1_e(3,_4) + f_n1_e(3,_9)
 - f_n1_e(1,_3) - f_n1_e(4,_3) - f_n1_e(9,_3) = -2
Sum_of_Flow_n1_on_node_n4: f_n1_e(4,_1) + f_n1_e(4,_3) + f_n1_e(4,_5)
 + f_n1_e(4,_8) - f_n1_e(1,_4) - f_n1_e(3,_4) - f_n1_e(5,_4) - f_n1_e(8,_4)
 = 0
Sum_of_Flow_n1_on_node_n5: f_n1_e(5,_2) + f_n1_e(5,_4) + f_n1_e(5,_6)
 + f_n1_e(5,_7) + f_n1_e(5,_8) - f_n1_e(2,_5) - f_n1_e(4,_5) - f_n1_e(6,_5)
 - f_n1_e(7,_5) - f_n1_e(8,_5) = 0
Sum_of_Flow_n1_on_node_n6: f_n1_e(6,_2) + f_n1_e(6,_5) + f_n1_e(6,_7)
 - f_n1_e(2,_6) - f_n1_e(5,_6) - f_n1_e(7,_6) = 0
Sum_of_Flow_n1_on_node_n7: f_n1_e(7,_5) + f_n1_e(7,_6) + f_n1_e(7,_8)
 - f_n1_e(5,_7) - f_n1_e(6,_7) - f_n1_e(8,_7) = 0
Sum_of_Flow_n1_on_node_n8: f_n1_e(8,_4) + f_n1_e(8,_5) + f_n1_e(8,_7)
 + f_n1_e(8,_9) - f_n1_e(4,_8) - f_n1_e(5,_8) - f_n1_e(7,_8) - f_n1_e(9,_8)
 = 0
Sum_of_Flow_n1_on_node_n9: f_n1_e(9,_8) + f_n1_e(9,_3) - f_n1_e(8,_9)
 - f_n1_e(3,_9) = 0
Sum_of_Flow_n2_on_node_n0: f_n2_e(0,_1) + f_n2_e(0,_2) - f_n2_e(1,_0)
 - f_n2_e(2,_0) = 0
Sum_of_Flow_n2_on_node_n1: f_n2_e(1,_0) + f_n2_e(1,_2) + f_n2_e(1,_3)
 + f_n2_e(1,_4) - f_n2_e(0,_1) - f_n2_e(2,_1) - f_n2_e(3,_1) - f_n2_e(4,_1)
 = 0
Sum_of_Flow_n2_on_node_n2: f_n2_e(2,_0) + f_n2_e(2,_1) + f_n2_e(2,_5)
 + f_n2_e(2,_6) - f_n2_e(0,_2) - f_n2_e(1,_2) - f_n2_e(5,_2) - f_n2_e(6,_2)
 = 1
Sum_of_Flow_n2_on_node_n3: f_n2_e(3,_1) + f_n2_e(3,_4) + f_n2_e(3,_9)
 - f_n2_e(1,_3) - f_n2_e(4,_3) - f_n2_e(9,_3) = -2
Sum_of_Flow_n2_on_node_n4: f_n2_e(4,_1) + f_n2_e(4,_3) + f_n2_e(4,_5)
 + f_n2_e(4,_8) - f_n2_e(1,_4) - f_n2_e(3,_4) - f_n2_e(5,_4) - f_n2_e(8,_4)
 = 0
Sum_of_Flow_n2_on_node_n5: f_n2_e(5,_2) + f_n2_e(5,_4) + f_n2_e(5,_6)
 + f_n2_e(5,_7) + f_n2_e(5,_8) - f_n2_e(2,_5) - f_n2_e(4,_5) - f_n2_e(6,_5)
 - f_n2_e(7,_5) - f_n2_e(8,_5) = 0
Sum_of_Flow_n2_on_node_n6: f_n2_e(6,_2) + f_n2_e(6,_5) + f_n2_e(6,_7)
 - f_n2_e(2,_6) - f_n2_e(5,_6) - f_n2_e(7,_6) = 0
Sum_of_Flow_n2_on_node_n7: f_n2_e(7,_5) + f_n2_e(7,_6) + f_n2_e(7,_8)
 - f_n2_e(5,_7) - f_n2_e(6,_7) - f_n2_e(8,_7) = 0
Sum_of_Flow_n2_on_node_n8: f_n2_e(8,_4) + f_n2_e(8,_5) + f_n2_e(8,_7)
 + f_n2_e(8,_9) - f_n2_e(4,_8) - f_n2_e(5,_8) - f_n2_e(7,_8) - f_n2_e(9,_8)
 = 0
Sum_of_Flow_n2_on_node_n9: f_n2_e(9,_8) + f_n2_e(9,_3) - f_n2_e(8,_9)
 - f_n2_e(3,_9) = 0
_C1: x_e(1,_2) = 1
_C2: x_e(1,_3) = 1
_C3: f_n1_e(1,_3) = 1
_C4: f_n2_e(2,_1) = 1
_C5: f_n2_e(1,_3) = 1
Binaries
x_e(0,_2)
x_e(0,_1)
x_e(1,_2)
x_e(1,_3)
x_e(1,_4)
x_e(2,_5)
x_e(2,_6)
x_e(3,_4)
x_e(5,_6)
x_e(5,_7)
x_e(4,_8)
x_e(5,_8)
x_e(4,_5)
x_e(6,_7)
x_e(7,_8)
x_e(8,_9)
x_e(3,_9)
End
