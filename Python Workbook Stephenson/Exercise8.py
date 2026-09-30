widget_num=int(input("Enter the number of widgets: "))
gizmos_num=int(input("Enter the number of Gizmos: "))

one_widget_weight=75  #weight in grams
one_gizmos_weight=112 #weight in grams

#computation of the weights
Total_weight_widget=widget_num*one_widget_weight
Total_weight_gizmos=gizmos_num*one_gizmos_weight
total_weight=Total_weight_widget+Total_weight_gizmos

#output
print(f"Total weight of the order: {total_weight:.2f} grams")

