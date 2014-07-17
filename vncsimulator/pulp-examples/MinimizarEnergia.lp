\* Minimize Energy *\
Maximize
Total_Profit: 50 x_vm1_s1 + 50 x_vm1_s2 + 37 x_vm2_s1 + 37 x_vm2_s2
 + 48 x_vm3_s1 + 48 x_vm3_s2 + 30 x_vm4_s1 + 30 x_vm4_s2 + 23 x_vm5_s1
 + 23 x_vm5_s2 - 80 y_s1 - 69 y_s2
Subject To
Allocation_Constraint_of_VM_vm1: x_vm1_s1 + x_vm1_s2 <= 1
Allocation_Constraint_of_VM_vm2: x_vm2_s1 + x_vm2_s2 <= 1
Allocation_Constraint_of_VM_vm3: x_vm3_s1 + x_vm3_s2 <= 1
Allocation_Constraint_of_VM_vm4: x_vm4_s1 + x_vm4_s2 <= 1
Allocation_Constraint_of_VM_vm5: x_vm5_s1 + x_vm5_s2 <= 1
Sum_of_VM_demands_on_Server_s1: 25 x_vm1_s1 + 27 x_vm2_s1 + 49 x_vm3_s1
 + 35 x_vm4_s1 + 14 x_vm5_s1 - 44 y_s1 <= 0
Sum_of_VM_demands_on_Server_s2: 25 x_vm1_s2 + 27 x_vm2_s2 + 49 x_vm3_s2
 + 35 x_vm4_s2 + 14 x_vm5_s2 - 45 y_s2 <= 0
Binaries
x_vm1_s1
y_s1
x_vm1_s2
x_vm2_s1
x_vm2_s2
x_vm3_s1
x_vm3_s2
x_vm4_s1
x_vm5_s2
y_s2
x_vm5_s1
x_vm4_s2
End
