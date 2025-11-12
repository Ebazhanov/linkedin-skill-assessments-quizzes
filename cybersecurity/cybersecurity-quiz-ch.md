## 資訊安全（Cybersecurity）測驗

#### Q1. 根據共享責任模型，哪一種雲端運算模型讓雲端服務供應商（CSP）承擔最多責任？

- [ ] Hybrid Cloud（混合雲）
- [x] Software as a Service (SaaS)
- [ ] Platform as a Service (PaaS)
- [ ] Infrastructure as a Service (IaaS)

#### Q2. 哪個選項可消除雲端運算中的多租戶風險？

- [ ] PaaS
- [ ] public cloud（公有雲）
- [x] private cloud（私有雲）
- [ ] IaaS

#### Q3. 貴組織最近實施了整合通訊解決方案，並在每個桌面配備 VoIP 電話。你負責研究 VoIP 系統的弱點。VoIP 電話最容易受到哪種類型攻擊？

- [x] denial-of-service（DoS）
- [ ] brute force attacks（暴力破解）
- [ ] malware（惡意程式）
- [ ] buffer overflow（緩衝區溢位）

#### Q4. 哪項安全控制無法對安全事件做出主動回應？

- [ ] cloud access security broker (CASB)
- [ ] intrusion prevention system (IPS)
- [x] intrusion detection system (IDS)
- [ ] next generation firewall（下一代防火牆）

**說明**：入侵偵測系統（`IDS`）是一種裝置或軟體應用，用於監控網路或系統是否存在惡意活動或政策違規。

[Quizlet](https://quizlet.com/217188159/cissp-practice-testschapter-7-security-operations-domain7-flash-cards/)

#### Q5. Packet sniffer 又稱為什麼？

- [ ] SIEM
- [ ] UTM
- [x] protocol analyzer
- [ ] data sink

#### Q6. 哪個選項是在程式碼運行時進行測試？

- [ ] code review（程式碼審查）
- [ ] code analysis（程式碼分析）
- [ ] static analysis（靜態分析）
- [x] dynamic analysis（動態分析）

#### Q7. 哪個選項描述的是個別軟體開發者可以對其自身程式碼進行的測試？

- [ ] gray box testing（灰箱測試）
- [ ] integration testing（整合測試）
- [ ] white box testing（白箱測試）
- [x] unit testing（單元測試）

#### Q8. 在 black box penetration testing（黑箱滲透測試）中，會向測試人員提供關於目標環境的哪些資訊？

- [x] none（無）
- [ ] limited details of server and network infrastructure
- [ ] all information
- [ ] limited details of server infrastructure

#### Q9. 哪種安全控制最能透過識別與防止未核可的雲端應用與服務來防範影子 IT？

- [ ] intrusion prevention system (IPS)
- [ ] next generation firewall（下一代防火牆）
- [x] cloud access security broker (CASB)
- [ ] intrusion detection system (IDS)

#### Q10. 哪個選項是對抗串通（collusion）的最佳防禦？

- [ ] 監控員工對系統與資料的正常存取模式
- [ ] 規律套用系統與應用更新
- [ ] 容錯基礎架構與資料備援
- [x] separation of duties（職責分離）與 job rotation（職務輪調）

[Stack Exchange](https://security.stackexchange.com/a/114835/249930)

#### Q11. 在滲透測試期間，你找到一個包含系統雜湊密碼的檔案。以下哪種攻擊最可能在合理時間內成功取得這些雜湊密碼？

- [x] rainbow table attack
- [ ] pass-the-hash attack
- [ ] password spray attack
- [ ] brute force attack

**說明**：彩虹表攻擊能更有效率地破解大量雜湊密碼；相較之下，暴力破解所需時間更長，且常無法在合理時間內完成。

[Professor Messer](https://www.professormesser.com/free-a-plus-training/220-1002/brute-force-attacks-3).

#### Q12. 圖中哪個區域為 DMZ？

![image](https://user-images.githubusercontent.com/50566479/136518616-8712a45f-8ba5-48bd-ac60-5a96ddf754ae.png?raw=png)

- [ ] 4
- [ ] 1
- [x] 2
- [ ] 3

#### Q13. 你為使用者設定了加密 USB 隨身碟，需在面對面會議中傳遞敏感檔案。通常使用哪一種加密來加密該檔案？

- [ ] file hash（雜湊）
- [ ] asymmetric encryption（非對稱加密）
- [ ] digital signature（數位簽章）
- [x] symmetric encryption（對稱加密）

#### Q14. DRP 與 BCP 的差異是什麼？

- [x] DRP 讓企業在災難下仍能持續運作；BCP 著重於回復原始能力。
- [ ] BCP 讓企業在災難下仍能持續運作；DRP 著重於回復原始能力。
- [ ] BCP 是 DRP 的一部分。
- [ ] DRP 是 BCP 的一部分。

#### Q15. 分散式阻斷服務（DDoS）攻擊最主要影響資訊安全的哪個面向？

- [ ] non-repudiation（不可否認）
- [ ] integrity（完整性）
- [x] availability（可用性）
- [ ] confidentiality（機密性）

#### Q16. 你需要建議一套解決方案，能自動依 CIS 基準評估你在雲端託管的 VM，以識別偏離安全最佳實務之處。應建議哪種類型的解決方案？

- [x] Cloud Security Posture Management (CSPM)
- [ ] Intrusion Detection and Prevention System (IDPS)
- [ ] Cloud Workload Protection Platforms (CWPP)
- [ ] Cloud Access Security Brokers (CASBs)

#### Q17. 何者可驗證資料檔案的完整性？

- [ ] Compression（壓縮）
- [x] Hashing（雜湊）
- [ ] Symmetric encryption（對稱加密）
- [ ] Stenography（隱寫術）

#### Q18. 下列何者是美國州政府層級的隱私法規範例？

- [x] CCPA
- [ ] GDPR
- [ ] NIST Privacy Framework
- [ ] OSPF

#### Q19. 用於保護、限制、監控、稽核與治理可存取敏感資料與資源之身分的政策與技術合稱為何？

- [x] identity and access management (IAM)
- [ ] privileged account management (PAM)
- [ ] authentication and authorization
- [ ] least privilege（最小權限）

#### Q20. 你已在組織的雲端服務中設定稽核，以便在發生安全事件時使用。稽核軌跡屬於哪一種安全控制？

- [ ] preventive control（預防性）
- [x] detective control（偵測性）
- [ ] directive control（指導性）
- [ ] corrective control（修正性）

**說明**：在 CISSP 的脈絡中，稽核軌跡一般被視為「偵測性」安全控制。

#### Q21. 電力供應短期中斷稱為什麼？

- [ ] grayout
- [x] blackout
- [ ] brownout
- [ ] whiteout

#### Q22. 安全部門建議在所有端點新增一層防護，以對抗持續性威脅與 zero-day 漏洞。該解決方案應能保護所有連網裝置，且不受作業系統限制。哪種方案最適合？

- [ ] Security Information Event Management (SIEM)
- [ ] Extended Detection and Response (XDR)
- [x] next generation firewall (NGFW)
- [ ] Cloud App Security Broker (CASB)

#### Q23. 下列何者「不是」威脅建模方法論？

- [ ] TRIKE
- [x] TOGAF
- [ ] STRIDE
- [ ] MITRE ATT&CK

#### Q24. 貴組織正進行一個新電商應用的試點部署，你需建議評估該軟體安全性的策略。組織無法取得其原始碼。

#### 應選擇哪一種策略？

- [x] dynamic application security testing（動態應用安全測試）
- [ ] unit testing
- [ ] white box testing
- [ ] static application security testing

#### Q25. 你需要停用公司裝置的相機，以防止對敏感文件、會議與對話進行截圖與錄影。哪種解決方案最合適？

- [x] Mobile Device Management (MDM)
- [ ] Data Loss Prevention (DLP)
- [ ] Intrusion Detection and Prevention System (IDPS)
- [ ] Cloud Access Security Broker (CASB)

#### Q26. 在一個非對稱加密系統中，100 位使用者共需要多少把金鑰？

- [x] 200
- [ ] 400
- [ ] 100
- [ ] 300

**說明**：非對稱加密所需金鑰數量的公式為 `2n`，其中 `n` 為通訊雙方（或多方）的數量。

#### Q27. 兩家競爭的線上零售商在全球各大洲處理信用卡交易。一家位於美國，另一家位於荷蘭。兩者在確保交易安全時都必須遵循哪項規範？

- [ ] Federal Information Security Management Act (FISMA)
- [x] Payment Card Industry Data Security Standard (PCI-DSS)
- [ ] General Data Protection Regulation (GDPR)
- [ ] International Organization for Standardization and International Electrotechnical Commission (ISO/IEC 27018)

**說明**：Payment Card Industry Data Security Standard（`PCI DSS`）是全球信用卡產業的安全標準，凡是儲存、處理或傳輸持卡人資料的所有實體（含金融機構、線上零售商與服務供應商）皆必須遵循。

[PCI Security Overview](https://www.pcisecuritystandards.org/pci_security/standards_overview)

#### Q28. 什麼提供一種共通語言，用結構化且可重複的方式描述安全事件？

- [ ] Common event format
- [ ] common weakness enumeration
- [x] common vulnerabilities and exposures
- [ ] common vulnerability scoring system

**說明**：Common Vulnerabilities and Exposures（`CVE`）提供一種標準化的參照方法，用於記錄並辨識已公開的資訊安全弱點與曝露。

#### Q29. 哪種類型的應用可在網路區段攔截諸如密碼等敏感資訊？

- [ ] log server
- [ ] network scanner
- [ ] firewall
- [x] protocol analyzer

**說明**：`protocol analyzer` 是用於擷取並分析通訊通道上訊號與資料流量的工具。

[WireShark](https://www.wireshark.org) is a protocol analyzer.

#### Q30. 攻擊者發現可以透過分析多個較不敏感的公開資料，推斷出敏感機密資訊。這屬於哪種安全問題？

- [ ] aggregation
- [x] inference
- [ ] SQL injection
- [ ] cross-origin resource sharing

**說明**：`Inference Attack` 是透過分析資料以不正當方式推得個體或資料庫敏感資訊的資料探勘技術。若攻擊者能以高度信心推斷出受保護資訊的真實值，即可視為敏感資訊外洩。**來源**：([Wikipedia](https://en.wikipedia.org/wiki/Inference_attack))。

#### Q31. 哪個動作是授與已驗證的一方執行操作或存取資源的許可？

- [ ] Zero Trust Security
- [ ] Role-Based Access Control (RBAC)
- [x] authorization
- [ ] Single Sign-On

[Okata.com](https://www.okta.com/identity-101/authentication-vs-authorization/)

#### Q32. 根據 GDPR，data \_ 指的是被蒐集資料的那個人。

- [ ] processor
- [ ] object
- [x] subject
- [ ] controller

[Intersoft Consulting](https://gdpr-info.eu/art-4-gdpr/)

#### Q33. 下列何者不是零信任（zero trust）安全的原則？

- [ ] use least privilege access（最小權限）
- [ ] verify explicitly（明確驗證）
- [x] trust but verify（信任但驗證）
- [ ] assume breach（假設已遭入侵）

**說明**：零信任假設系統終將被入侵，並以「不存在邊界」為前提來設計安全防護；因此預設不信任任何人事物。

[NIST](https://www.nist.gov/blogs/taking-measure/zero-trust-cybersecurity-never-trust-always-verify)

#### Q34. 哪種攻擊是利用輸入驗證的弱點？

- [ ] ARP spoofing
- [ ] pharming attacks
- [x] cross-site scripting (XSS)
- [ ] DNS poisoning

[White Hat Sec](https://www.whitehatsec.com/glossary/content/input-validation)

#### Q35. 你是資安分析師，收到簡訊告警可能發生攻擊。哪項安全控制最不可能產生這種告警？

- [ ] IDS
- [ ] SIEM
- [x] packet sniffer
- [ ] IPS

#### Q36. SQL injection 會插入使資料庫敘述永遠為真的程式碼片段，例如哪一個？

- [ ] `SELECT * FROM users WHERE username = " AND 1=1--'`
- [ ] `SELECT * FROM users WHERE username = " AND 1!=1--'`
- [x] `SELECT * FROM users WHERE username = " OR 1=1--'`
- [ ] `SELECT * FROM users WHERE username = " OR 1!=1--'`

#### Q37. 哪種類型的安全評估需要存取原始碼？

- [x] static analysis
- [ ] black box testing
- [ ] dynamic analysis
- [ ] penetration testing

#### Q38. 哪個是用於掃描網路上活動主機與開放連接埠的開源解決方案？

- [ ] Autopsy
- [ ] Snort
- [x] Nmap
- [ ] Wireshark

**說明**：nmap 是連接埠掃描器（[Wikipedia](https://en.wikipedia.org/wiki/Nmap)）；Wireshark 是流量分析器；Snort 是 IDS；Autopsy 用於鑑識分析。

#### Q39. 在實施資料外洩防護（DLP）策略時，流程的第一步是什麼？

- [x] 評估可用 DLP 產品的功能，以判斷最符合組織需求者。
- [ ] 檢視組織內敏感資料的流向，以更了解其使用模式。
- [ ] 盤點組織所有資料，依敏感度建立分類。
- [ ] 進行風險評估，以決定最佳的資料標籤策略。

#### Q40. 哪種惡意程式會變更作業系統並隱藏其行跡？

- [ ] virus
- [ ] worm
- [x] rootkit
- [ ] Trojan horse

#### Q41. Virtual Private Networks (VPNs) 使用什麼在兩個網路之間建立安全連線？

- [x] encryption
- [ ] a metropolitan area network
- [ ] a virtual local area network
- [ ] a wide area network

#### Q42. 挑戰使用者證明其身分的過程稱為什麼？

- [x] authentication
- [ ] Single Sign-On
- [ ] authorization
- [ ] Role-Based Access Control (RBAC)

#### Q43. 哪種網攻旨在消耗應用資源，使合法使用者無法使用？

- [ ] SQL injection
- [ ] dictionary attack
- [x] Distributed Denial of Service (DDoS)
- [ ] rainbow table attack

#### Q44. 你是新進資安人員，第一個任務是簡報貴組織可能遭遇的威脅。下列哪一項最能描述此任務？

- [ ] risk mitigation（風險緩解）
- [ ] threat assessment（威脅評估）
- [x] risk management（風險管理）
- [ ] enumeration（盤點）

#### Q45. 你在咖啡店連上公共無線存取點（WAP）。最可能遭遇哪種攻擊？

- [x] man-in-the-middle attack（中間人攻擊）
- [ ] back door
- [ ] logic bomb
- [ ] virus

#### Q46. 你被指派建議一套能集中管理組織內行動裝置的解決方案。哪種技術最能滿足需求？

- [ ] Extended Detection and Responde (XDR)
- [ ] Security Information Event Management (SIEM)
- [ ] Intrusion Detection and Prevention System (IDPS)
- [x] Mobile Device Management (MDM)

#### Q47. 下列哪種弱點無法在一般的弱點評估中被發現？

- [ ] file permissions
- [ ] buffer overflow
- [x] zero-day vulnerability
- [ ] cross-site scripting

#### Q48. DLP 專案團隊即將為組織的資料進行分類。分類的主要目的為何？

- [ ] 它識別法規遵循需求。
- [ ] 它能為 IT 預算支出排定優先順序。
- [ ] 它量化資料外洩的潛在成本。
- [x] 它建立資料對組織的價值。

**說明**：在 DLP 脈絡下，資料分類的主要目的在於協助組織識別、標示並保護敏感資訊，避免未授權揭露或外洩。DLP 是一組技術與流程，用於防止敏感資料遭未授權存取、使用與傳輸。

#### Q49. 你負責管理組織的公有雲基礎架構安全。你需要為多種 IaaS 與 PaaS 服務（包含新的 Kubernetes 叢集）上的資料與應用提供保護。哪種解決方案最適合？

- [x] Cloud Workload Protection Platforms (CWPP)
- [ ] Cloud Security Posture Management (CSPM)
- [ ] Cloud Access Security Brokers (CASBs)
- [ ] Intrusion Detection and Prevention System (IDPS)

[Explanation](https://www.gartner.com/reviews/market/cloud-workload-protection-platforms)

#### Q50. 共用帳號憑證違反存取控制的哪個面向？

- [ ] identification（識別）
- [ ] authorization（授權）
- [ ] accounting（稽核）
- [x] authentication（認證）

**說明**：共用帳號憑證違反了存取控制中的「認證」面向。認證是用來核驗使用者、系統或應用身分的過程；憑證共用會讓多人使用同一組登入資訊，進而削弱認證機制並危及系統安全。

#### Q51. 你已將遭受惡意軟體攻擊的伺服器還原至先前狀態。事件回應流程的最後一步是什麼？

- [ ] Eradication / Remediation（根除 / 修復）
- [ ] Certification（認證）
- [ ] Reporting（回報）
- [x] Lessons Learned（經驗教訓）

#### Q52. 哪種加密方式使用一組公鑰與私鑰來加解密資料？

- [x] asymmetric（非對稱）
- [ ] symmetric（對稱）
- [ ] hashing（雜湊）
- [ ] all of these answers

#### Q53. 你剛剛識別並緩解了一起使用 command and control 的使用者端惡意軟體攻擊。下一步是什麼？

- [ ] Reporting
- [ ] Recovery
- [x] Eradiction / Remediation
- [ ] Lessons Learned

[Explanation: Pages 29 to 31 ->](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-83r1.pdf)

#### Q54. 哪種程式語言最容易受到緩衝區溢位攻擊？

- [x] C
- [ ] Java
- [ ] Ruby
- [ ] Python

#### Q55. 哪一列正確描述了風險管理技術？

- [ ] risk acceptance, risk mitigation, risk containment, and risk qualification
- [ ] risk avoidance, risk transference, risk containment, and risk quantification
- [ ] risk avoidance, risk mitigation, risk containment, and risk acceptance
- [x] risk avoidance, risk transference, risk mitigation, and risk acceptance

#### Q56. 要實作傳輸中加密，例如安全瀏覽使用的 HTTPS，會使用哪種類型的加密？

- [ ] asymmetric
- [x] both symmetric and asymmetric
- [ ] neither symmetric or asymmetric
- [ ] symmetric

#### Q57. 哪種程式使用 Windows Hooks 來攔截使用者鍵入的按鍵、隱藏於程序清單，並可能危及系統與線上存取憑證？

- [ ] trojan
- [ ] keystroke collector
- [ ] typethief
- [x] keylogger

#### Q58. 勒索軟體如何影響受害者的檔案？

- [ ] 破壞它們
- [x] 將它們加密
- [ ] 竊取它們
- [ ] 出售它們

#### Q59. 你的電腦被感染，並在收到 botmaster 的指令後對目標系統發送流量。你目前處於何種狀態？

- [ ] 它成為 money mule。
- [x] 它成為 zombie。
- [ ] 它成為 bastion host。
- [ ] 它成為 botnet。

#### Q60. 你為金融組織選擇一個網安框架，以導入有效且可稽核的 IT 治理與管理流程。你會選擇哪個框架？

- [ ] C2M2
- [x] NIST SP 800-37
- [ ] ISO/IEC 27001
- [ ] COBIT

#### Q61. NIST 在 2018 年 12 月發布了 SP 800-37 的修訂版，提供管理安全與隱私風險的紀律化、結構化與彈性流程。SP 800-37 屬於哪種類型文件？

- [x] a risk management framework
- [ ] a guide to risk assessments
- [ ] a guideline for vulnerability testing
- [ ] a step-by-step guide for performing business impact analyses

#### Q62. 2010 年最惡名昭彰的軍規 APT 針對伊朗離心機，該 APT 名稱為？

- [ ] duqu
- [ ] agent BTZ
- [x] stuxnet
- [ ] flame

#### Q63. 你會在哪裡記錄已識別的風險及其詳細資訊（如 ID 與名稱、資訊分類、風險負責人）？

- [ ] in the risk assessment documentation
- [x] in the risk register
- [ ] in the business impact ledger
- [ ] in the Orange Book

#### Q64. 為防止事件壓垮資源，什麼是必要的？

- [ ] 斷開網路連線
- [x] early containment（早期圍堵）
- [ ] 繼續監控其他事件
- [ ] 問題根除

#### Q65. FUD 昂貴且常使低風險事件被戲劇化。哪兩種晶片弱點曾被報導需完全更換，但最後以韌體更新修復？

- [ ] fire and ice exploits
- [x] meltdown and spectre exploits
- [ ] Intel and STMicro CPU exploits
- [ ] super microboard and Apple iPhone exploits

#### Q66. ASD Top Four 包含應用白名單、應用修補、作業系統修補與限制管理權限。它們可防堵多少比例的入侵？

- [ ] 40 percent
- [ ] 60 percent
- [x] 85 percent
- [ ] 100 percent

#### Q67. 你在 SOC 分析網路流量，偵測到疑似連接埠掃描。這代表什麼？

- [ ] 可能是會計部門執行的特定程式。
- [ ] 這是進行中的攻擊，應立即回報。
- [ ] 這是你的業務正常操作。
- [x] 這可能是攻擊的前兆。

#### Q68. ISF Standard of Good Practice 多久更新一次？

- [x] annual（每年）
- [ ] biannually
- [ ] bimonthly
- [ ] monthly

#### Q69. 你的事件回應團隊因缺乏授權，無法在不經管理層核准下採取行動以圍堵事件。準備階段的哪個關鍵步驟被跳過了？

- [ ] 成立事件回應委員會以監督可能發生的事件。
- [x] 取得預先授權，可單方面採取行動並做出或指示緊急變更。
- [ ] 邀請管理層加入事件回應團隊並擔任領導。
- [ ] 指派具備適當權限的緊急回應負責人。

#### Q70. NIST SP 800-53 是兩大重要控制框架之一，另一個是什麼？

- [ ] ISO 27001
- [ ] NIST SP 800-54
- [x] ISO 27002
- [ ] NIST SP 751-51

#### Q71. 由 NIST 於 1990 年成立，透過工作坊促進事件預防協調、加速對事件的反應、並讓專家分享資訊的是哪個組織？

- [x] Forum of Incident Response and Security Teams
- [ ] Crest UK Response Teams
- [ ] Community of Computer Incident Response Teams
- [ ] NIST Special Publication 800-61 Response Teams

#### Q72. 你已實施控制以降低威脅、弱點與對業務的影響。剩下的是哪種風險？

- [ ] inherent risk（固有風險）
- [x] residual risk（剩餘風險）
- [ ] applied risk
- [ ] leftover risk

[Explanation](https://www.sans.org/brochure/course/information-security-risk-management/226)

#### Q73. 風險被識別後有四種處置方式。哪一項是導入控制以降低風險？

- [x] risk mitigation（風險緩解）
- [ ] risk acceptance（風險接受）
- [ ] risk avoidance（風險迴避）
- [ ] risk transfer（風險移轉）

#### Q74. 廠商常將產品提交至哪種安全控制評估方案，以提供獨立的產品保證觀點？

- [x] Common Criteria
- [ ] risk management certification board
- [ ] OWASP security evaluation
- [ ] ISO 27000

#### Q75. 哪個組織在其 IoT 安全指南中發布了最全面的一組控制？

- [ ] IoT ISACA
- [x] IoT Security Foundation
- [ ] OWASP
- [ ] GSMA

#### Q76. 哪份主要參考與 Cloud Security Alliance Guidance 一同構成雲端運算關鍵領域安全指南？

- [ ] ISO 27001
- [ ] ISO 27017
- [ ] Cloud Security Guidelines
- [x] Cloud Controls Matrix

[Explanation](https://www.cybersaint.io/blog/six-steps-of-the-nist-risk-management-framework)

#### Q77. 參考監視器（reference monitor）的基本特性為何？

- [ ] 多功能、準確且高速運作。
- [x] 防篡改、可被一致喚起、且足夠小以便測試。
- [ ] 受限、機密、與極機密。

#### Q78. 根據 NIST，要利用網安框架的第一個動作是什麼？

- [x] Identify the key business outcomes.
- [ ] Understand the threats and vulnerabilities.
- [ ] Conduct a risk assessment.
- [ ] Analyze and prioritize gaps to create the action plan.

[Explanation](https://www.cybersaint.io/blog/six-steps-of-the-nist-risk-management-framework)

#### Q79. 你要在組織內實施網安計畫並希望採用「事實上的標準」框架。你會選擇哪個？

- [ ] the ISACA Cybersecurity Framework
- [ ] the COBIT Cybersecurity Framework
- [ ] the ISC2 Cybersecurity Framework
- [x] the NIST Cybersecurity Framework

#### Q80. 2014 年，有 4,278 個殭屍電腦 IP 被用來在約一小時內每分鐘發送逾百萬封包癱瘓一家企業。這是哪種攻擊？

- [ ] salami attack
- [ ] DoS (Denial of Service) attack
- [x] DDoS (Distributed Denial of Service) attack
- [ ] botnet attack

[Explanation](https://www.forbes.com/sites/parmyolson/2014/11/20/the-largest-cyber-attack-in-history-has-been-hitting-hong-kong-sites/?sh=56e071cd38f6)

#### Q81. 資料外洩通報的法規要求，特別是歐盟 GDPR，對企業造成何種影響？

- [x] 在資料外洩事件中提高企業責任。
- [ ] 在資料外洩事件中提高消費者責任。
- [ ] 在資料外洩事件中降低消費者責任。
- [ ] 在資料外洩事件中降低企業責任。

#### Q82. 哪個法規框架規範美國醫療產業的要求？

- [ ] FedRAMP
- [ ] GDPR
- [ ] PCI-DSS
- [x] HIPAA

[Explanation](https://online.maryville.edu/blog/5-important-regulations-in-united-states-healthcare/)

#### Q83. DevOps 與 DevSecOps 的差異為何？

- [x] DevSecOps 要求在 DevOps 的 CI/CD 流程中納入資安工程師。
- [ ] DevSecOps 會放慢 DevOps 的 CI/CD 流程。
- [ ] DevSecOps 在 DevOps 的 CI/CD 流程中放置安全控制。
- [ ] DevSecOps 讓資安工程師主導 DevOps 的 CI/CD 流程。

[Explanation](https://www.linkedin.com/learning/devops-foundations-devsecops/introduction-to-devsecops)

#### Q84. 何時靜態應用安全測試需要存取原始碼？

- [x] always
- [ ] only when assessing regulatory compliance
- [ ] only if following the Agile model
- [ ] never

[Explanation:](https://www.synopsys.com/glossary/what-is-sast.html)

#### Q85. 貴組織以自研系統服務客戶訂單。你需建議一種雲端模型以符合以下需求：

    Control of security required for regulatory compliance
    Legacy application and database support
    Scalability to meet seasonal increases in demand

哪一種雲端模型最合適？

- [ ] government cloud
- [ ] public cloud
- [x] hybrid cloud
- [ ] private cloud

#### Q86. 你剛掃描完一個網路，沒有知名連接埠是開啟的。如何找出在某主機上以隨機連接埠運作的 webserver？

- [ ] 放棄目前目標網路並改掃下一個。
- [ ] 換用其他掃描工具，或對所有開啟連接埠發動隨機攻擊等高資源探測。
- [ ] 開啟隱身模式並檢查是否漏掉任何與網頁伺服器相關的連接埠。
- [x] 啟用掃描工具的其他選項，深入偵測其餘開啟連接埠上應用的型別與版本。

#### Q87. 貴公司高層在談判重要合約時與外部夥伴互通電子郵件。為確保法律效力，資安團隊建議對訊息加入數位簽章。此情境下數位簽章的主要目標為何？（選最佳答案。）

- [x] integrity 與 non-repudiation
- [ ] privacy 與 non-repudiation
- [ ] privacy 與 confidentiality
- [ ] integrity 與 privacy

#### Q88. 下列哪個機制可確保 non-repudiation？

- [ ] MD5
- [ ] Caesar cipher
- [ ] symmetric-key encryption
- [x] asymmetric-key encryption

[Explanation:](https://medium.com/geekoffee/ensuring-integrity-authenticity-and-non-repudiation-in-data-transmission-using-node-js-af73c2404153)

#### Q89. 哪種軟體開發生命週期方法最相容於 DevSecOps？

- [x] Agile
- [ ] Model-Driven Development
- [ ] Waterfall
- [ ] Model-Driven Architecture

#### Q90. 哪項資訊安全原則指出應以多種彼此獨立的方法來防禦任何特定攻擊？

- [ ] separation of duties
- [ ] privileged account management (PAM)
- [x] defense-in-depth
- [ ] least privilege

[Explanation:](<https://en.wikipedia.org/wiki/Defense_in_depth_(computing)>)

#### Q91. 下列哪個描述符合 DevSecOps 的核心原則？

- [ ] 測試與釋出應 100% 自動化
- [ ] 角色分離是軟體安全的關鍵
- [ ] 最終安全責任在應用架構師
- [x] 流程中的每個人都對安全負責

**說明**：DevSecOps 強調在整個軟體開發生命週期中整合安全實務，並推動文化轉型，使參與開發與營運流程的所有人（含開發者、營運團隊與其他利害關係人）共同承擔安全責任，協力在每個階段納入安全。

#### Q92. 你需要保護對外的應用避免常見攻擊，如 XSS、CSRF 與 SQL injection。哪個選項最適合？

- [ ] Security Information Event Management (SIEM)
- [ ] an Instruction Detection and Prevention System (IDPS) appliance
- [x] a web application firewall (WAF)
- [ ] a stateful packet inspection firewall

#### Q93. 事件回應流程中，哪個階段緊接在 identification 之後？

- [ ] Eradication / Remediation
- [x] Reporting
- [ ] Containment / Mitigation
- [ ] Recovery

#### Q94. 資料保存政策如何降低組織的法律責任？

- [ ] 藉由降低 DLP 授權成本
- [x] 藉由確保資料不會被保留超過必要期限
- [ ] 藉由銷毀可能牽連高層不誠實行為的資料
- [ ] 藉由降低與資料存放與保護相關的成本

#### Q95. 你認為最近的服務中斷是內部人員發動的 denial-of-service 攻擊所致。該員工的惡意行為稱為什麼？

- [ ] espionage（間諜活動）
- [x] sabotage（破壞）
- [ ] fraud（詐欺）
- [ ] confidentiality breach（機密外洩）

#### Q96. 哪個框架被廣泛用於制定安全治理標準？

- [ ] Software Capability Maturity Model (SW-CMM)
- [x] Control Objectives for Information and Related Technologies (COBIT)
- [ ] The Open Group Architecture Framework (TOGAF)
- [ ] Software Development Life Cycle (SDLC)

#### Q97. 網路中有連線導向與無連線協定。瀏覽器用什麼確保傳送與接收資料的完整性？

- [ ] 具連線導向的 UDP
- [x] 具連線導向的 TCP
- [ ] 無連線的 UDP
- [ ] 無連線的 TCP

#### Q98. 哪種攻擊針對將 MAC 位址轉換為 IP 位址的相關弱點？

- [ ] DNS poisoning
- [ ] CRL trapping
- [x] ARP spoofing
- [ ] DDoS

#### Q99. 你在公司的事件回應小組中，從 SIEM 蒐集的日誌中發現可疑紀錄，想進一步調查。對這些需要額外審查的紀錄活動，最佳的稱呼是？

- [ ] attack
- [ ] information
- [ ] threat
- [x] event

#### Q100. 你負責組織的鑑識調查，被指派調查一台遭入侵的虛擬應用伺服器。由於其上運行營收應用，需儘快恢復服務。為同時履行職責與滿足業務需求，你下一步該做什麼？

- [ ] 立刻自備份還原伺服器。
- [ ] 將伺服器下線直至調查完成。
- [x] 先對受害虛擬伺服器拍攝快照供調查。
- [ ] 重新啟動伺服器，於非營業時間修復。

#### Q101. Site-to-site VPN 提供從一個網路位址空間（192.168.0.0/24）到另一個位址空間 \_ 的存取。

- [ ] 192.168.0.1/24
- [ ] 192.168.0.3/24
- [x] 10.10.0.0/24
- [ ] 192.168.0.2/24

#### Q102. 你在研究可能威脅公司對外網站應用的攻擊向量。應參考哪個組織做為網頁攻擊向量的權威資料來源？

- [ ] EC-Council
- [ ] ISACA
- [ ] NIST
- [x] OWASP

[Explanation:](https://www.imperva.com/learn/application-security/application-security/)

#### Q103. 哪個作法最能簡化安全人員訓練、改善安全元件之間的整合，並降低企業風險？（選最佳答案。）

- [x] 採用「best-in-suite」的安全策略
- [ ] 採用「trust but verify」的安全策略
- [ ] 採用「best-of-breed」的安全策略
- [ ] 採用「defense-in-depth」的安全策略

**說明**：「best-in-suite」作法指從單一供應商選擇涵蓋多元安全元件的整合方案。此作法可簡化訓練（人員只需熟悉單一套件），並因組件設計上可無縫協作而改善整合度；同時能提供更一致的安全策略，降低多套工具並行管理的複雜度。例：使用 Okta 提供全組織的 SSO。

#### Q104. 何種攻擊可將攻擊者注入的程式碼作為使用者輸入的一部分而被執行？

- [ ] Ping of death
- [x] Buffer overflow
- [ ] Distributed Denial of Service
- [ ] Denial of Service

#### Q105. 下列哪個活動「不是」風險評估的一部分？

- [ ] 識別與估值資產
- [ ] 依關鍵性與成本分析風險
- [x] 停止帶來風險的活動
- [ ] 識別威脅並分析弱點

#### Q106. 你在分析可能的安全事件告警時，於 Web 應用日誌中看到字串：`./../../../var/secrets`。最可能嘗試的是哪種攻擊？

- [ ] brute force
- [ ] session hijacking
- [ ] cross-site scripting
- [x] directory traversal

#### Q107. 風險管理應聚焦哪個象限？

- ![Which quadrant should be the focus of risk management?](Q107-risk-quadrant.jpg)

- [x] 2
- [ ] 1
- [ ] 3
- [ ] 4

#### Q108. 下列哪個選項不會主動辨識安全事件？

- [ ] Extended Detection and Response (XDR)
- [x] Cloud Security Posture Management (CSPM)
- [ ] Security Information Event Management (SEIM)
- [ ] Endpoint Detection and Response (EDR)

#### Q109. 某網站同時要求輸入密碼，並傳送驗證碼到你的手機。此多因子驗證情境使用了哪些因子？

- [ ] what you have 與 what you do
- [ ] what you know 與 what you are
- [x] what you have 與 what you know
- [ ] what you do 與 what you know

[Explanation:](https://www.investopedia.com/terms/t/twofactor-authentication-2fa.asp)

#### Q110. 下列哪個是已公開揭露的資安缺陷清單？

- [ ] DBIR
- [ ] CVE
- [x] CWE
- [ ] CERT

**說明**：Common Weakness Enumeration（CWE）是電腦軟體中已發現之安全缺陷的通用線上字典。

#### Q111. 什麼是 cryptovirology？

- [ ] Plain cryptography
- [ ] Antivirus
- [x] Design powerful malicious software
- [x] Asymmetric backdoor

**說明**：Cryptovirology 研究運用密碼學技術打造具破壞性的惡意軟體；勒索軟體即為代表案例，常以加密受害者檔案的方式要求支付贖金以換取解密金鑰。

#### Q112. metamorphic virus 會做什麼？

- [ ] Static analyser
- [ ] Antivirus
- [x] Generates a whole variable code using a variable encryptor
- [ ] Mutation function

[Explanation:](https://link.springer.com/content/pdf/10.1007/11560647.pdf)

#### Q113. 組織中網路事件最常見的成因是什麼？

- [ ] Vulnerabilities in softwares
- [x] Social Engineering
- [ ] Ransomware
- [ ] Phishing

**說明**：社交工程與人為疏失是網路事件最常見的成因；相較直接入侵並利用系統弱點，攻擊者往往更容易誘使員工洩露密碼或接受 MFA 提示。可參考近期 Uber 與 Cisco 事件。

1. [Reference](https://www.protocol.com/bulletins/uber-breach-hacker-twilio-mfa)
2. [Reference](https://www.swarmnetics.com/blog/cisco-network-breach-voice-phishing-mfa-fatigue-are-becoming-common-attacks/)

#### Q114. 下列哪個術語用於描述一組彼此無關的修補集合？

- [x] Hotfix
- [ ] Update
- [ ] Security Fix
- [ ] Service Pack

#### Q115. 安全團隊應多久審查一次使用者對敏感系統的特權存取？

- [x] 週期性地
- [x] 當使用者離職時
- [x] 當使用者調職時
- [ ] 每天

**說明**：特權存取審查是組織安全計畫中至關重要的一環，可確保僅有獲授權者得以存取最敏感的系統。審查應定期執行，並在特權使用者離職或職務變動時進行。

#### Q116. 用於描述新帳號建立時預設授予使用者的一組權限的術語是什麼？

- [ ] Aggregation
- [ ] Transitivity
- [ ] Baseline
- [x] Entitlement

**說明**：Entitlement 指的是帳號初次佈建時授予使用者的一組權限。

#### Q117. 誰被稱為電腦安全之父？

- [x] August Kerckhoffs
- [ ] Bob Thomas
- [ ] Charles Thomas
- [ ] Robert Kerckhoffs

**說明**：August Kerckhoffs 為語言學家、HEC 的德語教授；其於 1883 年在《Journal of Military Science》發表文章，無意中奠定現代密碼學的基礎，因而被稱為「電腦安全之父」。

#### Q118. 下列哪種攻擊使用正式電子郵件引誘特定個人登入並變更密碼？

- [ ] vishing
- [x] spear phishing
- [ ] brute force attack
- [ ] password spray attack

#### Q119. 資料資產登錄應包含下列哪些項目？

- [ ] 資料位置
- [ ] 資產價值
- [ ] 資產擁有者
- [x] 以上皆是

#### Q120. 確認 Burpsuite 正在攔截網站請求後，你可在哪裡檢查是否有 cleartext 憑證可用於存取目標網頁？

- [ ] 在 Repeater 分頁選 Go
- [ ] 在 Options 分頁確認 loopback 位址與連接埠啟用
- [ ] 檢查 Intercept 分頁的 Raw 區段
- [x] 在 Proxy 分頁尋找 login.php 行

#### Q121. 威脅行為者會藉由繪製攻擊的什麼，嘗試找出目標上的攻擊向量？

- [x] surface（攻擊面）
- [ ] infrastructure
- [ ] threat
- [ ] door

#### Q122. 若供應商倒閉或賣給競爭對手，組織要如何確保軟體產品仍能獲得支援？

- [ ] 供應商倒閉後僱用其開發者。
- [ ] 透過收購供應商確保支援。
- [x] 透過 escrow agreement（軟體託管）確保支援。
- [ ] 反向工程產品以便內部支援。

#### Q123. 下列哪個安全標準適用於產品安全控制的認證？

- [ ] ISO/IEC 27001.
- [ ] ISO/IEC 9000.
- [x] ISO/IEC 15408.
- [ ] ISO/IEC 13335.

#### Q124. 被稱為資訊安全經理（information security manager）的董事會成員主要角色是什麼？

- [x] 確保適當的安全控制在組織內實施。
- [ ] 提供資訊保證職能的日常管理。
- [ ] 具備對組織弱點的詳細理解。
- [ ] 具備對組織面臨威脅的詳細理解。

#### Q125. 用於判定威脅發生可能性的兩大方法是什麼？

- [ ] Qualitative and statistical
- [ ] Statistical and quantitative
- [ ] Statistical and assumptive
- [x] Qualitative and quantitative

#### Q126. 哪種駭客通常由國家軍事情報或安全機構組織與資助，試圖取得外國對手的國家機密或軍事情報？

- [ ] hacktivists
- [ ] competitors
- [ ] black hat hackers
- [x] state-sponsored hackers

#### Q127. 下列哪種方法會將兩個二進位串流組合為一個新串流，其中包含未持有另一個原始串流便無法取回的隱藏資訊？

- [ ] substitution cipher
- [ ] weaponization
- [ ] transposition cipher
- [x] XOR encryption

#### Q128. 什麼是 Drupalgeddon？

- [ ] A web app proxy tool
- [ ] A DDoS bot
- [ ] A network packet capturing device
- [x] a SQL injection flaw

#### Q129. 加密技術用來隱藏資訊的演算法稱為什麼？

- [x] cipher
- [ ] XOR
- [ ] encoding
- [ ] cyber kill chain

#### Q130. 下列哪一項不是外包軟體開發可能引發的問題？

- [ ] 意外或刻意植入惡意程式碼。
- [ ] 智慧財產或商業機密的流失。
- [ ] 客戶與供應商之間可能產生法律爭議。
- [x] 資料保護法不適用於傳送給第三方的資訊。

#### Q131. \_ hat 指的是可能不遵循道德測試標準、但不具惡意意圖的駭客。

- [x] gray
- [ ] blue
- [ ] red
- [ ] purple

#### Q132. 明白多因素驗證（MFA）是最佳實務，下列哪個選項應盡量避免作為次要因子？

- [ ] biometric authentication
- [ ] OAUTH Token
- [ ] authenticator apps
- [x] SMS message

**說明**：相較其他方法，以 SMS 作為 MFA 因子通常較不安全；SMS 可能遭攔截（如 SIM 交換攻擊），而電信基礎設施亦未必能充分抵禦各種攻擊向量。常見更安全的替代方案包含生物特徵驗證、OAUTH token 與驗證器 App。

[Reference](https://www.zdnet.com/article/fbi-warns-about-attacks-that-bypass-multi-factor-authentication-mfa/) `"(...)All in all, MFA is still very effective at preventing most mass and automated attacks; however, users should be aware that there are ways to bypass some MFA solutions, such as those relying on SMS-based verification."`

#### Q133. 下列哪一項「不是」常見的身分驗證因子？

- [ ] Something you know
- [ ] Something you have
- [ ] Something you are
- [x] Something you want

#### Q134. 下列何者最能描述網安中的「Honeytoken」？

- [x] 一個對攻擊者看似合法的誘捕型網路主機。
- [ ] 用於管理網路流量的易用介面。
- [ ] 安全通訊中使用的加密金鑰。
- [ ] 兩因素驗證的硬體裝置。

#### Q135. 在網路安全架構中，「Bastion Host」的主要目的為何？

- [x] 對外提供可公開存取的服務，同時保護內部網路。
- [ ] 截取並分析所有網路流量以保障安全。
- [ ] 作為主伺服器故障時的備援伺服器。
- [ ] 促成兩個遠端網路之間的安全通訊。

#### Q136. 在網路分析中，「Port Mirroring」指的是什麼？

- [x] 將網路封包複製到指定目的地以供分析的過程。
- [ ] 在傳輸過程中加密資料以確保安全的方法。
- [ ] 進行網路流量負載平衡的機制。
- [ ] 允許特定連接埠流量通行的防火牆規則。

#### Q137. 下列哪一項「不是」常見的在網路上隱藏惡意軟體的方法？

- [ ] Polymorphic malware
- [ ] Rootkit
- [x] Packet Sniffing
- [ ] Stealthy tunneling protocols

#### Q138. 在資安脈絡中，縮寫「IDS」代表什麼？

- [ ] Internet Domain System
- [x] Intrusion Detection System
- [ ] Internet Data Security
- [ ] Integrated Defense Strategy

#### Q139. 「Man-in-the-Middle (MitM)」攻擊涉及什麼？

- [x] 在不為雙方所知的情況下攔截雙方通訊。
- [ ] 破解加密密碼。
- [ ] 以 DDoS 攻擊破壞網路服務。
- [ ] 在網路伺服器上安裝惡意軟體。

#### Q140. 下列哪一項是 Public Key Infrastructure (PKI) 的必要元素？

- [ ] 用於網路安全的防火牆。
- [x] 受信任的 Certificate Authority (CA)。
- [ ] 虛擬私人網路（VPN）。
- [ ] 網路路由器。

#### Q141. 在 WPA3 無線網路中，通常使用哪種加密來保護無線流量？

- [ ] WEP (Wired Equivalent Privacy)
- [x] AES (Advanced Encryption Standard)
- [ ] SSL (Secure Sockets Layer)
- [ ] DES (Data Encryption Standard)

#### Q142. 哪種網路安全協定用於在網際網路上提供安全且加密的通訊，常用於保護網站？

- [ ] SSH (Secure Shell)
- [ ] SNMP (Simple Network Management Protocol)
- [x] HTTPS (Hypertext Transfer Protocol Secure)
- [ ] ICMP (Internet Control Message Protocol)

#### Q143. 在資安中，「Zero-Day Vulnerability」指的是什麼？

- [ ] 已知並修補為期零天的弱點。
- [x] 尚未被軟體供應商或大眾所知的弱點。
- [ ] 影響零台網路裝置的弱點。
- [ ] 無法被利用的弱點。

#### Q144. 防火牆在網路安全中的目的為何？

- [ ] 加密資料傳輸
- [ ] 辨識並移除惡意軟體
- [x] 控制進出網路的流量
- [ ] 提供安全的網路存取

#### Q145. 哪種網攻旨在欺騙個人透露敏感資訊（如密碼或信用卡號）？

- [ ] Ransomware
- [ ] DDoS Attack
- [x] Phishing Attack
- [ ] SQL Injection

#### Q146. 在資安中，「Social Engineering」指的是什麼？

- [ ] 進階加密技術
- [ ] 入侵社群媒體帳號
- [x] 操縱個人洩露機密資訊
- [ ] 保護社群媒體網路

#### Q147. 哪種加密演算法常用於在網際網路上保護資料傳輸？

- [ ] ROT13
- [x] AES
- [ ] Caesar Cipher
- [ ] RSA

#### Q148. 在資安中，縮寫「VPN」代表什麼？

- [x] Virtual Private Network
- [ ] Very Private Network
- [ ] Virtual Personal Network
- [ ] Virtual Public Network

#### Q149. 下列哪個是強密碼的範例？

- [ ] Password123
- [ ] 123456
- [ ] JohnSmith
- [x] P@ssw0rd!

#### Q150. 在資安脈絡中，「Zero Trust」代表什麼？

- [ ] 信任所有網路流量
- [x] 驗證所有網路流量，不論其位置
- [ ] 只信任內部網路流量
- [ ] 僅驗證來自信任來源的網路流量

#### Q151. Security Information and Event Management (SIEM) 系統的目的為何？

- [ ] 封鎖所有進入的網路流量
- [ ] 加密敏感資料
- [ ] 管理使用者密碼
- [x] 蒐集、分析並回應安全事件

#### Q152. 哪項資安作法刻意探測網路或系統以找出弱點？

- [ ] Firewall Configuration
- [ ] Encryption
- [x] Penetration Testing
- [ ] Patch Management

#### Q153. Red Team 在資安中的主要目標為何？

- [ ] 開發軟體應用
- [ ] 監控網路流量
- [x] 模擬網攻以找出弱點
- [ ] 實施安全政策

#### Q154. 哪種惡意軟體會加密受害者的檔案，並要求支付贖金以解密？

- [ ] Spyware
- [ ] Worm
- [ ] Trojan
- [x] Ransomware

#### Q155. 在資安中，「Patch Management」指的是什麼？

- [ ] 保護伺服器的實體存取
- [x] 管理軟體更新與修補
- [ ] 加密敏感資料
- [ ] 實作網路防火牆

#### Q156. Data Loss Prevention (DLP) 解決方案的主要目的為何？

- [ ] 防止裝置的實體竊盜
- [ ] 加密所有網路流量
- [ ] 監控使用者活動
- [x] 防止敏感資料未經授權外洩

#### Q157. 哪個資安框架提供一組保護資訊系統的最佳實務？

- [ ] ISO 9001
- [ ] COBIT
- [ ] Six Sigma
- [x] NIST Cybersecurity Framework

#### Q158. Secure Sockets Layer (SSL) 憑證的目的為何？

- [ ] 封鎖進入的網路流量
- [x] 加密在 Web 伺服器與瀏覽器之間傳輸的資料
- [ ] 在網路上驗證使用者
- [ ] 監控使用者活動

#### Q159. 哪種攻擊會以大量流量淹沒系統或網路，致其無法使用？

- [ ] Phishing
- [ ] Ransomware
- [ ] Man-in-the-Middle
- [x] Distributed Denial of Service (DDoS)

#### Q160. 在資安中，「Two-Factor Authentication」是什麼意思？

- [ ] 使用兩種不同的瀏覽器
- [x] 使用兩種不同的驗證方法以提升安全性
- [ ] 連續登入系統兩次
- [ ] 使用兩種不同的防毒程式

#### Q161. Security Token 在驗證中的目的為何？

- [ ] 產生一次性密碼
- [ ] 封鎖進入的網路流量
- [x] 提供額外一層驗證
- [ ] 加密敏感資料

#### Q162. Security Operations Center (SOC) 在資安中的角色為何？

- [ ] 開發軟體應用
- [ ] 管理使用者密碼
- [x] 監控並回應安全事件
- [ ] 加密敏感資料

#### Q163. 哪種攻擊會將惡意程式偽裝成合法檔案或應用，誘使使用者執行？

- [ ] DDoS Attack
- [ ] SQL Injection
- [ ] Ransomware
- [x] Malware

#### Q164. 下列哪個「不是」多因素驗證（MFA）中常見的驗證因子？

- [ ] Something you are
- [ ] Something you do
- [ ] Something you have
- [x] Something you say

#### Q165. 哪種網攻旨在以流量淹沒服務使其無法使用？

- [x] DDoS (Distributed Denial of Service)
- [ ] Phishing
- [ ] Ransomware
- [ ] Malware

#### Q166. VPN（Virtual Private Network）在資安中的目的為何？

- [ ] 提升網速
- [x] 匿名化網路活動並加密資料傳輸
- [ ] 監控惡意網路活動
- [ ] 阻擋惡意程式與病毒

**說明**

- VPN（Virtual Private Network）會在不安全的網路（如網際網路）之上建立安全、加密的連線。它可隱藏使用者 IP 位址、加密傳輸中的資料，並提高第三方攔截難度；其主要目的在於保護使用者隱私並防止未授權存取。

#### Q167. 防火牆在網路中的主要功能為何？

- [ ] 在傳輸前加密資料
- [x] 監控並控制進出網路的流量
- [ ] 提供伺服器的實體安全
- [ ] 管理使用者對應用的存取

**說明**

- 防火牆是一種依安全規則監控並篩選進出網路流量的安全設備，主要用於在可信任的內部網路與不受信任的外部網路（如網際網路）之間建立屏障；其核心職能即為流量過濾。

#### Q168. 攻擊者常用哪種方式取得未授權的系統存取？

- [ ] Phishing
- [x] Encryption
- [ ] Data anonymization
- [ ] Two-factor authentication

**說明**

- Phishing 是一種網攻，攻擊者偽裝成合法實體，誘使受害者提供帳號、密碼或財務資料；常見手法包含偽造 email、網站或簡訊。其他選項（加密、資料匿名化、雙因素驗證）則屬於保護性安全措施。

#### Q169. 社交工程攻擊常用的技巧是哪一個？

- [ ] Encryption
- [ ] Firewalling
- [x] Pretexting
- [ ] Patching

**說明：**
Pretexting 是一種社交工程技巧，攻擊者編造可信情境以操弄受害者，使其洩露敏感資訊或執行有利於攻擊者的動作；常見方式包括偽裝權威身分、製造緊迫感或操弄情緒。其餘選項（加密、防火牆、修補）屬於安全措施，並非社交工程技巧。

來源： [SANS Institute - Social Engineering Attacks](https://www.sans.org/blog/the-big-four-social-engineering-attacks/)

#### Q170. Security Information and Event Management (SIEM) 系統的主要目的為何？

- [ ] 加密敏感資料
- [ ] 管理使用者密碼
- [x] 蒐集、分析並回應安全事件
- [ ] 封鎖所有進入的網路流量

**說明：**
Security Information and Event Management（SIEM）是彙整、分析並關聯全組織多來源安全資料的解決方案；目的在提供集中化的安全態勢視圖、偵測並回應安全事件，以及輸出合規與稽核所需報告。它的主要用途並非加密、密碼管理或封鎖所有網路流量。

來源： [NIST Special Publication 800-94 - Guide to Intrusion Detection and Prevention Systems (IDPS)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-94.pdf)
