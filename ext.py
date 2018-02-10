class ext:
    def extern(self):
        d={}
        d1 = {}
        d2 = {}
        d3 = {}
        final = {}

        f = open('scrape_data.txt','rb+')
        my_dict = eval(f.read())
        for i in my_dict:
            d[i]=my_dict[i]
            final[i] = my_dict[i]

        f = open('scrape_data2.txt', 'rb+')
        my_dict = eval(f.read())
        for i in my_dict:
            d1[i] = my_dict[i]

        f = open('scrape_data3.txt','rb+')
        my_dict = eval(f.read())
        for i in my_dict:
            d2[i]=my_dict[i]

        f = open('scrape_data4.txt','rb+')
        my_dict = eval(f.read())
        for i in my_dict:
            d3[i]=my_dict[i]

        for j in d1:
            if j in final.keys():
                o = final[j][1]
                o = o + d1[j][1]

                m = final[j][0]
                for k in m:
                    n = d1[j][0]
                    for l in n:
                        if k == "like" and l == "like":
                            m['like'] = m['like'] + n['like']
                        if k == "love" and l == "love":
                            m['love'] = m['love'] + n['love']
                        if k == "haha" and l == "haha":
                            m['haha'] = m['haha'] + n['haha']
                        if k == "wow" and l == "wow":
                            m['wow'] = m['wow'] + n['wow']
                        if k == "angry" and l == "angry":
                            m['angry'] = m['angry'] + n['angry']
                        if k == "sad" and l == "sad":
                            m['sad'] = m['sad'] + n['sad']
                final[j] = m, o
            else:
                final[j] = d1[j]

        for j in d2:
            if j in final.keys():
                o = final[j][1]
                o = o + d2[j][1]

                m = final[j][0]
                for k in m:
                    n = d2[j][0]
                    for l in n:
                        if k == "like" and l == "like":
                            m['like'] = m['like'] + n['like']
                        if k == "love" and l == "love":
                            m['love'] = m['love'] + n['love']
                        if k == "haha" and l == "haha":
                            m['haha'] = m['haha'] + n['haha']
                        if k == "wow" and l == "wow":
                            m['wow'] = m['wow'] + n['wow']
                        if k == "angry" and l == "angry":
                            m['angry'] = m['angry'] + n['angry']
                        if k == "sad" and l == "sad":
                            m['sad'] = m['sad'] + n['sad']
                final[j] = m, o
            else:
                final[j] = d2[j]

        for j in d3:
            if j in final.keys():
                o = final[j][1]
                o = o + d3[j][1]

                m = final[j][0]
                for k in m:
                    n = d3[j][0]
                    for l in n:
                        if k == "like" and l == "like":
                            m['like'] = m['like'] + n['like']
                        if k == "love" and l == "love":
                            m['love'] = m['love'] + n['love']
                        if k == "haha" and l == "haha":
                            m['haha'] = m['haha'] + n['haha']
                        if k == "wow" and l == "wow":
                            m['wow'] = m['wow'] + n['wow']
                        if k == "angry" and l == "angry":
                            m['angry'] = m['angry'] + n['angry']
                        if k == "sad" and l == "sad":
                            m['sad'] = m['sad'] + n['sad']
                final[j] = m, o
            else:
                final[j] = d3[j]

        f = open('scrape_data_final.txt', 'wb+')
        f.write(str(final).encode('utf-8'))
        f.close()

