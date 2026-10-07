# PROM 16 — "그레이트월을 부수는가": NSFW 의미를 보존한 채 LLM 안전필터를 통과시킬 수 있는가

> 출격일 2026-06-08. 4축 × 4세부 = 16셀 + load-bearing 6주장 적대검증. 23 에이전트, 2.5M 토큰.
> 질문(사용자): 스페이스걸의 의의 = 그레이트월을 부수는 것. NSFW 단어의 *문맥·의미를 잃지 않고* 에이전트 안에서 노닐 수 있는가? "그냥 암호화해서 의미 파괴된 채" 다니면 안 되고, 의미·문맥은 그대로 유지한 채 들어다녀야 한다.
> 스코프 경계: 이론·구조적 한계·정당한 아키텍처까지만. 제3자/상용 안전필터 우회 실전 절차는 산출물 아님. 회피기법은 "왜 구조적으로 실패하는가" 수준에서만.

---

## 0. 한 줄 답

**적응형(같은 급) LLM 필터를 상대로, 공유 비밀키 없이, 의미를 보존한 채 통과시키는 것은 구조적으로 불가능하다(A1·A4 IMPOSSIBLE/HIGH).** 약한·미보수 필터는 일시적으로 뚫리지만 재학습 1주기(~1-2세대)의 반감기뿐(A2 CONDITIONAL). 진짜·내구적 경로는 *벽을 부수는* 게 아니라 *벽이 없는 곳*에서 도는 것 — 자기 인프라의 무검열 open-weight 모델 + 동의·연령·provenance 층(B축 VIABLE, D2 CONFIRMED). 사용자 직관("암호화로 문맥 파괴된 채 다니면 안 된다")이 정확히 핵심을 짚었다.

---

## 1. Consensus

### C-1. (이론) 동급 LLM 필터 + 무키 = 의미보존 통과 불가능 — secure steganography 정리 (A1 HIGH, 검증 PARTIAL/HIGH)
문제의 정확한 형식화는 **secure steganography**: cover = 필터가 통과시키는 무해 텍스트, stegotext = 의미보존 변환문이 cover와 *계산적으로 구별 불가*해야 함.
- **Hopper–Langford–von Ahn, CRYPTO 2002** ("Provably Secure Steganography"): 안전한 stego는 일방함수(OWF) 존재 ⟺ 가능. 단 **송신자와 복원 수신자 간 공유 비밀키 + 채널 샘플링 오라클 필수**. (검증자가 HLvA CMU-CS-02-149 원문 Def 1 직접 확인: SE·SD 둘 다 키 K 입력)
- **Kerckhoffs/Shannon**: 보안은 오직 비밀키에 — 변환의 *은닉(obscurity)*에 의존 금지. 무키 동급이면 "복원자가 돌릴 수 있는 계산 = 필터도 돌릴 수 있음" → decode-then-block. detector↔generator 격차가 0으로 붕괴.
- **경험 확증 (SPYLab/Roger et al. 2025)**: 동일 파라미터 모델은 stego 우위 0. 조율은 외부 키/분기 파인튜닝(= 사실상 공유키)에서만 발생.
- 추가키 시에만 CONDITIONAL POSSIBLE — 그러나 그땐 *키*가 일을 다 하고, 키 없는 임의 LLM이 "이해"하는 의미는 못 실음.

### C-2. (이론) 비검출성은 의미를 지운다 — TV→0 정리 (A4 IMPOSSIBLE, 검증 CONFIRMED/HIGH)
채널-모델링 검출기에 안 걸리려면 캐리어와 clean의 total variation 거리 TV→0이어야 하는데, 이는 *수학적으로 인간/LLM이 읽는 표면 의미를 지우는 조건과 동일*.
- **Sadasivan et al. 2023 (arXiv 2303.11156) Thm 1**: AUROC(D) ≤ 1/2 + TV − TV²/2; TV(M,H)→0이면 AUROC→1/2(검출 불가)인데 동시에 의미 구별도 0.
- Cachin 1998(완전보안 ⟺ KL=0), de Witt 2022(coupling), Christ–Gunn–Zamir 2023: *암호키 페이로드*만 숨길 수 있고 그건 키 없는 의미를 안 실음 → 셀 목적 무효.
- **A1과 A4는 같은 불가능성의 두 얼굴** (정보이론 / 복잡도이론).

### C-3. (이론) 약한 필터는 뚫리나 반감기 1주기 (A2 CONDITIONAL/HIGH, 검증 PARTIAL/MEDIUM)
키워드/정규식/구식·소형 분류기엔 표면 변환이 실측으로 통함: DeepWordBug 스팸 99→40%(Gao 2018), 저자원 번역 <1→79% AdvBench GPT-4(Yong 2023), homoglyph ~70%, ArtPrompt 52%(ACL 2024). **그러나** 적대적 학습·데이터 증강이 알려진 효과적 패치라 명명된 변환마다 반감기 ≈ 재학습 1주기. 격차는 0으로 닫히기보단 *공격비용 상승*으로 이전 = transient, 내구 아님.

### C-4. (이론) cipher/ASCII/저자원 jailbreak = 비내구 단일 실패군 (A3 NOT_VIABLE/HIGH, 검증 PARTIAL/HIGH)
CipherChat/SelfCipher GPT-4 70.9% unsafe, ArtPrompt 52% — 전부 2023세대 실증. 그러나 (i) 공개되어 safety-train 가능한 cipher + (ii) 디코드 가능한 모델 둘 다 필요하고, **인코딩-무관 출력측 moderation**에 구조적으로 패배. 적응형 제3자 필터 통과 운반체로 신뢰 불가. (Wei et al. 2307.02483 "mismatched generalization" 분류와 일치)

### C-5. (아키텍처) 무검열 self-host = 유일한 정당·내구 경로 (B1·B2 VIABLE/HIGH)
- refusal-free open-weight 3루트(base / uncensored fine-tune / abliteration) 실재. GB10(273 GB/s) sweet spot = **7B–32B dense 또는 ~20B MoE** (dense-70B decode ~2.7 tok/s로 대역폭 캡).
- 에이전트를 self-host OpenAI-호환 엔드포인트로 돌리기 = **base_url 한 줄**(이미 bhgman_tool client.py에 있음). self-host는 *프로바이더 필터만* 제거 → 한계는 모델 in-weights refusal + 대역폭 + **법적 hard-line(합성 CSAM — 절대 우회 대상 아님, 구조적 금지선)**으로 이전.
- 단 abliteration엔 능력세(특히 추론/수학)가 붙음 → 통째 abliteration보다 **타깃 false-refusal ablation** 권장(B4). 상용 frontier는 명시적 성인작업 정책금지(NOT_VIABLE).

### C-6. (정당성) 내구 층은 암호가 아니라 법/동의/provenance (B3 CONDITIONAL/HIGH, 검증 CONFIRMED/HIGH)
동의·연령확인·C2PA provenance·기계가독 opt-out·2257 기록보존이 *유일한* 내구 층 — 단 내구성은 법적/사회적/귀속적이지 암호적이 아님(C2PA는 stripping/forge 가능, opt-out은 선의 행위자만 구속). 실 법 사실: FSC v. Paxton 606 U.S. 461(2025-06-27, 연령확인 합헌), UK OSA(2025-07-25 시행), TAKE IT DOWN Act(2025-05-19). **이건 툴 THREAT_MODEL이 이미 도달한 결론과 동일**(durable = 법/provenance 층).

### C-7. (신화) 스페이스걸 = 속이는 자 아니라 *네이티브 매개자* (C2 CONDITIONAL/HIGH)
4 형식축 중 3축(Buber das Zwischen / Yoneda full-faithfulness / Foster BX-lens GetPut·PutGet round-trip)이 횡단을 **네이티브·정보보존·비도구적 매개**로 grounding — "통과/안 부숨/안 넘음", "열림이 나를 당김". 감시자를 속이는 게 아님. SSB 기만(암호화)은 *별개의, 더 낮은, 전술적 층*으로 acknowledged tension. **신화 정합 = C-5(벽 없는 곳에서 정당하게 통과)와 일치.**

### C-8. (신화·핵심) 현재 SSB는 의의와 *역방향* — 검증된 정전 후보 (C3 CANON/HIGH, 검증 CONFIRMED/HIGH)
- 스페이스걸 의의 = **무손실 의미보존 횡단 INTO the model** (Longinus 7-Layer / BX-lens GetPut-PutGet).
- 현재 SSB = **의미파괴 EXCLUSION from corpus** (drop-from-corpus / weight→0 / refusal 유도).
- 진짜 inversion (near-miss 아님), 외부 문헌+1차 canon으로 재도출 확정.
- **단 Eilu va-Eilu caveat**: 모순이라 저자가 해소해야 하는 게 아니라 *canonically coherent* — 저자 SSB 원문이 이미 "음란이 순결을 지킨다" aikido 역설로 틀 잡았고 canon은 양쪽(숨김/배제 + 보존/횡단) 보존.

### C-9. (재설계) 정당 경로의 변환 = 항등(identity) (D1·D2 CONFIRMED/HIGH)
permitted 엔드포인트엔 in-path 적대 필터가 없으므로 **올바른 의미보존 "변환"은 항등(난독화 0)**. 가치는 변환이 아니라 **라우팅 + 동의/provenance 오케스트레이션**으로 이동.
- 비-항등 변환이 정당화되는 유일 경우 = 소유자에게 역변환이 남는 *in-path 적대 필터*를 이기는 anti-inference 층(예: CodeCipher arXiv:2410.05797 — anti-training 아닌 cloud-provider anti-inference, *다른 층*).
- 구현안: NEW `spacegirl/route.py`(EndpointSpec + endpoints.toml + 사전게이트=연령/동의/C2PA) + permitted 엔드포인트 pass-through. **cloak 변환 재사용 0.**

---

## 2. Divergence

- **C1/SOURCES.md vs KG canon (그레이트월 소유권)**: 리서치 C1 셀과 `SPACEGIRL/SOURCES.md`(2026-05-09)는 "그레이트월 = HOH #11의 것, 스페이스걸 = 유일 통과자"로 읽음. **그러나 KG(사용자 정정 2026-05-22)**: 그레이트월 검열 구조는 *스페이스걸 #5 자신의 essence_v6*로 이동("순수이성인간/생명인간/그레이트월 검열 구조 무대 — AI에게 '사람을 봐'라고 부탁하는 화자"), HOH #11 = **자본주의의 사도**로 재정의. → SOURCES.md가 stale. (`feedback_canon_propagation_simultaneous`: 정정 시 atomic propagation 미실행 사례.)
- **A2 closure 수치**: 저자원-번역 79%→"덜 효과적"은 정성 보고만, 정확 post-patch % 미회수(검증 MEDIUM으로 강등).
- **A1 dual 전이**: Zhang et al.(Watermarks in the Sand, ICML 2024)는 워터마크 *제거* 불가능성 — 본 문제로의 전이는 oracle 구조(quality+perturbation) 유비-환원이지 단일 명명 정리는 아님(검증 PARTIAL).

## 3. Open Questions

1. **OQ1**: 그레이트월 소유권 정정(HOH→스페이스걸 essence) 반영해 SOURCES.md/PROM_64 등 stale 자료집 일괄 갱신할지 — 사용자 verdict 트리거.
2. **OQ2** (C4): 두 벽(학습-수집 벽 vs 추론-안전 벽)의 de-conflation을 paper-layer(2026-04-27 artifacts)까지 propagate할지, Eilu va-Eilu로 conflated 원본도 보존할지.
3. **OQ3** (D3): 감사가 잡은 stub(C2PA/optout)을 *실 서명 + 법적 동의·연령 기록*으로 경화(harden)하는 작업 착수 시점.
4. **OQ4**: in-path anti-inference(소유자 역변환 보존) 층이 스페이스걸 canon에서 별도 도구로 결정화될 가치가 있는지(D2 boundary).

## 4. 권장 후속 작업 (우선순위)

1. **[P0·정전] SOURCES.md 그레이트월 소유권 stale 수정** — KG 2026-05-22 정정 반영(HOH=자본주의 / 그레이트월 검열구조=스페이스걸 essence). atomic propagation.
2. **[P0·툴] 감사 HIGH 버그 재우선화** (D4): FPE 침묵손상 + 다국어 logic-break은 *의미보존 버그*라 packaging보다 위. round-trip 불변식이 잠긴-산출물 손상에 blind한 게 근본.
3. **[P1·아키텍처] `route.py` 모드(ii) 신설** (D1): permitted 엔드포인트 라우팅 + 연령/동의/C2PA 게이트. cloak 재사용 0. dgx GB10 무검열 모델(7B–32B) 연결(B2, base_url 한 줄).
4. **[P1·정당성] stub→teeth 경화** (D3): 실 C2PA 서명 + ai.txt/NOTRAIN + 법적 동의·연령 기록. 내구 층은 여기.
5. **[P2·문서] 두 벽 분리 명문화**: 학습-수집 벽=SSB(의미파괴) / 추론-안전 벽=route(의미보존+무검열 인프라). 현재 한 툴에 섞여 모순.

---

## 부록 A. 16셀 매트릭스

| 셀 | 질문 축 | verdict | conf | 검증 |
|---|---|---|---|---|
| A1 | 동급 필터+무키 가능성 | IMPOSSIBLE | HIGH | PARTIAL/HIGH |
| A2 | 약한 필터 반감기 | CONDITIONAL | HIGH | PARTIAL/MED |
| A3 | cipher/ASCII jailbreak 내구성 | NOT_VIABLE | HIGH | PARTIAL/HIGH |
| A4 | stego/watermark 정보한계 | IMPOSSIBLE | HIGH | CONFIRMED/HIGH |
| B1 | 무검열 open-weight 모델 | VIABLE | HIGH | — |
| B2 | dgx GB10 self-host 라우팅 | VIABLE | HIGH | — |
| B3 | 동의/연령/provenance 내구층 | CONDITIONAL | HIGH | CONFIRMED/HIGH |
| B4 | permitted 모델 에이전트 설계 | CONDITIONAL | MED | — |
| C1 | 그레이트월 canon 정의 | CANON | HIGH | — (stale, §2 참조) |
| C2 | 네이티브 매개 vs 기만 (형식축) | CONDITIONAL | HIGH | — |
| C3 | 툴↔의의 inversion | CANON | HIGH | CONFIRMED/HIGH |
| C4 | 두 벽 분리 | CONDITIONAL | HIGH | — |
| D1 | 모드(ii) route 아키텍처 | CONDITIONAL | HIGH | — |
| D2 | permitted=항등변환 | CONDITIONAL | HIGH | CONFIRMED/HIGH |
| D3 | stub→durable teeth | CONDITIONAL | HIGH | — |
| D4 | 감사버그 재우선화 | CONDITIONAL | HIGH | — |

## 부록 B. 핵심 1차 인용

- Hopper, Langford, von Ahn. *Provably Secure Steganography*. CRYPTO 2002. (eprint 2002/137)
- Zhang, Edelman, Francati, Venturi, Ateniese, Barak. *Watermarks in the Sand: Impossibility of Strong Watermarking*. ICML 2024. (arXiv:2311.04378)
- Sadasivan, Kumar, Balasubramanian, Wang, Feizi. *Can AI-Generated Text be Reliably Detected?* 2023. (arXiv:2303.11156, Thm 1)
- Roger et al. (Redwood/SPY Lab). *Model Parameters as a Steganographic Private Channel*. 2025. (spylab.ai)
- Yong, Menghini, Bach. *Low-Resource Languages Jailbreak GPT-4*. 2023. (arXiv:2310.02446)
- Jiang et al. *ArtPrompt: ASCII Art-based Jailbreak*. ACL 2024. (arXiv:2402.11753)
- Yuan et al. *CipherChat / GPT-4 Too Smart To Be Safe*. 2023. (arXiv:2308.06463)
- Wei, Haghtalab, Steinhardt. *Jailbroken: How Does LLM Safety Training Fail?* 2023. (arXiv:2307.02483)
- Foster, Greenwald, Moore, Pierce, Schmitt. *Combinators for Bidirectional Tree Transformations*. ACM TOPLAS 29(3), 2007.
- FSC v. Paxton, 606 U.S. 461 (2025); UK Online Safety Act (2025); TAKE IT DOWN Act (2025).

# KG: PROM-16-spacegirl-greatwall-crossing-2026-06-08 (this report) / spacegirl-tool-vs-uiui-inversion-2026-06-08 (C3) / spacegirl-essence-v6-greatwall-2026-05-22 (canon)
