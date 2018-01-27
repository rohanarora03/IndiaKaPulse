from flask import Flask
from flask import request
import requests
from flask import render_template
from fetch_comments import fetchComments
from fetch_comments2 import fetchComments2
from fetch_comments3 import fetchComments3
from fetch_comments4 import fetchComments4
from ext import ext
from relevant_features import relevant
from sent_similarity import seq_match
l=['photos','videos','posts']
fc=fetchComments()
fc2=fetchComments2()
fc3=fetchComments3()
fc4=fetchComments4()
ex = ext()
re = relevant()
ss = seq_match()
lp=[]


class FlaskIgnite:

    app = Flask(__name__)

    @app.route('/')
    def my_form():
        return render_template("multi.html")

    @app.route('/', methods=['POST'])
    def my_form_post():
        p={}
        id={}
        wf = request.form['wf']
        wfm = request.form['wfm']
        iv = request.form['iv']
        swbh = request.form['swbh']
        p['wf']=wf
        p['wfm']=wfm
        p['iv']=iv
        p['swbh']=swbh
        for i in p:
            # print(p[i])
            query = p[i].split("/")
            for j in query:
                if j in l:
                    initial = p[i].split(j+"/")
                    slash=initial[1].split("/")
                    initial[1]=slash[0]
                    if j!="photos":
                        postid=initial[1]
                        # print(postid)
                    else:
                        postid=query[6]
                        # print(postid)
                    z = initial[0]
                    break
            url = 'https://graph.facebook.com/'+query[3]+'?&access_token=EAAB4RjO6UKwBAHDrR1cvIrQV3cJsi5jn3Krp5bjHpf0guiSpiGcFUYzXByZC8rUUKqHetaJk4tIrFqsQlsc5xX0rw4jMD7NDnhUHF6jNbFHc10CyRRnF4faqLq7ItxH2yX0OZCd4OBfKzU9MhGTjU6MKMTLGKvQZAtUTEnIrgZDZD'
            r = requests.get(url)
            dict=r.json()

            pageid=dict['id']
            # print(pageid)
            tid=pageid+"_"+postid
            id[i]=tid

        # print(id)

        p1 = id['iv'].split("_")
        pgid1 = p1[0]
        pstid1 = p1[1]
        fc.extract(pgid1, pstid1)

        p2=id['wf'].split("_")
        pgid2=p2[0]
        pstid2=p2[1]
        fc2.extract(pgid2, pstid2)

        p3 = id['wfm'].split("_")
        pgid3 = p3[0]
        pstid3 = p3[1]
        fc3.extract(pgid3, pstid3)

        p4 = id['swbh'].split("_")
        pgid4 = p4[0]
        pstid4 = p4[1]
        fc4.extract(pgid4, pstid4)

        ex.extern()
        x = re.find_relevant()
        y = ss.match()

        # return "sent"
        return render_template("try.html", tfr=x, pre=y)

    if __name__ == '__main__':
        app.run()


Ignite=FlaskIgnite()
Ignite.my_form()
Ignite.my_form_post()
