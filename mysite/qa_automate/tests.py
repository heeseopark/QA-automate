from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from openai import OpenAI

def cluster_qapairs(qa_pairs):

    # Convert qa_pairs to a list of dictionaries to maintain compatibility with the remaining code
    qa_pairs = [{"question": pair[0], "answer": pair[1]} for pair in qa_pairs]

    # 1. Extract keywords (simplified using TF-IDF)
    vectorizer = TfidfVectorizer(max_df=0.5, max_features=10000, min_df=2, stop_words='english', use_idf=True)
    X = vectorizer.fit_transform([" ".join(pair.values()) for pair in qa_pairs])

    # 2. Cluster Q&A pairs (using K-means)
    km_model = KMeans(n_clusters=5)
    km_model.fit(X)

    clusters = km_model.labels_.tolist()

    # 3. Organize Q&A pairs into clusters
    clustered_qa_pairs = {i: [] for i in range(5)}
    for i, cluster in enumerate(clusters):
        clustered_qa_pairs[cluster].append(qa_pairs[i])

    # 4. Generate estimated answers
    openai = OpenAI("your-api-key")
    estimated_answers = {}

    for cluster, pairs in clustered_qa_pairs.items():
        prompt = ""
        for pair in pairs:
            prompt += f"Question: {pair['question']}\nAnswer: {pair['answer']}\n"

        response = openai.Completion.create(
        model="gpt-4.0-turbo",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
        )

        estimated_answers[cluster] = response.choices[0].text.strip()

    # 5. Return top 5 classification cases
    # Assuming 'top' means 'most Q&A pairs'
    top_clusters = sorted(clustered_qa_pairs.items(), key=lambda x: len(x[1]), reverse=True)[:5]
    result = []

    for cluster, pairs in top_clusters:
        print(f"Cluster: {cluster}, Keywords: {vectorizer.get_feature_names()}, Estimated answer: {estimated_answers[cluster]}")
        # Convert pairs back to the original format and add to the result
        result.extend([[pair["question"], pair["answer"]] for pair in pairs])

    return result

qapairs = [


]


"""

질문1:

3. a,b가 1보다 작은 경우는 왜 고려 안 해요? 1보다 작으면 싹 다 0이 되어서 0으로 수렴하는거 아닌가요?

답변1:

안녕하세요!

강의에서 변형한 식인 (2^n-1)bn/(2^n+1)bn 은 a,b>0 인 경우에 성립하는 식으로

1보다 작은 경우도 포함하는 식입니다.

따라서 a,b가 0과 1 사이이더라도 위의 식으로 변형할 수 있고 결국 bn 이 약분되어 같은 결론을 얻게 됩니다.

답변이 도움이 됐으면 좋겠습니다;)

질문2:

1.미적분 상 시발점 44쪽. 8번
2. 24:00
3. 식을 정리했을때 분모 분자에 모두 (2b) ^n이 생기는데 b보다 2b가 항상 크니까 등비수열의 극한의 성질을 사용해서 공비가 큰 2b만 보고 발로 1이라 답 할순 없나요?
4.b거 양수이므로 2b가 b보다 항상 크기때문

답변2:

안녕하세요 :)

문항에서 b가 양수라고 주어졌으며 2b는 학생의 말씀대로 항상 b보다 클 수 밖에 없습니다.

따라서 말씀하신 대로 2b에 대해 생각해 답을 하셔도 되겠습니다..!
답변이 도움이 되었으면 좋겠습니다. 열공하세요!

질문3:

3. 구하는 극한식을 b^n으로 다 나누어서 a/b=2를 바로 활용해도 되나요?

답변3:

안녕하세요, 조교 이수진입니다. 답변 드리겠습니다.

분자 분모에 대해서 모두 같은 값에 대해 나누어 수렴의 형태를 봐주실 수 있는

꼴이므로 첨부하신 사진과 같이 구해주실 수 있겠습니다.

도움이 되었길 바래요 : )

질문4:

1. 시발점 미적분 상) 44p 8번
2. 22:11
3. 영상에 나오는 가장 최근 식에서 다른 방법으로 풀었는데 되는지 안 되는지 궁금해요
4. n승이 있으면 공비로 봐도 되니까 괄호 안 절댓값이 큰 2b만 남기고 그 앞에 계수가 1로 있다고 생각하고 풀었어요 괜찮을까요?

답변4:

안녕하세요! QA조교 이상화 입니다!
네 괜찮습니다! b가 양수이므로 2b가 더 크므로

공비 2b로 전체식을 나눠준다면 2b의 계수만 남을 것이므로

계수만 계산해주셔도 괜찮습니다!
답변이 도움되셨길 바랍니다! 오늘도 열공하세요!

질문5:

1. 44p 8번
3.이렇게 풀어도 되나요?.

답변5:

안녕하세요 조교 신치호입니다.

예 상관없습니다.

분모, 분자를 같은 값으로 나눠 생각해준 뒤 n이 무한대로 갈 때에 대한 극한식 풀이를 사용한 것으로 옳은 방법이 됩니다.

감사합니다.

질문6:

1. (시발점 미적분)p.44, 8번
2. (시발점 미적분 상 step1 theme1~4)24분
3. a=2b 니까 밑의 절댓값이 a>b임으로 b^n으로 묶지 않고 바로 계수비를 적용해서 극한값을 1로 판단해도 되나요?

답변6:

안녕하세요. 소영 조교입니다.

네 가능합니다.

a와 b의 대소 관계를 이용해 바로 극한값을 구하셔도 무방합니다.

도움이 되셨기를 바랍니다. 감사합니다 :)

질문7:

3. a/b=2 로 바로 계산하면 틀린건가용?
4. 현우진샘은 저 a/b=2 에서 a=2b로 가셨는데, 저는 그냥 저 형태로 주어진 문제 변형시킬라고, 주어진 문제를 b^n으로 나누니 (a/b)^n 나와서 2대입하니까 답은 맞췄는데, 요로코롬하면 틀리나영??

답변7:

안녕하세요 QA조교 정준우입니다

극한식 전체를 b^n으로 나눠준다고 생각해주시면 됩니다

그럼 a/b꼴만 남게 되어서

계산할 수 있습니다

답변이 도움이 되었으면 좋겠습니다 감사합니다 !

질문8:

1. ㅅㅣ발점 44쪽 8번
3. 제 풀이처럼 풀면 안되나요,,?

답변8:

안녕하세요! QA조교 이상화 입니다!
학생의 풀이도 괜찮습니다! 식조작을 통해

공비가 1/2인 수열을 0으로 수렴시켜서

계산하셔도 괜찮습니다!
답변이 도움되셨길 바랍니다! 오늘도 열공하세요!

질문9:

3. 첨부한 사진 속 풀이가 가능한지 궁금해요 감사합니다:)

답변9:

안녕하세요 조교 희서입니다.

i) 풀이는 잘못된 풀이이지만 ii) 풀이는 문제가 없습니다.

i에서 지수로 올려버리면 2^(log2(a) - log2(b)) = 1 이 됩니다.

2^(x-y)와 2^x - 2^y는 서로 다른 식인 것을 보시면 됩니다.

도움이 되셨길 바랍니다:)

질문10:

3. 여기서 바로 공비가 2b인것끼리 약분하면 안되나요??
4. 공비가 제일 크니까요

답변10:

안녕하세요 조교 김예진입니다.

가능합니다 ! bn으로 묶어주기전에 2bn 으로 나눠줘도 같은 결과가 나옵니다 !

감사합니다 :)

질문11:

=========================================
=========================================
3. 44쪽 8번 문제 a=2b에서 등비수열의 극한은 공비의 절댓값이 큰 것만 보면 되니까 a가 b보다 절댓값이 커서 b^n은 없애고 a^2/a^2=1이라서 답을 1이라고 생각했는데 잘못된 점이 았나요?

답변11:

안녕하세요 현우진 선생님 QA답변 조교 박재민입니다.

네 말씀하신 논리대로 풀이를 전개해주셔도 괜찮습니다.

결국 절댓값이 큰 항으로 판단을 해야 하는데, a=2b이므로 a에 집중해서 판단하면 되겠습니다.

원하시는 답변이 되었으면 좋겠습니다. 감사합니다! 오늘 하루도 열공하세요:)

질문12:

3. 구해야하는 식에서 bn이 0으로 수렴하는지ㅜ모르는 상황애서 분자 분모를 bn으로 나누어도 되나요?

답변12:

안녕하세요 조교 이민서입니다.
리미트 내에서는 식 조작이 자유롭기 때문에,
분모와 분자를 같은 식으로 곱하거나 나누어 계산이 가능한 형태로 바꿔준다면
해당 방식의 풀이 역시 옳은 풀이가 됩니다.

도움이 되었으면 좋겠습니다. 감사합니다.
질문13:

3. 사진에 있는 식에서, (2b)^n의 공비가 (b)^n의 공비보다 크니까 바로 (2b)^n/(2b)^n=1 로 생각할수있지않나요??
4. 등비수열을 포함하고 무한대/무한대 꼴인 수열에선 분자,분모에서 공비의 절댓값이 가장 큰 것만을 남긴후 약분해야한다고 배웠어요..

답변13:

안녕하세요 조교 성준입니다.

네 질문자님의 관점으로 보셔도 됩니다!

그렇게 보셔도 1이 되기에 상관없습니다.

강의에서는 b^n에 초점을 맞추어 묶어서 본 것임을 참고 바랍니다.

도움이 되셨기 바랍니다.

감사합니다.

질문14:

1. 시발점 미적 상 p44 8번
3. 대소비교방식으로 풀어도 올바른 풀이인가요?

답변14:

안녕하세요 :)

네 그렇습니다.

학생께서 말씀하신 대로 아예 a = 2b가 b보다 영향력이 크다는 판단 하에

b의 부분을 지우고 풀이를 진행하셔도 되며 동일한 결과가 나오니 참고 부탁드립니다!

답변이 도움이 되었으면 좋겠습니다. 열공하세요!

[참고]

학습 Q&A 게시판 상단의 공지사항을 확인하시어
본문에 포함된 질문양식에 맞춰 질문해 주시길 바랍니다.
특히 4. 질문하는 내용에 대한 근거를 명시하시기 바랍니다.
게시판 상단의 공지사항을 확인하시기 바라며,
반복적으로 질문 작성 규칙이 지켜지지 않는다면 답변이 제한된다는 점 참고 바랍니다.

질문15:

=========================================
=========================================
1.시발점 미적분 44p 8번
2.23분14초
3. a=2b 라는 식을 뽑아낸 후 a가 2b 보다 크니까 b의 n제곱 무시하고 a의 n제곱의 계수 비로 쓰면 안되나요?
4. 만약 a,b가 1보다 작아 0분의 0 꼴이 나온다해도 응꼴에서도 더 공비가 큰 것의 계수 비로 풀기 때문에

답변15:

안녕하세요!

a=2b 이므로 a가 b보다 크다는 것을 알 수 있고

말씀하신 대로 공비가 더 큰 것의 계수 비교를 통해 극한값을 구할 수 있으므로

a^n의 계수 비교로 답을 구하셔도 됩니다.

답변이 도움이 됐으면 좋겠습니다:)

질문16:

1. 시발점 미적분 상 44페이지 8번
3. 저 사진상 풀이과정처럼 b의 n제곱으로 나누어서 (a/b)의 n제곱으로 바로 계산하면 안 되는 건가요?
4. 리미트 내부에 있는 식을 조작 하는 건 상관없지 않나요?

답변16:

안녕하세요 조교 신치호입니다.

예 상관없습니다.

a/b가 2로써 절댓값이 1보다 큰 상황임을 알고 계신다면 질문자님과 같이 식을 고쳐서 가장 영향력있는 항만을 남겨 풀이하셔도 됩니다.

감사합니다.

질문17:

3. 이렇게 풀어도 되나요
4. a/b 가 2 이므로 a>b 로 놓으면 준식에서 a^n 와 b^n 중 밑이 a가 더 크기 때문에 b^n 을 지우고 계산하면 lim( a^n/a^n) 이 되므로 1이라고 계산하였는데 이렇게 풀이해도 될까요?

답변17:

안녕하세요 :)

네 그렇습니다.

학생께서 말씀하신 대로 아예 a = 2b가 b보다 영향력이 크다는 판단 하에

b의 부분을 지우고 풀이를 진행하셔도 되며 동일한 결과가 나오니 참고 부탁드립니다!

답변이 도움이 되었으면 좋겠습니다. 열공하세요!

질문18:

====﻿=====================================
=========================================
1. 시발점 - 미적분 (상): p. 44, 08번
3. 이 문제에 해결에 있어서 b>0에서 2b>b, 즉 ∣2b∣>∣b∣이므로
lim(n->inf) [ {(2b)^n - b^n} / {(2b)^n + b^n} ]의 식에서,
분모와 분자에서 공비의 절댓값이 가장 큰 것만을 남겨
lim(n->inf) { (2b)^n / (2b)^n } 로 만들어 1이라는 답을
도출해내는 풀이는 불가능한가요?

답변18:

안녕하세요 조교 서성빈입니다.


말씀하신대로 푸셔도 상관이 없습니다.

다만 칠판에서는 공통으로 b^n을 가지는 상황이기 때문에

b^n으로 묶는 것으로 접근했다고 보시면 될 것 같습니다:)


답변이 되셨길 바랍니다. 감사합니다~


[참고]

학습 Q&A 게시판 상단의 공지사항을 확인하시어
본문에 포함된 질문양식에 맞춰 질문해 주시길 바랍니다.
특히 4. 질문하는 내용에 대한 근거를 명시하시기 바랍니다.
게시판 상단의 공지사항을 확인하시기 바라며,
반복적으로 질문 작성 규칙이 지켜지지 않는다면 답변이 제한된다는 점 참고 바랍니다.

질문19:

3. 8번 문제 그냥 a=2b니까 어찌됐건 절댓값이 a가 b보다 클 것이니 그냥 a의 n제곱으로 나누면 안될까요??

답변19:

안녕하세요 :)

말씀하신 대로 판단을 하여 진행하셔도 됩니다.

그렇게 풀이를 진행하셔도 무방하니 참고 부탁드립니다..!

답변이 도움이 되었으면 좋겠습니다. 열공하세요!

[참고]

학습 Q&A 게시판 상단의 공지사항을 확인하시어
본문에 포함된 질문양식에 맞춰 질문해 주시길 바랍니다.
특히 4. 질문하는 내용에 대한 근거를 명시하시기 바랍니다.
게시판 상단의 공지사항을 확인하시기 바라며,
반복적으로 질문 작성 규칙이 지켜지지 않는다면 답변이 제한된다는 점 참고 바랍니다.

"""