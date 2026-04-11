# Chapter 19. 유전적 이질성에서 기능적 수렴으로

이 챕터를 시작하기 전에 하나의 사고 실험을 해보자. 어느 도시에 같은 증상을 가진 환자들이 수백 명 모였다고 가정하자. 그들 모두 비슷한 어려움을 겪지만, 각자가 왜 그 상태가 됐는지를 들여다보면 각각의 이유가 다르다. 어떤 사람은 뇌의 특정 영역에 가해진 초기 손상 때문이고, 어떤 사람은 발달 시기에 특정 호르몬이 제대로 조절되지 않았기 때문이며, 어떤 사람은 어릴 때 특정 회로가 형성되는 방식에 미묘한 차이가 있었기 때문이다. 원인은 제각각이지만 결과는 비슷하다. 신경발달 질환, 특히 자폐스펙트럼장애(autism spectrum disorder)가 정확히 이런 상황이다. 그리고 유전학의 언어로 이것을 표현하면 유전적 이질성(genetic heterogeneity)이라는 개념이 된다.

유전적 이질성이란 같은 표현형(phenotype)을 보이는 개인들이 서로 다른 유전 변이(genetic variant)를 가지는 현상을 말한다. 여기서 용어를 명확히 할 필요가 있다. 변이(variant)와 유전자(gene)는 다른 개념이다. 유전자는 특정 단백질이나 기능적 RNA를 코딩하는 DNA의 기능적 단위다. 반면 유전 변이는 그 유전자의 DNA 서열에서 발생하는 특정한 차이, 즉 단일 염기의 치환이거나, 짧은 서열의 삽입/결실이거나, 더 큰 규모의 복제수 변이(copy number variant, CNV)일 수 있다. 하나의 유전자에서 수십 가지의 서로 다른 유전 변이가 발생할 수 있고, 그것들이 각각 서로 다른 효과를 낼 수 있다. 유전 변이가 DNA 서열의 차이라면, 유전자는 그 차이가 일어나는 문맥이다. 이 구분은 단순한 용어 문제가 아니라, 자폐스펙트럼장애의 유전적 구조를 이해하는 데 핵심적인 개념이다.

자폐스펙트럼장애의 유전적 이질성은 극단적이다. 현재까지 수백 개의 유전자가 자폐스펙트럼장애 위험과 연관된 것으로 보고되었고, 추산에 따르면 드노보 유전 변이(de novo variant, 부모로부터 유전된 것이 아니라 개인에게서 새로 발생한 유전 변이)만으로도 1,000개 이상의 유전자가 관여할 수 있다. 어떤 연구자들은 자폐스펙트럼장애가 하나의 질환이 아니라 수백 가지 다른 생물학적 원인을 가진 증후군들의 집합일지도 모른다고 주장했다. 이 관점에서 보면 "자폐스펙트럼장애"라는 단일 진단 범주는 단순히 비슷한 증상을 묶어 놓은 임상적 편의의 산물이지, 하나의 일관된 생물학적 실체를 반영하지 않을 수도 있다. 그런데 여기서 반전이 일어난다. 수백 개의 서로 다른 유전자들이 관여하지만, 그 유전자들이 속한 네트워크와 경로는 일관되게 수렴한다는 것이 대규모 유전체 연구들을 통해 점점 더 명확해졌다.


# 엑솜 시퀀싱이 밝힌 신생 변이의 수렴

기능적 수렴의 증거가 본격적으로 드러나기 시작한 것은 2012년이다. 이 해에 자폐스펙트럼장애의 유전적 구조를 근본적으로 바꿔놓은 논문 네 편이 거의 동시에 출판되었다. 2012년 4월, Nature에 세 편의 엑솜 시퀀싱 논문이 같은 날 나란히 실렸다. 예일 대학교의 매튜 스테이트(Matthew State) 연구실의 스테판 샌더스(Stephan Sanders)가 이끈 연구, 하버드 대학교의 마크 닐(Mark Daly) 연구실의 벤자민 닐(Benjamin Neale)이 이끈 연구, 그리고 워싱턴 대학교의 제이 슈렌도프(Jay Shendure) 연구실의 브라이언 오록(Brian O'Roak)이 이끈 연구였다. 같은 달 Neuron에는 콜드스프링하버 연구소의 이반 이오시포프(Ivan Iossifov) 연구팀의 논문이 실렸다. 네 연구 모두 자폐스펙트럼장애 환자와 그 가족의 엑솜을 시퀀싱하여 신생 유전 변이(de novo variant)를 체계적으로 발굴했고, 독립적인 데이터셋에서 일관된 결론에 도달했다. 자폐스펙트럼장애 환자에서 신생 기능 손실성 변이(de novo loss-of-function variant)가 대조군보다 유의하게 많고, 이 변이들이 크로마틴 리모델링과 시냅스 기능 관련 유전자에 집중된다는 것이었다. 네 개의 서로 다른 연구실이 서로 다른 코호트를 분석하여 같은 결론에 도달했다는 사실 자체가, 이 발견의 신뢰성을 강력하게 뒷받침했다.

이 네 편의 논문이 중요한 또 다른 이유는 통계적 프레임워크의 확립이다. Sanders et al. 연구는 유전자 길이와 서열 맥락에 따른 신생 유전 변이의 기대 빈도를 모델링하여, 관찰된 변이 수가 기대치를 초과하는 유전자를 통계적으로 발견하는 방법론을 정립했다. 이것은 이후 모든 대규모 엑솜 시퀀싱 연구의 표준 분석 방법이 되었다. 개별 유전자 수준에서 통계적 유의성을 확보하려면 충분한 표본 크기가 필요했고, 2012년의 표본 규모로는 [CHD8](https://www.genecards.org/cgi-bin/carddisp.pl?gene=CHD8), [SCN2A](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SCN2A), [DYRK1A](https://www.genecards.org/cgi-bin/carddisp.pl?gene=DYRK1A), [KATNAL2](https://www.genecards.org/cgi-bin/carddisp.pl?gene=KATNAL2) 등 소수의 유전자만이 재현적으로 확인되었다. 하지만 이 소수의 유전자들이 이미 크로마틴 조절과 시냅스 기능이라는 두 가지 주제를 가리키고 있었다. 더 큰 코호트를 모으면 더 많은 유전자가 발견될 것이고, 수렴의 패턴은 더 뚜렷해질 것이라는 예측이 가능했다. 그리고 그 예측은 2년 뒤 현실이 되었다.


# 세 가지 경로로의 수렴 — 시냅스, 전사 조절, 크로마틴

2012년의 토대 위에서, Autism Sequencing Consortium이 수행한 De Rubeis et al. (2014) 연구는 수렴을 본격적으로 증명했다. 이 연구는 3,871명의 자폐스펙트럼장애 환자와 9,937명의 대조군을 대상으로 전체 엑솜 시퀀싱(whole-exome sequencing)을 수행했다. 엑솜(exome)이란 유전체 중 단백질로 번역되는 부분인 엑손(exon)들의 총합인데, 전체 유전체의 약 1.5%에 불과하지만 현재까지 알려진 질환 유발 유전 변이의 대다수가 이 영역에 집중되어 있다. 전체 유전체 중 실제 단백질 설계도로 쓰이는 부분은 1.5%뿐이고, 나머지 98.5%는 조절 서열, 반복 서열, 아직 기능이 잘 모르는 서열들이다. 엑솜 시퀀싱은 이 1.5%만 집중적으로 읽는 방법으로, 전체 유전체를 읽는 것보다 훨씬 저렴하면서도 단백질 기능을 바꾸는 변이를 효율적으로 찾아낸다. 엑솜 시퀀싱은 전체 유전체 시퀀싱보다 비용이 낮고 데이터 해석이 상대적으로 용이하여, 2010년대 초반부터 신경발달 질환 유전자 발견의 주력 기술로 자리잡았다.

당시 기준으로 가장 큰 자폐스펙트럼장애 엑솜 시퀀싱 연구에서, FDR(거짓 발견율, false discovery rate) 5% 기준으로 22개의 자폐스펙트럼장애 위험 유전자가 발견되었고, 보다 넓은 FDR 30% 기준으로는 107개 유전자가 자폐스펙트럼장애 위험과 연관된 것으로 나타났다. 이 유전자들은 인구 집단 내에서 기능 손상성 유전 변이에 대한 진화적 불내성(evolutionary intolerance)이 높은 것들이었는데, 이는 이 유전자들이 뇌 발달에서 매우 중요한 기능을 담당하기 때문에 그것들에 변이가 생기면 자연선택에 의해 제거된다는 의미다. 달리 말하면, 수백만 년간 인류의 조상들 중에서 이 유전자에 심각한 변이가 생긴 개체들은 자녀를 덜 남기는 방식으로 걸러져왔기 때문에, 오늘날 인구집단에서 이 변이들이 매우 드물다는 뜻이다. 유전체의 어떤 부분들은 변이를 허용하지 않는다. 자폐스펙트럼장애 위험 유전자들은 바로 그런 엄격한 보존이 요구되는 영역에 집중되어 있었다.

그런데 22개 혹은 107개의 유전자 목록 자체보다 더 중요한 발견이 있었다. 이 유전자들을 기능적으로 분류하면 세 가지 주요 경로로 수렴한다는 것이었다. 첫째, 시냅스 형성과 기능에 관여하는 경로, 예를 들어 [SHANK2](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SHANK2), [SYNGAP1](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SYNGAP1), [NRXN1](https://www.genecards.org/cgi-bin/carddisp.pl?gene=NRXN1) 같은 유전자들이다. 둘째, 전사 조절(transcriptional regulation)에 관여하는 경로, [TBR1](https://www.genecards.org/cgi-bin/carddisp.pl?gene=TBR1), [FOXP1](https://www.genecards.org/cgi-bin/carddisp.pl?gene=FOXP1), [ADNP](https://www.genecards.org/cgi-bin/carddisp.pl?gene=ADNP) 같은 전사인자들이다. 셋째, 크로마틴 리모델링(chromatin remodeling), 특히 히스톤 리신 메틸화/탈메틸화(histone lysine methylation/demethylation)에 관여하는 경로, CHD8, [ARID1B](https://www.genecards.org/cgi-bin/carddisp.pl?gene=ARID1B), [KDM5C](https://www.genecards.org/cgi-bin/carddisp.pl?gene=KDM5C), [SETD5](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SETD5) 같은 유전자들이다. 전압 의존성 이온 채널(voltage-gated ion channel) 유전자들도 하나의 군을 형성했다. 수백 개까지 확장될 수 있는 위험 유전자 목록이 결국 세너 개의 생물학적 주제로 축약되는 것이다. 마치 수백 가지 다른 재료들로 요리를 만들었는데, 그 재료들을 분류하면 결국 단백질, 탄수화물, 지방이라는 세 가지 범주로 나뉘는 것과 비슷하다.


# 더 큰 코호트, 더 뚜렷한 수렴

De Rubeis et al. (2014) 이후 유전체 연구의 규모는 더욱 확대되었다. Satterstrom et al. (2020) 연구는 35,584명의 총 표본에서 11,986명의 자폐스펙트럼장애 환자를 포함하는, 당시까지 가장 큰 규모의 자폐스펙트럼장애 엑솜 시퀀싱 연구였다. Autism Sequencing Consortium과 iPSYCH-Broad Consortium이 공동으로 수행한 이 연구는 FDR 10% 기준으로 102개의 자폐스펙트럼장애 위험 유전자를 발견했다. 표본이 약 10배 늘어남으로써 더 많은 유전자를 발견한 것은 당연하지만, 더 흥미로운 것은 이 102개 유전자가 어떤 패턴을 보였느냐다.

102개 유전자는 두 가지 큰 생물학적 주제로 나뉘었다 (Satterstrom et al. 2020). 하나는 유전자 발현 조절(regulation of gene expression)로, 전사인자, 크로마틴 리모델러, RNA 결합 단백질 등 유전자들이 언제 어떻게 발현되는지를 조절하는 유전자들의 범주다. 다른 하나는 신경 소통(neuronal communication)으로, 시냅스 신호 전달, 이온 채널, 신경전달물질 수용체 등 뉴런들이 서로 소통하는 과정에 관여하는 유전자들이다. 이 두 범주는 서로 다른 발달적 문제를 가리킨다. 유전자 발현 조절 유전자들이 손상되면 뇌 발달 초기의 프로그램 설정 자체가 잘못된다. 신경 소통 유전자들이 손상되면 만들어진 뉴런들이 서로 소통하는 방식이 비정상화된다. 하나는 설계도의 문제이고, 다른 하나는 완성된 시스템의 작동 문제라고 할 수 있다.

Satterstrom et al. (2020) 연구에서 또 하나의 중요한 관찰은 102개 유전자들이 크게 두 가지 표현형 집단과 연관된다는 것이었다. 49개 유전자는 심각한 신경발달 지연(neurodevelopmental delay) 집단에서 더 자주 기능 손상성 드노보 유전 변이가 발견되었고, 53개 유전자는 자폐스펙트럼장애로 진단된 집단에서 더 두드러졌다. 이것은 자폐스펙트럼장애의 위험 유전자들이 하나의 균일한 집합이 아니라, 표현형의 심각도와 특성에 따라 부분적으로 다른 유전자 집합이 관여한다는 것을 시사한다. 같은 경로 안에서도 어느 유전자가 손상되느냐, 그리고 어떤 종류의 유전 변이가 발생하느냐에 따라 표현형의 스펙트럼이 달라진다.

이 발견은 Fu et al. (2022) 연구에서 더 정교하게 확장되었다. 이 연구는 63,237명이라는 당시 최대 규모 코호트에서 185개의 자폐스펙트럼장애 위험 유전자를 발견했고, 그 유전자들의 세포 유형 특이적 발현 패턴을 정밀하게 분석했다. 핵심 발견은 자폐스펙트럼장애에 더 특이적인 유전자군(53개)과 발달장애(developmental disorder)에 더 특이적인 유전자군(49개) 사이에서 뚜렷한 발달 시간 기울기(developmental gradient)가 존재한다는 것이었다. 자폐스펙트럼장애 특이적 유전자들은 태아 후기부터 출생 후까지 지속되는 성숙 흥분성 뉴런(maturing excitatory neuron)에서 발현이 높았다. 반면 발달장애 특이적 유전자들은 신경 전구세포(neural progenitor)와 미성숙 뉴런, 즉 더 이른 발달 단계의 세포들에서 발현이 집중되어 있었다. 이 기울기는 단순한 통계적 패턴이 아니다. 더 심각한 신경발달 질환일수록 더 초기 발달 과정, 즉 세포가 만들어지고 증식하는 단계에서 교란이 일어나고, 지적 기능이 상대적으로 보존된 자폐스펙트럼장애는 세포가 이미 만들어진 후 성숙하고 연결되는 단계에서 교란이 일어난다는 발달 논리를 반영한다. 같은 스펙트럼 안에서도 어느 유전자가 손상되느냐에 따라 그 손상이 영향을 미치는 발달 창이 달라지고, 그 창의 시점이 표현형의 심각도를 결정한다.

Sanders et al. (2015)이 Neuron에 발표한 연구는 다른 각도에서 같은 이야기를 확인해줬다. 이 연구는 드노보 복제수 변이(de novo copy number variant)와 드노보 단일 염기 변이(de novo single nucleotide variant)를 통합 분석하여 71개의 자폐스펙트럼장애 위험 좌위(risk loci)와 65개의 위험 유전자를 발견했다. 이 유전자들의 기능 분석(enrichment analysis)은 크로마틴 조절과 시냅스 기능이라는 두 경로로의 수렴을 다시 한번 확인했다. CHD8, ADNP, ARID1B, KDM5C 같은 크로마틴 조절 유전자들과 SHANK2, SYNGAP1, NRXN1, [CNTNAP2](https://www.genecards.org/cgi-bin/carddisp.pl?gene=CNTNAP2) 같은 시냅스 기능 유전자들이 두 주요 군을 이루고 있었다. 이 연구는 또한 크기가 작은 드노보 결실(deletion) 안에는 보통 단 하나의 고효과 위험 유전자가 들어 있는 반면, 1 Mb 이상의 큰 복제수 변이 안에는 여러 기여 유전자가 있다는 구조적 통찰도 제공했다.


# 조현병에서도 같은 이야기: 시냅스 네트워크의 수렴

기능적 수렴이 자폐스펙트럼장애만의 이야기가 아니라는 것을 보여주는 중요한 연구가 Fromer et al. (2014)이 Nature에 발표한 논문이다. 이 연구는 623개 조현병(schizophrenia) 가계의 엑솜 시퀀싱을 통해 드노보 유전 변이를 분석했다. 조현병은 자폐스펙트럼장애와는 다른 임상적 특성을 가지며, 발병 연령도 다르고, 진단 기준도 다르다. 그런데 드노보 유전 변이들이 어떤 유전자들에서 빈번하게 발견되어 있는지를 분석하자, 자폐스펙트럼장애에서 발견된 것과 매우 유사한 패턴이 나타났다. 조현병의 드노보 변이들은 [ARC](https://www.genecards.org/cgi-bin/carddisp.pl?gene=ARC) 복합체(ARC complex) 유전자들과 NMDA 수용체 복합체(NMDAR complex) 유전자들에 유의하게 빈번하게 포함되어 있었다. ARC 복합체는 시냅스 활성-조절 세포골격(synaptic activity-regulated cytoskeleton) 복합체로, 시냅스 강도와 가소성(plasticity)을 조절하는 데 핵심적인 역할을 한다. 시냅스 가소성이란 경험에 따라 두 뉴런 사이의 연결 강도가 변하는 능력인데, 기억과 학습이 일어날 때 "이 연결은 더 강하게"라는 신호가 ARC 복합체를 통해 실행된다.

FMRP 표적 유전자(FMRP target genes)에도 유의하게 빈번한 발견이 관찰되었다. FMRP는 취약 X 증후군(Fragile X syndrome)을 유발하는 [FMR1](https://www.genecards.org/cgi-bin/carddisp.pl?gene=FMR1) 유전자가 만드는 단백질인데, 수백 개의 다른 유전자들의 mRNA에 결합하여 그것들의 번역(translation)을 조절한다. FMRP는 일종의 번역 브레이크 역할을 하는데, "지금은 이 단백질 너무 많이 만들지 마"라는 지시를 내리는 분자다. FMRP가 없으면 이 브레이크가 사라져서 뇌에서 과잉 단백질이 만들어지고, 시냅스가 과도하게 형성되며 가지치기가 제대로 일어나지 않는다. FMRP가 결합하는 mRNA들의 목록은 시냅스 기능과 관련된 유전자들로 풍부하게 채워져 있다. 이 연구에서 조현병의 드노보 변이들이 FMRP 표적 유전자들에서 빈번하게 발견되어 있다는 것은, 조현병도 시냅스 기능과 조절이라는 공통된 생물학적 허브에 수렴한다는 것을 의미한다. 더 나아가, 이 연구는 자폐스펙트럼장애의 기능 손실성 드노보 변이가 있는 유전자들과 조현병의 드노보 변이가 있는 유전자들 사이에 유의한 중복이 있다는 것도 보였다(p=0.0007). 전혀 다른 임상적 진단을 받은 두 질환이 분자 수준에서 같은 허브 유전자들을 공유하는 것이다.

이것은 단순한 우연이 아니다. 자폐스펙트럼장애와 조현병이 공통적으로 시냅스 기능 유전자들에 영향을 미친다는 것은, 흥분성 시냅스의 기능이 두 질환 모두의 병태생리에서 중심적인 역할을 한다는 것을 의미한다. 물론 두 질환은 다르다. 자폐스펙트럼장애에서는 크로마틴 리모델링 경로의 기여가 특히 강조되고, 조현병에서는 NMDA 수용체와 도파민 시스템의 역할이 더 부각된다. 하지만 시냅스 네트워크라는 공통된 수렴 지점은 두 질환이 완전히 다른 생물학적 실체가 아니라, 일부 공통된 분자적 취약성을 공유하는 연속체 위에 있을 수 있음을 시사한다. 유전학과 임상 진단의 경계가 반드시 일치하지 않는다는 것, 그것이 현대 신경발달 유전체학이 우리에게 주는 불편하지만 중요한 교훈이다.


# CNV 연구에서 본 수렴: Pinto et al. 2014

복제수 변이(copy number variant, CNV) 수준에서 이루어진 가장 큰 자폐스펙트럼장애 연구 중 하나인 Pinto et al. (2014) 연구는 2,446명의 자폐스펙트럼장애 환자와 2,640명의 대조군을 비교했다. 복제수 변이란 유전체의 특정 구간이 정상보다 더 많이 혹은 더 적게 복제되어 있는 현상으로, 통상적으로 1 kb 이상의 크기를 가진다. 단일 염기 변이가 책에서 철자 하나가 잘못 쓰인 것이라면, 복제수 변이는 책의 한 단락 전체가 사라지거나 두 번 중복 인쇄된 것에 해당한다. 단일 염기 변이와 달리, 복제수 변이는 동시에 여러 유전자에 영향을 미칠 수 있고, 따라서 그 영향이 더 복잡하고 광범위할 수 있다. 이 연구에서 자폐스펙트럼장애 환자에서 드문 가능성이 높은 손상성 복제수 변이는 대조군에 비해 약 1.19배 높은 빈도로 관찰되었는데, 이 변이들이 영향을 미치는 유전자들의 기능적 범주를 분석하면 역시 시냅스 기능, 신경 발달, 크로마틴 리모델링 경로로 수렴했다.

특히 이 연구의 중요한 기여는 복제수 변이 기반 연구에서 크로마틴 리모델링 경로를 자폐스펙트럼장애의 새로운 위험 경로를 처음 명확하게 밝힌 것이다. 그 이전에는 시냅스와 신경 발달 경로가 주로 강조되었는데, Pinto et al. (2014)은 복제수 변이가 영향을 미치는 유전자들 중 크로마틴 구조를 조절하는 유전자들이 대조군 대비 유의하게 많다는 것을 보였다. 이것은 De Rubeis et al. (2014) 엑솜 시퀀싱 연구에서 단일 염기 변이 수준에서 발견된 크로마틴 리모델링 경로의 수렴을 서로 다른 종류의 유전 변이로 독립적으로 재확인한 것이다. 단일 염기 변이든 복제수 변이든, 크고 작은 유전 변이들이 결국 같은 세포 경로를 손상시킨다는 것이다. 더욱이 복제수 변이가 영향을 미치는 유전자들과 드노보 단일 염기 변이가 영향을 미치는 유전자들이 단백질 상호작용 네트워크(protein-protein interaction network) 수준에서 서로 연결되어 있다는 것도 보였다. 다른 종류의 유전 변이들이 같은 단백질 상호작용 망 안의 서로 다른 노드들을 건드리고 있는 것이다.


# 기능적 수렴이 왜 치료적 가능성을 열어주는가

유전적 이질성에서 기능적 수렴으로의 전환은 단순히 학문적 이해의 진보가 아니다. 이것은 자폐스펙트럼장애와 관련 신경발달 질환에 대한 치료 전략의 설계에 근본적인 변화를 가져온다. 만약 자폐스펙트럼장애의 각 사례가 완전히 독립적인 생물학적 메커니즘에 의해 발생한다면, 치료 전략은 본질적으로 수백 가지의 서로 다른 것들을 개발해야 하는, 사실상 불가능에 가까운 도전이 된다. 그러나 수백 개의 유전자들이 결국 세너 가지 공통 경로로 수렴한다면, 그 공통 경로를 표적하는 치료법은 서로 다른 유전적 원인을 가진 환자들에게 광범위하게 적용될 수 있다. 수렴은 다양성 안에서 치료적 레버리지(therapeutic leverage)를 찾게 해준다.

예를 들어 시냅스 경로 수렴의 발견은 흥분/억제 균형(E/I balance)을 회복하는 것이 다양한 유전적 원인을 가진 자폐스펙트럼장애 환자들에게 공통적으로 도움이 될 수 있다는 가설로 이어진다. 서로 다른 시냅스 유전자들이 손상되더라도, 결과적으로 흥분성과 억제성 신경 전달의 불균형이 생긴다면, 그 불균형을 보정하는 방식의 개입이 효과를 가질 수 있다. 크로마틴 리모델링 경로의 수렴은 특정 크로마틴 수정 효소들의 활성을 조절하는 약물이 CHD8, ARID1B, KDM5C 등 여러 다른 크로마틴 유전자들에 변이가 있는 환자들에게 공통적으로 적용될 수 있는 가능성을 열어준다. 물론 이 경로들은 뇌에서만 작동하는 것이 아니기 때문에 특이성을 확보하는 것이 쉽지 않지만, 경로 수렴의 발견은 적어도 어디를 봐야 하는지를 알려준다.

이것이 현대 신경발달 유전체학의 역설이기도 하다. 우리는 더 많은 위험 유전자를 발견할수록, 역설적으로 그 다양성 안에서 공통된 생물학적 주제를 더 뚜렷하게 볼 수 있게 된다. 처음에는 수백 개의 서로 다른 유전자들이 관여한다는 사실이 절망스럽게 느껴질 수도 있다. 하지만 그 유전자들을 기능적 경로의 렌즈로 바라보면, 수백 개의 다양성이 몇 가지 공통 주제로 수렴하는 질서가 드러난다. 유전적 이질성은 표면의 이야기고, 기능적 수렴은 그 아래 흐르는 원리다. 그리고 치료는 표면이 아니라 원리를 겨냥해야 한다.

수렴이 경로 수준에서만 일어나는 것이 아니라는 것을 보여주는 연구가 있다. Darbandi et al. (2024)의 연구는 자폐스펙트럼장애 위험 전사인자 다섯 개, 즉 ARID1B, [BCL11A](https://www.genecards.org/cgi-bin/carddisp.pl?gene=BCL11A), FOXP1, TBR1, TCF7L2가 태아 피질에서 어떤 조절 패턴을 공유하는지를 염색질 면역침강 시퀀싱(ChIP-seq)으로 직접 측정했다. 이 다섯 전사인자들이 모두 함께 결합하는 유전체 위치는 프로모터 근위 영역에서만 12,347개에 달했다. 그리고 Satterstrom et al. (2020)이 발견한 102개 자폐스펙트럼장애 위험 유전자들 중 96개가 이 공유 결합 특징(shared co-binding signature)을 보유하고 있었다. 더 나아가 ARID1B와 TBR1에 CRISPRi를 적용하여 각각의 발현을 억제했을 때, 두 개의 서로 다른 전사인자 억제 실험에서 수렴하는 전사체 변화가 관찰되었고, 그 변화의 패턴이 자폐스펙트럼장애 환자의 사후 뇌에서 보고된 전사체 특징과 일치했다. 이것은 조절 수렴(regulatory convergence)이다. 수백 개의 자폐스펙트럼장애 위험 유전자들이 같은 경로에 속해 있다는 것이 경로 수렴이라면, 그 유전자들이 태아 피질 발달 중에 소수의 마스터 전사인자 집합에 의해 공통으로 조절된다는 것은 더 상위의 수렴이다. 기능적 수렴의 이유를 경로 수준에서 찾는 것을 넘어, 그 경로 자체가 왜 함께 작동하는지를 조절 허브 수준에서 설명하는 것이다.

---

References

Sanders, S. J., Murtha, M. T., Gupta, A. R., Murdoch, J. D., Raubeson, M. J., Willsey, A. J., ... & State, M. W. (2012). De novo mutations revealed by whole-exome sequencing are strongly associated with autism. *Nature*, 485(7397), 237–241. doi:10.1038/nature10945

Neale, B. M., Kou, Y., Liu, L., Ma'ayan, A., Samocha, K. E., Sabo, A., ... & Daly, M. J. (2012). Patterns and rates of exonic de novo mutations in autism spectrum disorders. *Nature*, 485(7397), 242–245. doi:10.1038/nature11011

O'Roak, B. J., Vives, L., Girirajan, S., Karakoc, E., Krumm, N., Coe, B. P., ... & Eichler, E. E. (2012). Sporadic autism exomes reveal a highly interconnected protein network of de novo mutations. *Nature*, 485(7397), 246–250. doi:10.1038/nature10989

Iossifov, I., Ronemus, M., Levy, D., Wang, Z., Hakker, I., Rosenbaum, J., ... & Wigler, M. (2012). De novo gene disruptions in children on the autistic spectrum. *Neuron*, 74(2), 285–299. doi:10.1016/j.neuron.2012.04.009

De Rubeis, S., He, X., Goldberg, A. P., Poultney, C. S., Samocha, K., Cicek, A. E., ... & Buxbaum, J. D. (2014). Synaptic, transcriptional and chromatin genes disrupted in autism. *Nature*, 515(7526), 209–215. doi:10.1038/nature13772

Satterstrom, F. K., Kosmicki, J. A., Wang, J., Breen, M. S., De Rubeis, S., An, J. Y., ... & Daly, M. J. (2020). Large-scale exome sequencing study implicates both developmental and functional changes in the neurobiology of autism. *Cell*, 180(3), 568–584. doi:10.1016/j.cell.2019.12.036

Sanders, S. J., He, X., Willsey, A. J., Ercan-Sencicek, A. G., Samocha, K. E., Cicek, A. E., ... & State, M. W. (2015). Insights into autism spectrum disorder genomic architecture and biology from 71 risk loci. *Neuron*, 87(6), 1215–1233. doi:10.1016/j.neuron.2015.09.016

Fromer, M., Pocklington, A. J., Kavanagh, D. H., Williams, H. J., Dwyer, S., Gormley, P., ... & O'Donovan, M. C. (2014). De novo mutations in schizophrenia implicate synaptic networks. *Nature*, 506(7487), 179–184. doi:10.1038/nature12929

Pinto, D., Delaby, E., Merico, D., Barbosa, M., Merikangas, A., Klei, L., ... & Scherer, S. W. (2014). Convergence of genes and cellular pathways dysregulated in autism spectrum disorders. *American Journal of Human Genetics*, 94(5), 677–694. doi:10.1016/j.ajhg.2014.03.018

Sullivan, P. F., & Posthuma, D. (2015). Biological pathways and networks implicated in psychiatric disorders. *Current Opinion in Behavioral Sciences*, 2, 58–68. doi:10.1016/j.cobeha.2014.09.003

Fu, J. M., Satterstrom, F. K., Peng, M., Brand, H., Collins, R. L., Dong, S., ... & Talkowski, M. E. (2022). Rare coding variation provides insight into the genetic architecture and phenotypic context of autism. *Nature Genetics*, 54(9), 1320–1331. doi:10.1038/s41588-022-01104-0

Darbandi, S. F., Robinson, M. D., & An, J. Y. (2024). ASD transcriptional regulators share promoter-proximal binding in fetal cortex. *Nature*, 629, 120–128. doi:10.1038/s41586-024-07303-5
