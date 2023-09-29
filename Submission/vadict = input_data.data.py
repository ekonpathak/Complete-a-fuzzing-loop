vadict = input_data.data
        l = len(vadict)
        list1 = []
        condict = []
        print("****************")
        print(input_data.id)
        print(input_data.data)
        print(coverageInfo.curr_metric)
        for j in coverageInfo.total_metric[::-1]:
            print(j)
            if j >= len(irList):
                continue
            i = irList[j]
            print(i)
            if isinstance(i[0],kachuaAST.ConditionCommand):
                condict.append(i[0].cond)
                if type(i[0].cond) == LT:
                #     print("yes")
                #     print(i[0].cond.lexpr)
                #     print(type(i[0].cond.rexpr.val))
                #     print(type(input_data.data[str(i[0].cond.lexpr)]))
                        print(i[0].cond.lexpr)
                        if input_data.data[str(i[0].cond.lexpr)] < i[0].cond.rexpr.val:
                            input_data.data[str(i[0].cond.lexpr)] = i[0].cond.rexpr.val + randint(10,100)
                        else:
                            input_data.data[str(i[0].cond.lexpr)] = i[0].cond.rexpr.val - randint(1,i[0].cond.rexpr.val)  
                             
        print(input_data.id)
        print(input_data.data)   
         # for i in range (l):
        #     x = randint(0,100)
        #     list1.append(x)
        # vadict = dict(zip(list(vadict.keys()), list1))
        # print(" ** this is input data **")
        # input_data.data = vadict