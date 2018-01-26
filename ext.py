class ext:
    def extern(self):
        d={}

        f = open('scrape_data.txt','rb+')
        my_dict = eval(f.read())
        for i in my_dict:
            d[i]=my_dict[i]

        f = open('scrape_data2.txt', 'rb+')
        my_dict = eval(f.read())
        for i in my_dict:
            d[i] = my_dict[i]

        f = open('scrape_data3.txt','rb+')
        my_dict = eval(f.read())
        for i in my_dict:
            d[i]=my_dict[i]

        f = open('scrape_data4.txt','rb+')
        my_dict = eval(f.read())
        for i in my_dict:
            d[i]=my_dict[i]

        f = open('scrape_data_final.txt', 'wb+')
        f.write(str(d).encode('utf-8'))
        f.close()
