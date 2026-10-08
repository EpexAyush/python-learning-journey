class list:

    def count(self,list_count):
        self.list_count=list_count
        count=0
        total_1=0
        total_2=0
        for num in self.list_count:
            count+=1
            if type(num)==str:
                total_1+=1
            else:
                total_2+=1
        return f'''
1. Total items in the list: {count}
2. Total strings values: {total_1}
3. total integar values: {total_2}
'''

c1=list()
print(c1.count(["Ayush","Subhash",10,30,"Divyanshu","10"]))






