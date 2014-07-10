\* Maior Lucro *\
Maximize
Sum_of_profit_of_vms: 86 x_vm1_s1 + 86 x_vm1_s2 + 79 x_vm2_s1 + 79 x_vm2_s2
 + 23 x_vm3_s1 + 23 x_vm3_s2 + 26 x_vm4_s1 + 26 x_vm4_s2 + 79 x_vm5_s1
 + 79 x_vm5_s2 + 44 x_vm6_s1 + 44 x_vm6_s2 + 29 x_vm7_s1 + 29 x_vm7_s2
 + 87 x_vm8_s1 + 87 x_vm8_s2 + 20 x_vm9_s1 + 20 x_vm9_s2 + 31 x_vm10_s1
 + 31 x_vm10_s2
Subject To
Allocation_Constraint_of_VM_vm1: x_vm1_s1 + x_vm1_s2 <= 1
Allocation_Constraint_of_VM_vm10: x_vm10_s1 + x_vm10_s2 <= 1
Allocation_Constraint_of_VM_vm2: x_vm2_s1 + x_vm2_s2 <= 1
Allocation_Constraint_of_VM_vm3: x_vm3_s1 + x_vm3_s2 <= 1
Allocation_Constraint_of_VM_vm4: x_vm4_s1 + x_vm4_s2 <= 1
Allocation_Constraint_of_VM_vm5: x_vm5_s1 + x_vm5_s2 <= 1
Allocation_Constraint_of_VM_vm6: x_vm6_s1 + x_vm6_s2 <= 1
Allocation_Constraint_of_VM_vm7: x_vm7_s1 + x_vm7_s2 <= 1
Allocation_Constraint_of_VM_vm8: x_vm8_s1 + x_vm8_s2 <= 1
Allocation_Constraint_of_VM_vm9: x_vm9_s1 + x_vm9_s2 <= 1
Sum_of_VM_demands_on_Server_s1: 40 x_vm1_s1 + 17 x_vm2_s1 + 20 x_vm3_s1
 + 47 x_vm4_s1 + 13 x_vm5_s1 + 40 x_vm6_s1 + 19 x_vm7_s1 + 27 x_vm8_s1
 + 26 x_vm9_s1 + 37 x_vm10_s1 <= 43
Sum_of_VM_demands_on_Server_s2: 40 x_vm1_s2 + 17 x_vm2_s2 + 20 x_vm3_s2
 + 47 x_vm4_s2 + 13 x_vm5_s2 + 40 x_vm6_s2 + 19 x_vm7_s2 + 27 x_vm8_s2
 + 26 x_vm9_s2 + 37 x_vm10_s2 <= 50
Binaries
x_vm1_s1
x_vm1_s2
x_vm2_s1
x_vm2_s2
x_vm3_s1
x_vm3_s2
x_vm4_s1
x_vm5_s2
x_vm6_s1
x_vm5_s1
x_vm6_s2
x_vm4_s2
x_vm7_s1
x_vm7_s2
x_vm8_s1
x_vm8_s2
x_vm9_s1
x_vm9_s2
x_vm10_s1
x_vm10_s2
End
