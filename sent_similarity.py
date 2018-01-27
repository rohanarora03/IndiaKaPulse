###### spacy w/o max

import spacy
nlp = spacy.load('en_core_web_sm')


class seq_match(object):
    def match(self):

        f = open('scrape_data_final.txt', 'rb+')
        my_dict = eval(f.read())
        new_dict = {}
        for i in my_dict:
            count = 0
            for j in new_dict:
                doc1 = nlp(i)
                doc2 = nlp(j)
                s = doc1.similarity(doc2)
                if s < 0.7:
                    count = count + 1
                else:
                    o = new_dict[j][1]
                    o = o + my_dict[i][1]
                    m = new_dict[j][0]
                    for k in m:
                        n = my_dict[i][0]
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
                    new_dict[j] = m, o

            if count == len(new_dict) and len(i) > 3:
                new_dict[i] = my_dict[i][0],my_dict[i][1]

        list_total = 0
        for i in new_dict:
            list_total = list_total + new_dict[i][1]            

        summ = 0
        neww_dict = {}
        new_list_total = 0
        for i in new_dict:
            percent = new_dict[i][1] / list_total    
            summ = summ + new_dict[i][1]
            if percent*100 > 1.7:
                new_list_total = new_list_total + new_dict[i][1]
                neww_dict[i] = new_dict[i][0],new_dict[i][1]

        summ1 = 0
        final_dict = {}
        for i in neww_dict:
            new_percent = neww_dict[i][1] / new_list_total
            summ1 = summ1 + neww_dict[i][1]
            new_percent = new_percent * 100
            new_percent = float("{0:.2f}".format(new_percent))
            final_dict[i,new_percent] = neww_dict[i][0]

        freq_list = []
        for ll in final_dict:
            freq_list.append(ll[1])
        freq_list = sorted(freq_list,reverse=True)

        final = {}
        for h in freq_list:
            for b in final_dict:
                if h == b[1]:
                    final[b] = final_dict[b]

        return final
