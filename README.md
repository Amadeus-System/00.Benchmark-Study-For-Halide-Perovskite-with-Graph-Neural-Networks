# 00.Application of Crystal Graph Neural Network for Spatial Search of Halide Perovskite Potential Energy
Repository for my GNN Benchmark Research for Halide Perovskite

* 2022-08-30 : Googlecolab pro+ code를 연구실 Workstation 서버로 모두 이전

* **Date : 2022-04-05**
* **Last Modified Date : 2022-08-15**


# Graph Neural Network and Its Application for Computational Physics

![Graph Neural Network](https://user-images.githubusercontent.com/76824867/160241710-4e567f9f-7ccc-4bd5-a1f7-212d754fc552.jpeg)

<!-- TOC -->

- [Graph Neural Network and Its Application for Computational Physics](#graph-neural-network-and-its-application-for-computational-physics)
    - [Background of the Research](#background-of-the-research)
        - [Computational Physics](#computational-physics)
        - [Deep Learning](#deep-learning)
        - [Why do we use Machine Learning in the Physics?](#why-do-we-use-machine-learning-in-the-physics)
    - [What is the Data about?](#what-is-the-data-about)
    - [Material Data Preprocessing](#material-data-preprocessing)
        - [구조 정보에 대한 전처리](#%EA%B5%AC%EC%A1%B0-%EC%A0%95%EB%B3%B4%EC%97%90-%EB%8C%80%ED%95%9C-%EC%A0%84%EC%B2%98%EB%A6%AC)
        - [물성 정보에 대한 전처리](#%EB%AC%BC%EC%84%B1-%EC%A0%95%EB%B3%B4%EC%97%90-%EB%8C%80%ED%95%9C-%EC%A0%84%EC%B2%98%EB%A6%AC)
    - [Graph Neural Network](#graph-neural-network)
        - [Typical Data Structure and Neural Network Euclidean](#typical-data-structure-and-neural-network-euclidean)
        - [The Graph Neural Network IEEE 2019](#the-graph-neural-network-ieee-2019)
        - [Notation and Principles](#notation-and-principles)
        - [Generalization of Recurrent Neural Network](#generalization-of-recurrent-neural-network)
        - [Graph Convolution Network GCN by Kipf & Welling, 2017](#graph-convolution-network-gcn-by-kipf--welling-2017)
        - [Graph Convolution Example](#graph-convolution-example)
        - [Overall Structure of GNN](#overall-structure-of-gnn)
        - [Downstream Tasks by GNN](#downstream-tasks-by-gnn)
    - [Main Idea of CGCNN 2018](#main-idea-of-cgcnn-2018)
    - [CGCNN Performance](#cgcnn-performance)
    - [Performance Test : Energy per Atom](#performance-test--energy-per-atom)
    - [Challenge : Property Prediction of Non-equilibrium States](#challenge--property-prediction-of-non-equilibrium-states)
    - [Related Research by Tian Xie](#related-research-by-tian-xie)
    - [Summary](#summary)
    - [References](#references)

<!-- /TOC -->

이 연구는 2021년 1월에 지도교수님께서 내게 보여주셨던 하나의 논문에서 시작되었다.

해당 논문은 **Crystal Graph Convolutional Neural Network (CGCNN)**를 최초로 제안하여 결정구조 물질에 대한 물성예측을 시도했던 한 연구에 관한 것이었다. 연구에 사용된 코드를 저자가 Github Repository에 공개했었기 때문에, 그 코드를 다운로드하여 코드 분석을 시작했었다. 대략적인 코드 분석에는 한 달 정도의 시간이 소요되었던 것 같다.

코드는 PyTorch 기반으로 작성되어 있었는데, 당시의 나는 TensorFlow, Keras를 주 프레임워크로 사용했기 때문에 Torch에 대해서는 기본적인 수준의 지식밖에 없었다. 결국 코드를 깊게 이해하기 위해서는 Torch에 대한 일정 수준의 이해가 필요했고, Torch를 공부하는 기나긴 여정에 들어갔다. 여러가지로 복잡했지만, 결국 대략적인 내용은 다른 딥러닝 프로젝트와 크게 다르지 않았다.

즉, 데이터를 생성하거나 어딘가에서 가져와서, 전처리하고, 신경망을 모델링하여 학습 후 성능을 체크하는 것이 전부였다. 다만, 저자는 다양한 딥러닝 레이어와 모델을 직접 작성하였고, 데이터를 전처리하는 다양한 부분이 모두 전형적인 Torch 스타일 또는 저자가 직접 작성한 커스텀 함수들로 구성되어 있었다.

현재 시점의 내가 보기에는 그렇게까지 어려운 수준의 코드는 아니지만, Torch를 처음 접했던 시절의 내가 보기에는 굉장히 복잡하고 큰 규모의 프로젝트 코드로 보였다. 결국 함수와 클래스, 메서드를 하나하나 분석하며 코드 리뷰를 하게 되었다.

생각해보면, 이 때가 나의 프로그래밍 경험에서 처음으로 진지하게 타인의 코드를 분석한 첫 사례였던 것 같다. 이전까지는 타인의 코드를 주의깊게 볼 필요가 없었고, 가끔 인터넷에서 보이는 몇 줄 안되는 코드가 전부였기 때문에 코드 분석에 어려움을 느끼는 것이 없었다. 그러나 연구에서 처음으로 경험하게 된, MIT 물리학과 박사과정 학생이 발표한 물성예측 코드는 인터넷에서 떠도는 코드와는 정말 차원이 다른 수준이었다. 그것들을 완전한 수준으로 이해하는 데에는 내 생각보다 훨씬 오랜 시간이 걸렸다. 그리고 그 과정에서 정말 많은 것을 배웠다고 생각한다.

지금의 나는 CGCNN을 비롯하여 다양한 수준의 딥러닝 모델을 나름대로 잘 이해할 정도의 지식은 갖게 되었다고 조심스럽게 생각한다. 그리고 문제상황에 맞춰 적절한 커스텀을 할 수도 있다. 또한, CGCNN 코드로부터 수준 높은 코딩스타일과 객체지향 프로그래밍에 대한 감각도 익힐 수 있었다. 이제는 해당 연구가 갖고 있는 충분하지 않은 점도 비판적으로 지적할 수 있게 되었다.

이 글에서는, 지금까지 내가 진행해온 CGCNN과 관련된 공부 및 연구의 여정을 기억나는대로 모두 적어보고자 한다.

<br>

## Background of the Research

연구 배경에 대해 먼저 설명하자면, 기본적으로 **물성예측(Prediction of Physical/Chemical Property)**를 하기 위함이라고 볼 수 있다.

우리 주변의 세상을 보자. 우주는 수많은 **물질(Material)**로 이루어져 있다. 건물은 단단한 건축자재로 구성되고, 종이는 나무를 구성하는 다양한 유기물로부터 만들어진다. 내가 지금 사용중인 컴퓨터와 모니터, 키보드는 반도체와 공업용 금속, 알루미늄, 플라스틱 등 어떤 도구를 만들기에 적합한 물성을 가진 물질로 만들어져 있다. 눈 앞에 아무것도 없는 공간을 손으로 휘저으면 제대로 지각되기 어렵지만, 그 공간을 채우고 있던 수많은 공기 분자들이 움직일 것이다. 우리는 살아가면서 이러한 물질을 활용한다. 어떤 물질은 거의 그대로 활용되고, 어떤 물질은 그렇지 않다. 예를 들면, 나무에서 과일을 따서 먹는다면, 그것은 특별한 가공과정을 거치지 않고 거의 그대로 활용된 셈이다. 반면, 어떤 물질은 그렇지 않다. 만약 당신이 원시적인 생활환경에서 집을 짓고자 한다면, 집을 구성하는 다양한 건축자재들의 원형(Raw-material)을 준비해야 할 것이다. 그리고 그 각각에 대한 가공을 해야 할 것이다. 그것들을 조합하여 집을 만들게 될 것이다.

여기서 중요한 것은, 우리가 어떤 목적을 이루기 위해 주변의 물질을 활용할 때, 특정한 종류의 물질만이 적합하다는 사실이다. 예를 들면, 튼튼한 창고를 만들려고 할 때 당신이 자연스럽게 자재로 고려하는 것은 근처에 있는 바위, 나무와 같은 단단한 재질의 무언가일 것이다. 창고의 벽을 물렁한 재질로 만든다던가, 혹은 물과 같은 액체로 구성하려는 생각은 애초에 하지 않을 것이다. 즉, **우리가 물질을 활용할 때는 적합한 물성(Desired Property)을 갖는 물질만이 필요하다**. 그리고 여기에서 모든 것이 시작된다.

조금 더 구체적으로, 당신이 효율적인 **태양전지(Solar Cell)**를 개발하는 연구원이라고 하자. 태양전지는 말 그대로 태양으로부터 백색광을 받아 전기를 생산할 수 있게 도와주는 친환경적인 소자이다. 수십년 동안 태양전지의 효율성을 높이기 위한 다양한 연구가 진행되었고, 현 시점에서도 다양한 물질이 태양전지의 후보물질로 연구되고 있다. 그리고 태양전지의 효율성을 높이기 위해 연구되는 유망한 후보물질 중 하나에는 **페로브스카이트(Perovskite)**라는 것이 있다. 페로브스카이트의 화학식은 **$ABX_3$**로 표현되는데, 아름다운 결정구조를 갖는 물질군이다. 이것은 최근 몇 년 동안 태양전지의 효율성을 높이기 위해 사용된 인기있는 후보물질이라고 한다.

그렇다면 이 분야의 연구원들이 하는 다양한 고민들 중에는 이런 것이 있을 것이다.

> '태양전지의 효율을 높이기 위해서는 중간에 특정한 물리적 성질을 갖는 층이 있으면 좋을 것 같다. 그런데 그런 물성을 갖는 구조를 어떻게 찾아내지?'

어떤 물질을 넣고 실험을 했을 때, 원자 레벨에서 물질의 상호작용이 어떻게 될 지 미리 예측하는 것은 매우 어려운 일이다. (아주 불가능하지는 않다) 이 세상에는 온갖 다양한 구조와 조성을 갖는 물질들이 있고, 이 모든 경우의 수를 일일이 다 확인해가며 연구를 할 수는 없다. 실험물리를 하는 연구원들이 이런 고민을 할 때, 물리학의 다른 분야에서는 흥미로운 연구가 진행되고 있었다.

<br>

### Computational Physics

양자역학의 발전 이후 정립된 원자의 상호작용에 관한 이론과 컴퓨터의 연산능력을 결합하여 이론적인 시뮬레이션을 수행함으로써, 실제 실험을 하지 않고도 물질 내부의 복잡한 상호작용을 어느 정도 예측하는 방법이 발달되어 왔다.

**계산물리학(Computational Physics)**으로 불리는 이 분야는, 원자 수준에서 일어나는 복잡한 상호작용을 양자역학적 이론에 기반하여 수식을 세우고, 컴퓨터의 연산능력을 이용하여 수치적으로 풀이함으로써 물질 내부의 세상을 보고자 하였다.

![EmbeddedImage](https://user-images.githubusercontent.com/76824867/161013759-8e217b07-3793-4886-9642-a62a1f6d74f6.png)

나의 지도교수님의 전문분야인 이것은 다양한 세부분야가 있는데, 그 중에서 내가 배운 것은 **밀도범함수 이론(Density Functional Theory, DFT)**라고 불린다. 보통 계산물리학 분야에서는 DFT가 주를 이루고, 계산화학이나 재료분야에서는 관점에 따라 **전산유체역학(Computational Fluid Dynamics, CFD)**, **분자동역학(Molecular Dynamics, MD) 시뮬레이션**과 같은 방법론을 고려한다고 한다. 어쨌든 여기서 DFT는 물질 내부의 복잡한 상호작용을 시뮬레이션할 수 있는 기법 정도로 이해하면 될 것 같다.

자, 그럼 DFT와 같은 시뮬레이션 기술이 있어서 물질의 상호작용을 실험을 하지 않고도, 대략적으로 예측할 수 있다고 하자. 

그럼 도대체 뭐가 문제일까? 실험물리 연구원들과 이론물리 연구원들이 협업하여 여러가지 물질에 대한 시뮬레이션을 하고, 그 중에 괜찮은 결과를 보이는 후보물질에 대하여 실제 실험으로 검증하면 간단히 끝나는 것이 아닐까? 이 세상 모든 물질조합에 대한 탐색을 쉽게 할 수 있지 않을까?

그러나 생각보다 그렇게 간단한 것 같지 않다. 왜냐하면 DFT를 비롯하여 다른 수많은 물질 시뮬레이션 기법의 단점은, 일반적으로 정확도(Accuracy)와 연산시간(Computational Time) 사이에 교환관계(Trade-off)가 성립하기 때문이다. 즉, 현실의 물리현상을 반영하여 물질을 정확하게 계산하려고 할수록, 더 엄격한 조건들이 요구되며 연산시간 또한 급증하게 된다.

여기서는 자세히 언급하지 않고 넘어가지만, 물질의 시뮬레이션은 굉장히 다양한 방식으로 사용자가 조정할 수 있다. DFT 등의 계산과학기법은 보통 상용화된 무료/유료 프레임워크가 존재하여 이를 이용하면 학부생이라도 시뮬레이션을 하는 것은 어렵지 않다. 다만, 수많은 시뮬레이션 관련 변수의 정확한 의미를 알고, 그 결과를 해석하기 위해서 복잡한 고체물리 이론을 깊게 공부하는 것이 요구되므로, 전문가 수준으로 DFT를 다루기 위해서는 지적훈련을 위한 오랜 세월이 걸린다.

결과적으로 계산과학기법으로도 여러가지 한계(방대한 연산시간, 이론적 가정과 현실의 불일치 등)로 인해 가능한 모든 물질조합에 대해 계산하는 것은 불가능했다. 그럼에도 불구하고, 수십년 동안 계산과학 분야의 시뮬레이션 데이터들은 차곡차곡 생성 및 축적되어 왔는데, 이것이 오늘날 딥러닝을 계산물리학 분야에 적용할 수 있는 원동력이 되었다.

<br>

### Deep Learning

이제 딥러닝에 대해 아주 간략히 알아보자.

인위적으로 지능을 구현하려는 **인공지능(Artificial Intelligence, AI)** 분야에는 다양한 하위분야가 있다. 생물의 원리를 모방하여 지능을 구현하려는 분야가 있고, 컴퓨터 안에서 지능을 구현하려는 시도가 있으며, 로보틱스(Robotics)와 같이 하드웨어와 밀접하게 연관된 분야도 있다.

여기서 **컴퓨터(Machine)**을 이용하여 지능을 구현하려는 분야가 바로 요즘 자주 언급되는 **기계학습(Machine Learning)**이며, 그 안에서도 다양한 방식의 학습 알고리즘들이 있지만, 생물의 두뇌를 아주 간략하게 모방하여 발전한 분야가 바로 **심층학습(Deep Learning)**이다.

대부분의 딥러닝 응용연구에서 딥러닝은 좋은 패턴학습의 도구로 활용된다. 즉, 어떤 데이터 $X$와 $Y$의 쌍이 있을 때, 이들 사이에 존재하는 복잡하고 추상적인 패턴을 학습해내는 것이 딥러닝의 강점이라고 할 수 있다. 딥러닝은 머신러닝의 역사 초기에는 별로 주목을 받지 못했지만, 2000년대 이후 알고리즘의 발전과 방대한 계산을 뒷받침할 수 있는 GPU 등 하드웨어의 발전으로 빛을 보게 되었다.

그럼 이제 눈치를 채는 사람들이 있을 것이다.

* **수십년 동안 DFT와 같은 계산과학 분야에는 방대한 계산데이터베이스가 축적되어 왔다.**
* **최근 재조명 받기 시작한 Deep Learning은 데이터가 충분히 있으면, 패턴학습을 잘한다.**

계산과학 데이터베이스에는 일반적으로 다음과 같은 형식으로 데이터가 축적되어 있다.

$$ \mathbf{Material Structure} \Longleftrightarrow \mathbf{Physical/Chemical Properties} $$

즉, 물질의 구조정보를 $X$라 하고 이에 대응하는 물성정보를 $Y$라 하면, $X$ vs $Y$의 패턴을 딥러닝을 이용하여 학습할 수 있다. 딥러닝 모델은 둘 사이에 존재하는 복잡한 비선형 패턴을 학습하여, DFT에 비해 훨씬 빠른 계산시간의 이점을 갖게 될 것이다. 딥러닝을 공부한 사람은 알겠지만, 딥러닝 모델은 학습과정에서 시간이 오래 걸리지만, 일단 학습된 모델이 새로운 데이터 샘플에 대해 그 예측을 출력하는데는 불과 몇 초밖에 걸리지 않는다. 그리고 이러한 딥러닝 모델을 활용하여 방대한 경우의 수를 가진 물질공간을 탐색할 수 있다면? 굉장히 많은 물질조합에 대하여 대략적인 물성예측을 할 수 있고, 이 중에서 특정한 물성조건을 만족하는 후보물질들만을 소수 채택하여 실제 실험에서 검증할 수 있을 것이다!!

그리고 물리학 분야에서 이러한 꿀 아이디어를 먼저 떠올리고 구현한 사람이 바로, 이 글에서 언급된 논문의 저자라고 할 수 있다. (역시 무엇이든 최초가 중요하다 ㅠ.ㅠ)

물론 내가 지금까지 설명한 것은 굉장히 단순화해서 설명한 것이다. 실제로는 어느정도 고체물리학이나 계산물리학에 대한 지식이 있어야 관련 데이터를 가져오고, 그 의미를 해석하여 전처리할 수 있으며, 딥러닝 분야에서 GNN이라고 하는.. 컴퓨터비전이나 자연어처리에 비해 늦게 발전된 특수한 딥러닝 모델에 대한 지식, 그리고 PyTorch, Tensorflow 등의 딥러닝 라이브러리를 일정 수준 이상으로 다룰 수 있어야 위의 연구를 구현할 수 있다.

CGCNN 이후 관련연구 논문이 많이 나왔으며, 내가 석사과정 동안 한 연구도 이것의 연장선상에 있다고 할 수 있다.

<br>

### Why do we use Machine Learning in the Physics?

그럼 왜 물리학 분야에서는 기계학습을 사용하는 것일까? 이에 대해서는 여러가지 이유가 있다.

다음 그림을 보면, 물리학의 발전에 따른 연구의 패러다임 변화를 설명하고 있다. 그림을 보면 알 수 있듯이, 과거에는 경험을 통해 과학적 사실을 정립했다. 그리고 르네상스 이후 급격한 학문의 발달에서 가장 먼저 빛을 본 물리학은, 수학적 이론을 기반으로 하여 만물의 원리를 설명하는 법칙을 만들었다. 이후 1900년대가 되어 컴퓨터의 등장으로, 이제 복잡한 계산은 컴퓨터에게 맡기고 시스템이 어떻게 변화하는가를 관찰할 수 있게 되었다. 그리고 2000년대 이후 머신러닝의 재등장으로 이제 데이터 기반의 연구 패러다임이 강세를 띠기 시작했다.

![그림1](https://user-images.githubusercontent.com/76824867/161016923-90fe0516-a1eb-40be-9787-2e264a7ebc58.png)

위 그림은 'from DFT to machine learning' 이라는 리뷰논문에서 발췌한 것이다. 해당 논문은 DFT 분야에서 응용이 많아진 머신러닝을 설명하는 간단한 수준의 리뷰논문이다. 

그러나 모든 물리학 분야에서 딥러닝을 사용할 수 있는 것은 아니다. 예를 들면, 실험물리학의 대부분의 분야는 일단 각각의 연구실에서 서로 다른 조건에서 만들어진 실험 데이터들이 있고, 그것들은 보통 잘 데이터베이스화 되어있지 않다. 내가 알기로 물리학의 수많은 세부 분야에서, 딥러닝 적용이 상대적으로 쉬운 것은 계산물리학, 이론물리학 등 주로 이론 및 시뮬레이션과 관련된 분야로 한정된다. 가장 대표적인 응용은 **입자물리학, 고에너지(High Energy) 물리학 분야와 관련하여 유럽입자물리연구소(CERN)에서 가동하는 LHC가 생성한 입자물리 데이터에 대한 분석**이라 할수있다.

즉, 연구가 대형화되고 데이터가 쏟아져 나오는 현 시점에서 데이터 기반의 연구 패러다임이 점점, 기존의 이론이나 직관에 기반한 패러다임을 따라오고 있고, 이 과정에서 머신러닝이 활약할 수 있다는 것이다. 여기서 특히 GNN은 물질의 원자구조를 가장 자연스럽게 표현할 수 있기 때문에 활용가능성이 더 높다고 생각한다.

다음 그림은 재료과학 분야에서 특정한 표적물성을 갖는 물질의 디자인을 위해, 충분히 학습된 모델이 활용되는 예시를 보여준다. 

![그림2](https://user-images.githubusercontent.com/76824867/161016965-b9b30510-8bf6-4a92-946c-ef2eba67d0e7.png)

위 그림의 오른쪽과 같이 수많은 후보물질이 있는 상황에서, 충분히 잘 학습된 머신러닝 모델이 있다면 그것은 여러 물성을 구조 정보만으로 예측할 수 있을 것이다. 학습된 모델은 일종의 필터로 활용되어, 적합한 물성조건을 갖는 소수의 후보물질들만을 채택할 수 있게 된다.

<br>

## What is the Data about?

Original CGCNN 논문을 보면, 저자는 Materials Project라는 데이터베이스에서 Perovskite 물질군 데이터를 가져와서 모델을 학습했다고 언급하고 있다.

[Materials Project](https://materialsproject.org/)에 접속하면 'Harnessing the power of supercomputing and state of the art electronic structure methods, the Materials Project provides open web-based access to computed information on known and predicted materials as well as powerful analysis tools to inspire and design novel materials.' 이라는 문구가 눈에 들어온다.

간단히 말하자면, 지금까지 계산된 DFT 기반의 전자구조계산 결과들을 저장하고 있는 데이터베이스이며 여러가지 분석 Tool까지 제공하는 것 같다.

![Material Project 1](https://user-images.githubusercontent.com/76824867/155843080-2e32c5de-a535-44be-931a-df6c26a18bea.PNG)

![Material Project 2](https://user-images.githubusercontent.com/76824867/155843078-3e14027b-74dd-4d97-b6a8-2b8983af9881.PNG)

기본적인 사용 방법은 매우 간단하다.

1. 회원가입 후 로그인을 한다. Google 아이디가 있다면 바로 로그인이 가능하다.
2. 검색하고 싶은 적절한 물질의 화학식을 입력한다. 예를 들면, $\mathrm{SrTiO_3}$라는 페로브스카이트의 한 종류를 입력해보자.

![Material Project 3](https://user-images.githubusercontent.com/76824867/155843217-3fb5c8a3-04bc-4977-9803-16cc81121c17.PNG)

3. 다음과 같이 동일한 화학식을 가졌지만, 세부적으로 다른 다양한 계산결과들이 나온다.

![Material Project 4](https://user-images.githubusercontent.com/76824867/155843220-f1e15927-273a-4e83-8d5e-347d9db48be0.PNG)

4. $\mathrm{mp}-5229$ ID를 갖는 물질에 대해 알고 싶다면, 해당 라인을 클릭하자. 그럼 다음과 같은 자료가 나온다.

![Material Project 5](https://user-images.githubusercontent.com/76824867/155843221-2d6ecbeb-a625-4b40-b53a-8420729c330e.PNG)

![Material Project 6](https://user-images.githubusercontent.com/76824867/155843223-4bc63714-9a38-4f9a-8d4a-fdf62d24cfb4.PNG)

물질의 Unitcell 구조와 여러가지 관련 물성정보들이 소개되고 있다. 밑으로 스크롤을 내리면, Density of States(DOS)와 같이 DFT 계산에서 자주 다뤄지는 중요한 정보들도 시각화되어 있다.

결국 이 데이터베이스가 갖고 있는 것은 수십년 동안 연구되어 온 DFT 분야의 다양한 물질구조와 그에 대응하는 여러 물성정보임을 알 수 있다. Materials Project는 이 데이터베이스에 대해 프로그래밍적으로 접근할 수 있는 API(Python MPRester)를 제공한다. 해당 API를 사용하여 자신이 작업하는 환경에 방대한 물질 데이터를 가져올 수 있고, 그것들을 전처리하면서 연구의 첫 단계가 시작된다고 볼 수 있다.

<br>

## Material Data Preprocessing

자, 이제 Materials Project에서 데이터를 필요한 만큼 받아왔다고 하자. 보통 물리학 분야에서 딥러닝을 적용하는 프로젝트는 제대로 된 데이터를 구하거나, 직접 생성하는 단계에서 전체 프로젝트의 절반 가까운 시간이 소모되는 경우가 많다. 계산과학 분야의 석학들이 모인 연구그룹에서 종종 발표되는 딥러닝 응용논문들을 보면, 연구원들이 고도의 이론적 지식을 동원하여 실제 물리현상을 모방할 수 있는 유사 데이터를 직접 만들어 사용했음을 볼 수 있다. 그런데 현실의 복잡한 물리현상(Real-world Physics)을 모방하는 유사 데이터를 만드는 것이 쉬울까? 보통은 매우 어렵다. 그런 의미에서 학습 데이터를 자신이 직접 생성할 필요가 없다는 것은 굉장한 행운이다.

하지만 그래도 여전히 쉽지 않다. 모든 딥러닝 프로젝트에서 가장 귀찮고, 지루하지만, 실수하면 전체 프로젝트에 지대한 영향을 미쳐서 방심해서는 안되는.. **전처리(Preprocessing)** 단계가 남아있다.

![그림3](https://user-images.githubusercontent.com/76824867/161016975-7b27cff3-aaa5-4877-aba3-1b0d4b86df4a.png)

여기서는 **결정구조(Crystal Structure)를 가진 고체**에 한정하여 설명할 것이다. 고체물질이 계산과학의 주요 연구주제가 되는 이유는 고체의 **주기적 경계조건(Periodic Boundary Condition, PBC)에 의해 수학적으로 분석이 용이**하기 때문이다. 예를 들면, 주기적인 결정구조에 대해 **푸리에 변환(Fourier Transform)**을 하면, 그 결과 또한 주기적 성질을 갖는다. 또한, 주변의 세상을 보면 대부분의 안정되고 자주 활용되는 물질은 고체형태인 경우가 많아서이기도 하다.

전처리 과정은 크게 2단계로 나눌 수 있을 것 같다.

<br>

### 구조 정보에 대한 전처리

구조 정보에 대한 전처리는 결국 Unitcell 단위에서 정의된 여러 원자들의 좌표 정보를 그래프(Graph) 구조로 변환하는 과정이라고 할 수 있다. 

여기서 Graph는 무엇일까? 이산수학 또는 컴퓨터과학 분야에서 자주 연구되는 그래프는 노드(Node)와 엣지(Edge)로 이루어진 자료구조이다. 여기서 노드는 어떤 객체를 의미하고, 엣지는 그러한 객체들 사이의 관계를 표현하는 개념이라고 볼 수 있다. 즉, 이 세상에 존재하는 여러 객체 사이의 추상적인 관계는 모두 그래프로 표현될 수 있다.

그럼 물질의 정보를 그래프로 변환한다는 것은 정확히 어떤 의미일까? 물질을 구성하는 원자(Atom)를 노드로 표현하고, 원자 사이의 상호작용을 엣지로 표현함을 의미한다.

예를 들면, 물 분자 $\mathrm{H_2O}$를 생각해보자. $\mathrm{H_2O}$는 원자 단위에서 수소원자 $\mathrm{H}$ 2개와 산소원자 $\mathrm{O}$ 1개로 구성되어 있다. 따라서 이는 그래프의 노드 3개로 표현될 수 있을 것이다. 그리고 2개의 $\mathrm{H}$와 1개의 $\mathrm{O}$는 수소결합을 하고, 결합의 특수성에 의해 특정한 각도로 조금 기울어져서 위치하게 된다는 것도 알고 있다. 즉, 각각의 원자 노드 사이에는 상대적인 변위가 존재하고 이것은 그래프의 엣지로 표현될 수 있다.

물리학을 공부한 사람들이라면, 결국 엣지가 의미하는 것은 원자간의 힘(Force)이 아닐까? 라고 추측할 것이다. 사실 그 말이 맞다. 문제는.. 물질 안에 존재하는 온갖 종류의 복잡한 상호작용을 모두 제대로 고려하여 전처리하기는 매우 어렵다는 것이다! 

원자 수준에서 이루어지는 힘에 대해 조금만 떠올려보자. 일단 힘의 종류가 여러가지가 있다. 고등학교때 배운 것을 대충 기억해봐도 공유결합, 수소결합, 반데르발스 결합 같은 용어들이 떠오른다. 제대로 분석해서 들어가자면, 여러 원자들의 전자구조인 오비탈(Orbital)에 대해 알아야 하고 이들 사이의 상호작용이 어떻게 이루어지는가를 다 고려해야 할 것 같다. **그리고 그것은 이론적으로 매우 어렵다.**

따라서 CGCNN 저자는 힘이 아니라 **방향에 무관한 거리(Distance)**를 엣지의 주요 정보로 표현한다. 논문의 레퍼런스를 거슬러 읽어가다보면, 그 전부터 관련분야의 연구원들이 공통적으로 이러한 방식을 사용했던 것 같다. 즉, 물질 내부의 원자 사이에 아무리 복잡한 상호작용이 있다고 할지라도, 결국에 그것은 원자간의 끌거나 밀어내는 힘으로 표현될 것이고, 그 **영향력은 최종적으로 거리로 표현**될 것이다! 라고 해석하는 관점이다. 이것은 전처리 문제를 상당히 쉽게 만들어주는 거의 유일한 방법이라고 본다.

<br>

### 물성 정보에 대한 전처리

Materials Project에서 받아오는 데이터를 활용하기만 한다면, 물성 정보에 대한 전처리는 사실 굉장히 간단하다. 만약 직접 DFT 데이터를 생성하고, 거기서 특정한 물성을 추출한다면 조금 귀찮은 과정이 추가된다. 

다음과 같이 $N$개의 물성 정보가 있다고 하자.

$$ (X_1, Y_1), (X_2, Y_2), ..., (X_i, Y_i) ... $$

여기서 물성 $Y_i$만을 모으면, $N$개의 스칼라 값이 나란이 있는 분포가 된다. 어떤 값들의 분포가 있을 때, 정규화(Normalization)를 사용하는 것은 머신러닝 프로젝트에서 자주 보이는 방식이다. CGCNN 저자는 간단한 정규화를 통해 평균이 0, 표준편차가 1인 분포를 만들어 사용하였다. 다음과 같다.

1. $Y$ 분포의 평균을 구한다 : Y.mean
2. $Y$ 분포의 표준편차를 구한다 : Y.std
3. 정규화한다 : Y = (Y - Y.mean) / Y.std

이렇게 정규화를 하는 이유는, 최종적으로 딥러닝 모델이 수행하게 될 Regression 문제에서 값의 분포가 넓게 펼쳐져 있는 것보다 좁게 모여있는 편이 더 쉽기 때문일 것이다. Classification 문제와 달리, Regression 문제에서는 각각의 $Y$ 샘플들에 대한 값에 치밀하게 근접한 값을 추출하도록 모델의 가중치들이 보다 섬세하게 최적화될 필요가 있다. 따라서 값의 분포가 넓을 경우, 학습이 어려워지게 될 것은 자명하다. 따라서 이런 정규화 과정이 선행되었다.

<br>

## Graph Neural Network

모델링을 설명하기 전에 잠시 딥러닝에 대해 말하자면, 일반인들에게 딥러닝은 2016년 알파고와 이세돌의 대국을 통해 알려지게 되었다고 볼 수 있다. 딥러닝 열풍 이전에도 꾸준히 해당 분야의 연구자들이 논문을 발표해왔지만, 다른 분야에서까지 딥러닝 응용논문이 쏟아진 것은 확실히 알파고 이후, TensorFlow와 PyTorch 등 각종 프레임워크의 발전이 영향을 주었다고 생각한다. 인공지능 분야를 원래부터 공부하던 특정 전공분야(통계학, 컴퓨터공학 등)을 제외하면, 대부분의 비전공자 학부생들이 머신러닝을 공부하게 되면 대체적으로 다음과 같은 순서로 학습을 경험할 것 같다.

1. 일반적인 정형데이터에 대해 적용될 수 있는 고전적인 통계 기반의 머신러닝 알고리즘을 배우고
2. 다양한 머신러닝 알고리즘들 중에서, 특별히 신경망 형태로 작동하는 딥러닝 모델에 대해 알게 될 것이고
3. 딥러닝 모델의 학습과정, Backpropagation 같은 것들을 배우고나서 CNN, RNN 등에 대해 알게 될 것이다.
4. CNN 기반의 모델이 발전하여 컴퓨터비전(Computer Vision, CV) 분야에서 발전하고, RNN/LSTM 등의 순환신경망 모델이 자연어처리(Natural Language Processing, NLP) 분야에서 Bert, Transformer, GPT2 등으로 발전되고 있으며..
5. 맨날 모델을 훈련시켜 예측하는 Supervised Learning에 질려서 Unsupervised Learning의 클러스터링을 알게 되고
6. 새로운 것에 목말라 GAN과 같은 생성모델링이나 강화학습(Reinforcement Learning)에 눈을 돌리게 될 것이다.

2010년쯤부터 CV 분야의 CNN 모델이 급격히 발전하다가 조금 정체되는 느낌이 있고, 이후에 자연어처리 분야에서 폭발적인 발전이 있다가 요즘에 다시 잠잠해진 느낌이 있다. (어디까지나 일반인 입장에서) 그러다가 2020년쯤부터, (실제로는 2017년 이전부터도 논문이 나왔지만) 외국 딥러닝 커뮤니티에서 자주 언급되기 시작하는 새로운 신경망 모델이 있었는데 그것이 바로 GNN 이었다. 이제부터 GNN에 대해 알아보자.

신경망에 대해 공부한 사람들이라면, 이미지에 특화된 CNN이나 자연어처리에서 자주 쓰이는 RNN, LSTM 등의 모델을 잘 알 것이다. 그런데 이런 모델들에는 몇 가지 전제가 있었다. 이미지와 자연어는 모두 비정형 데이터이지만, 결국 특정한 공간에서 하나의 벡터로 표현될 수 있었다. 이것이 불가능하다면, 자연어처리 분야의 Word Embedding은 있을 수 없다.

그런데 우리가 이제부터 다루는 데이터는 조금 다르다. 기본적으로 물질의 구조 정보는 그래프로 표현되는 것이 가장 자연스럽다. 따라서 그 정보를 학습해야 할 우리의 모델 또한, 그래프 정보를 입력으로 받아들일 수 있어야 한다. 그리고 여기서 조금 문제가 생긴다.

> Q. 그래프를 벡터로 표현할 수 있는가?

대부분의 머신러닝 모델에는 공통적인 가정이 있다. 바로 데이터의 Feature가 서로 독립이라는 것이다. 그러나 그래프는 이와 다르다. 그래프는 본질적으로 **Irregular domain (Non-euclidean space)**에 존재하며, 데이터의 Feature 사이에 **추상적인 관계(Relationship)**가 존재한다. 그러므로 이러한 관계를 잘 포착하는 학습 방법이 필요했다. 기존의 CNNM, RNN 기반의 모델은 이러한 기능이 없었으므로, 그래프 정보 자체를 입력으로 받아들일 수 있는 GNN 모델이 발전하게 되었다. GNN은 말 그대로 그래프라는 자료구조 자체를 입력으로 받아들일 수 있다. 그래프라는 범용적인 자료구조를 처리한다는 점에서 기존의 신경망들이 다루는 데이터와는 약간의 차이가 발생한다.

<br>

### Typical Data Structure and Neural Network (Euclidean)

다음 그림의 왼쪽과 오른쪽은 각각 이미지를 학습하는 CNN, 자연어를 학습하는 RNN의 간단한 그림을 보여준다.

![그림1](https://user-images.githubusercontent.com/76824867/160383689-70c87d6d-a9c3-4e75-8061-236ff03a4e2d.png)

여기서 중요한 것은, 이미지와 자연어 모두 단일 데이터의 관점에서 벡터로 표현될 수 있다는 것이다. 이미지를 예로 들어보자. 이미지는 Convolution과 Pooling 층을 반복적으로 통과하고 비선형화되면서 최종적으로 이미지의 기하학적 정보를 잘 표현하는 특성벡터로 변환된다. 그리고 그 벡터가 FCL에 입력되면서 특정한 라벨을 예측하도록 학습된다. 

자연어의 경우는 어떨까? 보통 자연어처리 분야에서 텍스트는 단어(Word)의 Sequence로 RNN에 입력된다. 이 때 단어들은 단어의 특성을 잘 표현하는 Word Embedding (ex. Skip-gram, C-BOW etc.) 알고리즘에 의해 dense vector representation으로 변환되어 입력되는데, 이는 곧 RNN에 입력되는 개별 입력이 벡터로 표현됨을 뜻한다.

이렇게 어떤 데이터가 하나의 데이터포인트(벡터)로 서로 직교하는 축을 갖는 벡터공간의 한 요소로 표현될 수 있다면, 그것을 보통 Euclidean space에 존재한다고 한다. 다음 그림은 그러한 공간의 예시를 보여준다.

![그림2](https://user-images.githubusercontent.com/76824867/160383694-dde462ad-6988-49d0-b287-ee7e87ee1b5b.png)

CNN, RNN 계열의 모델은 이전 세대의 고전적인 머신러닝 모델들이 정형데이터를 잘 다루었던 것을 넘어, 비정형데이터인 이미지와 자연어를 잘 학습한다는 강점으로 떠올랐다. 그러나 이러한 모델은 모두 입력 데이터가 유클리디언 공간에 존재한다는 가정을 기반으로 성립되었다.

<br>

### The Graph Neural Network (IEEE 2019)

그럼 GNN은 뭐가 다를까? 우선 그래프에 대해 알아보자. 

그래프는 **정점(Vertex, Node)과 간선(Link, Edge)의 집합**으로 표현되는 범용적인 자료구조이다. 여기서 노드는 어떤 객체들의 정보를 나타내고, 엣지는 그러한 객체들 사이의 추상적인 관계를 표현하는 개념으로 이해하면 적절하다. 

그래프의 엣지가 방향성이 있으면 Directed, 없으면 Undirected 그래프라고 한다. 만약 엣지가 단순히 연결성을 표현하는 것 이상으로 특수한 가중치가 할당되어 있다면 Weighted, 없다면 Unweighted 그래프라고 한다.

![그림3](https://user-images.githubusercontent.com/76824867/160383695-3fe5cd52-22f8-41c5-acd2-347fbd5a0b50.png)

그래프로 표현될 수 있는 구조는 어디에나 있다. 위 그림과 같이 여러 원자의 조합으로 구성되는 분자는 그 자체로 그래프이다. 원자는 노드로 표현되고, 원자 간 결합은 엣지로 표현될 수 있다. 성과 같은 건축물이 있다면, 건축물의 개별 파츠는 노드로 표현되고, 파츠 간의 결합은 엣지로 표현될 수 있다. 인터넷은 어떨까? 인터넷은 수많은 HTML 페이지들이 하이퍼링크를 통해 연결되어 있다. 각 페이지는 노드로 표현되고, 하이퍼링크는 엣지로 표현될 수 있다.

우리가 배우게 될 GNN은 이러한 그래프 구조를 학습해야 한다.

<br>

### Notation and Principles

그럼 이제부터 약간 어려운 내용을 배워보자. 지금부터 설명할 내용은 2009년에 발표되었던 하나의 Graph Neural Network 논문을 기반으로 한다. 해당 논문에서 일부 이미지와 수식을 다음과 같이 발췌하였다.

![그림4](https://user-images.githubusercontent.com/76824867/160383698-92cab578-b083-4225-8b05-79bb74a79d2d.png)

위 그림에서 왼쪽을 먼저 보자. 그림과 같은 임의의 그래프 구조가 주어졌을 때, 우리는 1번 노드인 $l_1$에 주목하는 상황이라고 하자. 지금부터 우리가 하려는 것은, 우리가 관심을 갖고 바라보는 한 노드의 정보를 어떻게 업데이트시킬 것인지에 대해서이다.

그림을 보면 다음과 같은 수식이 적혀있다.

$$ x_1 = f_w (l_1, l_{1, 3}, l_{1, 4}, l_{1, 6}, x_2, x_3, x_4, x_6, l_2, l_3, l_4, l_6) $$

여기서 $x_i$는 노드 $i$의 특성벡터를 의미한다. $l_i$는 노드 $i$의 라벨을 의미하고, $l_{i, j}$는 노드 $i$와 $j$ 사이의 엣지를 표현한다. 그리고 $f_w$라는 함수가 있는데, 해당 논문에서 이는 Local Transition Function으로 언급되어 있다.

갑자기 여러 수식이 나와서 어렵게 느껴질 수도 있지만, 사실 핵심내용은 간단하다.

지금부터 우리는 $f_w$라는 특수한 함수를 사용할 것인데, **이 함수는 어떤 노드의 주변 노드, 엣지 정보를 모두 포함해서 그 결과로 중심노드의 정보를 업데이트**한다. 이 함수의 작용은 한번이 아니라, **여러번 반복**될 수 있고, **최종적으로 $g_w$로 표현되는 Local Output Function에 의해 최종출력**이 만들어질 것이다.

대문자로 표현된 수식은 개별 노드가 아니라 그래프 전체의 Global한 관점에서 연산을 행렬로 표현한 것일 뿐이다.

<br>

### Generalization of Recurrent Neural Network

이제 방금 배운 $f_w$, $g_w$ 함수를 조금 다른 그림으로 바라보자. 미리 말하자면, $f$와 $g$는 Parametric Function이다. 즉, 일종의 Neural Network로 생각해도 된다.

다음 그림을 보면, 왼쪽의 4개의 노드와 4개의 엣지로 구성된 작은 그래프가 있다. 주어진 그래프에 대해 방금 배웠던 Local Transition Function과 Local Output Function의 작용을 계산 그래프로 표현하면 중간의 도식이 된다. 원 논문에서 $f$와 $g$는 MLP의 일종으로 표현된다.

![그림5](https://user-images.githubusercontent.com/76824867/160383700-69b88660-6b5b-4af1-8f73-4f8773667324.png)

이제 위에서 본 그림을 다시 한번 변형해보자. 다음 그림에서 왼쪽은 위의 상황을 조금 더 보기 좋은 형태로 정리한 것이다. 이제 $f_w$라는 함수의 작용이 연속적으로 일어나고, 최종적으로 $g_w$ 함수의 영향을 받아 어떤 값이 최종 출력되는 모양이 확연히 보인다. 

![그림6](https://user-images.githubusercontent.com/76824867/160383703-f0e8020f-dedf-44a3-aa84-eb305abb2139.png)

그런데 이 모양. 어디서 본 것 같지 않은가?

앞서 설명했던, 자연어처리 분야에서 자주 사용되는 RNN은 주어진 입력에 대해 Recurrent하게 반복된 연산을 한다. 그리고 원 논문에서 Embedding Network로 표현되는 $f_w$ 함수도 마찬가지로 Recurrent하게 반복되고 있다.

사실 여기서 논문의 주장이 모두 나왔다. 

**결국 논문의 주장은, Graph Neural Network에서 Graph의 노드 정보를 업데이트하기 위한 연산이, 이미 사용되고 있는 RNN의 Generalization으로 볼 수 있다는 것이다.** RNN은 이미 **Back-Propagation-Through-Time (BPTT)**에 의해 학습 알고리즘이 정립되어 있으니, 동일한 원리에 의해 Graph Neural Network도 학습가능한 모델로 기능할 수 있다!

2009년에 발표된 이 논문은, **Graph Neural Network가 RNN의 Generalization으로서 학습이 가능하다**는 사실을 직관적으로 설명하고, 뒷 부분에서는 정량적인 증명으로 내용을 전개하고 있다. 수학적인 증명은 대부분 미분의 연쇄법칙과 목적함수의 최소화 과정을 지루하게 설명한 것이기에 여기서는 넘어가도록 한다.

<br>

### Graph Convolution Network (GCN) by Kipf & Welling, 2017

이제부터 좀 더 본격적으로 GNN에 대해 알아보자. GNN이 학습가능하다는 사실이 증명된 이후로, 기존의 Convolution과 Recurrence 연산을 그래프 도메인에 대해 일반화하려는 많은 연구들이 발표되었다. 굉장히 많은 논문들이 있지만, 그 중에서 대표적인 한 연구를 설명하려고 한다. 설명의 기반이 되는 논문은 **2017년, Kipf & Welling**에 의해 발표되었던 **Semi-Supervised Node Classification** 상황에서의 **Graph Convolution Network (GCN)** 이다.

다음 그림을 보자. 우리의 GNN이 해야 하는 것은 노드의 정보를 여러 은닉층을 통해 업데이트시키고, 개별 노드의 정보 $Z$가 라벨 $Y$와 일치하도록 학습하는 것이다.

![그림8](https://user-images.githubusercontent.com/76824867/160383704-ed7d8dea-8e49-400c-b6d2-24a112d8746f.png)

이미지를 학습하기 위해 CNN에서 국소적인 영역의 여러 Pixel들의 관계를 학습하려 했던 것처럼, 이제는 그래프에서 특정한 노드와 그 주변 이웃노드들 사이의 관계를 학습하려고 한다. 즉, CNN에서 사용되었던 Spatial Filter Convolution의 개념을 Graph로 확장한 것이라 할 수 있다.

이러한 Graph Convolution에 의해 충분히 업데이트된 그래프는 Graph-level Task 상황에서 Readout(또는 Graph Pooling) 레이어를 통과하며, 그래프 레벨의 vector representation으로 변환될 수 있다. 이후에는 평범하게 MLP 등에 입력되어 학습을 할 수 있게 된다.

<br>

### Graph Convolution Example

그럼, Graph Convolution 이라는 연산을 살짝 알아보자. 다음 그림과 같이 8개의 노드와 7개의 엣지로 구성된 간단한 그래프가 있다고 하자.

그래프 안에서 노드 사이의 연결정보는 인접행렬(Adjacency Matrix)로 불리는 $N \times N$ 크기의 Binary Matrix로 표현된다. 각 노드는 고정된 크기의 특성벡터로 표현되고, 이러한 벡터들이 노드의 개수 $N$ 만큼 쌓여서 Node Attribute Matrix $X$를 정의한다.

이제 신경망의 한 층에 대응되는 Trainable Weight Matrix $W$를 생각하자. $W$는 먼저 행렬 $X$와 행렬곱을 하여 $S$라는 결과를 얻는다.

![그림9](https://user-images.githubusercontent.com/76824867/160383705-2b5f8482-442d-4467-87b8-1cf89f9739fa.png)

여기서 $S$의 우변을 보면, 가중치와 벡터성분의 곱의 전체합이 성분으로 담겨있음을 알 수 있다. 이는 어떤 중심노드에 대하여, 주변노드의 정보를 가중치화하여 모두 더한 값을 중심노드 쪽으로 보내 업데이트하겠다는 의미를 나타낸다.

결국 다음 그림과 같이 (우리가 7번 노드에 주목한다고 하면), 7번 노드는 주변에 연결되어 있는 3, 4, 6, 8번 노드로부터 가중치화된 정보(Message)를 받아, 임의의 방식으로 업데이트된다. 

![그림10](https://user-images.githubusercontent.com/76824867/160383706-8d8ee404-de24-4c74-ae3d-86a344d15a62.png)


### Overall Structure of GNN

결국 GNN의 대략적인 구조는 다음 그림처럼 표현될 수 있다.

![그림11](https://user-images.githubusercontent.com/76824867/160383710-44234196-e3d5-4725-b117-0431af0eb936.png)

즉, Input으로 들어온 그래프 정보는 Graph Convolution Layer를 여러번 지나면서 매번 업데이트되고, 상황에 따라 필요하다면 Readout 층을 통과하며 Graph representation의 벡터가 될 수 있다. 그리고 이러한 벡터는 이제 문제상황에 적합한 그래프 정보를 잘 표현할 것이므로, MLP와 같은 평범한 Feed-forward Neural Network에 입력되어 학습될 수 있다.

논문마다 조금씩 표현이 다르지만, 여기서 설명한 Graph Convolution $\rightarrow$ Node Update $\rightarrow$ Readout의 프로세스는 요즘은 **Message Passing Scheme**이라는 표현으로 더 자주 언급되는데, 이는 2017년에 양자화학 분야에서 발표되었던 Gilmer의 **Message Passing Neural Network (MPNN)** 논문의 영향인 것 같다.

<br>

### Downstream Tasks by GNN

다음 그림은 다양한 문제상황에서 GNN이 활용되는 구조를 보여준다. 그래프 학습이 가능하다는 점을 제외하면, 기존의 컴퓨터비전, 자연어처리 분야에서 활용되는 모델 구조와 크게 다르지 않다.

![그림12](https://user-images.githubusercontent.com/76824867/160383713-749383f5-bce8-438f-a5da-b5b84af881e2.png)

* 왼쪽 위의 그림은 예를 들면, 그래프 정보를 입력받아 그래프의 노드 정보 또는 노드 라벨을 학습하는 Node Classification 상황에 적합해보인다.
* 오른쪽 위의 그림은 그래프 정보를 입력받아, Encoder로 그래프 특성을 학습하여 은닉벡터(Latent Representation) $z$를 생성하고, Decoder로 원형 그래프를 재현하는 방법을 학습하는 Graph AutoEncoder (GAE)의 전형적인 모습을 보여준다.
* 왼쪽 아래 그림은 그래프를 입력받아, Graph level representation을 얻고, 이를 MLP에 넣어 그래프 레벨 분류문제를 하는 상황에 적절하다.
* 마지막으로 오른쪽 아래의 그림은 조금 특이한데, Spatio-Temporal GNN이라 불린다. 이는 그래프의 공간정보와 시간정보를 동시에 학습하는 구조라고 알려져 있는데, 논문으로 읽어보았을 뿐 실제 코드로 연구에서 활용한 적은 없다. 아마도 Temporal GNN을 공부하게 되면, 더 깊게 이해할 수 있을 것 같다.

<br>

## Main Idea of CGCNN (2018)

이제 GNN에 대해 알았으니, 이를 계산물리학 분야의 고체결정에 대하여 적용한 Crystal Graph Convolution Neural Network (CGCNN)에 대해 알아보자. GNN을 공부하고 CGCNN을 보면, 사실 아주 특별한 점은 별로 없다.

다음 그림의 (a)는 NaCl 이온결정처럼 보이는 규칙적인 결정구조가 원자를 나타내는 노드와 원자간 결합을 나타내는 엣지로 변환되어 그래프 구조로 변환되는 도식을 보여준다. 물론, 변환과정이 아주 단순하지는 않고, 실제로는 조금 귀찮은 전처리 과정이 들어간다. 예를 들어, 원자는 원자번호에 따라 초기 임베딩 벡터를 어떻게 처리해야 할지에 대한 정보가 필요하고, 원자간 거리를 측정한 뒤, 이를 오름차순으로 정렬하고, Gaussian Expansion이라는 변환을 통해 Edge Attributes로 바꿔주어야 한다.

그러나 이러한 전처리는 고체물리학 도메인 지식을 갖고 있다면 누구나 어렵지 않게 할 수 있다. 중요한 것은 **이제부터 물질의 특성에 대한 연구를, 그래프 구조를 다루는 문제로 바꿔 접근할 수 있다**는 것이다.

![그림4](https://user-images.githubusercontent.com/76824867/161016986-2fe13df6-3835-40d5-9b46-fe2be124ed43.png)


그림 (b)는 그래프 구조로 변환된 Crystal Graph가 GNN에 입력되는 도식을 보여준다.

오른쪽의 수식들은, CGCNN 논문에서 표현하는 모델의 작용을 나타낸 수식이다.

예를 들면, 오른쪽 위의 첫번째 수식은 중심노드 $i$의 정보가 주변노드 $j$의 정보를 기반으로 Graph Convolution을 거쳐 업데이트된다는 사실을 말해준다. Graph Convolution은 여러 층의 레이어를 통해 여러번 노드 정보를 업데이트할 수 있고, 최종적으로 Pooling 연산에 의해 Graph level의 정보를 표현하는 vector representation이 얻어진다. 이러한 모델의 출력은 학습데이터의 $Y$ 값과 비교되어 Cost Function이 정의되고, 이러한 손실을 최소화하는 방향으로 GNN을 구성하는 내부 가중치 파라미터 $W$들이 학습된다.

아마 데이터마이닝 분야에서 GNN을 배운 학생이라면, 이 모델이 GNN의 단순한 응용처럼 느껴질지도 모르겠다. 하지만, 저자는 해당 논문에서 기존의 Graph Convolution을 수정하여 결정구조 도메인에 적합한 성능을 이끌어내는 조금 특수한 Convolution 수식을 제안하였다.

수식을 보면, $z_{(i, j)}_k^t가 서로 다른 두 종류의 Parameterized 선형변환을 통과하고, 서로 다른 두 종류의 비선형 함수의 작용을 받아 처리되어 (CGCNN 코드에 의하면, 각각 Sigmoid 함수와 Softplus 함수), Concatenation으로 하나의 벡터로 합쳐진다는 것을 알 수 있다.

이 논문을 처음 보았을 때는 이 수식의 의미를 별로 깊게 생각하지 않고, 그냥 저자가 여러가지 방법으로 실험해보다가 괜찮은 구조를 찾고 수식화한 것이구나, 정도로 이해했었는데, 지도교수님의 말씀에 따르면 그렇지 않은 것 같았다.

지도교수님의 말씀으로는, 벡터 $z$를 두 가지 서로 다른 방식으로 연산하는 것은 노드 정보에 대한 일반적인 그래프 컨볼루션을 수행하면서, 동시에 주변노드에 대한 가중치까지 학습하기 위한 의도인 것 같다고 하셨다. 아마 가중치라는 말을 듣는 시점에서 데이터마이닝 쪽 학생들은 2018년 ICLR에 발표되었던 Graph Attention Network (GAT)를 떠올릴 것 같다. CGCNN 저자가 연구할 당시에 GAT의 개념을 알았는지 알 수 없으나, 특정 도메인에 GNN을 적용하는 과정에서 GAT와 유사한 발상으로 Graph convolution을 최적화한 것은 다소 놀랍다. (역시 MIT 물리학과 박사과정의 위엄이다. 나는 이런거 못한다..ㅠ.ㅠ)

<br>

## CGCNN Performance

다음 그림은 CGCNN에 대하여 Materials Project에서 47000개의 페로브스카이트 데이터셋을 학습하여 얻어진 물성예측 결과를 보여준다.

그림 (a)는 각 결정구조가 Unitcell 안에서 갖고 있는 구성원자의 분포를 보여준다. Perovskite는 $ABX_3$의 화학식을 갖고 있고, 결정구조는 무한한 주기적 경계조건을 가지지만, Unitcell을 보면 (일부러 확장하여 계산하지 않는 한) 생각보다 원자 수가 그렇게 많지 않다. 이는 Crystal Graph가 GNN 분야에서 자주 사용되는 Benchmark Dataset, 예를 들면 Cora, Citeseer, PPI 등과는 다르다는 점을 보여준다.

그림 (b)는 학습에 사용된 결정구조의 수에 따라 물성예측의 오차(MAE)가 감소하는 것을 보여준다. 이것은 딥러닝을 공부한 사람 입장에서는 자연스러운 결과이므로 따로 설명이 필요없을 것 같다.

![그림5](https://user-images.githubusercontent.com/76824867/161016995-74f5a540-adf2-4a51-9aae-5b25c6cff41b.png)


그림 (c)는 모델이 예측하는 에너지와 DFT 계산에 의해 얻어진 에너지가, 동등한 수준에서 선형관계로 잘 일치하고 있음을 보여준다. 즉, CGCNN은 DFT와 유사한 수준의 정확도 및 그보다 훨씬 빠른 Inference 능력을 갖고 있다.

그림 (d)는 CGCNN을 물성예측(Regression)이 아니라, Metal/Semiconductor을 이진분류(Classification)하는 문제에 적용했을 때 분류 성능을 보여준다. 물리화학 분야에서는 물성예측에 비하면, 물질의 분류는 상대적으로 쉬운 편에 속하기 때문에 당연히 준수한 결과가 나왔다.

오른쪽의 Table 1은 7가지 주요한 물성예측에 대해 모델학습에 사용된 훈련 데이터의 수, 물성의 단위, 학습된 모델의 오차와 DFT 오차의 비교를 보여준다. 생각보다 적은 수의 데이터(MNIST 예제데이터보다 적은 수)로 DFT 수준의 오차를 갖는 모델 학습이 이루어질 수 있다는 점이 흥미롭다.

<br>

## Performance Test : Energy per Atom

CGCNN 논문을 읽고나서 이게 정말 가능한지 궁금해서, 코드 리뷰 이후 한가지 물성에 대하여 CGCNN 연구를 재현해보기로 하였다. 내가 선택했던 물성은 'Energy per Atom'이었고, 이는 Materials Project 계산과학 데이터베이스에서 약간의 Python API를 다룰 줄 알면 누구나 사용할 수 있다.

결정구조 데이터를 Python으로 다룰 경우, **PyMatgen (Python Materials Genomics)**를 활용하면 매우 편리하다.

다음 그림은 Pymatgen을 이용하여, 특정한 CIF(Crystallographic Information File) ID를 갖는 물질의 구조정보를 가져온 것이다. Pymatgen Structure 객체는 Primitive space에서 Unitcell을 구성하는 Lattice Parameter, 결정을 구성하는 원자 종류, 그리고 Cartesian 또는 Fractional Coordinates 기준의 원자좌표를 입력받아 정의된다.

![그림16](https://user-images.githubusercontent.com/76824867/160383724-860892a9-0158-4141-9de8-a99b95b9d2c9.png)


또한, Structure 객체는 다양한 메서드를 제공하는데, 이것을 이용하면 전처리를 좀 더 쉽게 할 수 있다. 실제로 CGCNN 저자는 전처리 과정에서 Pymatgen을 적극적으로 활용하여 Crystal Graph의 노드와 엣지 정보를 전처리하였다.

다음 그림은 CGCNN의 학습과정을 캡처한 것이다. Target Property는 Energy per Atom이고, 총 40 Epochs로 학습하였다. 또한, Original CGCNN은 Torch만으로 작성되었으며, 요즘 GNN 연구에 자주 사용되는 PyG나 dgl은 전혀 사용되지 않았다. 즉, Torch 레벨에서 데이터 전처리, Graph Batch를 위한 Collate Function, Custom Layer 등을 모두 구현하였기 때문에 코드가 상당히 길다. 코드가 불필요할 정도로 길고, 남의 코드는 자유롭게 다루기 불편해서, 내 연구에서는 거의 동일한 GNN을 PyG 형식으로 리팩토링하여 사용하고 있다.

![그림17](https://user-images.githubusercontent.com/76824867/160383725-437e9f9e-e0c9-4f30-88a9-6f006c40d749.png)


그림을 보면, 각 Epoch마다 MAE 값이 보이고 그 값은 최종적으로 약 0.1 수준임을 알 수 있다. 이는 CGCNN 논문의 주장과 일치하므로 부분적인 재현성을 확인할 수 있었다.

실제로 CGCNN을 사용하면서 다소 특이하다고 생각했던 점은, 학습과정에서 최초의 1 Epoch에 걸리는 시간이 굉장히 오래 걸렸다는 점이다. 아마 데이터를 전처리하고 Batch 단위로 받아오는 과정에서 시간이 오래 걸리는 것 같은데, 그 이후의 Epoch 에서는 그렇게 오랜 시간이 걸리지 않았다. PyG 버전으로 수정된 CGCNN에서는 매 Epoch마다 거의 일정한데, 왜 이런 현상이 발생하는지는 의문이다. ㅎㅎ

이렇게 해서 지금까지 응집물리학 분야에서의 GNN 응용에 대한 기초적인 내용을 살펴보았다. 그럼 이 분야는 이제 연구할 주제가 없을까? 사실 많이 남아있다. 그 중 한가지를 소개하겠다.

<br>

## Challenge : Property Prediction of Non-equilibrium States

대부분의 계산과학 데이터베이스는 보통 연산의 최종결과에 관심이 있다. 즉, DFT 등의 시뮬레이션 기법으로 물질을 계산하면 여러가지 Optimization이 가해지고, 그 과정에서 물질은 점점 안정된 구조로 변화되기 시작한다. 시뮬레이션이 끝나면, 최적화된 구조에서 물질의 Unitcell Lattice Parameter, 각 원자의 Coordinates, Free Energy, Basis 등이 얻어진다.

물리적 관점에서, 어떤 물질이 안정적(Stable), 또는 준안정적(Meta-stable)하다는 표현은 에너지가 안정된 상태라는 뜻이기 때문에, Hamiltonian(에너지) 함수의 관점에서 보면 물질은 국소적 최소점(local minimum)의 한 점에 있는 것과 같다. 따라서 그러한 상태의 물질은 local states에 있다고 한다.

그러나 물질의 상호작용은 Local states만 있는 것이 아니다. 안정된 상태가 있다면, 반대로 불안정하고 열적요동(Thermal Fluctuation)이 있는 비평형상태가 있으며, 물리학자들은 이런 상태에 대해서도 물성예측을 하고 싶어했다.

다음 그림은 내가 예전에 세미나에서 발표했던 자료의 일부이다.

![그림6](https://user-images.githubusercontent.com/76824867/161017005-4ccda0b6-dec2-40ce-b1bb-ad649cacbe37.png)

그림의 왼쪽을 보면, 질서정연하게 배열된 입자구조가 보인다. 이렇게 규칙적인 구조는 보통 에너지 관점에서도 안정적인 평형상태가 된다. 위 그림의 오른쪽을 보면, 여러 입자들이 불규칙하게 흩어져 있고, 입자간의 결합도 끊어져 있는 것을 알 수 있다. 이런 상태를 비평형상태라고 한다.

이러한 비평형상태에서의 물성예측은 사실 평형상태에서의 예측과 크게 다를 것 같지 않다. 데이터를 입력하여 딥러닝 모델을 훈련시키면 끝 아닐까? 

사실 데이터만 충분히 있다면 그게 가능할 것 같다. **문제는 대부분의 계산과학 데이터베이스에는 평형상태에 대한 자료만이 있으므로 비평형상태에 대한 물성예측을 학습시키고 싶어도 데이터가 없다는 것이다**.

그래서 요즘 이쪽 분야에서 발표되는 연구는 대부분, 연구원들이 관심있어하는 특정 물질에 한정하여 DFT 시뮬레이션으로 데이터를 생성하고, 그 데이터에 대한 분석이나 학습을 통해 유의미한 결과를 내는 방식이 많은 것 같다.

이와 관련하여 또 하나의 재미있는 연구를 소개한다.

<br>

## Related Research by Tian Xie

![그림7](https://user-images.githubusercontent.com/76824867/161017013-33302430-4049-47ab-bdf0-ce84b7ab00ea.png)

CGCNN 저자는 Unsupervised Graph Neural Network를 이용하여, Graph Sequence 형태의 데이터에 대해 Sequence적인 성질을 예측하는 연구를 발표한 적이 있다. 

간단히 해당 논문을 요약하자면, DFT를 이용하여 Ab-initio Molecular Dynamics 시뮬레이션을 하였고, 그 결과 얻어진 여러 입자들의 열적요동의 시간적변화를 일종의 Graph sequence 데이터로 전처리하여, 모델학습시켰다는 것 같다.

특이하게도 다름 그림과 같이, 모델에서 Feature Extraction을 위한 신경망으로 2대의 shared weight를 갖는 GCN이 사용되었으며, 두 GCN의 결과로 생성되는 벡터를 합쳐 VAMP loss라는 손실함수를 정의하고, 해당 손실함수에 대한 최적화 과정을 수행하여, MD simulation 속에서 Markov Process 패턴을 발견하였다고 한다.

![그림8](https://user-images.githubusercontent.com/76824867/161017024-8f6e2b47-8888-4296-826c-12a801ca0d05.png)

즉, 저자는 4종류의 Markov state가 있음을 밝혀내었고, 4개의 state들 사이의 전이확률(Transition Probability)까지 밝혀내어, 특정한 물질의 MD Simulation에 대한 유의미한 성과를 내었다.

![그림9](https://user-images.githubusercontent.com/76824867/161017029-bc466537-39ef-401a-926d-6013f54d26bc.png)

개인적으로 상당히 독창적인 연구라고 생각한다. 왜냐하면 일반적으로 MD Simulation에서 그 정도의 유의미한 관측 결과를 얻어내려면 상당히 오랜 시간 계산을 해야 하는데, 저자는 논문에서 수천개 정도의 MD trajectory로 해당 결과를 얻어내었기 때문이다! (나도 이런 연구 해봤으면.. )

<br>

## Summary

이렇게 해서 Graph Neural Network 및 계산물리학에 관한 글을 끝마치게 되었다. 내 블로그에서 이 글이 항상 검색의 상위권에 있었기 때문에, 제대로 마무리짓지 못한 글을 다시 한번 정리해야겠다고 마음먹고 있었다. 하지만 그 동안 엄청나게 바빠서 도저히 그럴 틈이 없었고, 이제서야 글을 마무리짓게 되었다. 

GNN이나 DFT는 모두 대단히 방대하고 어렵다. 그러나 제대로 익혀두면 응용가능성도 많은 분야이다. 나는 2가지 모두 못하는 바보 대학원생이지만, 그 동안 공부했던 내용의 정리를 위해 이 글을 쓰게 되었다. 잘못된 내용에 대한 지적이나 질문은 언제든 환영한다. ㅎㅎ

<br>

## References

* https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.120.145301 : CGCNN
* https://github.com/txie-93/cgcnn : CGCNN Repository
* https://ieeexplore.ieee.org/document/4700287 : 2009, GNN
* https://arxiv.org/abs/1609.02907 : GCN
* https://www.nature.com/articles/s41467-019-10663-6 : GDN
* https://arxiv.org/abs/1710.10903 : GAT
* https://en.wikipedia.org/wiki/Density_functional_theory : DFT
* https://dcollection.kangwon.ac.kr/srch/srchDetail/000000032796
* https://iopscience.iop.org/article/10.1088/2515-7639/ab084b : from DFT to machine learning

---
