\* Minimum Cost Steiner Tree *\
Minimize
Sum_of_edge_costs: x_e(1,_2) + x_e(2,_3) + x_e(3,_4) + x_e(4,_5) + x_e(1,_5)
Subject To
No_Contraditory_Flows_from_n1_and_from_n2_over_e(1,_2): - x_e(1,_2)
 + f_n1_e(1,_2) + f_n2_e(2,_1) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(1,_5): - x_e(1,_5)
 + f_n1_e(1,_5) + f_n2_e(5,_1) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(2,_3): - x_e(2,_3)
 + f_n1_e(2,_3) + f_n2_e(3,_2) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(3,_4): - x_e(3,_4)
 + f_n1_e(3,_4) + f_n2_e(4,_3) <= 0
No_Contraditory_Flows_from_n1_and_from_n2_over_e(4,_5): - x_e(4,_5)
 + f_n1_e(4,_5) + f_n2_e(5,_4) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(1,_2): - x_e(1,_2)
 + f_n1_e(2,_1) + f_n2_e(1,_2) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(1,_5): - x_e(1,_5)
 + f_n1_e(5,_1) + f_n2_e(1,_5) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(2,_3): - x_e(2,_3)
 + f_n1_e(3,_2) + f_n2_e(2,_3) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(3,_4): - x_e(3,_4)
 + f_n1_e(4,_3) + f_n2_e(3,_4) <= 0
No_Contraditory_Flows_from_n2_and_from_n1_over_e(4,_5): - x_e(4,_5)
 + f_n1_e(5,_4) + f_n2_e(4,_5) <= 0
Sum_of_Flow_n1_on_node_n0:0 = 0
Sum_of_Flow_n1_on_node_n1: f_n1_e(1,_2) - f_n1_e(2,_1) + f_n1_e(1,_5)
 - f_n1_e(5,_1) = 1
Sum_of_Flow_n1_on_node_n2: - f_n1_e(1,_2) + f_n1_e(2,_1) + f_n1_e(2,_3)
 - f_n1_e(3,_2) = 0
Sum_of_Flow_n1_on_node_n3: - f_n1_e(2,_3) + f_n1_e(3,_2) + f_n1_e(3,_4)
 - f_n1_e(4,_3) = -2
Sum_of_Flow_n1_on_node_n4: - f_n1_e(3,_4) + f_n1_e(4,_3) + f_n1_e(4,_5)
 - f_n1_e(5,_4) = 0
Sum_of_Flow_n1_on_node_n5: - f_n1_e(4,_5) + f_n1_e(5,_4) - f_n1_e(1,_5)
 + f_n1_e(5,_1) = 0
Sum_of_Flow_n1_on_node_n6:0 = 0
Sum_of_Flow_n1_on_node_n7:0 = 0
Sum_of_Flow_n1_on_node_n8:0 = 0
Sum_of_Flow_n1_on_node_n9:0 = 0
Sum_of_Flow_n2_on_node_n0:0 = 0
Sum_of_Flow_n2_on_node_n1: f_n2_e(1,_2) - f_n2_e(2,_1) + f_n2_e(1,_5)
 - f_n2_e(5,_1) = 0
Sum_of_Flow_n2_on_node_n2: - f_n2_e(1,_2) + f_n2_e(2,_1) + f_n2_e(2,_3)
 - f_n2_e(3,_2) = 1
Sum_of_Flow_n2_on_node_n3: - f_n2_e(2,_3) + f_n2_e(3,_2) + f_n2_e(3,_4)
 - f_n2_e(4,_3) = -2
Sum_of_Flow_n2_on_node_n4: - f_n2_e(3,_4) + f_n2_e(4,_3) + f_n2_e(4,_5)
 - f_n2_e(5,_4) = 0
Sum_of_Flow_n2_on_node_n5: - f_n2_e(4,_5) + f_n2_e(5,_4) - f_n2_e(1,_5)
 + f_n2_e(5,_1) = 0
Sum_of_Flow_n2_on_node_n6:0 = 0
Sum_of_Flow_n2_on_node_n7:0 = 0
Sum_of_Flow_n2_on_node_n8:0 = 0
Sum_of_Flow_n2_on_node_n9:0 = 0
Binaries
x_e(1,_2)
x_e(2,_3)
x_e(3,_4)
x_e(4,_5)
x_e(1,_5)
End
