import os

desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
path = os.path.join(desktop, '감염학_기출문제_정리집_v2.html')

html = r'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>감염학 기출문제 정리집 v2 (18~22학번)</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Malgun Gothic',sans-serif;background:#f0f4f8;color:#222;line-height:1.65;font-size:14.5px}
.wrap{max-width:980px;margin:0 auto;padding:18px}
h1{text-align:center;font-size:1.9em;color:#1a365d;padding:28px 0 6px;border-bottom:3px solid #2b6cb0}
.sub{text-align:center;color:#4a90d9;margin-bottom:24px;font-size:.9em}
.toc{background:#fff;border-radius:10px;padding:18px 26px;margin-bottom:22px;box-shadow:0 2px 8px rgba(0,0,0,.08)}
.toc h2{color:#2b6cb0;font-size:1em;margin-bottom:8px}
.toc ol{padding-left:18px;columns:2;gap:24px;font-size:.9em}
.toc li{margin:2px 0}.toc a{color:#2b6cb0;text-decoration:none}
.toc a:hover{text-decoration:underline}
.sec{background:#fff;border-radius:12px;padding:22px 26px;margin-bottom:22px;box-shadow:0 2px 8px rgba(0,0,0,.07)}
.sh{display:flex;align-items:center;gap:10px;margin-bottom:14px;padding-bottom:8px;border-bottom:2px solid #e2e8f0}
.sn{background:#2b6cb0;color:#fff;border-radius:50%;width:30px;height:30px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9em;flex-shrink:0}
.st{font-size:1.15em;font-weight:700;color:#1a365d}
.badge{background:#ebf8ff;color:#2b6cb0;border-radius:20px;padding:1px 9px;font-size:.75em;font-weight:700;margin-left:6px}
.cb{border-left:4px solid #2b6cb0;background:#ebf8ff;border-radius:0 6px 6px 0;padding:10px 14px;margin:10px 0;font-size:.92em}
.cb.r{border-left-color:#e53e3e;background:#fff5f5}
.cb.y{border-left-color:#d69e2e;background:#fffff0}
.cb.g{border-left-color:#38a169;background:#f0fff4}
.cb h4{font-size:.9em;font-weight:700;margin-bottom:5px;color:#2b6cb0}
.cb.r h4{color:#c53030}.cb.y h4{color:#975a16}.cb.g h4{color:#276749}
.qcard{border:1px solid #e2e8f0;border-radius:8px;padding:14px;margin:12px 0;background:#fafafa}
.ytag{background:#2b6cb0;color:#fff;font-size:.72em;padding:1px 7px;border-radius:10px;margin-right:6px;font-weight:600}
.ytag.r{background:#c53030}
.stem{font-weight:700;color:#1a365d;margin-bottom:10px;font-size:.95em;line-height:1.5}
.opt{border:1px solid #cbd5e0;border-radius:6px;padding:7px 11px;margin:3px 0;cursor:pointer;transition:.15s;font-size:.92em;user-select:none}
.opt:hover{background:#ebf8ff}
.opt.sel{background:#bee3f8;border-color:#2b6cb0;font-weight:600}
.opt.cr{background:#c6f6d5!important;border-color:#38a169!important;color:#22543d!important;font-weight:700}
.opt.wr{background:#fff5f5!important;border-color:#fc8181!important;color:#742a2a!important}
.chkbtn{background:#2b6cb0;color:#fff;border:none;padding:7px 18px;border-radius:6px;cursor:pointer;margin-top:8px;font-size:.9em;font-family:inherit}
.chkbtn:hover{background:#1a365d}
.ansbox{display:none;margin-top:12px;border-top:2px solid #e2e8f0;padding-top:12px}
.anslabel{font-weight:700;color:#2b6cb0;margin-bottom:6px;font-size:.95em}
.exitem{padding:4px 8px;margin:2px 0;border-radius:4px;font-size:.88em}
.exok{background:#c6f6d5;color:#22543d}
.exno{background:#fff5f5;color:#742a2a}
.exnote{background:#fffff0;color:#744210;border-left:3px solid #d69e2e;padding:4px 8px;margin:4px 0;font-size:.88em;border-radius:0 4px 4px 0}
.subjans{background:#fffff0;border-left:4px solid #d69e2e;padding:12px;border-radius:0 6px 6px 0;font-size:.92em}
.dt{width:100%;border-collapse:collapse;margin:8px 0;font-size:13px}
.dt th{background:#553c9a;color:#fff;padding:6px 10px;text-align:left}
.dt td{border:1px solid #e2e8f0;padding:5px 10px}
.dt tr:nth-child(even) td{background:#faf5ff}
.tt{width:100%;border-collapse:collapse;margin:8px 0;font-size:13px}
.tt th{background:#2b6cb0;color:#fff;padding:6px 10px;text-align:center}
.tt td{border:1px solid #cbd5e0;padding:5px 10px;text-align:center}
.tt tr:nth-child(even) td{background:#ebf4ff}
.s5{color:#e53e3e;font-weight:700}.s4{color:#dd6b20;font-weight:700}.s3{color:#d69e2e}.s2{color:#38a169}
.nota{color:#718096;font-size:.85em;font-style:italic;margin-top:4px}
</style>
<script>
function sel(el,qid){
  document.querySelectorAll('[data-q="'+qid+'"]').forEach(function(e){e.classList.remove('sel');});
  el.classList.add('sel');
}
function show(id){
  var ab=document.getElementById('ans'+id);
  if(ab)ab.style.display='block';
  var bn=document.getElementById('btn'+id);
  if(bn)bn.style.display='none';
  document.querySelectorAll('[data-q="'+id+'"]').forEach(function(e){
    e.onclick=null;e.style.cursor='default';
    if(e.dataset.correct==='1'){e.classList.add('cr');}else{e.classList.add('wr');}
  });
}
</script>
</head>
<body>
<div class="wrap">
<h1>감염학 기출문제 정리집 v2</h1>
<p class="sub">본과 1-1 | 18~22학번 김영준·이재훈 교수님 파트 기출 | 주제별 완전 정리 | 클릭하여 정답 확인</p>

<div class="toc"><h2>목차</h2><ol>
<li><a href="#t0">출제 경향 분석</a></li>
<li><a href="#t1">패혈증 · FUO · 해열제</a></li>
<li><a href="#t2">S. aureus / MSSA / MRSA / TSS</a></li>
<li><a href="#t3">요로감염 · E. coli · Proteus</a></li>
<li><a href="#t4">Vibrio vulnificus</a></li>
<li><a href="#t5">N. meningitidis</a></li>
</ol></div>

<!-- 출제 경향 -->
<div class="sec" id="t0">
<div class="sh"><div class="sn">★</div><div class="st">출제 경향 분석 (18~22학번)</div></div>
<table class="tt">
<tr><th>토픽</th><th>18정규</th><th>18재시</th><th>19</th><th>20</th><th>21</th><th>22</th><th>빈도</th></tr>
<tr><td>패혈증/FUO</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td class="s5">★★★★★</td></tr>
<tr><td>S. aureus / TSS</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td class="s5">★★★★★</td></tr>
<tr><td>UTI / E. coli</td><td>✓</td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td class="s5">★★★★★</td></tr>
<tr><td>Vibrio vulnificus</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td class="s5">★★★★★</td></tr>
<tr><td>N. meningitidis</td><td></td><td></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td class="s4">★★★★</td></tr>
</table>
<div class="cb r"><h4>항생제 선택 공식 — 전 범위 핵심 암기</h4>
MSSA → <b>nafcillin</b> | MRSA → <b>vancomycin</b> | VRSA → daptomycin/linezolid<br>
Listeria → <b>ampicillin</b> (cephalosporin 무효) | CoNS oxacillin내성 → <b>vancomycin</b><br>
Vibrio vulnificus → <b>FQ + 3세대 ceph</b> ± debridement | N. meningitidis 예방 → <b>ceftriaxone IM / rifampin / ciprofloxacin</b><br>
S. pyogenes → <b>penicillin</b> (내성 없음)
</div>
</div>

<!-- 패혈증/FUO -->
<div class="sec" id="t1">
<div class="sh"><div class="sn">1</div><div class="st">패혈증 · FUO · 해열제 <span class="badge">★★★★★</span></div></div>
<div class="cb r"><h4>Sepsis-3 정의</h4>
<b>Sepsis:</b> 감염에 의한 생명 위협적 장기 기능 부전 → SOFA score ≥2점 증가<br>
<b>qSOFA (중환자실 밖 선별):</b> ① 호흡수 ≥22/분 ② 의식변화 GCS<15 ③ 수축기혈압 ≤100 → 2개 이상=의심<br>
<b>Septic shock:</b> Sepsis + 수액불응 저혈압 + 젖산 >2 mmol/L<br>
<b>FUO:</b> 발열 38.3°C 이상 + 3주 이상 + 충분한 검사 후 원인 불명 → FDG-PET/CT
</div>

<div class="qcard">
<div class="stem"><span class="ytag r">22학번 Q2</span> Sepsis에 대한 예방적 항생제로 옳은 것은?</div>
<div class="opt" data-q="a1" data-correct="0" onclick="sel(this,'a1')">① 무분별한 항생제 남용 내성 방지를 위해 균 동정 후 투여해야 한다</div>
<div class="opt" data-q="a1" data-correct="0" onclick="sel(this,'a1')">② 응급실 내원 6시간 내 항생제를 투여한다</div>
<div class="opt" data-q="a1" data-correct="1" onclick="sel(this,'a1')">③ Sepsis 확정 1시간 내 항생제를 투여한다</div>
<div class="opt" data-q="a1" data-correct="0" onclick="sel(this,'a1')">④ 확실하게 균을 배양해야 투여할 수 있다</div>
<div class="opt" data-q="a1" data-correct="0" onclick="sel(this,'a1')">⑤ 수액 치료를 한 후 항생제를 투여한다</div>
<button class="chkbtn" id="btna1" onclick="show('a1')">정답 확인</button>
<div class="ansbox" id="ansa1">
<div class="anslabel">정답: ③</div>
<div class="exitem exno">① X — 경험적(empirical) 투여 가능. 균 동정 전에도 즉시 투여</div>
<div class="exitem exno">② X — 6시간이 아닌 <b>1시간</b> 내가 원칙 (Surviving Sepsis Campaign)</div>
<div class="exitem exok">③ O — Sepsis 인지 즉시 1시간 내 경험적 항생제 투여</div>
<div class="exitem exno">④ X — 혈액배양 채취 후 즉시 투여 (결과 기다리지 않음)</div>
<div class="exitem exno">⑤ X — 수액과 항생제는 동시 진행</div>
</div>
</div>

<div class="qcard">
<div class="stem"><span class="ytag r">22학번 Q3</span> 다음 중 qSOFA의 진단 기준이 아닌 것은?</div>
<div class="opt" data-q="a2" data-correct="1" onclick="sel(this,'a2')">① 체온</div>
<div class="opt" data-q="a2" data-correct="0" onclick="sel(this,'a2')">② 의식평가 (GCS)</div>
<div class="opt" data-q="a2" data-correct="0" onclick="sel(this,'a2')">③ 심박수</div>
<div class="opt" data-q="a2" data-correct="0" onclick="sel(this,'a2')">④ 혈압 (수축기 ≤100)</div>
<button class="chkbtn" id="btna2" onclick="show('a2')">정답 확인</button>
<div class="ansbox" id="ansa2">
<div class="anslabel">정답: ①</div>
<div class="exitem exno">① 체온 — qSOFA에 포함되지 않음. SIRS 기준에는 포함</div>
<div class="exitem exok">② O — 의식변화(GCS<15)는 qSOFA 기준</div>
<div class="exitem exno">③ 심박수 — qSOFA에 포함되지 않음. SIRS에는 포함(>90/분)</div>
<div class="exitem exok">④ O — 수축기혈압 ≤100 mmHg는 qSOFA 기준</div>
<div class="exnote">qSOFA 3기준: ① 호흡수 ≥22/분 ② 의식변화 ③ 수축기혈압 ≤100 → 체온·심박수는 SIRS 기준</div>
</div>
</div>

<div class="qcard">
<div class="stem"><span class="ytag r">22학번 Q15</span> 53세 여자, 발열 38.5°C 지속. 입원 1주 동안 혈액검사·약물 중단 등 시행했으나 발열 지속. 이때 해볼 수 있는 추가 검사는? (불명열로 기본검사 모두 시행 후)</div>
<div class="opt" data-q="a3" data-correct="0" onclick="sel(this,'a3')">① 해열 진통제 사용 후 경과관찰</div>
<div class="opt" data-q="a3" data-correct="0" onclick="sel(this,'a3')">② 미복원</div>
<div class="opt" data-q="a3" data-correct="0" onclick="sel(this,'a3')">③ 스테로이드 투여 고려</div>
<div class="opt" data-q="a3" data-correct="1" onclick="sel(this,'a3')">④ FDG-PET/CT</div>
<div class="opt" data-q="a3" data-correct="0" onclick="sel(this,'a3')">⑤ 복부/흉부 CT 촬영</div>
<button class="chkbtn" id="btna3" onclick="show('a3')">정답 확인</button>
<div class="ansbox" id="ansa3">
<div class="anslabel">정답: ④</div>
<div class="exitem exno">① X — 증상 완화일 뿐 진단 검사 아님</div>
<div class="exitem exno">③ X — 원인 불명 상태에서 스테로이드 투여는 감염 악화 위험</div>
<div class="exitem exok">④ O — FUO에서 기본 검사 소진 후 FDG-PET/CT: 대사 활성 병변(종양, 감염, 염증 부위) 탐색</div>
<div class="exitem exno">⑤ X — CT는 초기에 시행, FUO 진단 후반에는 PET/CT가 더 적합</div>
</div>
</div>
</div>

<!-- S. aureus / TSS -->
<div class="sec" id="t2">
<div class="sh"><div class="sn">2</div><div class="st">S. aureus / MSSA / MRSA / TSS <span class="badge">★★★★★</span></div></div>
<div class="cb r"><h4>핵심 정리</h4>
gram(+) 구균, catalase(+), coagulase(+) | beta-lactamase 생성 → ampicillin 내성<br>
MSSA → <b>nafcillin</b> | MRSA → <b>vancomycin</b> | VRSA → <b>daptomycin/linezolid</b><br>
TSS: TSST-1(superantigen) → T세포 대량 활성화 → cytokine storm<br>
TSS 기준: 발열≥38.9°C + 저혈압 + <b>미만성</b> 홍반 + 탈피(1~2주) + ≥3개 장기침범
</div>

<div class="qcard">
<div class="stem"><span class="ytag">19·20·21학번 공통</span> 화농성 관절염으로 관절천자 시행. Gram 염색: gram(+) 구균 집락. 가장 적절한 항생제는?</div>
<div class="opt" data-q="b1" data-correct="0" onclick="sel(this,'b1')">① vancomycin</div>
<div class="opt" data-q="b1" data-correct="1" onclick="sel(this,'b1')">② nafcillin (dicloxacillin)</div>
<div class="opt" data-q="b1" data-correct="0" onclick="sel(this,'b1')">③ ampicillin</div>
<div class="opt" data-q="b1" data-correct="0" onclick="sel(this,'b1')">④ penicillin G</div>
<div class="opt" data-q="b1" data-correct="0" onclick="sel(this,'b1')">⑤ cephalexin 경구</div>
<button class="chkbtn" id="btnb1" onclick="show('b1')">정답 확인</button>
<div class="ansbox" id="ansb1">
<div class="anslabel">정답: ②</div>
<div class="exitem exno">① X — vancomycin은 MRSA 확인 시 사용; 경험적으로는 nafcillin 우선</div>
<div class="exitem exok">② O — MSSA 화농성 관절염 1차: nafcillin (penicillinase-resistant penicillin)</div>
<div class="exitem exno">③ X — S. aureus는 beta-lactamase 생성 → ampicillin 내성</div>
<div class="exitem exno">④ X — penicillin G도 대부분 내성</div>
<div class="exitem exno">⑤ X — 화농성 관절염은 IV 항생제 필요</div>
</div>
</div>

<div class="qcard">
<div class="stem"><span class="ytag">18·20·21학번</span> TSS 진단 기준으로 옳은 것을 모두 고르시오.<br>가. 발열 38.9°C 이상 &nbsp; 나. 국소성 홍반 &nbsp; 다. 수축기혈압 90mmHg 미만 &nbsp; 라. 3개 이상 장기 침범</div>
<div class="opt" data-q="b2" data-correct="0" onclick="sel(this,'b2')">① 가, 나, 다</div>
<div class="opt" data-q="b2" data-correct="0" onclick="sel(this,'b2')">② 나, 다, 라</div>
<div class="opt" data-q="b2" data-correct="1" onclick="sel(this,'b2')">③ 가, 다, 라</div>
<div class="opt" data-q="b2" data-correct="0" onclick="sel(this,'b2')">④ 가, 나, 다, 라 모두</div>
<button class="chkbtn" id="btnb2" onclick="show('b2')">정답 확인</button>
<div class="ansbox" id="ansb2">
<div class="anslabel">정답: ③ (가, 다, 라)</div>
<div class="exitem exok">가 O — 발열 ≥38.9°C: TSS 기준</div>
<div class="exitem exno">나 X — <b>"국소성"</b> 홍반이 아닌 <b>"미만성(diffuse)"</b> 홍반이어야 함</div>
<div class="exitem exok">다 O — 수축기혈압 <90 mmHg: 저혈압</div>
<div class="exitem exok">라 O — ≥3개 장기 침범 (위장관, 근육, 신장, 혈액, 간, CNS 등)</div>
</div>
</div>

<div class="qcard">
<div class="stem"><span class="ytag">18학번 정규</span> S. aureus의 특성으로 옳은 것을 모두 고르시오.<br>① gram 양성 구균 ② catalase 양성 ③ coagulase 양성 ④ Protein A: IgG Fc에 결합 ⑤ gram 음성 구균</div>
<div class="opt" data-q="b3" data-correct="0" onclick="sel(this,'b3')">① ①②③ 만 옳다</div>
<div class="opt" data-q="b3" data-correct="1" onclick="sel(this,'b3')">② ①②③④ 모두 옳다</div>
<div class="opt" data-q="b3" data-correct="0" onclick="sel(this,'b3')">③ ①②만 옳다</div>
<div class="opt" data-q="b3" data-correct="0" onclick="sel(this,'b3')">④ ①②③④⑤ 모두 옳다</div>
<button class="chkbtn" id="btnb3" onclick="show('b3')">정답 확인</button>
<div class="ansbox" id="ansb3">
<div class="anslabel">정답: ② (①②③④)</div>
<div class="exitem exok">① O — gram 양성 구균 (포도상 배열)</div>
<div class="exitem exok">② O — catalase(+): Staphylococcus 속 특징</div>
<div class="exitem exok">③ O — coagulase(+): S. aureus의 CoNS 구별 기준</div>
<div class="exitem exok">④ O — Protein A: IgG Fc 부위에 결합 → 식균작용 방해</div>
<div class="exitem exno">⑤ X — gram 음성이 아님. gram 양성이 정확</div>
</div>
</div>

<div class="qcard">
<div class="stem"><span class="ytag r">22학번 Q9</span> 괴사성 근막염이나 TSS에서 clindamycin을 병합 투여하는 이유는?</div>
<div class="opt" data-q="b4" data-correct="0" onclick="sel(this,'b4')">① 내성균 예방</div>
<div class="opt" data-q="b4" data-correct="0" onclick="sel(this,'b4')">② 균 제거 속도 증가</div>
<div class="opt" data-q="b4" data-correct="0" onclick="sel(this,'b4')">③ 균 특성상 synergy 효과를 위해</div>
<div class="opt" data-q="b4" data-correct="1" onclick="sel(this,'b4')">④ 독소 제거 위해</div>
<div class="opt" data-q="b4" data-correct="0" onclick="sel(this,'b4')">⑤ 혐기성균 커버를 위해</div>
<button class="chkbtn" id="btnb4" onclick="show('b4')">정답 확인</button>
<div class="ansbox" id="ansb4">
<div class="anslabel">정답: ④</div>
<div class="exitem exno">① X — 내성균 예방 목적이 아님</div>
<div class="exitem exno">② X — 균 제거 속도 증가는 주 목적이 아님</div>
<div class="exitem exno">③ X — synergy 효과 목적이 아님</div>
<div class="exitem exok">④ O — clindamycin: 단백합성 억제(50S ribosome) → <b>독소(TSST-1, SPE) 생성 억제</b>. 균이 죽어도 독소는 남아있으므로 독소 생성 억제가 중요</div>
<div class="exitem exno">⑤ X — 혐기성균 커버는 clindamycin의 부가적 효과일 뿐 주목적 아님</div>
</div>
</div>

<div class="qcard">
<div class="stem"><span class="ytag r">22학번 Q12</span> 포도상구균 식중독에 대한 설명으로 옳은 것은?</div>
<div class="opt" data-q="b5" data-correct="0" onclick="sel(this,'b5')">① 잠복기 48~72시간</div>
<div class="opt" data-q="b5" data-correct="0" onclick="sel(this,'b5')">② 고열이 동반된다</div>
<div class="opt" data-q="b5" data-correct="1" onclick="sel(this,'b5')">③ 이미 만들어진 독소에 의해 발생한다</div>
<div class="opt" data-q="b5" data-correct="0" onclick="sel(this,'b5')">④ 혈변이 동반된다</div>
<div class="opt" data-q="b5" data-correct="0" onclick="sel(this,'b5')">⑤ 원인균 제거를 위해 항생제가 필요하다</div>
<button class="chkbtn" id="btnb5" onclick="show('b5')">정답 확인</button>
<div class="ansbox" id="ansb5">
<div class="anslabel">정답: ③</div>
<div class="exitem exno">① X — 잠복기 <b>1~6시간</b> (매우 짧음, 독소 중독이므로)</div>
<div class="exitem exno">② X — 고열 없음. 발열 없는 오심·구토·복통이 특징</div>
<div class="exitem exok">③ O — 열에 안정한 enterotoxin(장독소)이 이미 음식에서 생성 → 섭취 후 중독. 균 자체가 아닌 독소가 원인</div>
<div class="exitem exno">④ X — 혈변 없음. 수양성 설사·구토</div>
<div class="exitem exno">⑤ X — 독소 중독이므로 항생제 필요 없음 (지지치료만)</div>
</div>
</div>
</div>

<!-- 요로감염 / E. coli -->
<div class="sec" id="t3">
<div class="sh"><div class="sn">3</div><div class="st">요로감염 · E. coli · Proteus <span class="badge">★★★★★</span></div></div>
<div class="cb"><h4>핵심</h4>
E. coli 균혈증 원발부위 → <b>요로계(UTI)</b> (가장 흔함)<br>
Proteus mirabilis: urease → struvite 결석 | E.coli EHEC O157:H7 → Shiga독소 → HUS
</div>

<div class="qcard">
<div class="stem"><span class="ytag r">22학번 Q1</span> 환자의 소변에서 다음과 같은 결정(관 모양의 coffinlid 결정)이 발견되었다. 질병의 원인균은?</div>
<button class="chkbtn" id="btnc1" onclick="show('c1')">답 확인</button>
<div class="ansbox" id="ansc1">
<div class="subjans">
<b>정답: Proteus mirabilis</b><br><br>
<b>기전:</b> urease 생성 → 요소를 암모니아로 분해 → 소변 알칼리화(pH↑) → struvite(magnesium ammonium phosphate) 결석 형성 (관 모양 결정)<br>
<b>치료:</b> 결석 제거 + 항생제 (ampicillin, TMP-SMX, FQ 중 감수성 따라)
</div>
</div>
</div>

<div class="qcard">
<div class="stem"><span class="ytag r">22학번 Q14</span> 23세 여자, 1주일 전부터 배뇨시 통증·빈뇨·잔뇨·작열감. 3일 전부터 좌측 옆구리 통증 및 발열. 응급실 내원.<br>Urinary WBC 60/HPF, Gram stain: gram(-) rod. 원인균으로 가장 가능성 높은 것은?</div>
<div class="opt" data-q="c2" data-correct="0" onclick="sel(this,'c2')">① Bacillus cereus</div>
<div class="opt" data-q="c2" data-correct="0" onclick="sel(this,'c2')">② H. influenzae</div>
<div class="opt" data-q="c2" data-correct="1" onclick="sel(this,'c2')">③ E. coli</div>
<div class="opt" data-q="c2" data-correct="0" onclick="sel(this,'c2')">④ S. aureus</div>
<div class="opt" data-q="c2" data-correct="0" onclick="sel(this,'c2')">⑤ S. typhi</div>
<button class="chkbtn" id="btnc2" onclick="show('c2')">정답 확인</button>
<div class="ansbox" id="ansc2">
<div class="anslabel">정답: ③</div>
<div class="exitem exno">① X — Bacillus cereus: 식중독 원인균, 요로감염 아님</div>
<div class="exitem exno">② X — H. influenzae: 호흡기 감염</div>
<div class="exitem exok">③ O — 젊은 여성 + 방광염→신우신염 진행 + gram(-) rod = E. coli. UTI 1위 원인균</div>
<div class="exitem exno">④ X — S. aureus: gram(+) 구균</div>
<div class="exitem exno">⑤ X — S. typhi: 소화기 감염, 장티푸스 원인</div>
</div>
</div>

<div class="qcard">
<div class="stem"><span class="ytag">19·20·21학번 공통</span> 혈액배양에서 E. coli 동정. 원발 감염 부위로 가장 가능성 높은 것은?</div>
<div class="opt" data-q="c3" data-correct="1" onclick="sel(this,'c3')">① 요로계</div>
<div class="opt" data-q="c3" data-correct="0" onclick="sel(this,'c3')">② 폐</div>
<div class="opt" data-q="c3" data-correct="0" onclick="sel(this,'c3')">③ 뇌</div>
<div class="opt" data-q="c3" data-correct="0" onclick="sel(this,'c3')">④ 피부</div>
<div class="opt" data-q="c3" data-correct="0" onclick="sel(this,'c3')">⑤ 심장</div>
<button class="chkbtn" id="btnc3" onclick="show('c3')">정답 확인</button>
<div class="ansbox" id="ansc3">
<div class="anslabel">정답: ①</div>
<div class="exitem exok">① O — E. coli 균혈증 원발 부위 1위 = 요로계 (방광염→신우신염→균혈증)</div>
<div class="exitem exno">② X — 폐: gram(-) 폐렴은 Klebsiella, Pseudomonas가 흔함</div>
<div class="exitem exno">③ X — 성인 뇌수막염: S. pneumoniae, N. meningitidis 흔함 (신생아는 E. coli 가능)</div>
<div class="exitem exno">④ X — 피부 감염: S. aureus, Streptococcus</div>
<div class="exitem exno">⑤ X — 심내막염: Streptococcus, Enterococcus 흔함</div>
</div>
</div>

<div class="qcard">
<div class="stem"><span class="ytag">18학번 정규</span> E. coli에 대한 설명으로 옳은 것을 모두 고르시오.<br>① gram 음성 간균 &nbsp; ② 정상 장내 상재균으로 존재 가능 &nbsp; ③ EHEC O157:H7: Shiga독소 → HUS 유발 &nbsp; ④ UPEC: P fimbriae로 요로상피 부착 &nbsp; ⑤ 항상 병원성이다</div>
<div class="opt" data-q="c4" data-correct="0" onclick="sel(this,'c4')">① ①②③ 만</div>
<div class="opt" data-q="c4" data-correct="1" onclick="sel(this,'c4')">② ①②③④ 모두</div>
<div class="opt" data-q="c4" data-correct="0" onclick="sel(this,'c4')">③ ①③만</div>
<div class="opt" data-q="c4" data-correct="0" onclick="sel(this,'c4')">④ ①②③④⑤ 모두</div>
<button class="chkbtn" id="btnc4" onclick="show('c4')">정답 확인</button>
<div class="ansbox" id="ansc4">
<div class="anslabel">정답: ② (①②③④)</div>
<div class="exitem exok">① O — gram 음성 간균</div>
<div class="exitem exok">② O — 정상 장내 commensal, 무해하게 공존</div>
<div class="exitem exok">③ O — EHEC: Shiga-like toxin → 출혈성 장염, HUS(용혈성요독증후군)</div>
<div class="exitem exok">④ O — UPEC (Uropathogenic E.coli): P fimbriae → 요로상피 부착</div>
<div class="exitem exno">⑤ X — 상재균으로 존재 가능. 병원성 주식이 있어야 감염 발생</div>
</div>
</div>
</div>

<!-- Vibrio vulnificus -->
<div class="sec" id="t4">
<div class="sh"><div class="sn">4</div><div class="st">Vibrio vulnificus <span class="badge">★★★★★</span></div></div>
<div class="cb r"><h4>핵심</h4>
생굴·어패류, 여름철, <b>간경화(간질환)</b> 환자 → 치사율 매우 높음<br>
임상: 원발성 패혈증 or 괴사성 근막염(haemorrhagic bullae)<br>
치료: <b>ciprofloxacin(FQ) + ceftriaxone(3세대 ceph)</b> + aggressive debridement<br>
또는 doxycycline + 3세대 ceph (동등)
</div>

<div class="qcard">
<div class="stem"><span class="ytag r">22학번 Q18</span> 50세 환자, 전날 조개 날것으로 섭취. 기저 간경화. 내원 시 수축기혈압 80mmHg, 체온 39°C. 하지에 홍반성 반점 → haemorrhagic bullae로 진행. 가장 의심되는 병인균은?</div>
<div class="opt" data-q="d1" data-correct="1" onclick="sel(this,'d1')">① Vibrio vulnificus</div>
<div class="opt" data-q="d1" data-correct="0" onclick="sel(this,'d1')">② Staphylococcus aureus</div>
<div class="opt" data-q="d1" data-correct="0" onclick="sel(this,'d1')">③ Neisseria meningitidis</div>
<div class="opt" data-q="d1" data-correct="0" onclick="sel(this,'d1')">④ Streptococcus pneumoniae</div>
<div class="opt" data-q="d1" data-correct="0" onclick="sel(this,'d1')">⑤ Streptococcus pyogenes</div>
<button class="chkbtn" id="btnd1" onclick="show('d1')">정답 확인</button>
<div class="ansbox" id="ansd1">
<div class="anslabel">정답: ①</div>
<div class="exitem exok">① O — 생굴 섭취 + 간경화 + 하지 haemorrhagic bullae = Vibrio vulnificus 전형 소견</div>
<div class="exitem exno">② X — S. aureus: 피부감염 유발하나 이 임상상은 Vibrio</div>
<div class="exitem exno">③ X — N. meningitidis: 뇌수막염 + 피부자반(petechiae, purpura)</div>
<div class="exitem exno">④ X — S. pneumoniae: 폐렴, 뇌수막염</div>
<div class="exitem exno">⑤ X — S. pyogenes: 괴사성 근막염 유발 가능하나 해산물 섭취 + 간경화 조합은 Vibrio</div>
</div>
</div>

<div class="qcard">
<div class="stem"><span class="ytag">18·19·20·21학번 공통</span> 간경화 환자, 생굴 섭취 후 발열 + 하지 괴사성 피부병변. 치료로 옳은 것은?</div>
<div class="opt" data-q="d2" data-correct="0" onclick="sel(this,'d2')">① ampicillin 단독</div>
<div class="opt" data-q="d2" data-correct="0" onclick="sel(this,'d2')">② penicillin G 단독</div>
<div class="opt" data-q="d2" data-correct="1" onclick="sel(this,'d2')">③ ciprofloxacin + ceftriaxone</div>
<div class="opt" data-q="d2" data-correct="0" onclick="sel(this,'d2')">④ vancomycin 단독</div>
<div class="opt" data-q="d2" data-correct="0" onclick="sel(this,'d2')">⑤ metronidazole 단독</div>
<button class="chkbtn" id="btnd2" onclick="show('d2')">정답 확인</button>
<div class="ansbox" id="ansd2">
<div class="anslabel">정답: ③</div>
<div class="exitem exno">① X — ampicillin: Vibrio 단독 치료 부족</div>
<div class="exitem exno">② X — penicillin G: gram(-) 세균에 효과 불충분</div>
<div class="exitem exok">③ O — <b>FQ(ciprofloxacin) + 3세대 ceph(ceftriaxone)</b> 병합 + 괴사 부위 광범위 절제술</div>
<div class="exitem exno">④ X — vancomycin: gram(+) MRSA 치료제</div>
<div class="exitem exno">⑤ X — metronidazole: 혐기성균·원충 치료</div>
<div class="exnote">대안: doxycycline + 3세대 cephalosporin (동등 효과)</div>
</div>
</div>
</div>

<!-- N. meningitidis -->
<div class="sec" id="t5">
<div class="sh"><div class="sn">5</div><div class="st">N. meningitidis <span class="badge">★★★★</span></div></div>
<div class="cb r"><h4>핵심</h4>
CSF gram stain: gram(-) 쌍구균, 호중구 내 위치<br>
임상: 뇌수막염 + 피부자반(수막구균혈증) → 급격히 악화<br>
예방: <b>ceftriaxone IM 1회 / rifampin 경구 2일 / ciprofloxacin 1회</b>
</div>

<div class="qcard">
<div class="stem"><span class="ytag r">22학번 Q19</span> 21세 남자, 의식저하. 2일 전부터 발열·근육통. 혈압 70/40, 맥박 126, 호흡 25. CSF: WBC 1800/mm³ (Neutrophil 97%), gram(-) cocci. 원인균은?</div>
<div class="opt" data-q="e1" data-correct="0" onclick="sel(this,'e1')">① Vibrio vulnificus</div>
<div class="opt" data-q="e1" data-correct="0" onclick="sel(this,'e1')">② Staphylococcus aureus</div>
<div class="opt" data-q="e1" data-correct="1" onclick="sel(this,'e1')">③ Neisseria meningitidis</div>
<div class="opt" data-q="e1" data-correct="0" onclick="sel(this,'e1')">④ Streptococcus pneumoniae</div>
<div class="opt" data-q="e1" data-correct="0" onclick="sel(this,'e1')">⑤ Streptococcus pyogenes</div>
<button class="chkbtn" id="btne1" onclick="show('e1')">정답 확인</button>
<div class="ansbox" id="anse1">
<div class="anslabel">정답: ③</div>
<div class="exitem exno">① X — Vibrio: 어패류 섭취, 피부 bullae</div>
<div class="exitem exno">② X — S. aureus: gram(+) 구균</div>
<div class="exitem exok">③ O — gram(-) cocci (쌍구균) + 뇌수막염 + 호중구 우세 + 자반 → N. meningitidis</div>
<div class="exitem exno">④ X — S. pneumoniae: gram(+) 쌍구균 (lancet형). 성인 뇌수막염 1위이나 gram(+)</div>
<div class="exitem exno">⑤ X — S. pyogenes: gram(+) 구균</div>
<div class="exnote">CSF 감별: N. meningitidis(gram- 쌍구균) vs S. pneumoniae(gram+ 쌍구균) vs Listeria(gram+ 간균)</div>
</div>
</div>

<div class="qcard">
<div class="stem"><span class="ytag r">22학번 Q20</span> 위 환자(N. meningitidis)에게 기관삽관 시행. 균에 노출된 의사에게 사용해야 할 예방 약제는?</div>
<div class="opt" data-q="e2" data-correct="0" onclick="sel(this,'e2')">① cefazolin</div>
<div class="opt" data-q="e2" data-correct="1" onclick="sel(this,'e2')">② ciprofloxacin</div>
<div class="opt" data-q="e2" data-correct="0" onclick="sel(this,'e2')">③ vancomycin</div>
<div class="opt" data-q="e2" data-correct="0" onclick="sel(this,'e2')">④ clindamycin</div>
<div class="opt" data-q="e2" data-correct="0" onclick="sel(this,'e2')">⑤ metronidazole</div>
<button class="chkbtn" id="btne2" onclick="show('e2')">정답 확인</button>
<div class="ansbox" id="anse2">
<div class="anslabel">정답: ②</div>
<div class="exitem exno">① X — cefazolin: N. meningitidis 예방 적응 없음</div>
<div class="exitem exok">② O — <b>ciprofloxacin 단회 경구</b>: N. meningitidis 밀접접촉자 예방 (ceftriaxone IM, rifampin과 동등)</div>
<div class="exitem exno">③ X — vancomycin: gram(+) 치료제</div>
<div class="exitem exno">④ X — clindamycin: 혐기성균, gram(+) 치료</div>
<div class="exitem exno">⑤ X — metronidazole: 혐기성균·원충 치료</div>
<div class="exnote">N. meningitidis 예방: ceftriaxone 250mg IM 1회 / ciprofloxacin 500mg po 1회 / rifampin 600mg po 12시간마다 2일</div>
</div>
</div>

<div class="qcard">
<div class="stem"><span class="ytag">19·20·21학번 공통</span> 기숙사생, 두통·발열·경부강직 + 피부자반. CSF: gram(-) 쌍구균. 밀접접촉자 예방적 항생제로 옳은 것을 모두 고르시오.</div>
<div class="opt" data-q="e3" data-correct="0" onclick="sel(this,'e3')">① ampicillin</div>
<div class="opt" data-q="e3" data-correct="1" onclick="sel(this,'e3')">② rifampin 경구</div>
<div class="opt" data-q="e3" data-correct="1" onclick="sel(this,'e3')">③ ceftriaxone IM 1회</div>
<div class="opt" data-q="e3" data-correct="1" onclick="sel(this,'e3')">④ ciprofloxacin 1회</div>
<div class="opt" data-q="e3" data-correct="0" onclick="sel(this,'e3')">⑤ vancomycin</div>
<button class="chkbtn" id="btne3" onclick="show('e3')">정답 확인</button>
<div class="ansbox" id="anse3">
<div class="anslabel">정답: ②③④</div>
<div class="exitem exno">① X — ampicillin: N. meningitidis 예방 적응 없음</div>
<div class="exitem exok">② O — rifampin 600mg bid × 2일</div>
<div class="exitem exok">③ O — ceftriaxone 250mg IM 1회 (임산부에 선호)</div>
<div class="exitem exok">④ O — ciprofloxacin 500mg 1회</div>
<div class="exitem exno">⑤ X — vancomycin: 예방 적응 없음</div>
</div>
</div>
</div>
</div>
</body>
</html>'''

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Part 1 완료: {os.path.getsize(path)} bytes')
print(f'저장 위치: {path}')