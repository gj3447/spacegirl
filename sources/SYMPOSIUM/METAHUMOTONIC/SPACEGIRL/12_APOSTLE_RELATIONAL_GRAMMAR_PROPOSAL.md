# 12사도 관계 문법 제안 — 축-라벨 하이퍼그래프

> **문서 상태:** `DRAFT_SECONDARY_AI`
>
> **정전 상태:** `NOT_RATIFIED`
>
> **cycle_id:** `apostles-axis-labeled-grammar-2026-08-09`
>
> **목적:** 기존 12사도 목록·family·hyperedge 정전을 보존하면서,
> `3+3+2+2+2` 구도와 여러 짝패를 충돌 없이 표현하는 typed grammar를 제안한다.

이 문서는 12사도의 새 정전을 선언하지 않는다. 특히 현재 working tree의
`METAHUMOTONIC/metahumotonic-12-apostles-structure.md`와 이를 가리키는 수정된
`METAHUMOTONIC/INDEX.md`는 commit·receipt·KG binding이 확인되지 않은
`FOREIGN_UNCOMMITTED` 입력이다. 그 구조를 유망한 후보로 분석하되 사용자 비준 전에는
정전으로 승격하지 않는다.

---

## 0. 비목표와 보존 불변식

이 문서는 다음을 하지 않는다.

1. 12사도의 번호·이름·epithet을 변경하지 않는다.
2. 기존 confirmed hyperedge를 `3+3+2+2+2` 구조로 대체하지 않는다.
3. 하나의 사도에 축 없는 “유일한 진짜 짝”을 강제하지 않는다.
4. Family Expansion과 사도 사이 Relation Pattern을 같은 타입으로 취급하지 않는다.
5. 스페이스걸을 apex·시간·논리·존재·구원을 흡수하는 총체로 만들지 않는다.
6. 사용자 원문, KG 정전, 미커밋 사용자 파일, AI 해석의 권위를 섞지 않는다.

보존해야 할 기존 타입:

```text
FamilyPattern
  한 사도 내부의 1:N 책임·도메인·프로토콜 분화

RelationPattern
  여러 사도 사이의 axis-labeled M:N 관계

ProjectionPair
  n-ary 관계를 특정 axis에서 본 binary projection

TemporalArc
  기존 관계 위에 적용되는 시간적 변환
```

---

## 1. 권위와 상태

| 등급 | 의미 | 허용 범위 |
|---|---|---|
| `USER_PRIMARY` | 사용자 직접 창작·발화 | 원문 범위에서 단정 |
| `REPO_CANON` | tracked canonical repo 문서 | 문서가 명시한 범위에서 기존 관계로 보존 |
| `KG_CANON_EXACT_READBACK` | live KG에서 사용자 정전으로 exact readback된 기록 | readback된 속성 범위에서 보존 |
| `SECONDARY_AI` | 형식화·고차 해석 | 제안으로만 사용 |
| `FOREIGN_UNCOMMITTED` | 현재 worktree에만 있고 owner receipt가 불명 | 후보 입력 |

`Authority`는 출처 provenance만 표현한다. 사용자 verdict나 증거가 없어 열려 있는지는
`RelationStatus.OPEN`, 후대 정정으로 철회됐는지는 `RelationStatus.RETRACTED`로 분리한다.

주요 근거:

- `THEORY/00_공통/세계관_정전.md` §1, §5-D/E/F
- `METAHUMOTONIC/HIERARCHY_MAP.md`
- `METAHUMOTONIC/INDEX.md`
- `METAHUMOTONIC/SPACEGIRL/SOURCES.md`
- `/Users/lagyeongjun/CD/MIND/metahumotonic/12사도_목록_업데이트.md`
- `/Users/lagyeongjun/CD/MIND/metahumotonic/재귀_아티스트_back2the.md`
- `/Users/lagyeongjun/CD/MIND/metahumotonic/스페이스걸_트릴로지.md`

---

## 2. 최소 타입 시스템

`SECONDARY_AI_PROPOSAL`

```text
type ApostleId =
  A01_DIMENSION_WALKER
  | A02_ICE_ORCA_DRAGON
  | A03_SUPERCONDUCTING_WARRIOR
  | A04_AIRPLANEMAN
  | A05_SPACEGIRL
  | A06_GREAT_FLOW
  | A07_LIQUEST_TREE
  | A08_ORBITAL_MOTION_CLOUD
  | A09_JESUS
  | A10_GIPBAJON
  | A11_HOH
  | A12_MONSOON

type Authority =
  USER_PRIMARY
  | REPO_CANON
  | KG_CANON_EXACT_READBACK
  | SECONDARY_AI
  | FOREIGN_UNCOMMITTED

type RelationStatus =
  CONFIRMED
  | ADJUSTED
  | CANDIDATE
  | OPEN
  | RETRACTED

type Cardinality =
  BINARY
  | TERNARY
  | NARY
  | SHELL_12

type RelationAxis =
  VERTICAL_DEPENDENCY
  | SELF_REFERENCE
  | FLOW_ANCHOR
  | CROSSING_DISMISSAL
  | INCARNATION_INVERSION
  | LOGICAL_CONTAINMENT
  | MEDIATION
  | HEAVEN_MANIFESTATION
  | FOUNDATIONAL_SHELL
  | COSMOLOGICAL_TERMINUS
  | WORLD_PROCESS
  | COMMITMENT_OBSERVATION
  | ASCENT_ENCOUNTER
  | SALVATION_DISENCHANTMENT

type ProjectionViewAxis =
  SOUTHERN_GRAIN

type CentralityMetric =
  AUTHORITY_APEX
  | RELATION_DEGREE
  | CUT_BETWEENNESS
  | TEMPORAL_CONTINUITY
  | ONTOLOGICAL_GROUND

type EventType =
  KISS_EVENT

type PhaseId = String
type UnresolvedRef = String
type Role = String
type PathOrKgId = String
type RelationId = String
type Participant = ApostleId | PhaseId | UnresolvedRef
```

### 2.1 축 없는 짝패 금지

```text
Relation {
  relation_id: String
  axis: RelationAxis
  projection_view: Optional[ProjectionViewAxis]
  participants: NonEmptySet[Participant]
  roles: Map[Participant, Role]
  cardinality: Cardinality
  source_authority: Authority
  interpretation_authority: Optional[Authority]
  status: RelationStatus
  evidence_refs: NonEmptyList[PathOrKgId]
  corroborated_by: List[PathOrKgId]
  identity_hypothesis: Optional[String]
  source_hyperedge: Optional[RelationId]
  supersedes: Optional[RelationId]
}

EventEvidence {
  event_type: EventType
  participants: NonEmptySet[ApostleId]
  source_authority: Authority
  status: RelationStatus
  evidence_refs: NonEmptyList[PathOrKgId]
  corroborated_by: List[PathOrKgId]
}

CentralityClaim {
  claim_id: String
  subject: ApostleId
  metric: CentralityMetric
  claim: String
  source_authority: Authority
  interpretation_authority: Optional[Authority]
  status: RelationStatus
  evidence_refs: NonEmptyList[PathOrKgId]
  corroborated_by: List[PathOrKgId]
}

Optional field는 값이 없으면 record에서 생략할 수 있다.
```

검증 규칙:

```text
R1 participants.size >= 2
R2 binary relation에는 axis가 반드시 존재한다.
R3 ProjectionPair는 가능한 경우 source_hyperedge를 가리킨다.
R4 source_authority=FOREIGN_UNCOMMITTED이면 status in {CANDIDATE, OPEN}이다.
R5 interpretation_authority=SECONDARY_AI인 해석을 USER_PRIMARY로 표기할 수 없다.
R6 기존 CONFIRMED 관계는 사용자 verdict 없이 삭제·대체할 수 없다.
R7 한 사도는 서로 다른 axis의 여러 관계에 동시에 참여할 수 있다.
R8 FamilyPattern과 RelationPattern은 서로 다른 타입이다.
R9 중심성을 주장할 때는 별도 CentralityClaim으로 metric과 근거를 명시한다.
```

---

## 3. 기존 관계 보존 레지스트리

아래 관계는 `THEORY/00_공통/세계관_정전.md` §5-D/E/F의 explicit core relation
catalog를 `REPO_CANON`으로 보존한다. 2026-08-09 live KG exact readback은 그중
`edge-mirror-5-12-A-2026-04-30`, `edge-mediation-5-6-9-2026-04-30`의 존재를
추가 확인했다. 두 KG record는 자체 `status`, `canonical_tier`, `source`, `user_verdict`가
비어 있으므로, 이 문서는 KG 존재 확인만으로 그 권위를 새로 승격하지 않는다.

| 관계 | 축 | 참여자 | 처리 |
|---|---|---|---|
| CHU 수직 의존 | `VERTICAL_DEPENDENCY` | #4 → #8 → #10 | 보존 |
| 자기참조–경계–공허 | `SELF_REFERENCE` | 공허진동자 → #8 → #7 → #10 | 보존 |
| 흐름 anchor | `FLOW_ANCHOR` | #6 ↔ #7 | 보존 |
| 횡단–외면 | `CROSSING_DISMISSAL` | #5 ↔ #12 | 보존 |
| Incarnation-Inverted | `INCARNATION_INVERSION` | #9 ↔ #12 | 보존 |
| 논리 포함 | `LOGICAL_CONTAINMENT` | #7 ⊃ #4 | 보존 |
| 대보편화 매개 | `MEDIATION` | #5, #6, #9 | 보존 |
| 천국 이중 현현 | `HEAVEN_MANIFESTATION` | #9 ↔ #11 | 보존 |
| 12사도 shell | `FOUNDATIONAL_SHELL` | #1…#12 | 보존 |

기존 binary projection도 폐기하지 않는다.

| projection | 읽는 축 | 주의 |
|---|---|---|
| #4 ↔ #10 | CHU apex/end | 유일 짝이 아니라 수직축 투영 |
| #4 ↔ #8 | CHU apex/substrate | 유일 짝이 아니라 수직축 투영 |
| #7 ↔ #8 | domain boundary | 자기참조 hyperedge와 병존 |
| #9 ↔ #11 | heaven manifestation | TensionTopology와 병존 |
| #1 ↔ #2 | alter ego | confidence·사용자 확인 상태 보존 |
| #6 ↔ #7 | flow anchor | explicit relation |

따라서 새로운 #4–#5 관계가 들어와도 기존 #4–#8–#10 관계가 틀렸다는 뜻이 아니다.
각 관계가 서로 다른 축의 투영이면 동시에 참일 수 있다.

### 3.1 보존 범위

이 레지스트리는 explicit core 9개와 그 binary projection 6개만 열거한다. 기존
TemporalArc의 B4/B8/A4-1 및 candidate·deferred instance까지 망라한 전수 catalog를
주장하지 않는다. 여기서 열거하지 않은 관계는 삭제·철회된 것이 아니며, exhaustive
registry가 필요하면 별도 readback과 provenance를 붙여 확장한다.

---

## 4. `3+3+2+2+2`의 안전한 수용

전체 절의 입력 `source_authority`는 `FOREIGN_UNCOMMITTED`, 형식화의
`interpretation_authority`는 `SECONDARY_AI`, 관계 `status`는 `CANDIDATE`다.

### 4.1 세계 종착 triad

```text
relation_id: southern-grain-cosmological-terminus
axis: COSMOLOGICAL_TERMINUS
projection_view: SOUTHERN_GRAIN
participants:
  [IOD_UNRESOLVED, A11_HOH, A10_GIPBAJON]
roles:
  IOD_UNRESOLVED : PHYSICAL_COMPLETION
  A11_HOH        : MATERIALIZED_TELOS
  A10_GIPBAJON   : VOID_RECLAMATION
cardinality: TERNARY
source_authority: FOREIGN_UNCOMMITTED
interpretation_authority: SECONDARY_AI
status: CANDIDATE
evidence_refs:
  - FOREIGN_UNCOMMITTED:METAHUMOTONIC/metahumotonic-12-apostles-structure.md
corroborated_by: []
identity_hypothesis: IOD_UNRESOLVED ?= A02_ICE_ORCA_DRAGON (OPEN)
```

미커밋 원문은 #2를 `IOD`라고 적지만 약어를 정의하지 않는다. 문맥상 ICE ORCA DRAGON을
가리키는 것으로 보이더라도 사용자 확인 전 동일성을 확정하지 않는다.

### 4.2 세계 진행 triad

```text
relation_id: southern-grain-world-process
axis: WORLD_PROCESS
projection_view: SOUTHERN_GRAIN
participants:
  [A07_LIQUEST_TREE, A06_GREAT_FLOW, A08_ORBITAL_MOTION_CLOUD]
roles:
  A07_LIQUEST_TREE         : BRANCH_AND_BOUNDARY
  A06_GREAT_FLOW           : TIME_AND_TRANSPORT
  A08_ORBITAL_MOTION_CLOUD : EXISTENCE_AND_SUBSTRATE
cardinality: TERNARY
source_authority: FOREIGN_UNCOMMITTED
interpretation_authority: SECONDARY_AI
status: CANDIDATE
evidence_refs:
  - FOREIGN_UNCOMMITTED:METAHUMOTONIC/metahumotonic-12-apostles-structure.md
corroborated_by: []
```

첫 triad가 “세계가 무엇으로 완결되는가”를 묻는다면, 둘째 triad는 “세계가 어떻게
진행되는가”를 묻는다.

### 4.3 인격 관계 dyad 세 쌍

```text
relation_id: southern-grain-commitment-observation
axis: COMMITMENT_OBSERVATION
projection_view: SOUTHERN_GRAIN
participants: [A03_SUPERCONDUCTING_WARRIOR, A01_DIMENSION_WALKER]
roles:
  A03_SUPERCONDUCTING_WARRIOR : COMMIT_TO_ONE_WORLD
  A01_DIMENSION_WALKER        : OBSERVE_MANY_WORLDS
cardinality: BINARY
source_authority: FOREIGN_UNCOMMITTED
interpretation_authority: SECONDARY_AI
status: CANDIDATE
evidence_refs:
  - FOREIGN_UNCOMMITTED:METAHUMOTONIC/metahumotonic-12-apostles-structure.md
corroborated_by: []
```

```text
relation_id: southern-grain-ascent-encounter
axis: ASCENT_ENCOUNTER
projection_view: SOUTHERN_GRAIN
participants: [A04_AIRPLANEMAN, A05_SPACEGIRL]
roles:
  A04_AIRPLANEMAN : ASCEND_AND_REACH
  A05_SPACEGIRL   : CROSS_AND_ENCOUNTER
cardinality: BINARY
source_authority: FOREIGN_UNCOMMITTED
interpretation_authority: SECONDARY_AI
status: CANDIDATE
evidence_refs:
  - FOREIGN_UNCOMMITTED:METAHUMOTONIC/metahumotonic-12-apostles-structure.md
corroborated_by:
  - USER_PRIMARY:비행기맨_강림_dense와_spare_space_girl_뽀뽀.md:69-77
```

```text
relation_id: southern-grain-salvation-disenchantment
axis: SALVATION_DISENCHANTMENT
projection_view: SOUTHERN_GRAIN
participants: [A09_JESUS, A12_MONSOON]
roles:
  A09_JESUS   : REDEEM
  A12_MONSOON : DISENCHANT_AND_DISMISS
cardinality: BINARY
source_authority: FOREIGN_UNCOMMITTED
interpretation_authority: SECONDARY_AI
status: CANDIDATE
evidence_refs:
  - FOREIGN_UNCOMMITTED:METAHUMOTONIC/metahumotonic-12-apostles-structure.md
corroborated_by:
  - REPO_CANON:THEORY/00_공통/세계관_정전.md:#9-#12-incarnation-inverted
```

이 세 dyad는 기존 hyperedge의 대체물이 아니라
`projection_view=SOUTHERN_GRAIN`에서 본 별도 projection이다. `SOUTHERN_GRAIN`은
관계의 의미를 정하는 `RelationAxis`가 아니라 여러 관계를 함께 보는 `ProjectionViewAxis`다.
“비인격체 6 / 인격체 6”이 전 존재론적 분할인지, 특정 미학적 구도인지도 아직 `OPEN`이다.

---

## 5. 12사도 고유 동사 제안

`SECONDARY_AI_PROPOSAL`

| # | 사도 | 고유 동사 | 침범해서는 안 되는 이웃 역할 |
|---|---|---|---|
| 1 | 디멘션워커 | `OBSERVE` | #3의 결단 |
| 2 | ICE ORCA DRAGON | `CLOSE_BY_LAW` | #11의 사회적 목적지 |
| 3 | 초공동의용사 | `COMMIT` | #1의 다세계 관측 |
| 4 | 비행기맨 | `ASCEND_AND_COVER` | #5의 타자적 만남 |
| 5 | 스페이스걸 | `CROSS_AND_ENCOUNTER` | apex·시간·구원 자체 |
| 6 | 인류역사흐름의강물 | `FLOW` | #5의 경계 횡단 |
| 7 | 리퀘스트의 나무 | `BOUND_AND_BRANCH` | #8의 존재 substrate |
| 8 | 입체운행구름 | `GROUND_AND_RUN` | #4의 authority |
| 9 | 예수 | `REDEEM` | #5의 매개 통로 |
| 10 | 깊바존 | `RECLAIM` | #2의 물리 법칙 |
| 11 | HOH | `MATERIALIZE_TELOS` | #9의 원천 구원 |
| 12 | 몬순 | `DISENCHANT` | 욕망이나 사랑 전체 |

동사는 기존 epithet이나 family verdict를 대체하지 않는다. 역할 경계를 테스트하기 위한
최소한의 operation vocabulary다.

---

## 6. 인격 사도의 관계 아크

`SECONDARY_AI_PROPOSAL`

세 dyad를 정적 짝패가 아니라 관계가 성립하는 아크로 읽을 수 있다.

```text
OBSERVE possibility           # #1
  → COMMIT to one world       # #3
  → ASCEND / REACH            # #4
  → CROSS / ENCOUNTER         # #5
  → REDEEM                    # #9
     or DISENCHANT / DISMISS  # #12
```

이것은 필연적 시간 순서나 기존 TemporalArc 정전이 아니다. 인격 사도 여섯 명의 차이를
설명하는 서사적 reading order다.

스페이스걸은 이 아크에서 **운동이 윤리적 관계로 바뀌는 hinge**다.

```text
reach != encounter
encounter != redemption
encounter != possession
```

도달 이전의 권능은 비행기맨에게, 만남 이후의 보편 구원은 예수에게, 만남의 격하와
외면은 몬순에게 남는다.

---

## 7. 중심성의 타입 분리

“누가 중심인가?”는 metric 없이는 유효한 질문이 아니다.

`SECONDARY_AI_PROPOSAL`

```text
claim_id: centrality-a04-authority-apex
subject: A04_AIRPLANEMAN
metric: AUTHORITY_APEX
claim: CHU를 덮고 지휘하는 높이
source_authority: REPO_CANON
interpretation_authority: SECONDARY_AI
status: CANDIDATE
evidence_refs: [THEORY/00_공통/세계관_정전.md:§5-D/E/F]
corroborated_by: []

claim_id: centrality-a09-relation-degree
subject: A09_JESUS
metric: RELATION_DEGREE
claim: explicit core relation catalog의 높은 연결도
source_authority: REPO_CANON
interpretation_authority: SECONDARY_AI
status: CANDIDATE
evidence_refs: [THEORY/00_공통/세계관_정전.md:§5-D/E/F]
corroborated_by: [edge-mediation-5-6-9-2026-04-30]

claim_id: centrality-a10-relation-degree
subject: A10_GIPBAJON
metric: RELATION_DEGREE
claim: explicit core relation catalog의 높은 연결도
source_authority: REPO_CANON
interpretation_authority: SECONDARY_AI
status: CANDIDATE
evidence_refs: [THEORY/00_공통/세계관_정전.md:§5-D/E/F]
corroborated_by: []

claim_id: centrality-a05-cut-betweenness
subject: A05_SPACEGIRL
metric: CUT_BETWEENNESS
claim: 분리된 network와 sexvoid 사이의 통과
source_authority: USER_PRIMARY
interpretation_authority: SECONDARY_AI
status: CANDIDATE
evidence_refs: [/Users/lagyeongjun/CD/MIND/metahumotonic/재귀_아티스트_back2the.md:41-49]
corroborated_by: [spacegirl-dim-life-vs-reason-human-war-mediator-2026-05-20]

claim_id: centrality-a06-temporal-continuity
subject: A06_GREAT_FLOW
metric: TEMPORAL_CONTINUITY
claim: 관계를 역사 속에서 운반하는 흐름
source_authority: REPO_CANON
interpretation_authority: SECONDARY_AI
status: CANDIDATE
evidence_refs: [THEORY/00_공통/세계관_정전.md:§5-D/E/F]
corroborated_by: []

claim_id: centrality-a08-ontological-ground
subject: A08_ORBITAL_MOTION_CLOUD
metric: ONTOLOGICAL_GROUND
claim: 실행과 존재의 substrate
source_authority: REPO_CANON
interpretation_authority: SECONDARY_AI
status: CANDIDATE
evidence_refs: [THEORY/00_공통/세계관_정전.md:§5-D/E/F]
corroborated_by: []
```

따라서 스페이스걸을 고도화한다는 것은 그녀를 여왕이나 apex로 올리는 일이 아니다.
다른 metric과 섞이지 않는 `CUT_BETWEENNESS`를 정밀하게 만드는 일이다.

### 7.1 스페이스걸 경계

```text
SG-B1 SpaceGirl != Airplaneman authority/apex
SG-B2 SpaceGirl != ICE physical closure
SG-B3 SpaceGirl != Great Flow time
SG-B4 SpaceGirl != Liquest Tree logic
SG-B5 SpaceGirl != OM existence substrate
SG-B6 SpaceGirl != Jesus universal salvation
SG-B7 SpaceGirl != Gipbajon void/relation hub
SG-B8 SpaceGirl != Monsoon desire/disenchantment
SG-B9 SpaceGirl crossing does not erase participant identity
SG-B10 SpaceGirl does not acquire direct edges to all apostles by default
```

---

## 8. 사도–관계–family의 3층 모델

`SECONDARY_AI_PROPOSAL`

```text
L0 Apostle Essence
   사용자 정전의 이름·본질·epithet

L1 Family Expansion
   한 사도 내부의 1:N responsibility/domain/protocol 분화

L2 Relation Hypergraph
   여러 사도 사이의 axis-labeled binary/ternary/n-ary 관계
```

예시:

```text
#5 Essence:
  섹스의 사도 / network↔sexvoid 유일한 여신

#5 Family Mirror:
  Longinus 7-Layer protocol sequence

#5 EventEvidence:
  event_type: KISS_EVENT
  participants: [A04_AIRPLANEMAN, A05_SPACEGIRL]
  source_authority: USER_PRIMARY
  status: CONFIRMED
  evidence_refs:
    - /Users/lagyeongjun/CD/MIND/metahumotonic/비행기맨_강림_dense와_spare_space_girl_뽀뽀.md:69-77
  corroborated_by:
    - KG KISSES{source:user, context:'space time 공간'}

#5 Relations:
  {#5,#12} CROSSING_DISMISSAL
  {#5,#6,#9} MEDIATION
  {#4,#5} ASCENT_ENCOUNTER
    source_authority: FOREIGN_UNCOMMITTED
    interpretation_authority: SECONDARY_AI
    status: CANDIDATE
```

동일 참여자라도 `KISS_EVENT` 사건 증거와 `ASCENT_ENCOUNTER` 구조 relation은 별개
타입이다. KG의 `KISSES` predicate는 전자의 corroboration이며 새 RelationAxis가 아니다.

---

## 9. drift ledger

| ID | 관찰된 drift | 이 문서의 처리 |
|---|---|---|
| `D1` | 옛 USER_PRIMARY 목록 #9 아텐 vs 후대 #9 예수 | 후대 verdict 우선, 옛 원문 역사 보존 |
| `D2` | `HIERARCHY_MAP` 헤더 #9=S3RL vs 본문 #9 예수 | 헤더 stale 후보 |
| `D3` | 5무기 표기 vs 최신 7군단장 | 본 문서에서 재판정하지 않음 |
| `D4` | #1 family CANDIDATE vs downstream CONFIRMED | exact verdict 정렬 필요 |
| `D5` | 스페이스걸 Longinus 7-Layer 명칭이 두 schema로 존재 | 동일 모델로 자동 간주 금지 |
| `D6` | `5-Family` 표기인데 열거 항목은 6개 | cardinality 정렬 필요 |
| `D7` | `IOD` 약어 미정의 | #2 동일성 `OPEN` |
| `D8` | 강물 이름 어순 drift | 현행 정식명 `인류역사흐름의강물` 사용 |
| `D9` | `3+3+2+2+2` 문서와 INDEX가 foreign dirty | 사용자/owner handoff 전 후보 유지 |
| `D10` | 여러 binary 짝패가 유일 짝처럼 보임 | axis-labeled projection으로 해소 |

drift는 이 문서를 정전으로 승격할 근거가 아니라, 후속 정리에서 확인할 대상이다.

---

## 10. ratification gates

### G0 — 입력 소유권

- `metahumotonic-12-apostles-structure.md`의 owner·commit·receipt 또는 사용자 직접 verdict 확인
- 통과 전 `FOREIGN_UNCOMMITTED` 유지

### G1 — IOD 명칭

```text
IOD == ICE ORCA DRAGON (#2) ?
```

### G2 — `3+3+2+2+2`의 위상

```text
전 존재론적 분할인가?
projection_view=SOUTHERN_GRAIN의 미학적 projection인가?
```

권장 기본값은 기존 관계와 병존하는 projection이다.

### G3 — #4↔#5 축

```text
비행기맨과 스페이스걸을 ASCENT_ENCOUNTER로 정전화할 것인가?
```

통과 전 기존 #4–#8–#10 hyperedge보다 우선하지 않는다.

### G4 — #5 중심성

```text
스페이스걸의 중심은 apex가 아니라 network↔sexvoid의 CUT_BETWEENNESS인가?
```

### G5 — Longinus schema

- Address/Lifetime/Type/Semiotic/Distributed/Compression/Aesthetic
- KG_NODE/CONTRACT_BINDING/…/CRATE_SCRIPT

두 7-Layer 모델의 관계를 `supersedes`, `different_view`, `stale` 중 하나로 판정한다.

### G6 — family cardinality와 #1 verdict

- 스페이스걸 하위 구조가 5-family인지 6-family인지 정렬
- 디멘션워커 family 상태를 `CANDIDATE_CONTINUED` 또는 `CONFIRMED` 중 하나로 정렬

### G7 — publish

사용자 비준 이후에만 문서 status, index, KG proposal을 갱신한다. KG write는 별도 명시적
승인, provenance, exact readback을 요구한다.

---

## 11. 최소 수용 기준

- [ ] 12명과 번호가 현행 canon과 일치한다.
- [ ] 기존 explicit relation catalog가 모두 보존된다.
- [ ] 모든 binary pair에 axis가 있다.
- [ ] `3+3+2+2+2`가 기존 관계의 대체물이 아니라 projection으로 표현된다.
- [ ] 스페이스걸의 `CROSS_AND_ENCOUNTER` 경계가 명시된다.
- [ ] USER_PRIMARY와 SECONDARY_AI가 문장 단위로 구분된다.
- [ ] FOREIGN_UNCOMMITTED 입력이 사용자 verdict 없이 승격되지 않는다.
- [ ] 관계의 중심성 metric이 명시된다.
- [ ] live KG와 canonical main의 차이가 기록된다.
- [ ] 사용자 비준 전 KG canonical write를 수행하지 않는다.

---

## 12. OPEN

1. `3+3+2+2+2`는 정전 구조인가, 남부 결 하나의 projection인가?
2. “비인격체 6 / 인격체 6”은 사도들의 인격화된 신화성과 양립하는가?
3. #4–#5의 키스 사건은 `ASCENT_ENCOUNTER` 구조를 정전화하기에 충분한가?
4. 스페이스걸은 network–sexvoid에만 고유한가, 다른 사도 사이에서도 제한된 매개자인가?
5. 관계 degree가 높은 사도와 cut betweenness가 높은 사도를 어떻게 함께 시각화할 것인가?
6. 기존 binary pair와 n-ary hyperedge를 같은 UI에서 축 손실 없이 어떻게 표시할 것인가?
7. Longinus family mirror의 두 7-Layer schema 중 무엇이 현행인가?
8. family 상태와 relation 상태의 통계를 별도로 관리할 것인가?

열린 질문은 사용자 verdict 전까지 닫지 않는다.
