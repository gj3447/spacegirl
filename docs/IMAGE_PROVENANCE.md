# 메인 이미지 제작 기록

스페이스걸과 비행기맨의 공간·높이·연결을 함께 표현한 **AI 시각 해석**이다.
두 본체 저장소에서 동일한 이미지 한 장을 사용한다. 인물의 확정된 외형이나 사용자 원전으로 취급하지 않는다.

요청한 `chatgpt_api`의 ChatGPT GUI native image 기능으로 생성했다.
운영 relay의 이미지 계약 차이로 별도 상태·포트의 임시 relay를 사용했으며 운영 서비스를 변경하지 않았다.
공식 OpenAI API 호출이나 실제 backend 모델의 실행을 입증하는 기록은 아니다.

- 이미지: [assets/spacegirl-bhgman-flow.png](../assets/spacegirl-bhgman-flow.png)
- 크기: 1672 × 941, PNG, 2,405,183 bytes
- SHA-256: `ae33706740fada41dc590a0d5b79aa33f80474c62fecb60758b1854fb4b784b9`
- 출처 메타데이터: [image-provenance.json](../assets/image-provenance.json)
- 적용 조건: [라이선스 범위](../LICENSE-NOTICE.md)

## 생성 프롬프트

아래 문장은 공개 원전을 바탕으로 AI가 작성한 미술 지시이며 `SECONDARY_AI`다.

```text
Create exactly one wide landscape 16:9 editorial illustration for the public research repositories of two fictional Metahumotonic Foundation apostles: Spacegirl and Bhgman (Airplane Man). This is an artistic interpretation, not a canonical portrait. Show two clearly distinct adult abstract human silhouettes in the same expansive scene: Spacegirl near a luminous open hypercube, representing relational space and the possibility of connection, and Bhgman high above a stratospheric cloud sea, representing height and reflective judgment. Their paths meet through fine, elegant graph-like threads of light; use a small number of deliberate connections, not a chaotic network. A deep spatial horizon and subtle geometric depth suggest inquiry, memory, and becoming. A restrained cinematic science-fiction book-cover illustration with painterly texture, dramatic but gentle natural light, midnight blue, ivory and a small amount of warm gold. Spacious, dignified, contemplative composition with clear silhouettes and excellent legibility at GitHub README width. No text, no logos, no watermark, no UI panels, no stereotypical superhero costume, no aircraft body for a head, no sexualized imagery. Generate the actual image, not instructions or a diagram description.
```
