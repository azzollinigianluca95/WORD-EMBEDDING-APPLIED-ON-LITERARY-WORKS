import os
import subprocess
from tkinter import *
import tkinter.messagebox



class TextPreProcessing:

    def __init__(self, path):

        self.input_file_path = path

        self.output_file_path = 'temp.txt'

        self.symbol_list = [".", "," , ";" , ":" , "!" , "?", "...", "<", ">", " ' ", " / ", "(" , ")" , "-", "+", "^", "[", "]", "{", "}" , "<" , ">", '"']

    def filter(self):

        file_input = open(self.input_file_path, "r+")
        file_output = open(self.output_file_path, "w")

        stop_words=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

        text = file_input.read() # read file content as a stream:

        lines = text.splitlines() #split text in lines

        # filtering stop words and lowering words

        for line in lines: # for each line in the input text

            filtered_line = ""

            for word in line.split(): # for each words in each line in the input text

                word = word.lower() #lowering words

                for symbol in self.symbol_list:

                    word = word.replace(symbol, "")

                if word not in stop_words:

                    filtered_line = filtered_line + " " + word

            file_output.write(filtered_line + "\n")

        file_input.close()
        file_output.close()



    def lowFilter(self):


        file_input = open(self.input_file_path, "r+")
        file_output = open(self.output_file_path, "w")

        text = file_input.read() # read file content as a stream:

        lines = text.splitlines() #split text in lines

        for line in lines: # for each line in the input text

            filtered_line = ""

            for word in line.split():  # for each words in each line in the input text

                word = word.lower()  # lowering words

                for symbol in self.symbol_list:

                    word = word.replace(symbol, "")


                filtered_line = filtered_line + " " + word

            file_output.write(filtered_line + "\n")

        file_input.close()
        file_output.close()

    def datasetUnion(self, stopwords):

        if (self.input_file_path == 1):

            dataset_list1 = subprocess.check_output("./script1.sh", shell=True).decode("utf-8")

            dataset_list1 = dataset_list1.splitlines()

            if (dataset_list1 == []):

                tkinter.messagebox.showerror("NO DATASET FOUND", "The Classical dataset list is empty!")
                return 0

            else:

                file_classic = open("Classical/classical.txt","w+")
                file_classic.close()

                file_classic = open("Classical/classical.txt","a+")



                if (stopwords==0):

                    for x in dataset_list1:

                        file_a = open("1/" + x, "r+")


                        file_classic.write(file_a.read())

                        file_a.close()

                    file_classic.close()

                if (stopwords==1):

                    for x in dataset_list1:
                        file_a = open("1s/" + x, "r+")

                        file_classic.write(file_a.read())

                        file_a.close()

                    file_classic.close()

                return 1

        if (self.input_file_path == 2):

            dataset_list2 = subprocess.check_output("./script2.sh", shell=True).decode("utf-8")

            dataset_list2 = dataset_list2.splitlines()


            if (dataset_list2 == []):

                tkinter.messagebox.showerror("NO DATASET FOUND", "The Reinassance dataset list is empty!")
                return 0

            else:

                file_classic = open("Renaissance/renaissance.txt", "w+")
                file_classic.close()

                file_classic = open("Renaissance/renaissance.txt","a+")


                if (stopwords==0):

                    for x in dataset_list2:

                        file_a = open("2/" + x, "r+")


                        file_classic.write(file_a.read())

                        file_a.close()

                    file_classic.close()


                if (stopwords==1):

                    for x in dataset_list2:

                        file_a = open("2s/" + x, "r+")

                        file_classic.write(file_a.read())

                        file_a.close()

                    file_classic.close()

                return 1

        if (self.input_file_path == 3):

            dataset_list3 = subprocess.check_output("./script3.sh", shell=True).decode("utf-8")

            dataset_list3 = dataset_list3.splitlines()

            if (dataset_list3 == []):

                tkinter.messagebox.showerror("NO DATASET FOUND", "The Modern dataset list is empty!")
                return 0

            else:

                file_classic = open("Modern/modern.txt", "w+")
                file_classic.close()

                file_classic = open("Modern/modern.txt", "a+")

                if (stopwords==0):

                    for x in dataset_list3:

                        file_a = open("3/" + x, "r+")

                        file_classic.write(file_a.read())

                        file_a.close()

                    file_classic.close()

                if (stopwords==1):

                    for x in dataset_list3:

                        file_a = open("3s/" + x, "r+")

                        file_classic.write(file_a.read())

                        file_a.close()

                    file_classic.close()

                return 1

#TextPreProcessing("/Users/alberto/PycharmProjects/Word2Vec/the iliad.txt").filter()