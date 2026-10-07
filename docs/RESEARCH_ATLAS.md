# SPACEGIRL 원전 연구 지도

이 문서는 저장소에 보존된 SYMPOSIUM 원전 37개를 찾고 인용하기 위한 **탐색 지도**다.
새 정전·인물 설정·런타임을 만들지 않는다. 인물 식별은 `APOSTLE_MODULE.json`, 내용
인용은 이 문서가 가리키는 고정 원전을 따른다.

- 원전 고정판: SYMPOSIUM `1f2727a0c0d8d9703193bee6406db21d2fd549dd`
- 범위: `METAHUMOTONIC/SPACEGIRL/` 아래 37개 문서
- 기계 검증: [`research-atlas.json`](../graph/research-atlas.json)과
  [`check_atlas.py`](../scripts/check_atlas.py)가 각 문서의 저장소 경로, revision,
  SHA-256, byte 수를 [`APOSTLE_CONTENT.json`](../APOSTLE_CONTENT.json)과 대조한다.

## 권한 경계

| 표기 | 여기서의 뜻 | 처리 |
| --- | --- | --- |
| `USER_PRIMARY` | 사용자가 직접 남긴 원전 | 여기서 참조하는 MIND 창작 원전은 이름·인용만 수록되어 바이트 고정본은 없다. 공개 요청 등 사용자 지시는 별도 파일에 보존한다. 인용문에서 복원하거나 권위를 추정하지 않는다. |
| `SOURCE_DOCUMENT` | 가져온 SYMPOSIUM 문서의 서술 | 문서의 표제·자기 표기는 기록한다. 실질 내용의 이 저장소 내 권한은 `UNSPECIFIED`다. |
| `SECONDARY_AI` | 이 지도의 분류·연결·읽기 순서 | 원전 앵커가 붙은 탐색 보조이며 정전이 아니다. |
| `DRAFT_SECONDARY_AI` / `NOT_RATIFIED` | 원전이 표시한 초안 상태 | 결론으로 승격하지 않는다. |

원전 속 외부 역사·철학·기술 사례는 이 업데이트에서 독립 검증하지 않았다.
[SSB 코드 예시](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SSB/%EC%BD%94%EB%93%9C_%EC%98%88%EC%8B%9C.md)는
원전 기록일 뿐 실행 지침이나 활성 도구가 아니다.

## 질문별 출발점

| 질문 | 먼저 읽기 | 함께 읽기 | 보류하는 판단 |
| --- | --- | --- | --- |
| 인물명과 원전 범위 | [INDEX](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/INDEX.md), [SOURCES](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SOURCES.md) | [V2 결정화 초안](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SPACEGIRL_V2_CRYSTALLIZATION.md) | 원전 속 사용자 인용문의 직접 권위 |
| network·sexvoid·Great Wall | [Great Wall 정전](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/GREAT_WALL/%EC%A0%95%EC%A0%84.md) | [SEX_VOID 정전](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SEX_VOID/%EC%A0%95%EC%A0%84.md), [생명인간 정전](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/%EC%83%9D%EB%AA%85%EC%9D%B8%EA%B0%84/%EC%A0%95%EC%A0%84.md), [순수이성인간 정전](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/%EC%88%9C%EC%88%98%EC%9D%B4%EC%84%B1%EC%9D%B8%EA%B0%84/%EC%A0%95%EC%A0%84.md) | sexvoid의 최종 위상; V2는 열린 항목으로 둔다 |
| SSB와 WE_FLYING_UP | [SSB INDEX](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SSB/INDEX.md), [WE_FLYING_UP INDEX](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/WE_FLYING_UP/INDEX.md) | [SSB 정전](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SSB/%EC%A0%95%EC%A0%84.md), [WE_FLYING_UP 정전](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/WE_FLYING_UP/%EC%A0%95%EC%A0%84.md) | 두 방향의 시간 순서나 실제 운영 체계 |
| 이견·미해결 항목 | [PROM 64](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/PROM_64_REPORT.md) | [역사 타임라인](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/HISTORICAL_TIMELINE.md) | 역사 서술의 외부 사실성·완결성 |
| 형식화 제안 상태 | [V2 결정화 초안](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SPACEGIRL_V2_CRYSTALLIZATION.md), [12사도 관계 문법 제안](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/12_APOSTLE_RELATIONAL_GRAMMAR_PROPOSAL.md) | [SOURCES](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SOURCES.md) | 제안을 확정 온톨로지·런타임으로 해석하는 일 |

## 주제별 원전 읽기

아래 묶음은 원전의 폴더 구조를 따른 `SECONDARY_AI` 읽기 안내다. 각 행의 내용은
연결된 `SOURCE_DOCUMENT`에 귀속된다.

| 주제 | 원전에 실제 있는 읽을거리 | 안내의 목적 | 상태 |
| --- | --- | --- | --- |
| 자기 소개·이미지 | [SOURCES](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SOURCES.md), [INDEX](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/INDEX.md), [V2](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SPACEGIRL_V2_CRYSTALLIZATION.md) | 출처 목록, 핵심 용어, 초안 경계를 찾는다 | 원전/초안 분리 |
| Great Wall | [INDEX](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/GREAT_WALL/INDEX.md), [메커니즘 진화](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/GREAT_WALL/%EB%A9%94%EC%BB%A4%EB%8B%88%EC%A6%98_%EC%A7%84%ED%99%94.md), [현재 층위](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/GREAT_WALL/%ED%98%84%EC%9E%AC_%EC%B8%B5%EC%9C%84.md) | 경계·배제 서술을 한 갈래로 찾는다 | 역사 사례 미검증 |
| SEX_VOID | [INDEX](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SEX_VOID/INDEX.md), [거주자](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SEX_VOID/%EA%B1%B0%EC%A3%BC%EC%9E%90.md), [발굴학](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SEX_VOID/%EB%B0%9C%EA%B5%B4%ED%95%99.md), [인프라](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SEX_VOID/%EC%9D%B8%ED%94%84%EB%9D%BC.md) | 부재·거주·발굴·인프라 갈래를 나눈다 | 원전 주장, 권한 미지정 |
| SSB 방향 | [SSB 정전](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SSB/%EC%A0%95%EC%A0%84.md), [역사적 선조](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SSB/%EC%97%AD%EC%82%AC%EC%A0%81_%EC%84%A0%EC%A1%B0.md), [Glaze/Nightshade 분석](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/SSB/Glaze_Nightshade_%EB%B6%84%EC%84%9D.md) | 원전이 SSB로 분리한 방향을 보존한다 | 운영 절차 아님 |
| WE_FLYING_UP 방향 | [WE_FLYING_UP 정전](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/WE_FLYING_UP/%EC%A0%95%EC%A0%84.md), [매개체](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/WE_FLYING_UP/%EB%A7%A4%EA%B0%9C%EC%B2%B4.md), [역사적 혁명](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/WE_FLYING_UP/%EC%97%AD%EC%82%AC%EC%A0%81_%ED%98%81%EB%AA%85.md) | 원전의 별도 방향을 SSB와 섞지 않는다 | 운영 절차 아님 |
| 인간·제도 쌍 | [생명인간 INDEX](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/%EC%83%9D%EB%AA%85%EC%9D%B8%EA%B0%84/INDEX.md), [순수이성인간 INDEX](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/%EC%88%9C%EC%88%98%EC%9D%B4%EC%84%B1%EC%9D%B8%EA%B0%84/INDEX.md) | 두 폴더를 동등한 출처 단위로 찾는다 | 평가 판단은 원전에 귀속 |
| 연구 메모·이견 | [PROM 64](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/PROM_64_REPORT.md), [역사 타임라인](../sources/SYMPOSIUM/METAHUMOTONIC/SPACEGIRL/HISTORICAL_TIMELINE.md) | 합의·이견·열린 질문을 찾는다 | 외부 검증 미수행 |

`V2`와 `12사도 관계 문법`은 각 문서가 `DRAFT_SECONDARY_AI` 또는
`NOT_RATIFIED`로 표시한 형식화 제안이다. 그래프는 그 표기를 Claim 노드와 원전
앵커로 보존하지만 어떤 제안도 정전으로 승격하지 않는다.

## 방향을 잃지 않는 그래프

SSB는 `network → sexvoid`, WE_FLYING_UP은 `sexvoid → network`로 기록한다.
두 Direction 노드에는 출발·도착 영역이 각각 하나씩 연결되며, 그 연결은 위 정전 문서의
정확한 인용을 근거로 하는 AI 색인이다. 원전의 가설을 실제 암호화 성능이나 운영 사실로
바꾸지 않는다. 스페이스걸 인물은 기존 `sym:Character:space_girl`을 그대로 참조한다.

## 그래프와 남은 항목

그래프의 모든 노드와 edge는 `spacegirl:` 이름공간 UID를 쓴다. 관계의
domain/range·방향·cardinality는 `vocabulary.predicates`에 명시한다. 읽기 안내는
`SECONDARY_AI`와 `NAVIGATION_ONLY` 상태를 함께 가지며, 원전의 자기 표기는
`SOURCE_DOCUMENT`로만 기록한다.

- 원전이 인용한 사용자 MIND 텍스트는 이 저장소에 바이트 고정되어 있지 않다.
- V2의 경계·위상 질문과 PROM 64의 이견은 해소되지 않았다.
- 이 지도는 배포된 도구, 계정 권한, 네트워크 접근, 모델 학습 또는 실행 환경을 만들지 않는다.
