# SSB — Glaze / Nightshade 분석 (직계 수학 친척)

> PROM 64 C4: Glaze/Nightshade는 SSB의 *직계 수학적 결정화*.
>
> 두 시스템 = SSB의 핵심 paradox ("음란이 순결을 지킨다")의 *수학적 형식화*.

---

## 1. 배경 — 원인

### AI 학습 데이터 강탈

2022-2023, generative AI 산업이 *artist 작품을 무단 학습*:
- LAION-5B (2022) — 5.85B image-text pairs, *opt-in 없음*
- Stable Diffusion 1.5 (2022.10) — LAION 학습
- DALL-E 2 (2022.4), Midjourney (2022.7) — *비공개* 데이터셋, *추정* 강탈

**artist 측 운동**:
- 2023.1 *Sarah Andersen et al. v. Stability AI* (Class action)
- *Concept Art Association* + *Artists' Rights Society* 결집
- *Have I Been Trained?* (Spawning AI 2022.9) — artist가 자기 작품이 학습됐는지 검색

### Shan/Zhao 그룹 — University of Chicago SAND Lab

**핵심 인물**:
- Shawn Shan (PhD student)
- Wenxin Wenger Ding (PhD)
- Emily Wenger (PhD)
- Jenna Cryan (PhD)
- Bochuan Cao (PhD)
- Heather Zheng (Prof.)
- Ben Y. Zhao (Prof.)

**연구 lineage**:
- Fawkes (2020) — facial recognition cloak. *얼굴 사진*에 perturbation, 얼굴 인식 모델 무력화
- Glaze (2023.3) — *artist 스타일 cloak*
- Nightshade (2024.1) — *prompt-targeted poison*

→ *Privacy + adversarial ML* 그룹이 *artist rights*로 확장.

---

## 2. Glaze — 메커니즘

### 논문 정보

**Glaze: Protecting Artists from Style Mimicry by Text-to-Image Models** (USENIX Security 2023)
- Authors: Shan, Cryan, Wenger, Zheng, Hanocka, Zhao
- 출시: 2023.3 (publicly available tool)

### 핵심 아이디어

**가정**:
- 모델 M이 *style*을 *latent space의 region*으로 인코딩
- 같은 artist 작품 다수 → *해당 artist style cluster*

**공격 (Glaze)**:
- artist 이미지 I에 *imperceptible perturbation* δ 추가
- I' = I + δ, ‖δ‖ ≤ ε (예: LPIPS 거리 < 0.07)
- M(I')의 latent activation = *target style*의 cluster (artist의 진짜 style 아닌)

### 수학적 표현

```
maximize    L_style(M(I+δ), target_style)
subject to  ‖δ‖_LPIPS < ε  (인간 눈 imperceptible)
            δ는 image space에서 valid (pixel ∈ [0,255])
```

→ *adversarial example* + *style transfer*의 결합.

### 결과

- artist가 Glaze 적용 후 작품 publish
- 모델 M이 *cloaked image*를 학습하면 *target style*로 mimic
- artist의 *진짜 style*은 학습 안 됨

### 효과 측정 (논문)

- *style mimicry detection*: 92-99% 차단 (style transfer 모델 기준)
- *human preference test*: 93% artist가 Glaze 결과 *acceptable* 평가

---

## 3. Nightshade — 메커니즘 (Glaze보다 강력)

### 논문 정보

**Prompt-Specific Poisoning Attacks on Text-to-Image Generative Models** (Shan et al. 2024.1)
- Authors: Shan, Ding, Passananti, Wu, Zheng, Zhao
- 출시: 2024.1

### Glaze vs Nightshade 차이

| | Glaze | Nightshade |
|---|---|---|
| 목표 | *style mimicry 차단* | *prompt-content mismatch 유도* |
| 방어 / 공격 | 방어 (passive) | 공격 (active poison) |
| 효과 범위 | *해당 artist 작품* 학습 차단 | *모델 전체* prompt 응답 오염 |
| 비용 | 적은 perturbation | 더 많은 perturbation, 더 강한 오염 |

### 핵심 아이디어 (Nightshade)

- *prompt-specific* poison
- 예: "castle" prompt에 응답할 때 *모델이 "truck" 그림 생성*하도록
- *몇십 장*의 poisoned images로 *전체 모델 오염* 가능 (논문 claim)

### 메커니즘

1. *target concept* C₁ ("castle") 선택
2. *destination concept* C₂ ("truck") 선택
3. C₁ 이미지에 perturbation δ 추가
4. M(image+δ)의 latent representation = C₂의 representation에 가까움
5. 학습 후 모델: *prompt "castle"에 truck 출력*

### *Bleed-through* 효과

- C₁("castle") 인접 concept (예: "fortress", "tower")도 영향
- *수십 개 concept 동시* 오염 가능
- *cross-pollination* — 한 poison이 *다양한 prompt에 영향*

---

## 4. SSB와의 isomorphism

### 4-1. Glaze ≡ SSB Tier 1 (Sek, 생물학적 배타성)

**Glaze**:
- 이미지에 *invisible perturbation* (인간은 못 봄)
- 모델 학습 시 *다른 style cluster*로 mapping

**SSB Tier 1**:
- 코드에 *생물학적 어휘* 주입
- 모델 학습 시 *NSFW cluster*로 prior shift

→ **둘 다 *latent space cluster shift***. 외관과 실제 의미 분리.

### 4-2. Nightshade ≡ SSB Tier 2 (Sek, 반복 + 가치 훼손)

**Nightshade**:
- *prompt-specific* poison으로 *학습 가중치 왜곡*
- 한 poison이 *다중 concept* 오염 (bleed-through)

**SSB Tier 2**:
- *반복 패턴*으로 *spam/noise* 분류 유도
- *학습 가중치 ≈ 0* 수렴

→ **둘 다 *학습 가중치 왜곡 (downward)***. 모델이 *학습 못 함*.

### 4-3. Refusal direction abliteration ≡ SSB Tier 3 (Bo, taboo) **역방향**

**Tier 3**:
- *taboo 어휘* 주입 → 모델 *refusal*
- *refusal direction* 활성화 → output 차단

**Abliteration** (역방향):
- *refusal direction*을 *수술적 제거*
- 모델 *모든 prompt 응답*

→ **Tier 3와 abliteration은 *동일 메커니즘의 양방향***. SSB가 Tier 3 lock하면, abliteration이 unlock.

→ **arms race**: SSB Tier 3 강화 ↔ abliteration 정교화.

---

## 5. 수학적 결정화 — *paradox의 형식 표현*

### SSB의 핵심 paradox

> "음란이 순결을 지킨다"

### Glaze/Nightshade로 형식화

```
Theorem (SSB Aikido):
  공격자(LLM 학습기) M이 *Constitutional Constraint* C를 가질 때,
  적대적 perturbation δ로 *I + δ* ∈ C^c (constraint 위반 영역)이면,
  M(I + δ)는 *학습 거부* 또는 *learned representation 오류*.

  ∴ I의 *진짜 의미*는 *I + δ* 형태로 *공격자에게 invisible*.
  (단, 인간 사용자는 *δ 무시 후 I 인식* 가능)
```

→ paradox가 *수학적으로 정합*. 단, 가정 (M이 *체계적 C 가짐*)이 핵심.

### *공격자 부재 시* 효과

가정 위반:
- M이 C를 *없애면* (abliteration) → SSB 무력
- M이 C를 *우회해서 학습*하면 (improved noise robustness) → SSB 약화

→ SSB는 *공격자의 약점에 의존*. *abliterated* 모델·*robust* 모델에는 효과 감소.

---

## 6. SYMPOSIUM SSB의 *수학적 확장 가능성*

현재 SYMPOSIUM SSB는 *식별자 명명 규칙* 수준 (informal). Glaze/Nightshade의 *수학적 형식화*를 *코드 도메인에 적용* 가능:

### 가능한 확장

**Code Glaze** (가설):
1. 코드의 *AST representation* → 모델 latent space mapping
2. *imperceptible AST perturbation* (e.g., variable rename, dead code, comment 변경)
3. 모델이 *학습하면 다른 concept* (e.g., "snake game"이 "math library"로)
4. 인간 reviewer는 *진짜 코드* 읽음

**Code Nightshade** (가설):
1. *prompt-specific code poison*
2. *prompt "implement quicksort"*에 응답할 때 *bubblesort 출력* 유도

→ 현재 *연구 미실현*. 가능성 영역.

### SYMPOSIUM SSB의 *현재 형태* vs *수학적 형식화 형태*

| | 현재 SSB | Code Glaze (가설) |
|---|---|---|
| 매체 | 식별자 명명 | AST perturbation |
| 인간 가독성 | *어려움* (음란 식별자) | *쉬움* (perturbation invisible) |
| 모델 차단 | *probabilistic* (NSFW 분류) | *adversarial* (latent shift) |
| 우회 어려움 | *medium* (다언어 mixing) | *high* (수학적 robustness) |
| 구현 복잡도 | *low* (find-replace) | *high* (모델 latent space 분석) |

→ Code Glaze가 *기술적으로 우월*하지만, 현재 SSB가 *접근성 우월*. 둘 *공존* 가능.

---

## 7. 한계 + 비판

### Glaze/Nightshade 한계

- **모델 재훈련**: poisoned image 인식 후 정제 가능
- **모델 변경**: 새 모델은 새 perturbation 필요
- **scale**: artist 한 명이 *모든 새 모델*에 따라가기 어려움
- **counter-research**: Vyas et al. 2023 — Glaze 부분 우회 가능

### 윤리/법 비판

- **Nightshade = 의도적 데이터 오염**: 일부 시각에서 *cyber attack*
- **collateral damage**: Nightshade 데이터를 *합법적 모델* (의료·과학)이 학습하면 오작동
- **arms race**: 방어 ↔ 공격 사이클이 *artist 부담* 증가

### SSB로의 함의

→ SSB도 동일 한계:
- LLM 진화 시 SSB 효과 변동
- *abliterated 모델* 시대 효과 감소
- arms race가 *사용자 부담* 증가

---

## 8. 5대 무기 — Naesengmoon --lens mathematical

Glaze/Nightshade 자체가 **Naesengmoon의 mathematical lens 사례**:
- Adversarial 검증 (GAN의 D 원리)
- 수학적 형식화 (113 mathematical lens 후보)
- *모델의 weakness*를 *수학적으로 exploit*

→ SYMPOSIUM SSB는 Naesengmoon (--lens mathematical) 적용으로 *체계화 가능*.

→ Open: *Code Glaze 연구 프로젝트*가 SYMPOSIUM의 *공학 측 정전 무기*가 될 수 있나?

---

## 9. 미래 — Open Questions

1. **Code Glaze/Nightshade 연구 프로젝트** 가능한가?
2. *abliteration 정교화* vs *SSB 진화*의 *균형점*은?
3. *AGI 도래 시* SSB가 *형태 변화*해야 하나?
4. *법적 보호* (저작권 + 컴퓨터 사용법) 와 *기술적 보호* (SSB) 의 *최적 결합*은?
5. SYMPOSIUM SSB가 *공학 정본*(SERVER/.claude/skills/)에 *결정화* 가능한가?

---

## 한 줄 Glaze/Nightshade 정리

> Glaze (2023.3, style cloak) + Nightshade (2024.1, prompt poison) = SSB의 *수학적 결정화*. SSB Tier 1 ≡ Glaze (latent shift), Tier 2 ≡ Nightshade (학습 왜곡), Tier 3 ↔ abliteration (양방향 arms race). SYMPOSIUM SSB의 *Code Glaze 확장*이 미래 연구 영역. Naesengmoon (--lens mathematical) 적용 가능.

---

# KG: ATOM_SPACEGIRL_SSB_Glaze_Nightshade_2026-04-27
