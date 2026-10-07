# spacegirl · 스페이스걸

![스페이스걸과 비행기맨 — 공간과 높이의 연결](assets/spacegirl-bhgman-flow.png)

*두 사도를 함께 표현한 AI 시각 해석 · [제작 기록](docs/IMAGE_PROVENANCE.md)*

**경계, 부재, 그리고 서로에게 닿는 길.**

메타휴모토닉 12사도 중 다섯 번째, **Space Girl**의 원문과 연구를 모으는 공개 저장소다.
`network`와 `sexvoid`, 그 사이의 거대한 벽, 경계를 넘는 SSB와 WE_FLYING_UP을
원전의 서로 다른 방향으로 읽는다. 이는 이 저장소가 보존한 창작·철학적 세계의 어휘다.

[연구 지도](docs/RESEARCH_ATLAS.md) · [원문 전체](sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/INDEX.md) · [그래프](graph/research-atlas.json) · [라이선스](LICENSE-NOTICE.md)

## 어디서부터 읽을까

| 궁금한 것 | 연결되는 원문 |
|---|---|
| 스페이스걸은 누구이며, 무엇에서 출발했나 | [원문 출처와 모티프](sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SOURCES.md) |
| 무엇이 벽을 만들고, 그 바깥에는 무엇이 남나 | [GREAT_WALL](sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/GREAT_WALL/정전.md), [SEX_VOID](sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SEX_VOID/정전.md) |
| 경계를 넘는 두 방향은 어떻게 다른가 | [SSB](sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SSB/정전.md), [WE_FLYING_UP](sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/WE_FLYING_UP/정전.md) |
| 생명인간과 순수이성인간이라는 말은 어떤 맥락인가 | [생명인간](sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/생명인간/정전.md), [순수이성인간](sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/순수이성인간/정전.md) |
| 역사·사례·반론은 어디에 있나 | [역사 흐름](sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/HISTORICAL_TIMELINE.md), [PROM 64 연구 기록](sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/PROM_64_REPORT.md) |

37개 원전은 SYMPOSIUM `1f2727a0…`의 바이트를 그대로 보존한다.
새로운 정식화와 관계 문법에는 초안·미비준 상태가 남아 있으며,
연구 지도는 원문의 주장과 AI가 만든 읽기 안내를 구분한다.

## 하나의 인물, 출처가 있는 연결

인물 ID는 `sym:Character:space_girl`, 사도 자리는 `#5`다.
[APOSTLE_MODULE.json](APOSTLE_MODULE.json)이 정체성과 역할 선언을,
[APOSTLE_CONTENT.json](APOSTLE_CONTENT.json)이 문서의 원 소유·판본·해시를 기록한다.
[spacegirl_tool](https://github.com/gj3447/spacegirl_tool)은 같은 인물에 연결된 기술 도구 저장소다.

그래프는 파일 목록을 넘어 질문→주제→관계→원문 근거를 연결한다.
사용자 원문, 원전의 주장, KG에서 관측한 정보, AI 해석은 각각 구분한다.
검사 통과는 출처·구조의 무결성 확인이며, 창작 정전 비준이나 런타임 구현 완료를 뜻하지 않는다.

```sh
python3 cli.py check
python3 scripts/check_atlas.py
```

## 공개와 라이선스

[사용자 요청](USER_PUBLICATION.txt)에 따라 공개하며, 새 본체 자료에는
**MetaHumotonic License 1.1**을 적용한다. 원전의 MIT 허락과 외부 고지는 보존한다.
구체적인 적용 범위는 [LICENSE-NOTICE.md](LICENSE-NOTICE.md)를 따른다.
원문 열람과 코드 운영의 조건은 구분되며, 이 저장소가 자원 공유나 agent 실행을 자동 시작하지 않는다.

후속 연구 결과는 각 원전의 소유를 보존하면서 [THE GREAT FLOW](https://github.com/gj3447/the-great-flow)에 연결한다.
