class ListSum:

    def __init__(self, input_list):
        self.terms_list = input_list

    def stampa(self):
        for index, x in enumerate(self.terms_list):
            print("l'elemento {} è {} : {}".format(index, x[0], x[1]))



    def addList(self,new_list):

        distinct_elem_list = [] #temporary list in which saves the new synonysm

        for new_elem in new_list:

            insert_flag = 0

            for index, old_elem in enumerate(self.terms_list):

                if (new_elem[0] == old_elem[0]):

                    temp = new_elem[1] + old_elem[1]
                    self.terms_list[index] = (old_elem[0],temp)
                    insert_flag = 1

            if (insert_flag==0):

                 distinct_elem_list.append(new_elem)

        self.terms_list.extend(distinct_elem_list)

    def takeSecond(self, elem):
        return elem[1]

    def orderList(self):
        self.terms_list.sort(key=self.takeSecond, reverse=True)


