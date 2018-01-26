#########SWBH

import requests


class fetchComments4:

    def extract(self, page_id, post_id):

        graph_api_version = 'v2.11'
        access_token = 'EAAB4RjO6UKwBADZAk1bC9PUsPKuvjLlstZCkCazCvZCcqZBCVsbZA9YGiNBUYWEIxjl07cshozkpkHsHVFiYyLb2KrWZBnbGHutP7iP3gwJ30zsEYXPEoO7YkAjnNG4l4dwaEIGR5GztbB8gIl3kZCQwMI0TfjgpUc8jquCaMm2ZCAZDZD'

        url = 'https://graph.facebook.com/{}/{}_{}/comments'.format(graph_api_version, page_id, post_id)
        url1 = 'https://graph.facebook.com/{}/{}_{}/comments?fields=reactions.type(LIKE).limit(0).summary(true).as(like),reactions.type(LOVE).limit(0).summary(true).as(love),reactions.type(HAHA).limit(0).summary(true).as(haha),reactions.type(WOW).limit(0).summary(true).as(wow),reactions.type(ANGRY).limit(0).summary(true).as(angry),reactions.type(SAD).limit(0).summary(true).as(sad)'.format(
            graph_api_version, page_id, post_id)

        comments = []
        dictt = {}

        r = requests.get(url, params={'access_token': access_token})
        r1 = requests.get(url1, params={'access_token': access_token})

        while True:
            data = r.json()
            data1 = r1.json()

            if 'error' in data:
                raise Exception(data['error']['message'])
            if 'error' in data1:
                raise Exception(data1['error']['message'])

            c = 0
            for comment in data['data']:
                text = comment['message'].replace('\n', ' ')
                id = comment['id']
                comments.append((text, id))

            for reaction in data1['data']:
                reactionss = {}
                lisss = []

                for rea in reaction:
                    if rea == "like":
                        reactionss["like"] = reaction[rea]['summary']['total_count']
                    if rea == "love":
                        reactionss["love"] = reaction[rea]['summary']['total_count']
                    if rea == "haha":
                        reactionss["haha"] = reaction[rea]['summary']['total_count']
                    if rea == "wow":
                        reactionss["wow"] = reaction[rea]['summary']['total_count']
                    if rea == "angry":
                        reactionss["angry"] = reaction[rea]['summary']['total_count']
                    if rea == "sad":
                        reactionss["sad"] = reaction[rea]['summary']['total_count']
                dictt[reaction['id']] = reactionss

            if 'paging' in data and 'next' in data['paging']:
                r = requests.get(data['paging']['next'])
            else:
                break
            if 'paging' in data1 and 'next' in data1['paging']:
                r1 = requests.get(data1['paging']['next'])
            else:
                break

        final = {}
        for j in dictt:
            for i in comments:
                if j in i:
                    if i[0] in final:
                        qq = final[i[0]]
                        q = qq[1]
                        q = q + 1
                        mm = final[i[0]]
                        m = mm[0]
                        for k in m:
                            n = dictt[i[1]]
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
                        final[i[0]] = m,q
                    else:
                        final[i[0]] = dictt[j],1
        f = open('scrape_data4.txt', 'wb+')
        f.write(str(final).encode('utf-8'))
        f.close()
